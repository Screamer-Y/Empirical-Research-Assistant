# TodoList

## Working on
### Data Page
- [ ] 生成更多的data
- [ ] 一个Data类，可以用来组织页面中需要的所有属性，放在session_data
- [ ] 将完整的data导入到页面，graph、items、description
- [ ] prompt尝试，llm_generation开发和封装
- [ ] 将逻辑设计到按钮上，支持prompt修改
- [ ] 目前将生成的场景返回到一个变量即可，这个分支就做到这个程度

## Finished
## 前期工作
- [x] 尝试Streamlit上的Get Started的例子
- [x] 尝试创建一个mulitple page的streamlit app
- [x] 大致思考系统设计，如有确认可能用于实现系统的组件
- [x] 研究如何使用GitHub Project
- [x] 开展讨论，确定系统的设计
## 原型搭建
- [x] 先搭建一版简单的原型，包含所有页面和元素
- [x] 接入langchain的API，实现生成功能
- [ ] 考虑一下CoT的prompt编写
- [x] 测试图的更新和导入功能
> 以上内容在main分支上进行即可
> 5.28 开会update之后再设计
- [x] 把设计划分为milestones和具体的task，更新到project上
## 5.28update
- [ ] 对于Scenario中的节点，按分支往前显示对于上一个Scenario节点新增数据的高亮
> 仅先实现了高亮
- [x] 对于Hypothesis，左边是文字和变量的关系图，右边是代码编辑器
## 开发阶段
- [x] 基于feature branch开发
- [ ] 想了下，开发顺序调整，先实现Data Page， 在过程中尝试确定一个合适的后端组织形式，然后再实现其他Function和page

## Future Work
## 美化阶段
- [ ] 知识图谱和流程图的美化，颜色、大小、内置图片等