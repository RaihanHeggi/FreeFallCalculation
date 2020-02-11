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
    listKecepatanEuler.append(0)
    i = 0
    j = 0
    while i < time :
        kecepatanEuler = listKecepatan[j]+(gravity*timeStep)
        listKecepatanEuler.append(kecepatanEuler)
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
        if(posisiEuler < 0):
            break
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

      
def menuTampilan(listPosisi,listKecepatan,listKecepatanEuler,listPosisiEuler,timeStep):
    cls()
    iterasi = 0
    waktuData = 0
    print("Data List Posisi Analytic:")
    while iterasi < len(listPosisi) :
        print("Posisi Analytic Pada T =",waktuData,"Adalah :",listPosisi[iterasi])
        iterasi += 1
        waktuData += timeStep
    print("")
    print("Data List Kecepatan Analytic:")
    iterasiKecepatan = 0
    waktuData = 0
    while iterasiKecepatan < len(listKecepatan) :
        print("Kecepatan Analytic Pada T =",waktuData,"Adalah :",listKecepatan[iterasiKecepatan])
        iterasiKecepatan += 1
        waktuData += timeStep
    print("")
    print("Data List Kecepatan Numerik:")
    iterasiKecepatanEuler = 0
    waktuData = 0
    while iterasiKecepatanEuler < len(listKecepatanEuler) :
        print("Kecepatan Numerik Pada T =",waktuData," Adalah :",listKecepatanEuler[iterasiKecepatanEuler])
        iterasiKecepatanEuler += 1
        waktuData += timeStep
    print("")
    print("Data List Posisi Numerik:")
    iterasiPosisiEuler = 0
    waktuData = 0
    while iterasiPosisiEuler < len(listPosisiEuler) :
        print("Posisi Numerik Pada T =",waktuData," Adalah :",listPosisiEuler[iterasiPosisiEuler])
        iterasiPosisiEuler += 1
        waktuData += timeStep
    pilihan = str(input("Kembali Ke Menu Utama (Y/N) "))
    if(pilihan == 'Y'):
        main()

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
        menuTampilan(listPosisi,listKecepatan,listKecepatanEuler,listPosisiEuler,timeStep)        
    else :
        print("")
        print("Menu Anda Tidak Valid")


if __name__ == "__main__":
    main()