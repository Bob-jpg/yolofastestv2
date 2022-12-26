"""
#######生成train.txt和val.txt

import os  #通过os模块调用系统命令
#D:/yolov5fastv2/Yolo-FastestV2-main/Yolo-FastestV2-main/datasets
file_path = r"D:\work\Yolo-FastestV2-main\datasets/train/"  #文件路径
#file_path1 = "D:/yolov5fastv2/Yolo-FastestV2-main/Yolo-FastestV2-main/datasets/train/"  #文件路径
file_path1 = "D:/work/Yolo-FastestV2-main/datasets/train/"  #文件路径
path_list = os.listdir(file_path) #遍历整个文件夹下的文件name并返回一个列表

path_name = []#定义一个空列表

for i in path_list:
    print("12",i.split(".")[1])
    if  i.split(".")[1]=="jpg":
        print(i)
        path_name.append(i.split(".")[0]) #若带有后缀名，利用循环遍历path_list列表，split去掉后缀名

#path_name.sort() #排序

for file_name in path_name:
    # "a"表示以不覆盖的形式写入到文件中,当前文件夹如果没有"save.txt"会自动创建
    with open("D:\work\Yolo-FastestV2-main\datasets/train.txt", "a") as file:
        print(file_name)
        file_name=file_path1+file_name+".jpg"
        file.write(file_name + "\n")
        
    file.close()


"""


"""
划分数据集为train  val  test

# # # LastEditors: UniDome
# # # LastEditTime: 2022-04-20 16:39:56

# import os, shutil, random
# from tqdm import tqdm

# def split_img(img_path, label_path, split_list):
#     try :   # 创建数据集文件夹
#         Data = r'D:\work\Yolo-FastestV2-main/4\mydata'
#         os.mkdir(Data)

#         train_img_dir = Data + '/images/train'
#         val_img_dir = Data + '/images/val'
#         test_img_dir = Data + '/images/test'

#         train_label_dir = Data + '/labels/train'
#         val_label_dir = Data + '/labels/val'
#         test_label_dir = Data + '/labels/test'

#         # 创建文件夹
#         os.makedirs(train_img_dir)
#         os.makedirs(train_label_dir)
#         os.makedirs(val_img_dir)
#         os.makedirs(val_label_dir)
#         # os.makedirs(test_img_dir)
#         # os.makedirs(test_label_dir)

#     except:
#         print('文件目录已存在')
        
#     train, val, test = split_list
#     all_img = os.listdir(img_path)
#     all_img_path = [os.path.join(img_path, img) for img in all_img]
#     # all_label = os.listdir(label_path)
#     # all_label_path = [os.path.join(label_path, label) for label in all_label]
#     train_img = random.sample(all_img_path, int(train * len(all_img_path)))
#     train_img_copy = [os.path.join(train_img_dir, img.split('\\')[-1]) for img in train_img]
#     train_label = [toLabelPath(img, label_path) for img in train_img]
#     train_label_copy = [os.path.join(train_label_dir, label.split('\\')[-1]) for label in train_label]
#     for i in tqdm(range(len(train_img)), desc='train ', ncols=80, unit='img'):
#         _copy(train_img[i], train_img_dir)
#         _copy(train_label[i], train_label_dir)
#         all_img_path.remove(train_img[i])
#     val_img = random.sample(all_img_path, int(val / (val + test) * len(all_img_path)))
#     val_label = [toLabelPath(img, label_path) for img in val_img]
#     for i in tqdm(range(len(val_img)), desc='val ', ncols=80, unit='img'):
#         _copy(val_img[i], val_img_dir)
#         _copy(val_label[i], val_label_dir)
#         all_img_path.remove(val_img[i])
#     test_img = all_img_path
#     test_label = [toLabelPath(img, label_path) for img in test_img]
#     for i in tqdm(range(len(test_img)), desc='test ', ncols=80, unit='img'):
#         _copy(test_img[i], test_img_dir)
#         _copy(test_label[i], test_label_dir)


# def _copy(from_path, to_path):
#     shutil.copy(from_path, to_path)

# def toLabelPath(img_path, label_path):
#     img = img_path.split('\\')[-1]
#     label = img.split('.jpg')[0] + '.txt'
#     return os.path.join(label_path, label)

# def main():
#     img_path = r'D:\work\Yolo-FastestV2-main/4/images'
#     label_path = r'D:\work\Yolo-FastestV2-main/4/labels'
#     split_list = [0.8, 0.2, 0]	# 数据集划分比例[train:val:test]
#     split_img(img_path, label_path, split_list)

# if __name__ == '__main__':
#     main()

"""