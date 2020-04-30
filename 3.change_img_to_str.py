# Created by william from lexueoude.com. 更多正版技术视频讲解，公众号：乐学FinTech

import cv2

our_string = 'MGBWE@#$9845372||)(%&11+**^^}'

img = cv2.imread('sample.png')

grey_scale_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

grey_scale_img_resize = cv2.resize(grey_scale_img, (100, 30))

new_string_img = ''

for i in grey_scale_img_resize:
    for j in i:
        every_pixel_index = int(j /256 * len(our_string))
        new_string_img += our_string[every_pixel_index]
    new_string_img += '\n'

print(new_string_img)


# cv2.imshow('sample_img', grey_scale_img_resize)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
