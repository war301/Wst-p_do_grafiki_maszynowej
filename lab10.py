from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
 
im = Image.open("morf.jpg")
 
#zadanie1
 
def zmien_rozmiar(obraz,s1,s2,filtr):
    w,h = obraz.size
    newsize = (w*s1,h*s2)
    im1 = obraz.resize(newsize, filtr)
    im1.show()
#zmien_rozmiar(im, 12, 4, Image.NEAREST)
 
#zadanie2
 
def zad2(obraz):
    w,h = obraz.size
    newsize = (int(w/3),int(h/3))
    im1c = obraz.copy()
    im2c = obraz.copy()
    im3c = obraz.copy()
    im4c = obraz.copy()
    im5c = obraz.copy()
    im6c = obraz.copy()
 
    im1 = im1c.resize(newsize, Image.NEAREST)
    im2 = im2c.resize(newsize, Image.BILINEAR)
    im3 = im3c.resize(newsize, Image.BICUBIC)
    im4 = im4c.resize(newsize, Image.LANCZOS)
    im5 = im5c.resize(newsize, Image.BOX)
    im6 = im6c.resize(newsize, Image.HAMMING) 
    
    plt.subplot(2,3,1)
    plt.imshow(im1)
    plt.axis('off')
    plt.subplot(2,3,2)
    plt.imshow(im2)
    plt.axis('off')
    plt.subplot(2,3,3)
    plt.imshow(im3)
    plt.axis('off')
    plt.subplot(2,3,4)
    plt.imshow(im4)
    plt.axis('off')
    plt.subplot(2,3,5)
    plt.imshow(im5)
    plt.axis('off')
    plt.subplot(2,3,6)
    plt.imshow(im6)
    plt.axis('off')
    plt.savefig('resize.jpg')
    plt.show()
#zad2(im)
 
#zadanie3
 
def zad3(obraz,left,top,right,bottom):
    im1 = obraz.crop((left,top,right,bottom))
    w,h = obraz.size
    newsize = (w*2,h*3)
    im1 = im1.resize(newsize)
    im1.save('glowa.png')
    im1.show()  
#zad3(im, 200,50,300,150)
 
#zadanie4
 
def zad4(obraz):
    im1 = obraz.rotate(60,expand=1,fillcolor= 'red')
    im1.save('obrot.png')
    im1.show()
#zad4(im)
 
#zadanie5
 
def zad5(obraz):
    im1 = obraz.rotate(-30,expand=0,fillcolor= 'yellow')
    im1.save('obrot2.png')
    im1.show() 
#zad5(im)
 
#zadanie6

def zad6(obraz):
    im1 = obraz.rotate(45,center=(411,151),expand=0,fillcolor= 'pink')
    im1.save('obrot3.png')
    im1.show()
#zad6(im)