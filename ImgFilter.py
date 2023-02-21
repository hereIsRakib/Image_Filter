from PIL import ImageFilter


def filter_img(img):
    param = int(input(
        'Please Enter a Following Number to Filter the Photo.\nFor Blur Enter: 1\nFor Contour Enter: 2\nFor Detail Enter: 3\nFor Edge Enhance Enter: 4\nFor More Enhance Enter: 5\nFor EMBOSS Enter: 6\nFor Find Edges Enter: 7\nFor Sharpen Enter: 8\nFor Smooth Enter: 9\n'))
    if param == 1:
        img1 = img.filter(ImageFilter.BLUR)
    elif param == 2:
        img1 = img.filter(ImageFilter.CONTOUR)
    elif param == 3:
        img1 = img.filter(ImageFilter.DETAIL)
    elif param == 4:
        img1 = img.filter(ImageFilter.EDGE_ENHANCE)
    elif param == 5:
        img1 = img.filter(ImageFilter.EDGE_ENHANCE_MORE)
    elif param == 6:
        img1 = img.filter(ImageFilter.EMBOSS)
    elif param == 7:
        img1 = img.filter(ImageFilter.FIND_EDGES)
    elif param == 8:
        img1 = img.filter(ImageFilter.SHARPEN)
    elif param == 9:
        img1 = img.filter(ImageFilter.SMOOTH)
    return img1.save('converted_image.png', 'png')
