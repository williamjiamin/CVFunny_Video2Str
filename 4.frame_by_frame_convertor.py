# Created by william from lexueoude.com. 更多正版技术视频讲解，公众号：乐学FinTech

import os
import cv2

our_string = 'MGBWE@#$9845372||)(%&11+**^^}'

cust_video = cv2.VideoCapture('sample.m4v')

return_val, frame_by_frame = cust_video.read()

while return_val:
    new_string_img = ''
    grey_scale_image = cv2.cvtColor(frame_by_frame, cv2.COLOR_BGR2GRAY)
    resized_grey_scale_image = cv2.resize(grey_scale_image, (80, 30))

    for i in resized_grey_scale_image:
        for j in i:
            every_pixel_index = int(j / 256 * len(our_string))
            new_string_img += our_string[every_pixel_index]
        new_string_img += '\n'
    # os.system('cls')
    os.system('clear')
    print(new_string_img)
    return_val, frame_by_frame = cust_video.read()
    cv2.waitKey(5)
