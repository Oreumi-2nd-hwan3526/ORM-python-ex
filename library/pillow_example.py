from PIL import Image, ImageFilter
import os

current_dir = os.path.dirname(os.path.abspath(__file__))

img = Image.open(current_dir +'/abcd.jpg', mode = 'r')
img.show()
print(img.size)

croped_img = img.crop((100, 30, 500, 500))
croped_img.save(current_dir + '/croped_test.jpg')

blur_test = img.filter(ImageFilter.BLUR)
blur_test.save(current_dir + '/blur_test.jpg')

contour_test = img.filter(ImageFilter.CONTOUR)
contour_test.save(current_dir + '/contour_test.jpg')