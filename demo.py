# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 18:07:57 2020

@author: JHPDC- Shubham
"""

import tensorflow as tf
from keras.preprocessing.image import ImageDataGenerator
import numpy as np
from keras.preprocessing import image
import numpy as np
from keras.preprocessing import image

#execfile('.traffic.py')
exec(open("./traffic.py").read())
test_image = image.load_img('dataset/single_prediction/test 1.jpg', target_size = (64, 64))
test_image = image.img_to_array(test_image)
test_image = np.expand_dims(test_image, axis = 0)
result = cnn.predict(test_image)
training_set.class_indices
if result[0][0] == 1:
    prediction = 'No traffic'
else:
    prediction = 'Traffic'
print(prediction)