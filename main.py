from PIL import Image
from ImgFilter import filter_img

img_file_path = input('please enter the file path:  \n')
with Image.open(img_file_path) as img:
    filter_img(img)
