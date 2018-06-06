# Mahjong OCR PipeLine using darkflow for object detection and MobileNet for image classification

Read the [darkflow README](https://github.com/thtrieu/darkflow) to get started.

Download my pb file [here](https://drive.google.com/open?id=1KhL4KYRj6sb3ZMhRjsp8EI_BW1Lr-pdn)
and my meta file [here](https://drive.google.com/open?id=17N2DRIk41N6GDpE4ac4wDi8qQQB7Vhce)

The MobileNet pb and graph files are coming once I fine tune them.

I use darkflow to detect where in the image the tiles are in [darkflow/net/yolov2/predict.py](https://github.com/nith822/darkflow/blob/master/darkflow/net/yolov2/predict.py) and pipe those images into the MobileNet predictor in [label_image.py](https://github.com/nith822/darkflow/blob/master/label_image.py).


(everything I haven't edited) darkflow is distributed under GNU General Public License v3.0.
(label_image.py) tensorflow-for-poets-2 is distributed under Apache License 2.0.
