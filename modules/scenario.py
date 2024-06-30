import streamlit as st

class Scenario:
    def __init__(self, id: str, description: str):
        self.id = id
        self.description = description

class ScenarioBranch:
    def __init__(self, branch_id: str, description: str, selected_items: dict = {}):
        self.id = branch_id
        self.description = description
        self.selected_items = selected_items
        self.scenarios = []
        self.scenarios_relation = [] # source, target, relation

    def add_scenario(self, id: str ,description: str):
        scenario = Scenario(id, description)
        self.scenarios.append(scenario)
        
    def add_scenario_relation(self, source: str, target: str, relation: str):
        self.scenarios_relation.append((source, target, relation))

    def get_scenario_by_id(self, id: str):
        for scenario in self.scenarios:
            if scenario.id == id:
                return scenario
        return None


class ScenarioTree:
    def __init__(self, data):
        self.data = data
        self.branches = {}
        self.extra_edges = []  # 存储额外的边，用于链接不同的场景

    # 新增的函数
    def add_extra_edge(self, source_id, target_id):
        self.extra_edges.append((source_id, target_id))
    
    # 新增的函数
    def get_extra_edges(self):
        return self.extra_edges

    def add_branch(self, branch_id: str, description: str, selected_items: dict):
        if branch_id not in self.branches:
            branch = ScenarioBranch(branch_id, description)
            self.branches[branch_id] = branch
            self.branches[branch_id].selected_items = selected_items
        else:
            raise KeyError("Branch ID already exists")
        
    # def add_scenario(self, branch_id: str, scenario_id: str, description: str, selected_items: dict, branch_scenario:str = '', relation:str = ''):
    #     if branch_id in self.branches:
    #         branch: ScenarioBranch = self.branches[branch_id]
    #         branch.add_scenario_relation(branch.scenarios[-1].id, scenario_id, relation)
    #         branch.add_scenario(scenario_id, description)
    #     else:
    #         self.add_branch(branch_id, branch_scenario, selected_items)
    #         self.branches[branch_id].add_scenario(scenario_id, description)

    def add_scenario(self, branch_id: str, scenario_id: str, description: str, selected_items: dict, parent_scenario_id: str = None, branch_scenario: str = '', relation: str = ''):
        if branch_id in self.branches:    
            branch: ScenarioBranch = self.branches[branch_id]
            if parent_scenario_id:
                branch.add_scenario(scenario_id, description)
                branch.add_scenario_relation(parent_scenario_id, scenario_id, relation)
            else:
                branch.add_scenario_relation(branch.scenarios[-1].id, scenario_id, relation)
                branch.add_scenario(scenario_id, description)
        else:
            self.add_branch(branch_id, branch_scenario, selected_items)
            self.branches[branch_id].add_scenario(scenario_id, description)
            self.branches[branch_id].add_scenario_relation(branch_id, scenario_id, relation)


    def get_branch(self, branch_id: str):
        if branch_id in self.branches:
            return self.branches[branch_id]
        else:
            raise KeyError("Branch ID not found")
        
    def get_branch_by_items(self, selected_items: dict):
        for branch in self.branches.values():
            if branch.selected_items == selected_items:
                return branch
        return None
        
    def get_scenario(self, branch_id: str, scenario_id: str):
        if branch_id in self.branches:
            branch: ScenarioBranch = self.branches[branch_id]
            return branch.get_scenario_by_id(scenario_id)
        else:
            raise None