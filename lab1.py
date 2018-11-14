# Untitled - By: lsriw - Wed Nov 14 2018

import sensor, image, time

sensor.reset()
sensor.set_pixformat(sensor.GRAYSCALE)
sensor.set_framesize(sensor.QVGA)
sensor.skip_frames(time = 2000)

clock = time.clock()

while(True):
    clock.tick()
    img = sensor.snapshot()
    print(clock.fps())



# Predkosc przetwarzania (w zaleznosci od alg.)


# 1. Zaczac od wczytania w roznych formatach (DLA QVGA - 320x240)
# RGB565 - 28.6 (38)
# GRAYSCALE - 34.5 (51)
# BAYER - 14.1 (28)

# 2. HOME Co udostepnia
# 3. HOME Jak dziala

# 4.
