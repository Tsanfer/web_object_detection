from flask import Flask, request, jsonify  # 导入Flask，网络，json化模块
from PIL import Image  # 导入python图像库
import numpy as np  # 导入numpy
import base64  # 导入base64
import io  # 导入文件IO
import os  # 导入操作系统接口

from backend.tf_inference import load_model, inference  # 导入目标检测的相关函数

os.environ['CUDA_VISIBLE_DEVICES'] = '0'  # 配置操作系统环境变量，设置仅有GPU0可用

sess, detection_graph = load_model()  # 调用加载目标检测模块的函数

app = Flask(__name__)  # 初始化：所有的Flask都必须创建程序实例


@app.route('/api/', methods=["POST"])  # 配置页面路径，响应方式
# 主界面
def main_interface():
  response = request.get_json()  # 获取前端发来的json格式数据
  data_str = response['image']  # 提取出json数据中的image项
  point = data_str.find(',')  # 寻找到图片的base64编码
  # 移除没有使用的部分，比如: "data:image/jpeg;base64,"
  base64_str = data_str[point:]

  image = base64.b64decode(base64_str)  # 从base64编码解码为图片
  img = Image.open(io.BytesIO(image))  # 使用文件方式打开，解码出的图片信息

  if(img.mode != 'RGB'):  # 如果图片不是RGB格式的图片（比如某些带有Alpha通道的图片）
    img = img.convert("RGB")  # 将图片转化为RGB格式的图片

  # 将图片转化为numpy的序列
  img_arr = np.array(img)

  # 进行目标检测
  results = inference(sess, detection_graph, img_arr, conf_thresh=0.5)
  print(results)  # 打印结果

  return jsonify(results)  # 向前端返回一个JSON格式的数据


@app.after_request  # 请求得到响应后返回给用户前被调用
def add_headers(response):  # 添加HTTP相应头信息
  response.headers.add('Access-Control-Allow-Origin', '*')  # 允许所有域都具有访问资源的权限。
  response.headers.add('Access-Control-Allow-Headers',
                       'Content-Type,Authorization')  # 服务器允许请求中携带字段Content-Type和Authorization
  return response  # 返回数据


if __name__ == '__main__':  # 如果此文件被直接运行时
  # 运行程序（host为0.0.0.0）
  app.run(host='0.0.0.0', port='4000')
  # app.run(debug=True, host='0.0.0.0')
