# Created by william from lexueoude.com. 更多正版技术视频讲解，公众号：乐学FinTech

import cv2

# our_string = 'MGBWE98754321@#$%^&*()_+||||}'

img = cv2.imread('sample.png')

grey_scale_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

grey_scale_img_resize = cv2.resize(grey_scale_img, (100, 60))

cv2.imshow('sample_img', grey_scale_img_resize)
cv2.waitKey(0)
cv2.destroyAllWindows()
