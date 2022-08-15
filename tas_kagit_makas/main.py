#taş>makas
#makas>kağıt
#kağıt>taş
from cgitb import text
import random
from tkinter import *

#pencere ayarlanması
ekran = Tk()
ekran.geometry('400x400')
ekran.resizable(0,0)
ekran.title('Taş-Kağıt-Makas')
ekran.config(bg='seashell3')

#başlık
Label(ekran, text='tas, kagıt, makas', font='arial 20 bold', bg='seashell2').pack()

 
#oyuncu seçimi
user_take= StringVar()
Label(ekran, text = 'tercihinizi yapın: tas, kagit, makas', font='arial 15 bold', bg='seashell2').place(x=20,y=70)
Entry(ekran, font ='arial 15', textvariable= user_take, bg='antiquewhite2').place(x=90,y=130)

#karşılaşma
sonuc = StringVar()

def oyun():
   
        #bilgisayar tercihi
        pc_tercih= random.randint(1,3)
        if pc_tercih == 1:
            pc_tercih = 'tas'
        elif pc_tercih == 2:
            pc_tercih = 'kagit'
        elif pc_tercih == 3:
            pc_tercih = 'makas'

        oyuncu_tercih = user_take.get()
        if oyuncu_tercih == 'tas' and pc_tercih == 'tas':
            sonuc.set('Berabere, rakip tas seçti')
        elif oyuncu_tercih == 'tas' and pc_tercih == 'makas':
            sonuc.set('Kazandın, rakip makas seçti')
        elif oyuncu_tercih == 'tas' and pc_tercih == 'kagit':
            sonuc.set('Kaybettin, rakip kagıt seçti')
            

        elif oyuncu_tercih == 'makas' and pc_tercih == 'makas':
            sonuc.set('Berabere, rakip makas seçti')
        elif oyuncu_tercih == 'makas' and pc_tercih == 'kagit':
            sonuc.set('Kazandın, rakip kagıt seçti')
        elif oyuncu_tercih == 'makas' and pc_tercih == 'tas':
            sonuc.set('Kaybettin, rakip tas seçti')
          

        elif oyuncu_tercih == 'kagit' and pc_tercih == 'kagit':
            sonuc.set('Berabere, rakip kagıt seçti')
        elif oyuncu_tercih == 'kagit' and pc_tercih == 'makas':
            sonuc.set('Kaybettin, rakip makas seçti')
        elif oyuncu_tercih == 'kagit' and pc_tercih == 'tas':
            sonuc.set('Kazandın, rakip tas seçti')
           
    
        else: 
            sonuc.set('hatalı tercih: tas, makas veya kagit seçin')

def Sifirla():
    sonuc.set("")
    user_take.set("")

def Exit():
    ekran.destroy()

Entry(ekran, font = 'arial 10 bold', textvariable = sonuc, bg ='antiquewhite2',width = 50,).place(x=25, y = 250)
Button(ekran, font = 'arial 13 bold', text = 'Oyna'  ,padx =5,bg ='seashell4' ,command = oyun).place(x=150,y=190)
Button(ekran, font = 'arial 13 bold', text = 'Sıfırla'  ,padx =5,bg ='seashell4' ,command = Sifirla).place(x=70,y=310)
Button(ekran, font = 'arial 13 bold', text = 'Çıkış'  ,padx =5,bg ='seashell4' ,command = Exit).place(x=230,y=310)
ekran.mainloop()


