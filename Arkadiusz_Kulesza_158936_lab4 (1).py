from PIL import Image
import numpy as np
# zadanie 1
# funkcja rozkłada odcienie szarości tak aby kazy kolejny pasek miał inny odcień gradientu.
def paski_szare(w, h, dzielnik):
    t = (h, w)
    tab = np.ones(t, dtype=np.uint8)
    grub = int(w/dzielnik)
    k = 0
    for y in range(w):
        for x in range(h):
            if y in range(k*(grub), ((k+1)*(grub))):
                tab[x][y] = (255//grub) * k
            if y == ((k+1)*(grub)):
                k += 1
    return tab

tab = paski_szare(600, 400, 20)
paski = Image.fromarray(tab)  
paski.show()
#paski.save("zad1.jpg")

def paski_szare_negatyw(w, h, tab):
    t = (h, w)
    tab_temp = np.zeros(t, dtype=np.uint8)
    for y in range(w):
        for x in range(h):
            tab_temp[x][y] += (255 - int(tab[x][y]))
            # print (tab_temp[x][y])
    return tab_temp

tab_n = paski_szare_negatyw(600, 400, tab)
paski_n = Image.fromarray(tab_n)  
paski_n.show()
#paski_n.save("zad1_n.jpg")

# zadanie 2
# rysuje na przemian zaczynajac od czerwonego kończąc na zielonym
def zad2(w,h,dzielnik):
    nazwa="obraz1 "+str(w)+"x"+str(h)+"x"+str(dzielnik)+".bmp"
    t = (h, w, 3)  
    tab = np.zeros(t, dtype=np.uint8) 
    g = int(min(w, h) / dzielnik) 
    ilosc_ramek = h // g

    for i in range(ilosc_ramek+1):
        print(i)
        z1 = h - (g * i)
        z2 = w - (g * i)
        if i % 2 == 0:
            tab[g*i:z1 ,g*i:z2] = [255,0,0]  
        else:
            tab[g*i:z1 , g*i:z2] = [0,255,0]
    return tab        

tab_color = zad2(600, 400, 60)
ramka = Image.fromarray(tab_color)
ramka.show()
#im_ramka.save("zad2.jpg")

def rysuj_ramke_negatyw(w, h, tab):
    t = (h, w, 3)
    tab_temp = np.zeros(t, dtype=np.uint8)
    for y in range(w):
        for x in range(h):
            tab_temp[x][y][0] = 255 - tab[x][y][0]
            tab_temp[x][y][1] = 255 - tab[x][y][1]
            tab_temp[x][y][2] = 255 - tab[x][y][2]
    return tab_temp

tab_n = rysuj_ramke_negatyw(600, 400, tab_color)
ramka_n = Image.fromarray(tab_n)
ramka_n.show()
#ramka_n.save("zad2_n.jpg")

# zadanie 3

def zad3(plik, dzielnik):
    im = Image.open(plik)
    matrix = np.array(im)
    w, h = im.size
    t = (h, w, 3)
    k = 0
    tab = np.zeros(t, dtype=np.uint8)
    grub = int(w / dzielnik)
    for x in range(h):
        for y in range(w):
            if x in range(2*k*(grub), ((2*k+1)*(grub))) and matrix[x, y] == 0:
                tab[x][y] = [255, 0, 0]
            elif x in range((2*k+1)*(grub), ((2*k+2)*(grub))) and matrix[x, y] == 0:
                tab[x][y] = [0, 0, 255]
            elif x not in range(2*k*(grub), ((2*k+1)*(grub))) and x not in range((2*k+1)*(grub), ((2*k+2)*(grub))) and matrix[x, y] == 0:
                tab[x][y] = [0, 255, 0]
            else:
                tab[x][y] = [255, 255, 255]
        if x == ((2*k+1)*(grub)):
            k += 1
    return tab


tab = zad3("inicjały.bmp", 20)
inicjały = Image.fromarray(tab)  
inicjały.show()
#inicjały.save("zad3.jpg")