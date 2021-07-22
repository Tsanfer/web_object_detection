
> 参考链接：[AIZOOTech/flask-object-detection | Github](https://github.com/AIZOOTech/flask-object-detection)

# Web 在线目标识别

[![Docker ci](https://github.com/Tsanfer/web_object_detection/actions/workflows/docker-publish.yml/badge.svg)](https://github.com/Tsanfer/web_object_detection/actions/workflows/docker-publish.yml)
![Docker Image Size (latest by date)](https://img.shields.io/docker/image-size/tsanfer/web_object_detection?label=Docker%20image%20size&sort=date)
![GitHub repo size](https://img.shields.io/github/repo-size/Tsanfer/web_object_detection)
[![Uptime Robot status](https://img.shields.io/uptimerobot/status/m788067363-2813a393b48f8d4bd77ebbdf?label=Web%20status)](https://stats.uptimerobot.com/BRvBpuVrpD/788067363)
[![GitHub license](https://img.shields.io/github/license/Tsanfer/web_object_detection)](https://github.com/Tsanfer/web_object_detection/blob/main/LICENSE)

[![Docker Image](https://img.shields.io/badge/Docker%20Image-2496ED?style=flat-square&logo=Docker&logoColor=white)](https://hub.docker.com/r/tsanfer/web_object_detection)

[![Open in Gitpod](https://img.shields.io/badge/Gitpod-ready--to--code-blue?logo=gitpod)](https://gitpod.io/#https://github.com/Tsanfer/web_object_detection)

使用方法一：直接访问 [**在线网址**](http://hpc.tsanfer.xyz:8000/) 进行相应操作即可。

使用方法二：使用 Docker 在本地复制实验构建好的远程镜像进行测试。 [![Docker Image](https://img.shields.io/badge/Docker%20Image-2496ED?style=flat-square&logo=Docker&logoColor=white)](https://hub.docker.com/r/tsanfer/web_object_detection)
1. 先把 docker 的国内镜像加速配置好，然后输入如下命令
2. `docker run -d --name=object_detection -p 4000:4000 -p 8000:8000 tsanfer/web_object_detection:local`
3. 然后用浏览器打开本地的8000端口就能看见效果了。(http://127.0.0.1:8000 或 http://localhost:8000)

使用方法三：使用在线IDE查看：[![Open in Gitpod](https://img.shields.io/badge/Gitpod-ready--to--code-blue?logo=gitpod)](https://gitpod.io/#https://github.com/Tsanfer/web_object_detection)
