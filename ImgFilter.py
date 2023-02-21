from PIL import ImageFilter


def select_filter():
    valid_options = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    while True:
        param = input('Please Enter a Number to Select a Filter:\n'
                      '1. Blur\n'
                      '2. Contour\n'
                      '3. Detail\n'
                      '4. Edge Enhance\n'
                      '5. More Enhance\n'
                      '6. Emboss\n'
                      '7. Find Edges\n'
                      '8. Sharpen\n'
                      '9. Smooth\n')
        try:
            param = int(param)
            if param in valid_options:
                return param
            else:
                print('Invalid option. Please enter a number from 1 to 9.')
        except ValueError:
            print('Invalid input. Please enter a number from 1 to 9.')


def apply_filter(img, param):
    if param == 1:
        filtered_img = img.filter(ImageFilter.BLUR)
    elif param == 2:
        filtered_img = img.filter(ImageFilter.CONTOUR)
    elif param == 3:
        filtered_img = img.filter(ImageFilter.DETAIL)
    elif param == 4:
        filtered_img = img.filter(ImageFilter.EDGE_ENHANCE)
    elif param == 5:
        filtered_img = img.filter(ImageFilter.EDGE_ENHANCE_MORE)
    elif param == 6:
        filtered_img = img.filter(ImageFilter.EMBOSS)
    elif param == 7:
        filtered_img = img.filter(ImageFilter.FIND_EDGES)
    elif param == 8:
        filtered_img = img.filter(ImageFilter.SHARPEN)
    elif param == 9:
        filtered_img = img.filter(ImageFilter.SMOOTH)
    return filtered_img


def save_image(img, filename):
    img.save(filename, 'PNG')
    print(f'Filtered image saved as {filename}')


def filter_img(img):
    param = select_filter()
    filtered_img = apply_filter(img, param)
    save_image(filtered_img, 'converted_image.png')
