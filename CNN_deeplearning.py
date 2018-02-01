from keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Activation, Dropout, Flatten, Dense
from keras import backend as K
import cv2
import numpy as np


# dimensions of our images.
img_width, img_height = 150, 150

# Path of the trainng folder
train_data_dir = 'data/train'
# Path of the validation folder
validation_data_dir = 'data/validation'
# set it according to no of images in the train directory
nb_train_samples = 210
# set it according to no of images in the validation directory
nb_validation_samples = 50
epochs = 200
batch_size = 10

if K.image_data_format() == 'channels_first':
    input_shape = (3, img_width, img_height)
else:
    input_shape = (img_width, img_height, 3)
# CNN model design
model = Sequential()
model.add(Conv2D(32, (3, 3), input_shape=input_shape))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Conv2D(32, (3, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Conv2D(64, (3, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Flatten())
model.add(Dense(64))
model.add(Activation('relu'))
model.add(Dropout(0.5))
model.add(Dense(9, activation='softmax'))
#model.add(Activation('sigmoid'))

model.compile(loss='categorical_crossentropy',
              optimizer='rmsprop',
              metrics=['accuracy'])

# this is the augmentation configuration we will use for training
train_datagen = ImageDataGenerator(
    rescale=1. / 255,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True)

# this is the augmentation configuration we will use for testing:
# only rescaling
test_datagen = ImageDataGenerator(rescale=1. / 255)

train_generator = train_datagen.flow_from_directory(
    train_data_dir,
    target_size=(img_width, img_height),
    batch_size=batch_size,
    class_mode='categorical')

#print (class_indices)
validation_generator = test_datagen.flow_from_directory(
    validation_data_dir,
    target_size=(img_width, img_height),
    batch_size=batch_size,
    class_mode='categorical')
print (validation_generator.class_indices)
model.fit_generator(
    train_generator,
    steps_per_epoch=nb_train_samples // batch_size,
    epochs=epochs,
    validation_data=validation_generator,
    validation_steps=nb_validation_samples // batch_size)

# Set the path of the image to be classified
img = cv2.imread('map_12.jpg')
img = cv2.resize(img,(150,150))
img = np.reshape(img,[1,150,150,3])


cla = model.predict_classes(img)
print (cla[0])


if(cla[0] == 1):
    print ('This image can be described as a bar chart which represents data with rectangular bars with heights proportional to the values that they represent.')
elif(cla[0] == 2):
    print ('This image is a graph of a function. It has x and y axes with curves and lines depicting a function.')
elif(cla[0] == 3):
    print ('This image has a geometrical figure.')
elif(cla[0] == 4):
    print ('This image is a line graph in which information is displayed as a series of data points connected by straight line segments.')
elif(cla[0] == 5):
    print ('This image is a mapping of function which shows the relations of inputs and output in form of ordered pair. ')
elif(cla[0] == 6):
	print ('This image doesnot belong to any mathematical representation or figures.')                                                                                   
elif(cla[0] == 7):
	print ('This image is a pie chart, a circle which is divided into sectors that each represent a proportion of the whole.')
elif(cla[0] == 8):
	print ('This image is a graph with x and y axes where points are plotted and drawn.')
elif(cla[0] == 0):
	print ('This image is a venn diagram in which logical sets represented as circles or closed curves within an enclosing rectangle,the universal set.')

model.save('model1.h5')