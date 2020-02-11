import math
import numpy

def hitungWaktu(height,gravity):
    waktu = math.sqrt((2*(-height))/gravity)
    return waktu 

def tampilData(const_gravity,ketinggian,time,timeStep): 
    print("")
    print("T      P       V ")
    print(0.0," ",10.0," ",0.0)
    posisiEuler = ketinggian
    kecepatanEuler = 0
    iterasi = 0
    while True:
        hitungKecepatan = kecepatanEuler+(const_gravity*timeStep)
        hitungPosisi = posisiEuler+hitungKecepatan*timeStep
        posisiEuler = hitungPosisi
        kecepatanEuler = hitungKecepatan
        print(round(iterasi+timeStep,3)," ",round(posisiEuler,3)," ",round(kecepatanEuler,2))
        iterasi += timeStep
        if(posisiEuler < 0):
            break
    pilihan = str(input("Ingin Kembali Ke Awal (Y/N) "))
    if(pilihan == "Y"):
        main()

def main() :
    const_gravity = -9.8
    ketinggian = int(input("Masukkan Ketinggian Awal :"))
    timeStep = float(input("Masukkan Nilai Timestep :"))
    time = hitungWaktu(ketinggian,const_gravity)
    tampilData(const_gravity,ketinggian,time,timeStep)
    
        

if __name__ == "__main__": 
    main()