FROM tsanfer/web_object_detection:local

# Install custom tools, runtimes, etc.
# For example "bastet", a command-line tetris clone:
# RUN brew install bastet
#
# More information: https://www.gitpod.io/docs/config-docker/

# RUN sed -i 's/\/\/ const URL = "http:\/\/localhost/const URL = "http:\/\/localhost/g' /workspace/web_object_detection/js/index.js \
#   && sed -i 's/const URL = "http:\/\/raspberry/\/\/ const URL = "http:\/\/raspberry/g' /workspace/web_object_detection/js/index.js
