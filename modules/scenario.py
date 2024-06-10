import streamlit as st

class Scenario:
    def __init__(self, id: str, description: str):
        self.id = id
        self.description = description

class ScenarioBranch:
    def __init__(self, branch_id: str, description: str, selected_items: list = []):
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

    def add_branch(self, branch_id: str, description: str):
        if branch_id not in self.branches:
            branch = ScenarioBranch(branch_id, description)
            self.branches[branch_id] = branch
        else:
            raise KeyError("Branch ID already exists")

    def get_branch(self, branch_id: str):
        if branch_id in self.branches:
            return self.branches[branch_id]
        else:
            raise KeyError("Branch ID not found")