# Created by william from lexueoude.com. 更多正版技术视频讲解，公众号：乐学FinTech

import cv2

# 导入图片并显示，按下任意键关闭
img = cv2.imread('sample.png')
resize_img = cv2.resize(img, (100, 60))
cv2.imshow('sample_img', resize_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
