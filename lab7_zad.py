from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

obraz = Image.open('krajobraz.jpg')

#zad 1
def konwertuj_na_szary(obraz, w1, w2, w3):
    w, h = obraz.size
    for i in range(w):
        for j in range(h):
            p=obraz.getpixel((i,j))
            b=int(p[0]*w1+p[1]*w2+p[2]*w3)
            obraz.putpixel((i,j),(b,b,b))

im= obraz.copy()
konwertuj_na_szary(im,0.5,0.8,0.2)   
#im.show()
im.save('obraz1.jpg')

#zad2
def szary_na_czarnobialy(obraz, wsp):
    w, h = obraz.size
    for i in range(w):
        for j in range(h):
            p=obraz.getpixel((i,j))
            b=int(p[0]/(wsp+1))*255
            obraz.putpixel((i,j),(b,b,b))

im1=Image.open('obraz1.jpg')
szary_na_czarnobialy(im1, 200)
im1_1,g,b=im1.split()
#im1_1.show()
print("tryb", im1_1.mode)

#zad3
def utnij_wartości_pikseli(obraz, wsp_min,wsp_max):
    obraz=obraz.point(lambda i:wsp_min if i <= wsp_min else (wsp_max if i >= wsp_max else i ))
    return obraz

def utnij_wartości_pikseli2(obraz, wsp_min,wsp_max):
    obraz=obraz.point(lambda i: 0 if i <= wsp_min else ( 1 if i >= wsp_max else i ))
    return obraz

im2= obraz.copy()
im2_1= obraz.copy()
im2=utnij_wartości_pikseli(im2,50,150)
im2_1=utnij_wartości_pikseli2(im2_1,50,250)
im2.show()
im2.save('obraz2.jpg')
im2_1.show()
im2.save('obraz3.jpg')

# zadanie 4

def rysuj_prostokat (obraz,m,n,a,b,kolor):
    T = np.array(obraz)
    T [m:m+a,n] = kolor
    T [m:m+a,n+b] = kolor
    T [m,n:n+b] = kolor
    T [m+a,n:n+b+1] = kolor
    im3 = Image.fromarray(T)
    im3.show()
    im3.save('obraz4.jpg')
    
rysuj_prostokat(obraz,500,750,100,120,[255,255,0])

def rysuj_kwadrat (obraz,m,n,a,kolor):
    T = np.array(obraz)
    T [m+(a//2), n-(a//2):n+(a//2)] = kolor
    T [m-(a//2), n-(a//2):n+(a//2)] = kolor
    T [m-(a//2):m+(a//2),n-(a//2)] = kolor
    T [m-(a//2):m+(a//2)+1,n+(a//2)] = kolor
    im4 = Image.fromarray(T)
    im4.show()
    im4.save('obraz5.jpg')

rysuj_kwadrat(obraz,1000,1500,60,[255,255,0])

#Zad5.1
im5 = obraz.copy()
def odbij_w_poziomie(obraz):
    obraz = np.array(obraz)
    return Image.fromarray(obraz[:, ::-1, :])

#Zad5.2
odbij_w_poziomie(im5).save('obraz6.png')

#Zad5.3
def odbij_w_pionie(obraz):
    obraz = np.array(obraz)
    return Image.fromarray(obraz[::-1,:])

#Zad5.4
im6 = obraz.copy()
odbij_w_pionie(im6).save('obraz7.png')

#Zad5.5
def  odbij_w_poziomie_przez_srodek(obraz):
    w ,h = obraz.size
    polowa = int(w/2+1)
    obraz = np.array(obraz)
    obraz[:,1:polowa,:]= obraz[:,polowa-1:w,:][:,::-1,:]
    return Image.fromarray(obraz)

#Zad5.6
im7 = obraz.copy()
odbij_w_poziomie_przez_srodek(im7).save('obraz8.png')

#Zad5.7
def  odbij_w_pionie_przez_srodek(obraz):
    w ,h = obraz.size
    polowa = int(h/2+1)
    obraz = np.array(obraz)
    obraz[1:polowa,:,:]= obraz[polowa:h,:,:][::-1,:,:]
    return Image.fromarray(obraz)

#Zad5.8
im8 = obraz.copy()
odbij_w_pionie_przez_srodek(im8).save('obraz9.png')

#zad6
T= np.array(obraz, dtype="uint8")
w,h = obraz.size
for i in range(h):
    for j in range(w):
        for k in range (0,3):
            if T[i,j,k]+100>255:
                T[i,j,k]=255
            else:
                T[i,j,k] += 100


im9 = Image.fromarray(T,"RGB")
im9.show()

#nie można przekroczyć wartości 255 na pikselu