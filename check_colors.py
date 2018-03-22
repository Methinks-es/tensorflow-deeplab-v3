import numpy as np
import matplotlib.pyplot as plt

from skimage import io


palette = np.uint8([[0, 0, 0],  # 0=background
                 # 1=aeroplane, 2=bicycle, 3=bird, 4=boat, 5=bottle
                 [128, 0, 0], [0, 128, 0], [128, 128, 0], [0, 0, 128], [128, 0, 128],
                 # 6=bus, 7=car, 8=cat, 9=chair, 10=cow
                 [0, 128, 128], [128, 128, 128], [64, 0, 0], [192, 0, 0], [64, 128, 0],
                 # 11=dining table, 12=dog, 13=horse, 14=motorbike, 15=person
                 [192, 128, 0], [64, 0, 128], [192, 0, 128], [64, 128, 128], [192, 128, 128],
                 # 16=potted plant, 17=sheep, 18=sofa, 19=train, 20=tv/monitor
                 [0, 64, 0], [128, 64, 0], [0, 192, 0], [128, 192, 0], [0, 64, 128]])

m , n = 3 , 7

indices = np.reshape(list(range(21)), newshape=(3 , 7))
print(palette[indices])
io.imshow(palette[indices])
io.show()
