#!/usr/bin/env python
# coding: utf-8

# In[12]:


import tensorflow as tf


# In[13]:


import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import pandas as pd
import numpy as np
import os


# Arguments
# 
# directory: Directory where the data is located. If labels is "inferred", it should contain subdirectories, each containing images for a class. Otherwise, the directory structure is ignored.
# 
# labels: Either "inferred" (labels are generated from the directory structure), None (no labels), or a list/tuple of integer labels of the same size as the number of image files found in the directory. Labels should be sorted according to the alphanumeric order of the image file paths (obtained via os.walk(directory) in Python).
# 
# label_mode: - 'int': means that the labels are encoded as integers (e.g. for sparse_categorical_crossentropy loss). - 'categorical' means that the labels are encoded as a categorical vector (e.g. for categorical_crossentropy loss). - 'binary' means that the labels (there can be only 2) are encoded as float32 scalars with values 0 or 1 (e.g. for binary_crossentropy). - None (no labels).
# 
# class_names: Only valid if "labels" is "inferred". This is the explict list of class names (must match names of subdirectories). Used to control the order of the classes (otherwise alphanumerical order is used).
# color_mode: One of "grayscale", "rgb", "rgba". Default: "rgb". Whether the images will be converted to have 1, 3, or 4 channels.
# 
# batch_size: Size of the batches of data. Default: 32.
# 
# image_size: Size to resize images to after they are read from disk. Defaults to (256, 256). Since the pipeline processes batches of images that must all have the same size, this must be provided.
# 
# shuffle: Whether to shuffle the data. Default: True. If set to False, sorts the data in alphanumeric order.
# 
# seed: Optional random seed for shuffling and transformations.
# 
# validation_split: Optional float between 0 and 1, fraction of data to reserve for validation.
# 
# subset: One of "training" or "validation". Only used if validation_split is set.
# 
# interpolation: String, the interpolation method used when resizing images. Defaults to bilinear. Supports bilinear, nearest, bicubic, area, lanczos3, lanczos5, gaussian, mitchellcubic.
# 
# follow_links: Whether to visits subdirectories pointed to by symlinks. Defaults to False.
# 
# crop_to_aspect_ratio: If True, resize the images without aspect ratio distortion. When the original aspect ratio differs from the target aspect ratio, the output image will be cropped so as to return the largest possible window in the image (of size image_size) that matches the target aspect ratio. By default (crop_to_aspect_ratio=False), aspect ratio may not be preserved.
# 
# **kwargs: Legacy keyword arguments.

# In[14]:


print(os.walk("D:/AI, ML, DL/Deep Learning Projects and work/Brain_Tumer_MRI/MRI_scans_Data/Training/"))


# In[15]:


train = tf.keras.preprocessing.image_dataset_from_directory("D:/AI, ML, DL/Deep Learning Projects and work/Brain_Tumer_MRI/MRI_scans_Data/Training/"
                                                           ,labels="inferred",
                                                           label_mode='categorical',
#                                                            class_names=[''],#catrgorical, binary
                                                            image_size=(64,64),
                                                            shuffle=True,
                                                                                                                        
                                                           )


# In[16]:


test = tf.keras.preprocessing.image_dataset_from_directory("D:/AI, ML, DL/Deep Learning Projects and work/Brain_Tumer_MRI/MRI_scans_Data/Testing/"
                                                           ,labels="inferred",
                                                           label_mode='categorical',
#                                                            class_names=[''],#catrgorical, binary
                                                            image_size=(64,64),
                                                            shuffle=True,                                                             
                                                           )


# In[17]:


print(train.class_names)
print(test.class_names)


# In[18]:


from keras_preprocessing.image.utils import load_img
from tensorflow.keras import layers, models, datasets

#define Data generator in this cell
from keras.preprocessing.image import ImageDataGenerator, load_img
train_imagedata = ImageDataGenerator( rescale=1./255,
                                     shear_range = 0.2,
                                     zoom_range = 0.2,
                                     horizontal_flip = True)


# In[19]:


#Build a CNN model
cnn = tf.keras.models.Sequential()
#Build a cnn model
cnn.add(tf.keras.layers.Conv2D(filters=32, kernel_size=3, activation='relu', input_shape=[64,64,3]))
#step2: Polling
cnn.add(tf.keras.layers.MaxPool2D(pool_size=3, strides=2))

#Second convultional layer
cnn.add(tf.keras.layers.Conv2D(filters=32, kernel_size=3, activation='relu', input_shape=[64,64,3]))
cnn.add(tf.keras.layers.MaxPool2D(pool_size=3, strides=2))

# Flattening
cnn.add(tf.keras.layers.Flatten())
# Step 4: Connection
cnn.add(tf.keras.layers.Dense(units=1, activation='sigmoid'))

cnn.add(tf.keras.layers.Dense(units=1, activation='relu'))

cnn.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])


# In[ ]:





# In[ ]:


cnn.fit(x = train, validation_data=test, epochs=5)


# In[ ]:


train.class_names


# In[1]:


import numpy as np
from keras_preprocessing import image
inp = str(input("enter your number"))
test_image = image.load_img(f"D:/AI, ML, DL/Deep Learning Projects and work/Brain_Tumer_MRI/{inp}.jpeg", target_size=(64,64))
tm = image.img_to_array(test_image)
tm = np.expand_dims(tm, axis=0)
output = cnn.predict(tm)

cato = ['glioma_tumor', 'meningioma_tumor', 'no_tumor', 'pituitary_tumor']

print(cato[int(output[0][0])])


# In[ ]:





# In[ ]:




