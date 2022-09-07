# install OpenNRE
>git clone git@github.com:thunlp/OpenNRE.git

将 requirement.txt 改为
```
transformers>=3.4.0
pytest==5.3.2
scikit-learn==0.22.1
scipy==1.4.1
nltk>=3.6.4
```
再执行  
>pip install -r OpenNRE/requirements.txt

torch自行安装  

>python3 test.py

然后根据报错信息，再pip安装所需要的包