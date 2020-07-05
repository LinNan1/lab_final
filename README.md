# lab_final

## 目录结构

```
.
├── code
│   ├── myapp
│   │   ├── app.py           python代码
│   │   ├── Dockerfile       构建镜像所需的Dockerfile
│   │   ├── requirements.txt python应用依赖的包
│   │   └── templates        网页模板
│   │       └── result.html
│   └── myindex
│       ├── app.py           python代码
│       ├── Dockerfile       构建镜像所需的Dockerfile
│       ├── requirements.txt python应用依赖的包
│       └── templates        网页模板
│           └── index.html
├── yaml
│   ├── myapp.deployment.yaml   部署myapp的配置文件(包含service的部署)
│   ├── myapp.ingress.yaml      ingress的配置文件
│   ├── myindex.deployment.yaml 部署myindex的配置文件(包含service的部署)
│   └── nginx-ingress.yaml      部署nginx-ingress的配置文件
├── README
```


## ./code/myindex

- 使用`python`实现
- 主要实现了web端的用户界面，提供给用户输入，使用了`flask`框架。

- 代码很直观，无需注释便能看懂



## ./code/myapp

- 使用`python`实现
- 主要实现中文分词功能，供`myindex`调用。
- 代码很直观，无需注释便能看懂



## yaml

存放了一些部署应用需要的yaml配置文件
