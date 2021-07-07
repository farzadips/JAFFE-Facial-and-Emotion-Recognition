from ImageLoader import *

data , label = loadImages('jaffedbase', 'emotion')
print("number of images is" , data.shape[0] , "and number of features for each image is", data.shape[1])

### To show each images, you should reshape it to 256,256 and then use 'plt.imshow'
plt.imshow(data[0].reshape(256,256) , cmap='gray')
plt.show()