# 预热问题：
1. 什么叫做六重索引？
2. 关系数据库能实现免索引邻接吗？NoSQL数据库可以吗？
3. 举一个10个节点的BCI知识图谱片段例子，分别用RDF和属性图方式表示，形成文档，docx文档提交。说明RDF和属性图有什么不同。
4. 如何用json格式表示RDF和属性图知识图谱？以上一题中数据为例。
5. 用什么工具编辑json文档？yaml和json是一种文档格式吗？
6. 用python语言如何处理json数据？Julia语言呢？

answer:
```
1.六重索引是针对知识图谱数据和运算的特点提出的一种优化技术，利用知识图谱三元组的特点来构建索引。将三元组中主语、谓语、宾语的各种
排列情况都枚举出来，然后为它们一一构建索引。主语、谓语和宾语的排列情况共计六种。这些索引内容正好对应知识图谱运算中带变量的三元组
模式的各种可能，是一种典型的“空间换时间”策略。
这种方法不仅缓解了三元组表的单表自连接问题，而且加速了图谱的查询效率。但是也增加了更新和维护成本。
方案代表：RDF-3X、Hexastore
六张表：SPO、SOP、PSO、POS、OSP、OPS
SPO表举例：
![image](https://user-images.githubusercontent.com/74064347/150918533-7258188c-1cb6-4d8e-9199-c064a2f5a24d.png)

2.

5.json文档实际上是一个特定的数据交换格式，理论上任何文本编辑器都可以编辑json文档(比如vscode，vim).
yaml和json不是一种文档格式，yaml是层次化的，json中是利用数组或者字典并列的.
语法上yaml是json的超集，yaml解析器可以解析json.
二者都是面向对象的(个人理解)

6.python处理json一般使用官方包（import json), dumps/dump, 
loads/load,将python的类型(字典或者数组)转化为json文件/字符串，json文件/字符串转化为python类型（字典或者数组). 
这也是最方便的办法.此外第三方包Demjson可用于编码和解码 JSON 数据，包含了 JSONLint 的格式化及校验功能.
(julia简介）
Julia是一种即时(Just-In-Time，JIT)编译语言,而不是脚本（解释）语言（如Python，R，Ruby等）。
Julia使用LLVM(Low Level Virtual Machine)来进行JIT编译。具体过程是：Julia运行时会生成LLVM中间代码，并将其交给LLVM的JIT编译器，
最终以其生成在CPU上可执行的机器代码。 其实，在LLVM中所构建的编译技术已经为Julia的代码优化建立了一套强大的工作系统： 
既包含简单的操作，如循环展开或循环删除等；也涉及相对复杂的步骤，如SIMD向量化等。可见，是LLVM的存在促成了Julia在真正意义上的诞生。
julia处理json import该包：https://github.com/JuliaIO/JSON.jl 即可
```
