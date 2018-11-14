# Untitled - By: lsriw - Wed Nov 14 2018

import sensor, image, time

sensor.reset()
sensor.set_pixformat(sensor.GRAYSCALE)
sensor.set_framesize(sensor.QQVGA)
sensor.skip_frames(time = 2000)

clock = time.clock()

while(True):
    clock.tick()
    img = sensor.snapshot()
    #print(clock.fps())
    #eye_position = img.find_eye([0, 0, img.width(), img.height()])
    #img.draw_circle(eye_position[0], eye_position[1], 5)

    x = img.find_features(image.HaarCascade('eye'))
    for feature in x:
        print(x)
        img.draw_rectangle(feature[0], feature[1], feature[2], feature[3])
        eye_position = img.find_eye(feature)
        print(eye_position)
        img.draw_circle(eye_position[0], eye_position[1], 5)


    #if x:
        #print(x)
        #img.draw_circle(x[0][0], x[0][1], 5)


# 1. Zaczac od wczytania w roznych formatach (DLA QVGA - 320x240)
# TYP - Terminal (GUI)
# RGB565 - 28.6 (38)
# GRAYSCALE - 34.5 (51)
# BAYER - 14.1 (28)

# 2. HOME Co udostepnia
# 3. HOME Jak dziala

# 4. Predkosc przetwarzania przy barcodes:
# 2.6 w GUI 12 w terminalu
