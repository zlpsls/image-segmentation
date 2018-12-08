from skimage import data,filters
import matplotlib.pyplot as plt
%matplotlib inline
#image = data.camera()
image = cv2.imread('patches_50.jpg', 0)
print(type(image))
thresh = filters.threshold_otsu(image)   #返回一个阈值
dst =(image <= thresh)*1.0   #根据阈值进行分割

#plt.figure('thresh',figsize=(8,8))

# plt.subplot(121)
# plt.title('original image')
# plt.imshow(image,plt.cm.gray)

# plt.subplot(122)
#plt.title('binary image')

plt.imshow(dst,plt.cm.gray)
plt.axis('off')
fig = plt.gcf()
#plt.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=None, hspace=None)
fig.set_size_inches(2.0/3,2.0/3) #dpi = 300, output = 700*700 pixels
plt.gca().xaxis.set_major_locator(plt.NullLocator())
plt.gca().yaxis.set_major_locator(plt.NullLocator())
plt.subplots_adjust(top = 1, bottom = 0, right = 1, left = 0, hspace = 0, wspace = 0)
plt.margins(0,0)
fig.savefig('patches_bi_50.jpg', format='png', transparent=True, dpi=300, pad_inches = 0)
#plt.savefig("patches_bi_50.jpg", bbox_inches = 'tight')
plt.show()
