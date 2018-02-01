from keras.models import load_model
import cv2
import numpy as np

model = load_model('model1.h5')

model.compile(loss='categorical_crossentropy',
              optimizer='rmsprop',
              metrics=['accuracy'])

# Set the path of the image to be classified
img = cv2.imread('graph_2.jpg')
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


