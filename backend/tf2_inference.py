import tensorflow as tf
import numpy as np

from backend.config import id2name

PATH_TO_CKPT = 'models/ssdlite_mobilenet_v2.pb'

def load_model():
  detection_graph = tf.Graph()
  with detection_graph.as_default():
    od_graph_def = tf.compat.v1.GraphDef()
    with tf.io.gfile.GFile(PATH_TO_CKPT, 'rb') as fid:
      serialized_graph = fid.read()
      od_graph_def.ParseFromString(serialized_graph)
      tf.import_graph_def(od_graph_def, name='')
      with detection_graph.as_default():
        sess = tf.compat.v1.Session(graph=detection_graph)
        return sess, detection_graph


def inference(sess, detection_graph, img_arr, conf_thresh=0.5):
  image_tensor = detection_graph.get_tensor_by_name('image_tensor:0')
  detection_boxes = detection_graph.get_tensor_by_name('detection_boxes:0')
  detection_scores = detection_graph.get_tensor_by_name('detection_scores:0')
  detection_classes = detection_graph.get_tensor_by_name('detection_classes:0')
  num_detections = detection_graph.get_tensor_by_name('num_detections:0')
  image_np_expanded = np.expand_dims(img_arr, axis=0)
  (boxes, scores, classes, num) = sess.run(
      [detection_boxes, detection_scores, detection_classes, num_detections],
      feed_dict={image_tensor: image_np_expanded})

  height, width, _ = img_arr.shape
  results = []
  for idx, class_id in enumerate(classes[0]):
    conf = scores[0, idx]
    if conf > conf_thresh:
      bbox = boxes[0, idx]
      ymin, xmin, ymax, xmax = bbox[0] * height, bbox[1] * \
          width, bbox[2] * height, bbox[3] * width

      results.append({"name": id2name[class_id],
                      "conf": str(conf),
                      "bbox": [int(xmin), int(ymin), int(xmax), int(ymax)]
                      })

  return {"results": results}
