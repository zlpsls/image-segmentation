#coding:utf-8
import cv2
import numpy as np
from matplotlib import pyplot as plt
%matplotlib inline
image = cv2.imread("./a/meanshape.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#plt.subplot(131), plt.imshow(image, "gray")
#plt.title("source image"), plt.xticks([]), plt.yticks([])
#plt.subplot(132), plt.hist(image.ravel(), 256)
#plt.title("Histogram"), plt.xticks([]), plt.yticks([])
ret1, th1 = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU)  #方法选择为THRESH_OTSU
#plt.subplot(133), 
plt.axis('off')
fig = plt.gcf()
fig.set_size_inches(2.0/3,2.0/3) #dpi = 300, output = 700*700 pixels
plt.gca().xaxis.set_major_locator(plt.NullLocator())
plt.gca().yaxis.set_major_locator(plt.NullLocator())
plt.subplots_adjust(top = 1, bottom = 0, right = 1, left = 0, hspace = 0, wspace = 0)
plt.margins(0,0)


plt.imshow(th1, "gray")
fig.savefig('./a/001.jpg', format='png', transparent=True, dpi=300, pad_inches = 0)
#plt.title("OTSU,threshold is " + str(ret1)), plt.xticks([]), plt.yticks([])
#plt.savefig('./a/000.jpg')
plt.show()
