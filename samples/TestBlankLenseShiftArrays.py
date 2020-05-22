from picamera import PiCamera
import numpy as np
import time, datatime

with PiCamera() as cam:
    lst_shape = cam._lens_shading_table_shape()

lst = np.zeros(lst_shape, dtype=np.uint8)
lst[...] = 32 # NB 32 corresponds to unity gain

with PiCamera(lens_shading_table=lst) as cam:
    # cam.start_preview()
    # time.sleep(5)
    # cam.stop_preview()
    cam.resolution = (1280,720)
    cam.capture("./newimage" + datatime.now().replace("/","_").replace(".","_").replace(":","_").replace(" ","_")  + ".jpg")

