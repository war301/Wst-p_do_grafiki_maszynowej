from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from PIL import ImageFilter
from PIL import ImageChops
from PIL import ImageOps
from PIL.ImageFilter import (
    BLUR, CONTOUR, DETAIL, EDGE_ENHANCE, EDGE_ENHANCE_MORE,
    EMBOSS, FIND_EDGES, SMOOTH, SMOOTH_MORE, SHARPEN)
from PIL import ImageEnhance

im = Image.open('krajobraz.jpg')
print("tryb obrazu", im.mode)
print("rozmiar", im.size)

#  Class   PIL.ImageFilter.Kernel(size, kernel, scale=None, offset=0) -- scale jest zazwyczaj sumą wyrazów w kernel, w algorytmie kernel normalizujemy dzieląc przez scale
#fe = im.filter(ImageFilter.FIND_EDGES) # filtruje obraz im
#fe.show()
#print(ImageFilter.FIND_EDGES.filterargs)  # wyświetla argumenty, w tym rozmiar i  wartości tablicy Kernel

#ImageFilter.FIND_EDGES.filterargs = ((3, 3), 1, 0, (-1, -1, -1, -1, 6, -1, -1, -1, -1)) # pozwala zmieniac wartości listy Kernel, skalę i offset.
#fe1 = im.filter(ImageFilter.FIND_EDGES) # filtruje obraz im
#fe1.show()

#ImageFilter.FIND_EDGES.filterargs = ((3, 3), 1, 0, (-1, -1, -1, -1, 8, -1, -1, -1, -1)) # pozwala zmieniac wartości listy Kernel, skalę i offset.
#fe3 = im.filter(ImageFilter.FIND_EDGES) # filtruje obraz im
#fe3.show()
#fe_ker = im.filter(ImageFilter.Kernel(size = (3, 3), kernel = (-1, -1, -1, -1, 8, -1, -1, -1, -1), scale=1, offset=0))
#fe_ker.show()
#roznica = ImageChops.difference(fe3, fe_ker)
#roznica.show()

#zad1#######################################
def filtruj(obraz,kernel_1,scale_1):
    obraz = im.copy()
    obrazek_p = obraz.load()
    obraz1_p = obraz.load()
    w,h = obraz.size
    m = len(kernel_1)
    for x in range (int (m/2),w- int(m/2)):
        for y in range(int(m/2),h- int(m/2)):
            temp = [0,0,0]
            for a in range(m):
                for b in range(m):
                    xn = x + a - int(m/2)
                    yn = y + b - int(m/2)
                    pixel = obrazek_p[xn,yn]
                    temp[0] += pixel[0] * kernel_1[a][b]
                    temp[1] += pixel[1] * kernel_1[a][b]
                    temp[2] += pixel[2] * kernel_1[a][b]
            obraz1_p[x,y] = (int(temp[0]/scale_1),int(temp[1]/scale_1),int(temp[2]/scale_1))
    return obraz

#zad2 ###############################
#blur//////////////////////////////////////

im1 = im.filter(ImageFilter.BLUR)
im1.save("blur.jpg")

im1_1 = filtruj(im,((1/9,1/9,1/9),(1/9,1/9,1/9),(1/9,1/9,1/9)),1)
im1_1.save("blur1.jpg")

roz = ImageChops.difference(im1,im1_1)
roz.show()

#zad 3 ##################################
#sharpen/////////////////////////////////

im2 = im.filter(ImageFilter.SHARPEN)
im2.save("sharpen.jpg")

im2_1=filtruj(im,((-2,-2,-2),(-2,32,-2),(-2,-2,-2)), ImageFilter.SHARPEN.filterargs[1])
im2_1.save("sharpen1.jpg")

roz1 = ImageChops.difference(im2,im2_1)
roz1.show()

#find_edges//////////////////////////////

im3 = im.filter(ImageFilter.FIND_EDGES)
im3.save("find_edges.jpg")


im3_1=filtruj(im,[[-1,-1,-1],[-1,8,-1],[-1,-1,-1]], ImageFilter.FIND_EDGES.filterargs[1])
im3_1.save("find_edges1.jpg")

roz3 = ImageChops.difference(im3,im3_1)
roz3.show()

#zad 4 ####################################

im4=im.filter(ImageFilter.EMBOSS)
im4.show()
im4.save("emboss.jpg")

#zad 5 ####################################

im_1=im.convert('L')
print(ImageFilter.EMBOSS.filterargs)

ImageFilter.EMBOSS.filterargs = ((3, 3), 1, 128, (-1, 0, 1, -2, 0, 2, -1, 0, 1))
im5=im_1.filter(ImageFilter.EMBOSS)
im5.save("sobel1.jpg")

ImageFilter.EMBOSS.filterargs = ((3, 3), 1, 128, (-1, -2, -1, 0, 0, 0, 1, 2, 1))
im5_1=im_1.filter(ImageFilter.EMBOSS)
im5_1.save("sobel2.jpg")

#zad 6 ####################################

im6_1=im.filter(ImageFilter.DETAIL)
im6_2=im.filter(ImageFilter.EDGE_ENHANCE)
im6_3=im.filter(ImageFilter.EDGE_ENHANCE_MORE)
im6_4=im.filter(ImageFilter.SMOOTH)
im6_5=im.filter(ImageFilter.SMOOTH_MORE)
im6_6=im.filter(ImageFilter.CONTOUR)
im6_7=im.filter(ImageFilter.BoxBlur(1))
im6_8=im.filter(ImageFilter.GaussianBlur(radius=3))
im6_9=im.filter(ImageFilter.UnsharpMask(radius=2,percent=150,threshold=4))
im6_10=im.filter(ImageFilter.Kernel((3,3),(1,0,1,-1,0,-1,1,0,1),2,0))
im6_11=im.filter(ImageFilter.RankFilter(size=3,rank=0))
im6_12=im.filter(ImageFilter.MedianFilter(size=3))
im6_13=im.filter(ImageFilter.MinFilter(size=3))
im6_14=im.filter(ImageFilter.MaxFilter(size=3))

plt.figure(figsize=(32,16))
plt.subplot(2,7,1)
plt.imshow(im6_1)
plt.axis("off")
plt.subplot(2,7,2)
plt.imshow(im6_2)
plt.axis("off")
plt.subplot(2,7,3)
plt.imshow(im6_3)
plt.axis("off")
plt.subplot(2,7,4)
plt.imshow(im6_4)
plt.axis("off")
plt.subplot(2,7,5)
plt.imshow(im6_5)
plt.axis("off")
plt.subplot(2,7,6)
plt.imshow(im6_6)
plt.axis("off")
plt.subplot(2,7,7)
plt.imshow(im6_7)
plt.axis("off")
plt.subplot(2,7,8)
plt.imshow(im6_8)
plt.axis("off")
plt.subplot(2,7,9)
plt.imshow(im6_9)
plt.axis("off")
plt.subplot(2,7,10)
plt.imshow(im6_10)
plt.axis("off")
plt.subplot(2,7,11)
plt.imshow(im6_11)
plt.axis("off")
plt.subplot(2,7,12)
plt.imshow(im6_12)
plt.axis("off")
plt.subplot(2,7,13)
plt.imshow(im6_13)
plt.axis("off")
plt.subplot(2,7,14)
plt.imshow(im6_14)
plt.axis("off")
plt.savefig("reszta.jpg")
