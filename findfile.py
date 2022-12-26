"""  
移动文件夹得文件                            
# #################################移动整个文件夹中得文件
# import os  
# import shutil

# # file_dir =r"C:\Users/86166\Desktop/12\images/"
# # img_path=r"C:\Users/86166\Desktop/12\labels/"
# # newimg_path=r"C:\Users/86166\Desktop\shaixuantu/2/"
# file_dir =r"D:\work\Yolo-FastestV2-main\shujuji\焊前检测\第一种版型/12-20\labels"
# img_path=r"D:\work\Yolo-FastestV2-main\shujuji\焊前检测\第一种版型/12-20\images/"
# newimg_path=r"D:\work\Yolo-FastestV2-main\shujuji\焊前检测\第一种版型/12-20\images1/"
# # 获得文件完整路径
# for root, dirs, files in os.walk(file_dir):
#     for name in files:
#         # print(os.path.join(root, name))	# 文件
#         # name1=name.split('.')[0]+".txt"
#         # f = open(img_path+name1,'a')
#         # b = '0 0.0000000000000000 0.0000000000000000 0.0000000000000000 0.0000000000000000'
#         # f.write(str(b))
#         # f.close()
#         name1=name.split('.')[0]+".jpg"
#         path1=os.path.join(img_path,name1)
#         path2=os.path.join(newimg_path,name1)
#         print(path1)
#         shutil.move(path1,path2)

"""



"""
# ##################################移动整个文件夹中得文件
# import os  
# import shutil
# #C:\Users\86166\Desktop\shujuji\2022-11-28\DayShift\OK\0
# file_dir =r"D:\work\Yolo-FastestV2-main\shujuji\焊后检测\另一种版型\ok\labels"
# img_path=r"D:\work\Yolo-FastestV2-main\shujuji\焊后检测\另一种版型\ok\images/"
# newimg_path=r"D:\work\Yolo-FastestV2-main\shujuji\焊后检测\另一种版型\ok\images1/"
# if  not os.path.exists(newimg_path):# path是文件夹或者文件的相对路径或者绝对路径
#     os.makedirs(newimg_path)
# # 获得文件完整路径

# f = open(file_dir,"r") 
# lines =  f.read().splitlines()      #读取全部内容 ，并以列表方式返回
# for line in lines: 
#     print(line)
#     # print(os.path.join(root, name))	# 文件
#     name1=line+".jpg"
#     path1=os.path.join(img_path,name1)
#     path2=os.path.join(newimg_path,name1)
#     print(path1)
#     print(path2)
#     shutil.move(path1,path2)

"""






"""
###############################复制文件夹中部分文件

# import shutil
# import  os 

# file_dir =r"C:/Users/86166/Desktop/shaixuantu/labels/"
# img_path=r"C:/Users/86166/Desktop/shaixuantu/allimages"
# newimg_path=r"C:/Users/86166/Desktop/shaixuantu/images"
# # 获得文件完整路径
# for root, dirs, files in os.walk(file_dir):
#     for name in files:
#         # print(os.path.join(root, name))	# 文件
#         name1=name.split('.')[0]
#         name1=name1+".jpg"
#         path1=os.path.join(img_path,name1)
#         path2=os.path.join(newimg_path,name1)
#         print(path1)
#         shutil.copy(path1,path2)

"""