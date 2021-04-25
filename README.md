
> 参考链接：[AIZOOTech/flask-object-detection | Github](https://github.com/AIZOOTech/flask-object-detection)

# Web object detection

[![Docker ci](https://github.com/Tsanfer/web_object_detection/actions/workflows/docker-publish.yml/badge.svg)](https://github.com/Tsanfer/web_object_detection/actions/workflows/docker-publish.yml)
![Docker Image Size (latest by date)](https://img.shields.io/docker/image-size/tsanfer/web_object_detection?label=Docker%20image%20size&sort=date)
![GitHub repo size](https://img.shields.io/github/repo-size/Tsanfer/web_object_detection)
![GitHub](https://img.shields.io/github/license/Tsanfer/web_object_detection)

[![Docker Image](https://img.shields.io/badge/Docker%20Image-2496ED?style=flat-square&logo=Docker&logoColor=white)](https://hub.docker.com/repository/docker/tsanfer/web_object_detection)

[![Open in Gitpod](https://img.shields.io/badge/Gitpod-ready--to--code-blue?logo=gitpod)](https://gitpod.io/#https://github.com/Tsanfer/web_object_detection)


**Web 在线目标识别**

直接访问 [**在线网址**](http://clouddisk.tsanfer.xyz:8000/) 进行相应操作即可。

或者使用 Docker 在本地复制实验构建好的远程镜像进行测试。
先把 docker 的国内镜像加速配置好，然后运行

`docker run -p 4000:4000 -p 8000:8000 -d tsanfer/web_object_detection:local`