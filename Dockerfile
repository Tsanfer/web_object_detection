# 本地设置
# FROM daocloud.io/library/ubuntu:18.04

# Github云端设置
FROM ubuntu:18.04

WORKDIR /workdir

COPY ./ ./

# 本地构建镜像时，设置国内镜像
# RUN sed -i 's/archive.ubuntu.com/mirrors.163.com/g' /etc/apt/sources.list \
#   && apt-get update -qqy \
# #  && apt-get install -y build-essential cmake pkg-config libx11-dev libatlas-base-dev libgtk-3-dev libboost-python-dev python3.6-dev python3-pip wget\
#   && apt-get install -y python3.6-dev python3-pip\
#   && apt-get update \
#   && apt-get install -y git unzip \
#   && rm -rf /var/lib/apt/lists/* /var/cache/apt/* \
#   && apt-get clean \
#   && pip3 install --no-cache-dir -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/ \
#   && chmod 0777 -R /workdir
#   && cat /workdir/js/index.js | grep "const URL"

# Github云端设置
RUN apt-get update -qqy \
  && echo "apt-get update -qqy DONE!!!" \
  #  && apt-get install -y build-essential cmake pkg-config libx11-dev libatlas-base-dev libgtk-3-dev libboost-python-dev python3.6-dev python3-pip wget\
  && apt-get install -y python3.6-dev python3-pip \
  && echo "apt-get install -y python3.6-dev python3-pip DONE!!!" \
  && python3 -m pip install -U --force-reinstall pip \
  && echo "python -m pip install -U --force-reinstall pip DONE!!!" \
  && apt-get update \
  && echo "apt-get update DONE!!!" \
  && apt-get install -y git unzip vim \
  && echo "aapt-get install -y git unzip vim DONE!!!" \
  && rm -rf /var/lib/apt/lists/* /var/cache/apt/* \
  && echo "rm -rf /var/lib/apt/lists/* /var/cache/apt/* DONE!!!" \
  && apt-get clean \
  && echo "apt-get clean DONE!!!" \
  && pip3 install --no-cache-dir -r requirements.txt \
  && echo "ip3 install --no-cache-dir -r requirements.txt DONE!!!" \
  && chmod 0777 -R /workdir \
  && echo "chmod 0777 -R /workdir DONE!!!" \
  && cat /workdir/js/index.js | grep "const URL" \
  && echo "cat /workdir/js/index.js | grep 'const URL' DONE!!!"

# CMD ["python3", "app.py"]
ENTRYPOINT ["./run.sh"]
