> 参考链接：[AIZOOTech/flask-object-detection | Github](https://github.com/AIZOOTech/flask-object-detection)

# Web object detection

[![Docker ci](https://github.com/Tsanfer/web_object_detection/actions/workflows/docker-publish.yml/badge.svg)](https://github.com/Tsanfer/web_object_detection/actions/workflows/docker-publish.yml)
![Docker Image Size (latest by date)](https://img.shields.io/docker/image-size/tsanfer/web_object_detection?label=Docker%20image%20size&sort=date)
![GitHub repo size](https://img.shields.io/github/repo-size/Tsanfer/web_object_detection)
![GitHub](https://img.shields.io/github/license/Tsanfer/web_object_detection)


**Web 在线目标识别**

直接访问 [**在线网址**](http://clouddisk.tsanfer.xyz/flask_ob/) 进行相应操作即可。

或者使用 Docker 在本地复制实验构建好的远程镜像进行测试。
先把 docker 的国内镜像加速配置好，然后运行

`docker run -p 4000:4000 -p 8000:8000 -d tsanfer/web_object_detection`

然后再修改 Docker 容器中的./js/index.js 中的 URL 值，从

<http://raspberry.tsanfer.xyz:5000/api/>

修改为

<http://localhost:4000/api/>

后面这段改 URL 是为了实现前后端合并而修改的代码，以达到在本机测试的目的。端口从 5000 改到 4000 是因为，frp 内网穿透的服务器映射端口为 5000，后端实际发送的端口为 4000.

[Docker Hub 链接](https://hub.docker.com/repository/docker/tsanfer/web_object_detection)
