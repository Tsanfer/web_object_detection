# 本地设置
# FROM daocloud.io/library/ubuntu:18.04

FROM ubuntu:18.04
MAINTAINER Tsanfer <a1124851454@gmail.com>

WORKDIR /workdir

COPY ./ ./

# 本地构建镜像时，设置国内镜像
# sed -i 's/archive.ubuntu.com/mirrors.163.com/g' /etc/apt/sources.list \
#   && 
# && pip3 install --no-cache-dir -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/ \

RUN apt-get update -qqy \
#  && apt-get install -y build-essential cmake pkg-config libx11-dev libatlas-base-dev libgtk-3-dev libboost-python-dev python3.6-dev python3-pip wget\
  && apt-get install -y python3.6-dev python3-pip \
  && rm -rf /var/lib/apt/lists/* /var/cache/apt/* \
  && apt-get clean \
  && pip3 install --no-cache-dir -r requirements.txt \
  && chmod 0777 -R /workdir

# CMD ["python3", "app.py"]
ENTRYPOINT ["./run.sh"]
