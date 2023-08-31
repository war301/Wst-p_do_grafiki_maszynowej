from PIL import Image, ImageOps
import numpy as np
from PIL import ImageChops
import matplotlib.pyplot as plt

obraz = Image.open('krajobraz.jpg')
w, h = obraz.size
obraz.show()

#zad2
t = np.array(obraz)

t_r = t[:, :, 0]
im_r = Image.fromarray(t_r)
im_r.show()

t_g = t[:, :, 1]
im_g = Image.fromarray(t_g)
im_g.show()

t_b = t[:, :, 2]
im_b = Image.fromarray(t_b)
im_b.show()

#zad3

r, g, b = obraz.split()
r.show()
g.show()
b.show()

#zad4

obraz4 = Image.merge('RGB', (im_r, g, b))
obraz4.show()

#zad4.1

obraz4_1 = ImageChops.difference(obraz4, obraz)
obraz4_1.show()
# obraz_4_1 jest cały w czarnym kolorze co oznacza, że nie ma różnic pomiędzy dwoma obrazami

#zad4.2

porownanie = np.array(obraz4) == np.array(obraz)
czy_rowne = porownanie.all()
print(czy_rowne)
# obrazy są równe

#zad5

def rysuj_ramke(w, h, dzielnik):
    t = (h, w)  
    tab = np.zeros(t, dtype=np.uint8) 
    grub = int(min(w, h) / dzielnik)  
    z1 = h - grub
    z2 = w - grub
    tab[grub:z1,  grub:z2] = 1  
    return tab * 255

tab = rysuj_ramke(w,h,50)

obraz5 = Image.fromarray(tab)
obraz5.save('zadanie5.jpg')
obraz5.show()

obraz5_m = Image.merge('RGB', (obraz5, im_g, b))
obraz5_m.save('zadanie5_m1.jpg')
obraz5_m.show()

obraz5_m = Image.merge('RGB', (im_r, obraz5, b))
obraz5_m.save('zadanie5_m2.jpg')
obraz5_m.show()

obraz5_m = Image.merge('RGB', (im_r, g, obraz5))
obraz5_m.save('zadanie5_m3.jpg')
obraz5_m.show()

obraz5_m = Image.merge('RGB', (obraz5, b, im_g))
obraz5_m.save('zadanie5_m4.jpg')
obraz5_m.show()

obraz5_m = Image.merge('RGB', (b, obraz5, im_r))
obraz5_m.save('zadanie5_m5.jpg')
obraz5_m.show()

obraz5_m = Image.merge('RGB', (g, im_r, obraz5))
obraz5_m.save('zadanie5_m6.jpg')
obraz5_m.show()

#zad6

w1 = 0.5
w2 = 0.8
w3 = 0.2
szary = w1 * t_r + w2 * t_g + w3 * t_b
szary = szary.astype(np.uint8)
szary_im = Image.fromarray(szary)
szary_im.save('zadanie_6.jpg')
szary_im.show()

#zad7

lewo= Image.open('123.jpg')
gora = Image.open('321.jpg')
prawo = Image.open('1234.jpg')

lewo1=lewo.convert('L')
gora1=gora.convert('L')
prawo1=prawo.convert('L')

merge1 = Image.merge('RGB',(lewo,prawo,gora))
merge2 = Image.merge('RGB',(lewo,gora,prawo))
merge3 = Image.merge('RGB',(prawo,gora,lewo))
merge4 = Image.merge('RGB',(gora,prawo,lewo))
merge5 = Image.merge('RGB',(prawo,lewo,gora))
merge6 = Image.merge('RGB',(gora,lewo,prawo))
merge1.show()


plt.figure(figsize=(w,h))
plt.subplot(2,3,1)
plt.imshow(merge1)
plt.axis('off')
plt.subplot(2,3,2)
plt.imshow(merge2)
plt.axis('off')
plt.subplot(2,3,3)
plt.imshow(merge3)
plt.axis('off')
plt.subplot(2,3,4)
plt.imshow(merge4)
plt.axis('off')
plt.subplot(2,3,5)
plt.imshow(merge5)
plt.axis('off')
plt.subplot(2,3,6)
plt.imshow(merge6)
plt.axis('off')
plt.subplots_adjust(wspace=0.05, hspace=0.05)
plt.show()

