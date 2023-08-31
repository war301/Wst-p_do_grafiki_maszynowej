from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

def zakres(w, h): 
    return [(i, j) for i in range(w) for j in range(h)]

def wstaw_inicjaly(obraz,inicjaly, m, n,kolor):  
    w, h = inicjaly.size
    for i, j in zakres(w, h):
        if inicjaly.getpixel((i, j)) == 0:
            obraz.putpixel((i + m, j + n), (kolor))
    return obraz

def wstaw_inicjaly_maska(obraz, inicjaly, m, n, a, b, c): 
    w, h = inicjaly.size
    for i, j in zakres(w, h):
        if inicjaly.getpixel((i, j)) == 0:
            p = obraz.getpixel((i + m, j + n))
            obraz.putpixel((i + m, j + n), (p[0] + a, p[1] + b, p[2] + c))
    return obraz    

def wstaw_inicjaly_load(obraz,inicjaly, m, n,kolor): 
    tab =np.array(inicjaly)
    w, h = tab.shape
    pixele = inicjaly.load()
    pixele1 = obraz.load()
    for i in range(h):
        for j in range(w):
            if( pixele[i, j] == 0):
                pixele1[i+m,j+n] = kolor

def wstaw_inicjaly_maska_load(obraz,inicjaly,m,n,x,y,z): 
    tab =np.array(inicjaly)
    w, h = tab.shape
    pixele = inicjaly.load()
    pixele1 = obraz.load()
    for i in range(h):
        for j in range(w):
            if( pixele[i, j] == 0):
                p = pixele1[i+m,j+n]
                pixele1[i+m,j+n] = (p[0]+x,p[1]+y,p[2]+z)

def zastosuj_funkcje(image, func):
    w, h = image.size
    pixele = image.load()
    for i, j in zakres(w, h):
        pixele[i, j] = func(pixele[i, j])

def kontrast(obraz,wsp_kontrastu):
    mn =((255 + wsp_kontrastu)/255)**2
    obraz=obraz.point(lambda i:128 + (i-128)*mn)
    return obraz

def negatyw(obraz):
    obraz=obraz.point(lambda i:255-i)
    return obraz

def transformacja_logarytmiczna(obraz):
    obraz=obraz.point(lambda i:255*np.log(1+i/255))
    return obraz

def transformacja_gamma(obraz, gamma):
    obraz=obraz.point(lambda i:(i/255)**(1/gamma)*255)
    return obraz

def utnij_wartości_pikseli(obraz, wsp_min,wsp_max):
    obraz=obraz.point(lambda i:i > wsp_min and wsp_max)
    return obraz

im = Image.open('krajobraz.jpg')
print("tryb obrazu", im.mode)
print("rozmiar", im.size)        
    
inicjaly=Image.open('inicjały.bmp')
print("tryb obrazu", inicjaly.mode)
print("rozmiar", inicjaly.size)

im1= im.copy()
plt.title("zad2_1_A")
plt.imshow(wstaw_inicjaly(im1,  inicjaly, 857, 591, (0, 255, 0)))
#plt.show()
#im1.save('zad2_1_A.jpg')
im1.save("im1.jpg")

im2= im.copy()
plt.title("zad2_1_B")
plt.imshow(wstaw_inicjaly(im2,  inicjaly, 1590, 1120, (255, 0, 0)))
#plt.show()
#im2.save('zad2_1_B.jpg')
im2.save("im2.jpg")

im3= im.copy()
plt.title("zad2_2_A")
plt.imshow(wstaw_inicjaly_maska(im3,  inicjaly, 857, 591, 0, 255, 0))
#plt.show()
#im3.save('zad2_2_A.jpg')
im3.save("im3.jpg")


im4= im.copy()
plt.title("zad2_2_B")
plt.imshow(wstaw_inicjaly_maska(im4,  inicjaly, 1590, 0, 0, 0, 255))
#plt.show()
#im4.save('zad2_2_B.jpg')
im4.save("im4.jpg")

im5= im.copy()
wstaw_inicjaly_load(im5,  inicjaly, 850, 580,(255,0,0))
plt.title("zad_3_A")
#plt.imshow(im5)
#plt.show()
im5.save("im5.jpg")

im6= im.copy()
wstaw_inicjaly_maska_load(im6,  inicjaly, 850, 580,0,255,0)
plt.title("zad_3_B")
#plt.imshow(im6)
#plt.show()
im6.save("im6.jpg")

im7= im.copy()
im7=kontrast(im7,100)
plt.title("zad_4_A")
#plt.imshow(im7)
#plt.show()
im7.save("im7.jpg")

im8= im.copy()
im8=negatyw(im8)
plt.title("zad_4_B")
#plt.imshow(im8)
#plt.show()
im8.save("im8.jpg")

im9= im.copy()
im9=transformacja_logarytmiczna(im9)
plt.title("zad_4_C")
#plt.imshow(im9)
#plt.show()
im9.save("im9.jpg")

im10= im.copy()
im10=transformacja_gamma(im10,5)
plt.title("zad_4_D")
#plt.imshow(im10)
#plt.show()
im10.save("im10.jpg")

im11= im.copy()
im11=utnij_wartości_pikseli(im11,50,250)
plt.title("zad_4_D")
#plt.imshow(im11)
#plt.show()
im11.save("im11.jpg")