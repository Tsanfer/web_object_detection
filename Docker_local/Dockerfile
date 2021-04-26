# Github云端设置
FROM ubuntu:18.04
MAINTAINER Tsanfer <a1124851454@gmail.com>

WORKDIR /workdir

COPY ./ ./

# Github云端设置
RUN apt-get update -qqy \
#  && apt-get install -y build-essential cmake pkg-config libx11-dev libatlas-base-dev libgtk-3-dev libboost-python-dev python3.6-dev python3-pip wget\
  && apt-get install -y python3.6-dev python3-pip\
  && apt-get update \
  && apt-get install -y git unzip vim \
  && rm -rf /var/lib/apt/lists/* /var/cache/apt/* \
  && apt-get clean \
  && pip3 install --no-cache-dir -r requirements.txt \
  && chmod 0777 -R /workdir \
  && sed -i 's/\/\/ const URL = "http:\/\/localhost/const URL = "http:\/\/localhost/g' /workdir/js/index.js \
  && sed -i 's/const URL = "http:\/\/raspberry/\/\/ const URL = "http:\/\/raspberry/g' /workdir/js/index.js \
  && cat /workdir/js/index.js | grep "const URL"

# CMD ["python3", "app.py"]
ENTRYPOINT ["./run.sh"]
