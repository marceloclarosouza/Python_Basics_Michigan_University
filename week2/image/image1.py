#Consider the image shown below. Assume that the image is stored in a file called “luther.jpg”. Line 2 opens the file and uses the contents to create an image object that is referred to by img. Once we have an image object, we can use the methods described above to access information about the image or to get a specific pixel and check on its basic color intensities.

#When you run the program you can see that the image has a width of 400 pixels and a height of 244 pixels. Also, the pixel at column 45, row 55, has RGB values of 165, 161, and 158. Try a few other pixel locations by changing the getPixel arguments and rerunning the program.

#install the cImage module from http://pypi.org

import image
img = image.Image("D:\Python\Python_Basics_Michigan_University\week2\image\luther.jpg")

print(img.getWidth())
print(img.getHeight())

p = img.getPixel(2,2)
print(p.getred(), p.getGreen(), p.getBlue())
