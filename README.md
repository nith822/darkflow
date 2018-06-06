# Mahjong OCR PipeLine using darkflow for object detection and MobileNet for image classification

Read the darkflow README to get started.

Download my pb file [here](https://drive.google.com/open?id=1KhL4KYRj6sb3ZMhRjsp8EI_BW1Lr-pdn)
and my meta file [here](https://drive.google.com/open?id=17N2DRIk41N6GDpE4ac4wDi8qQQB7Vhce)

The MobileNet pb and graph files are coming once I fine tune them.

I use darkflow to detect where in the image the tiles are in [darkflow/net/yolov2/predict.py](https://github.com/nith822/darkflow/blob/master/darkflow/net/yolov2/predict.py) and pipe those images into the MobileNet predictor in [label_image.py](https://github.com/nith822/darkflow/blob/master/label_image.py).
