import math
import numpy

def hitungWaktu(height,gravity):
    waktu = math.sqrt((2*(-height))/gravity)
    return waktu 

def tampilData(const_gravity,ketinggian,time,timeStep): 
    print("")
    print("T      P       V ")
    for i in numpy.arange(0,time,timeStep):
        hitungPosisi = (const_gravity/2) * pow(i,2)+ketinggian
        hitungKecepatan = const_gravity * i
        print(round(i,3)," ",round(hitungPosisi,3)," ",round(hitungKecepatan,2))
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