# ***FastestDet: it has higher accuracy and faster speed than Yolo-fastest https://github.com/dog-qiuqiu/FastestDet***
# :zap:Yolo-FastestV2:zap:[![DOI](https://zenodo.org/badge/386585431.svg)](https://zenodo.org/badge/latestdoi/386585431)
![image](https://github.com/dog-qiuqiu/Yolo-FastestV2/blob/main/img/demo.png)
* ***Simple, fast, compact, easy to transplant***
* ***Less resource occupation, excellent single-core performance, lower power consumption***
* ***Faster and smaller:Trade 0.3% loss of accuracy for 30% increase in inference speed, reducing the amount of parameters by 25%***
* ***Fast training speed, low computing power requirements, training only requires 3GB video memory, gtx1660ti training COCO 1 epoch only takes 4 minutes***
* ***算法介绍：https://zhuanlan.zhihu.com/p/400474142 交流qq群:1062122604***
# Evaluating indicator/Benchmark
Network|COCO mAP(0.5)|Resolution|Run Time(4xCore)|Run Time(1xCore)|FLOPs(G)|Params(M)
:---:|:---:|:---:|:---:|:---:|:---:|:---:
[Yolo-FastestV2](https://github.com/dog-qiuqiu/Yolo-FastestV2/tree/main/modelzoo)|24.10 %|352X352|3.29 ms|5.37 ms|0.212|0.25M
[Yolo-FastestV1.1](https://github.com/dog-qiuqiu/Yolo-Fastest/tree/master/ModelZoo/yolo-fastest-1.1_coco)|24.40 %|320X320|4.23 ms|7.54 ms|0.252|0.35M
[Yolov4-Tiny](https://raw.githubusercontent.com/AlexeyAB/darknet/master/cfg/yolov4-tiny.cfg)|40.2%|416X416|26.00ms|55.44ms|6.9|5.77M

* ***Test platform Mate 30 Kirin 990 CPU，Based on [NCNN](https://github.com/Tencent/ncnn)***
# Improvement
* Different loss weights for different scale output layers
* The backbone is replaced with a more lightweight shufflenetV2
* Anchor matching mechanism and loss are replaced by YoloV5, and the classification loss is replaced by softmax cross entropy from sigmoid
* Decouple the detection head, distinguish obj (foreground background classification), cls (category classification), reg (detection frame regression) 3 branches,  
# How to use
## Dependent installation
  * PIP
  ```
  pip3 install -r requirements.txt
  ```
## Test
* Picture test
  ```
  python test.py --data data/my.data --weights weights/my-299-epoch-1.000000ap-model.pth --imgpath ./img
  ```
<div align=center>
<img src="https://github.com/dog-qiuqiu/Yolo-FastestV2/blob/main/img/000139_result.png"> />
</div>

## How to train
### Building data sets(The dataset is constructed in the same way as darknet yolo)
* The format of the data set is the same as that of Darknet Yolo, Each image corresponds to a .txt label file. The label format is also based on Darknet Yolo's data set label format: "category cx cy wh", where category is the category subscript, cx, cy are the coordinates of the center point of the normalized label box, and w, h are the normalized label box The width and height, .txt label file content example as follows:
  ```
  11 0.344192634561 0.611 0.416430594901 0.262
  14 0.509915014164 0.51 0.974504249292 0.972
  ```
* The image and its corresponding label file have the same name and are stored in the same directory. The data file structure is as follows:
  ```
  .
  ├── train
  │   ├── 000001.jpg
  │   ├── 000001.txt
  │   ├── 000002.jpg
  │   ├── 000002.txt
  │   ├── 000003.jpg
  │   └── 000003.txt
  └── val
      ├── 000043.jpg
      ├── 000043.txt
      ├── 000057.jpg
      ├── 000057.txt
      ├── 000070.jpg
      └── 000070.txt
  ```
* Generate a dataset path .txt file, the example content is as follows：
  
  train.txt
  ```
  /home/qiuqiu/Desktop/dataset/train/000001.jpg
  /home/qiuqiu/Desktop/dataset/train/000002.jpg
  /home/qiuqiu/Desktop/dataset/train/000003.jpg
  ```
  val.txt
  ```
  /home/qiuqiu/Desktop/dataset/val/000070.jpg
  /home/qiuqiu/Desktop/dataset/val/000043.jpg
  /home/qiuqiu/Desktop/dataset/val/000057.jpg
  ```
* Generate the .names category label file, the sample content is as follows:
 
  category.names
  ```
  person
  bicycle
  car
  motorbike
  ...
  
  ```
* The directory structure of the finally constructed training data set is as follows:
  ```
  .
  ├── my.names        # .names my label file
  ├── train                 # train dataset
  │   ├── 000001.jpg
  │   ├── 000001.txt
  │   ├── 000002.jpg
  │   ├── 000002.txt
  │   ├── 000003.jpg
  │   └── 000003.txt
  ├── train.txt              # train dataset path .txt file
  ├── val                    # val dataset
  │   ├── 000043.jpg
  │   ├── 000043.txt
  │   ├── 000057.jpg
  │   ├── 000057.txt
  │   ├── 000070.jpg
  │   └── 000070.txt
  └── val.txt                # val dataset path .txt file

  ```
### Get anchor bias
* Generate anchor based on current dataset
  ```
  python genanchors.py --traintxt ./datasets/train.txt
  ```
* The anchors6.txt file will be generated in the current directory,the sample content of the anchors6.txt is as follows:
  ```
  12.64,19.39, 37.88,51.48, 55.71,138.31, 126.91,78.23, 131.57,214.55, 279.92,258.87  # anchor bias
  0.636158                                                                             # iou
  ```
### Build the training .data configuration file
* Reference./data/coco.data
  ```
  [name]
  model_name=coco           # model name

  [train-configure]
  epochs=300                # train epichs
  steps=150,250             # Declining learning rate steps
  batch_size=64             # batch size
  subdivisions=1            # Same as the subdivisions of the darknet cfg file
  learning_rate=0.001       # learning rate

  [model-configure]
  pre_weights=None          # The path to load the model, if it is none, then restart the training
  classes=80                # Number of detection categories
  width=352                 # The width of the model input image
  height=352                # The height of the model input image
  anchor_num=3              # anchor num
  anchors=12.64,19.39, 37.88,51.48, 55.71,138.31, 126.91,78.23, 131.57,214.55, 279.92,258.87 #anchor bias

  [data-configure]
  train=/media/qiuqiu/D/coco/train2017.txt   # train dataset path .txt file
  val=/media/qiuqiu/D/coco/val2017.txt       # val dataset path .txt file 
  names=./data/coco.names                    # .names category label file
  ```
### Train
* Perform training tasks
  ```
  python train.py --data data/my.data
  ``` 
### Evaluation
* Calculate map evaluation
  ```
  python3 evaluation.py --data data/coco.data --weights modelzoo/coco2017-0.241078ap-model.pth
  ```
# Deploy
## NCNN
* Convert onnx
  ```
  python pytorch2onnx.py --data data/my.data --weights weights/my-299-epoch-1.000000ap-model.pth --output JBoxafter.onnx
  ```
* onnx测试
python yolo_fastestv2.py  里面需要修改路径
* onnx-sim
  ```
  python3 -m onnxsim yolo-fastestv2.onnx yolo-fastestv2-opt.onnx
  ```
* Build NCNN
  ```
  git clone https://github.com/Tencent/ncnn.git
  cd ncnn
  mkdir build
  cd build
  cmake ..
  make
  make install
  cp -rf ./ncnn/build/install/* ~/Yolo-FastestV2/sample/ncnn
  ```
* Covert ncnn param and bin
  ```
  cd ncnn/build/tools/onnx
  ./onnx2ncnn yolo-fastestv2-opt.onnx yolo-fastestv2.param yolo-fastestv2.bin
  cp yolo-fastestv2* ../
  cd ../
  ./ncnnoptimize yolo-fastestv2.param yolo-fastestv2.bin yolo-fastestv2-opt.param yolo-fastestv2-opt.bin 1
  cp yolo-fastestv2-opt* ~/Yolo-FastestV2/sample/ncnn/model
  ```
* run sample
  ```
  cd ~/Yolo-FastestV2/sample/ncnn
  sh build.sh
  ./demo
  ```
# Reference
* https://github.com/Tencent/ncnn
* https://github.com/AlexeyAB/darknet
* https://github.com/ultralytics/yolov5
* https://github.com/eriklindernoren/PyTorch-YOLOv3





# 数据集准备
# filename.py脚本
代码里面有注释
# findfile.py脚本
代码里面有注释

# 扩充数据集
yolotoxml.py是将yolo数据集转换为xml; voctoyol.py是将xml数据集转换为yolo
# 这是一个目标检测和目标分割增强的小工具，需要您事先标记一些图片，然后变化增强图片(支持LabelIMg和LabelMe标注的文件)，希望对您有所帮助！<br>
**包括3个python文件（rename_file.py、DataAugmentforLabelImg.py和DataAugmentforLabelMe.py）**<br>
1. rename_file.py能实现文件的重命名,注意修改文件的路径
2. DataAugmentforLabelImg.py能实现LabelImg标注后的图片的增强（包括模糊，亮度，裁剪，旋转，平移，镜像等变化）
3. DataAugmentforLabelMe.py能实现LabelMe标注后的图片的增强（包括模糊、亮度、平移、镜像等变化）

**注意：一些包的安装是必要的，比如Opencv_python等**
<br>
##*将您需要增强的图片放在对应的文件夹即可，具体可参考demo给出的图片和xml文件存放路径，您放入即可*
<br>
**保存结果：**<br>
1. 目标检测增强后的图片默认会保存在./data/Images2中，xml文件会保存在./data/Annotations2中（包括新的图片和xml文件）<br>
2. 目标分割增强后的图片默认会保存在./data2中（包括新的图片和json文件）
<br>

**实现这个工具参考了：**<br>
https://github.com/maozezhong/CV_ToolBox/blob/master/DataAugForObjectDetection/


##Demo
<br>
**LabelImg标定用于检测的图片,使用DataAugmentforLabelImg**
DataAugmentforLabelImg.py 脚本来扩充数据集
![image](https://github.com/pureyangcry/tools/blob/master/Imgs/d_demo.jpg)
增强结果：
![image](https://github.com/pureyangcry/tools/blob/master/Imgs/d_results.jpg)


