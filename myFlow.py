from darkflow.net.build import TFNet
import cv2

options = {"model": "cfg/tiny-yolo-voc-3c.cfg", "pbLoad": "built_graph/tiny-yolo-voc-3c.pb", "metaLoad": "built_graph/tiny-yolo-voc-3c.meta"}

tfnet = TFNet(options)

imgcv = cv2.imread("./validate/1.jpg")
result = tfnet.return_predict(imgcv)
print(result)
