# 软件源代码分析技术课程作业
## Assignment 
Objective The goal of this assignment is to develop an optimizer that performs dataflow analysis.  
This assignment has the following components: 

▪ Construct the Control Flow Graph (CFG)

▪ Perform d-u path computation
## Introduce:
Win10  
Python3.8  
Graphviz
## File: 
example: 存放用来分析的源代码文件  
venv: 项目虚拟环境

# 24h紧急开发
时间紧任务重，紧急处理，至少实现解决示例一个程序
## 实现思路
### 1. 读取文件并进行处理
读取后缀为.c的文件，去除代码中的换行、include语句、缩进，将处理后的程序另存为同名txt文件以便查看  
同时按行保存为list用以后续处理，后续对list进行操作
### 2. 按行处理，进行词法分析
### 3. 分块处理，进行语法分析
### 4. 绘图
### 5. 找出define和use
### 6. 写出d-u路径


