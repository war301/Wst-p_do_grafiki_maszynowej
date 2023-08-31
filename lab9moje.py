from PIL import Image
import numpy as np
from PIL import ImageChops, ImageOps, ImageShow
from PIL import ImageStat as stat
from PIL import ImageFilter
import matplotlib.pyplot as plt

def zakres(w, h): # funkcja, która uprości podwójna petle for
    return [(i, j) for i in range(w) for j in range(h)]

def statystyki(im):
    s = stat.Stat(im)
    print("extrema ", s.extrema)  # max i min
    print("count ", s.count)  # zlicza
    print("mean ", s.mean)  # srednia
    print("median ", s.median)  # mediana
    print("stddev ", s.stddev)  # odchylenie standardowe



###zad 1 

obr=Image.open('zeby.jpg')
obr=obr.convert('L')
print(obr.mode)
statystyki(obr)

###zad 2

hist=obr.histogram()
plt.title("histogram")
plt.plot(range(256), hist[:256])
plt.show()

###zad 3
obr1=obr.copy()

def histogram_norm(obraz):
    s = stat.Stat(obraz)
    hist2 = obraz.histogram()   
    for i in range(len(hist2)):
        hist2[i] = hist2[i] / s.count[0]
    plt.title("histogram znormalizowany")
    plt.plot(range(256), hist2[:256])
    plt.savefig('norm.jpg')
    plt.show()

histogram_norm(obr1)

###zad 4 
obr2=obr.copy()
def histogram_cumul(obraz):
    s = stat.Stat(obraz)
    hist2 = obraz.histogram()
    hist3 = obraz.histogram()
    hist_cumul=[]
    for i in range(len(hist2)):
        hist2[i] = hist2[i] / s.count[0]
    for i in range(len(hist3)):
        suma = 0
        for j in range(i+1):
            suma+= hist2[j]
        hist_cumul.append(suma)
    plt.title("histogram kumulowany")
    plt.plot(range(256), hist_cumul[:256])
    plt.savefig('cumul.jpg')
    plt.show()
    return hist_cumul
    
histogram_cumul(obr2)

###zad 5

obr3=obr.copy()

def histogram_equalization(obraz):
    to=histogram_cumul(obraz)
    w, h = obraz.size
    pixele = obraz.load()
    for i, j in zakres(w, h):
        pixele[i, j] = int(to[pixele[i, j]]*255)
        
histogram_equalization(obr3)
obr3.save('equalized.jpg')
obr3.show()

###zad 6

obr4 = obr.copy()
obr4 = ImageOps.equalize(obr4)

obr4.save('equalized1.jpg')

diff = ImageChops.difference(obr3,obr4)
diff.show()

hist2 = obr3.histogram()
hist3 = obr4.histogram()

plt.subplot(1,2,1)
plt.plot(range(256), hist2[:256])
plt.subplot(1,2,2)
plt.plot(range(256), hist3[:256])
plt.show()


statystyki(obr3)
statystyki(obr4)

###zad 7
detailed = obr.filter(ImageFilter.DETAIL)
sharpened = obr.filter(ImageFilter.SHARPEN)
contoured = obr.filter(ImageFilter.CONTOUR)


plt.imshow(detailed)


plt.subplot(2,2,1)
plt.imshow(detailed)
plt.axis('off')
plt.subplot(2,2,2)
plt.imshow(sharpened)
plt.axis('off')
plt.subplot(2,2,3)
plt.imshow(contoured)
plt.axis('off')
plt.subplot(2,2,4)
plt.imshow(obr4)
plt.axis('off')
plt.savefig('filtry.jpg')
plt.show()