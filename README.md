# 预热问题：
1. 什么叫做六重索引？
2. 关系数据库能实现免索引邻接吗？NoSQL数据库可以吗？
3. 举一个10个节点的BCI知识图谱片段例子，分别用RDF和属性图方式表示，形成文档，docx文档提交。说明RDF和属性图有什么不同。
4. 如何用json格式表示RDF和属性图知识图谱？以上一题中数据为例。
5. 用什么工具编辑json文档？yaml和json是一种文档格式吗？
6. 用python语言如何处理json数据？Julia语言呢？

answer:
```
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