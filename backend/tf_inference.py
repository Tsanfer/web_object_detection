import tensorflow as tf  # 导入TensorFlow模块
import numpy as np  # 导入numpy模块

# 导入id与名字的映射关系
from backend.config import id2name

# 定义预训练模型的位置
PATH_TO_CKPT = 'models/ssdlite_mobilenet_v2.pb'

# 加载模块


def load_model():
  detection_graph = tf.Graph()  # 实例化一个类，用于 tensorflow 计算和表示用的数据流图
  with detection_graph.as_default():  # 将这个类实例，也就是新生成的图作为整个 tensorflow 运行环境的默认图
    od_graph_def = tf.GraphDef()  # 新建GraphDef文件，用于临时载入模型中的图
    with tf.gfile.GFile(PATH_TO_CKPT, 'rb') as fid:  # 以二进制读模式打开预训练模型文件
      serialized_graph = fid.read()  # 以字符串形式读取预训练模型文件
      od_graph_def.ParseFromString(serialized_graph)  # 得到模型中的计算图和数据
      # 将图从od_graph_def导入到当前默认图中（也就是detection_graph中）
      tf.import_graph_def(od_graph_def, name='')
      with detection_graph.as_default():
        sess = tf.Session(graph=detection_graph)  # 创建一个会话，用来运行detection_graph
        return sess, detection_graph  # 返回会话和预训练模型所生成的图


# 进行推测
# 导入会话，预训练模型所生成的图，输入的图像序列，设置推测的准确的阈值
def inference(sess, detection_graph, img_arr, conf_thresh=0.5):
  # with detection_graph.as_default():
  #     with tf.Session(graph=detection_graph) as sess:
  # 定义预训练模型所生成的图的输入和输出的张量
  image_tensor = detection_graph.get_tensor_by_name('image_tensor:0')
  # 每个方框代表图像中检测到的特定对象
  detection_boxes = detection_graph.get_tensor_by_name('detection_boxes:0')
  # 每个分数代表每个对象的置信度（准确度）。
  # 置信度显示在图像上，和目标类别一同显示
  detection_scores = detection_graph.get_tensor_by_name('detection_scores:0')
  detection_classes = detection_graph.get_tensor_by_name('detection_classes:0')
  num_detections = detection_graph.get_tensor_by_name('num_detections:0')
  image_np_expanded = np.expand_dims(img_arr, axis=0)
  (boxes, scores, classes, num) = sess.run(
      [detection_boxes, detection_scores, detection_classes, num_detections],
      feed_dict={image_tensor: image_np_expanded})

  height, width, _ = img_arr.shape  # 获取图像的长和宽，忽略第一维的数据
  results = []
  for idx, class_id in enumerate(classes[0]):  # 遍历推测出的类型
    conf = scores[0, idx]  # 获取推测的目标的可能性
    if conf > conf_thresh:  # 如果推测的目标可能性大于阈值
      bbox = boxes[0, idx]  # 获取目标的位置
      ymin, xmin, ymax, xmax = bbox[0] * height, bbox[1] * \
          width, bbox[2] * height, bbox[3] * width

      results.append({"name": id2name[class_id],
                      "conf": str(conf),
                      "bbox": [int(xmin), int(ymin), int(xmax), int(ymax)]
                      })  # 生成推测的信息

  return {"results": results}  # 返回推测的信息
