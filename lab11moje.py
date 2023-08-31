from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

#zad1
obraz1 = Image.open('kormin.jpg')
print(obraz1.mode)
print(obraz1.size)
obraz2 = Image.open('braum.jpg')
print(obraz2.mode)
print(obraz2.size)
maska1 = Image.open('wzorek.jpg').convert("1")
print(maska1.mode)
maska2 = Image.open('wzorek1.jpg').convert("L")
print(maska2.mode)
maska3 = Image.open('wzorek2.jpg').convert("RGBA")
print(maska3.mode)
#zad2
 
w,h = obraz1.size
w1,h1 = obraz2.size
 
W = min(w,w1)
H = min(h,h1)
 
obraz11 = obraz1.resize((W,H),0)
obraz22 = obraz2.resize((W,H),0)
obraz1_cropped = obraz1.crop((50,5,145,150))
obraz2_cropped = obraz2.crop((200,0,400,230))
 
maska11 = maska1.resize(obraz1_cropped.size, 0)
maska12 = maska2.resize(obraz1_cropped.size, 0)
maska13 = maska3.resize(obraz1_cropped.size, 0) 
 
maska21 = maska1.resize(obraz2_cropped.size, 0)
maska22 = maska2.resize(obraz2_cropped.size, 0)
maska23 = maska3.resize(obraz2_cropped.size, 0)
 
obraz111 = obraz11.copy()
obraz112 = obraz11.copy()
obraz113 = obraz11.copy()
obraz111.paste(obraz2_cropped,(30,30),maska21)
obraz112.paste(obraz2_cropped,(30,30),maska22)
obraz113.paste(obraz2_cropped,(30,30),maska23)
 
 
obraz221 = obraz22.copy()
obraz222 = obraz22.copy()
obraz223 = obraz22.copy()
obraz221.paste(obraz1_cropped,(50,50),maska11)
obraz222.paste(obraz1_cropped,(50,50),maska12)
obraz223.paste(obraz1_cropped,(50,50),maska13)
 
 
plt.subplot(2,3,1)
plt.imshow(obraz111)
plt.axis('off')
 
plt.subplot(2,3,2)
plt.imshow(obraz112)
plt.axis('off')
 
plt.subplot(2,3,3)
plt.imshow(obraz113)
plt.axis('off')
 
plt.subplot(2,3,4)
plt.imshow(obraz221)
plt.axis('off')
 
plt.subplot(2,3,5)
plt.imshow(obraz222)
plt.axis('off')
 
plt.subplot(2,3,6)
plt.imshow(obraz223)
plt.axis('off')
 
plt.savefig('zadanie2.png')
plt.show()
 
#zad 3
 
maska2c = maska2.resize((W,H),0)
maska3c= maska3.resize((W,H),0)
 
im1 = Image.composite(obraz11,obraz22,maska2c)
im2 = Image.composite(obraz22,obraz11,maska2c)
im3 = Image.composite(obraz11,obraz22,maska3c)
im4 = Image.composite(obraz22,obraz11,maska3c)
 
plt.subplot(2,2,1)
plt.imshow(im1)
plt.axis('off')
 
plt.subplot(2,2,2)
plt.imshow(im2)
plt.axis('off')
 
plt.subplot(2,2,3)
plt.imshow(im3)
plt.axis('off')

plt.subplot(2,2,4)
plt.imshow(im4)
plt.axis('off')
 
plt.savefig('zadanie3.png')
plt.show()
 
#zad4
 
obraz3 = Image.open('rick.jpg')

obraz4 = Image.open('jesien.jpg')
obraz4.paste(obraz3,(400,300),obraz3)
obraz4.save('zadanie4.png')
obraz4.show()
 
#zad5
obraz5 = Image.open('kormin.jpg')
obraz6 = Image.open('braum.jpg')

im1 = obraz5.copy()
im2 = obraz6.copy()
w2, h2 = im1.size
w3, h3 = im2.size
W2 = min(w3, w2)
H2 = min(h3, h2)
 
im1r = im1.resize((W2, H2), 0)
im2r = im2.resize((W2, H2), 0)
 
i = 1
plt.figure(figsize=(18,15))
for alpha in np.linspace(0,1,20):
    plt.subplot(4,5,i)
    mix = Image.blend(im1r, im2r, alpha=alpha)
    plt.imshow(mix)
    plt.axis('off')
    i += 1
plt.subplots_adjust(wspace=0.05, hspace=0.05)
plt.savefig('zadanie5.png')
plt.show()
 
#zad7
 
def powieksz(obraz,left,top,right,bottom):
    im1 = obraz.crop((left,top,right,bottom))
    w,h = obraz.size
    newsize = (((bottom-top)+50),((right-left)+50))
    im1 = im1.resize(newsize)
    return im1
 
glowa = powieksz(obraz3,0,0,240,310)
obraz3c = obraz3.copy()
obraz3c.paste(glowa,(-80,10),glowa)
obraz3c.save('zadanie7.png')
obraz3c.show()