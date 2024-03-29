import os
count = len(os.listdir('../'))-1
print(count)
file = os.listdir('./')
# for i in range(len(file)):
#     print(file[i]+'->',end=' ')
#     # if (file[i].endswith('.jpg')):
#     #     os.rename(file[i],'../'+f'{i+count}.jpg')
#     #     print(f'{i+count}.jpg')
#     # if (file[i].endswith('.png')):
#     #     os.rename(file[i],'../'+f'{i+count}.png')
#     #     print(f'{i+count}.png')
#     os.rename(file[i],'../'+f'{i+count}.jpg')
#     print(f'{i+count}.jpg')

from PIL import Image
import cv2 as cv
import os
 
def PNG_JPG(PngPath):
    img = cv.imread(PngPath, 0)
    w, h = img.shape[::-1]
    infile = PngPath
    outfile = os.path.splitext(infile)[0] + ".jpg"
    img = Image.open(infile)
    img = img.resize((int(w / 2), int(h / 2)), Image.ANTIALIAS)
    try:
        if len(img.split()) == 4:
            # prevent IOError: cannot write mode RGBA as BMP
            r, g, b, a = img.split()
            img = Image.merge("RGB", (r, g, b))
            img.convert('RGB').save(outfile, quality=70)
            os.remove(PngPath)
        else:
            img.convert('RGB').save(outfile, quality=70)
            os.remove(PngPath)
        return outfile
    except Exception as e:
        print("PNG转换JPG 错误", e)


path_root = os.getcwd()
Path='./'
img_dir = os.listdir(Path)
for img in img_dir:
    if img.endswith('.png'):
        PngPath= Path + img
        PNG_JPG(PngPath)
img_dir = os.listdir(Path)
for img in img_dir:
    print(img)


import os

# 设置目标文件夹路径
folder_path = './'

# 获取文件夹中所有.jpg文件
jpg_files = [f for f in os.listdir(folder_path) if f.endswith('.jpg')]

# 按文件名排序，这一步是可选的，根据需要决定是否需要
jpg_files.sort()

# 重命名文件
for i, filename in enumerate(jpg_files):
    # 构造原始文件的完整路径
    original_path = os.path.join(folder_path, filename)
    
    # 构造新文件的完整路径
    new_path = os.path.join(folder_path, f'{i}.jpg')
    
    # 重命名文件
    os.rename(original_path, new_path)

print("重命名完成。")

