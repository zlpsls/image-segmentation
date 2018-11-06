#method1
from PIL import Image  
import numpy as np
im = Image.open("./test2/papa791.jpg")
im.show() 
in_data = np.asarray(im, dtype=np.uint8)
img = np.array(in_data)   
print(img.shape)
print(img.ndim)


image = np.expand_dims(in_data, axis=2)
image = np.concatenate((image, image, image), axis=-1)
print(image.shape)
im = Image.fromarray(np.uint8(image))
im.save('a.jpg')

#method2
import os 
import numpy as np
from PIL import Image
file_names = os.listdir('./train2/')
for i in range(len(file_names)):
    im = Image.open('./train2/'+file_names[i])
    im2 = np.array(im)
    if im2.ndim == 2:
        pic = Image.fromarray(im2) # convert to Image type
        pic_l = pic.convert("RGB")
        pic_l.save('./3chTrain/'+file_names[i])    
    if im2.ndim == 3:
        im.save('./3chTrain/'+file_names[i])    
