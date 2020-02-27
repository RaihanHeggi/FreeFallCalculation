import matplotlib.pyplot as plt
import matplotlib.animation as animation
import math

fig = plt.figure()
ax = plt.axes(xlim=(0,0),ylim=(0,100))
line, = ax.plot([], [])

const_gravity = -9.8
height = int(input("Masukkan Ketinggian : "))
timeStep = float(input("Masukkan TimeStep : "))
posisiSumbuY = height
iterasi = 0
time = math.sqrt((2*(-height))/const_gravity)
nilaiV = 0

listSumbuY = []

while True :
        iterasi += timeStep
        nilaiV += (const_gravity*timeStep)
        posisiSumbuY += nilaiV*timeStep
        listSumbuY.append(posisiSumbuY)
        if(posisiSumbuY <= 0):
            break

def init():
    line.set_data([], [])
    return line,

xdata,ydata = [], []

def animate(i):
    x = 0
    y = listSumbuY[i]

    xdata.append(x)
    ydata.append(y)
    line.set_data(xdata, ydata) 
    return line,

plt.title("Simulasi Gerak Jatuh Bebas")

anim = animation.FuncAnimation(fig, animate, init_func=init, 
							frames=1000, interval=10, blit=True)
plt.show()
