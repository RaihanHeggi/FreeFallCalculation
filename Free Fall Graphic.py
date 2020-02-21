import matplotlib.pyplot
import numpy
import math
import os


def hitungPosisi(gravity,time,height,timeStep):
    listPosisi = []
    i = 0
    while i < time :
        posisi = (gravity/2)*pow(i,2)+height
        if(posisi < 0):
            break
        listPosisi.append(posisi)
        i += timeStep
    return listPosisi

def hitungKecepatan(gravity,time,timestep):
    listKecepatan = []
    i = 0
    while i < time :
        kecepatan = gravity*i
        listKecepatan.append(kecepatan)
        i += timestep
    return listKecepatan

def hitungKecepatanEuler(listKecepatan,gravity,timeStep,time):
    listKecepatanEuler = []
    listKecepatanBiasa = []
    listKecepatanBiasa.append(0)
    i = 0
    j = 0
    while i < time :
        kecepatanEuler = listKecepatanBiasa[j]+(gravity*timeStep)
        listKecepatanEuler.append(kecepatanEuler)
        listKecepatanBiasa.append(kecepatanEuler)
        i += timeStep
        j += 1
    return listKecepatanEuler

def hitungPosisiEuler(listPosisi,listKecepatanEuler,time,timeStep,height):
    ListPosisiEuler = []
    ListPosisiBiasa = []
    ListPosisiBiasa.append(10)
    i = 0
    j = 0
    while i < time :    
        posisiEuler = ListPosisiBiasa[j]+(listKecepatanEuler[j]*timeStep)
        ListPosisiBiasa.append(posisiEuler)
        ListPosisiEuler.append(posisiEuler)
        i += timeStep
        j += 1
    return ListPosisiEuler
    
def hitungWaktu(gravity,height):
    waktu = math.sqrt((2*(-height)/gravity))
    return waktu

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def showGraph(listPosisi,listKecepatan):
    matplotlib.pyplot.plot(listKecepatan,listPosisi)   
    matplotlib.pyplot.show()

def main():
    cls()
    const_gravity = -9.8
    listPosisi = []
    listKecepatan = []
    listKecepatanEuler = []
    listPosisiEuler = []
    print("=================================MENU=====================================")
    print("                           1. Mulai Aplikasi")
    print("==========================================================================")
    pilihan = int(input("Silahkan Masukkan Menu Yang Anda Butuhkan :"))
    if(pilihan == 1) :
        cls()
        ketinggian = int(input("Masukkan Ketinggian Awal Benda :"))
        timeStep = float(input("Masukkan TimeStep Pergerakan :"))
        time = hitungWaktu(const_gravity,ketinggian)
        listPosisi = hitungPosisi(const_gravity,time,ketinggian,timeStep)
        listKecepatan = hitungKecepatan(const_gravity,time,timeStep)
        listKecepatanEuler = hitungKecepatanEuler(listKecepatan,const_gravity,timeStep,time)
        listPosisiEuler = hitungPosisiEuler(listPosisi,listKecepatanEuler,time,timeStep,ketinggian)
        pilihanTampil = str(input("Ingin Menampilkan Graphic Posisi (Analytic (1) / Numerical (2))"))
        if(pilihanTampil == "1"):
            showGraph(listPosisi,listKecepatan)
        elif(pilihanTampil == "2"):
            showGraph(listPosisiEuler,listKecepatanEuler)
    else :
        print("")
        print("Menu Anda Tidak Valid")


if __name__ == "__main__":
    main()