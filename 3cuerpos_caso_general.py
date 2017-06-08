from math import *
from visual import *
from random import*
enc="CUERPO"

print(enc, "1: ")
x1=int(input("Introduce la posición en X del cuerpo 1: "))
y1=int(input("Introduce la posición en Y del cuerpo 1: "))
z1=int(input("Introduce la posición en Z del cuerpo 1: "))
print(enc, "2: ")
x2=int(input("Introduce la posición en X del cuerpo 2: "))
y2=int(input("Introduce la posición en Y del cuerpo 2: "))
z2=int(input("Introduce la posición en Z del cuerpo 2: "))
print(enc, "3: ")
x3=int(input("Introduce la posición en X del cuerpo 3: "))
y3=int(input("Introduce la posición en Y del cuerpo 3: "))
z3=int(input("Introduce la posición en Z del cuerpo 3: "))
print("MASAS CUERPO", enc, "1: ")
m1=int(input("Introduce la masa del cuerpo 1: "))
m2=int(input("Introduce la masa del cuerpo 2: "))
m3=int(input("Introduce la masa del cuerpo 3: "))
vi1x=int(input("Introduce la velocidad en x del cuerpo 1: "))
vi1y=int(input("Introduce la velocidad en y del cuerpo 1: "))
vi1z=int(input("Introduce la velocidad en z del cuerpo 1: "))
vi2x=int(input("Introduce la velocidad en x del cuerpo 2: "))
vi2y=int(input("Introduce la velocidad en y del cuerpo 2: "))
vi2z=int(input("Introduce la velocidad en z del cuerpo 2: "))
vi3x=int(input("Introduce la velocidad en x del cuerpo 3: "))
vi3y=int(input("Introduce la velocidad en y del cuerpo 3: "))
vi3z=int(input("Introduce la velocidad en z del cuerpo 3: "))
radio1=int(input("Introduce el radio del cuerpo 1: "))
radio2=int(input("Introduce el radio del cuerpo 2: "))
radio3=int(input("Introduce el radio del cuerpo 3: "))
ttotal=100e45
dt=.0002
t=0
G=4.478976e-10

xaxis = curve(pos=[(0,0,0), (1e9,0,0)], color=(0.5,0.5,0.5))
yaxis = curve(pos=[(0,0,0), (0,1e9,0)], color=(0.5,0.5,0.5))
zaxis = curve(pos=[(0,0,0), (0,0,1e9)], color=(0.5,0.5,0.5))

p1=sphere(pos=(x1,y1,z1), radius=radio1,color=color.orange, make_trail=true)
p2=sphere(pos=(x2,y2,z2), color=color.cyan, make_trail=true,radius=radio2)
p3=sphere(pos=(x3,y3,z3), radius=radio3,color=color.red, make_trail=true)

while(t<ttotal):
    rate(1e308)
    
    r12=sqrt((x2-x1)**2+(y2-y1)**2+(z2-z1)**2)
    r13=sqrt((x3-x1)**2+(y3-y1)**2+(z3-z1)**2)
    r23=sqrt((x2-x3)**2+(y2-y3)**2+(z2-z3)**2)
    if (r12<=(radio1+radio2)):
        vi1x=0
        vi1y=0
        vi1z=0
        vi2x=0
        vi2y=0
        vi2z=0
    elif (r13<=(radio1+radio3)):
        vi1x=0
        vi1y=0
        vi1z=0
        vi3x=0
        vi3y=0
        vi3z=0
    elif (r23<=(radio3+radio2)):
        vi3x=0
        vi3y=0
        vi3z=0
        vi2x=0
        vi2y=0
        vi2z=0
    ax1=G*(((m2*(x2-x1))/r12**3)+(m3*(x3-x1))/r13**3)
    ay1=G*(((m2*(y2-y1))/r12**3)+(m3*(y3-y1))/r13**3)
    az1=G*(((m2*(z2-z1))/r12**3)+(m3*(z3-z1))/r13**3)

    ax2=G*(((m1*(x1-x2))/r12**3)+(m3*(x3-x2))/r23**3)
    ay2=G*(((m1*(y1-y2))/r12**3)+(m3*(y3-y2))/r23**3)
    az2=G*(((m1*(z1-z2))/r12**3)+(m3*(z3-z2))/r23**3)

    ax3=G*(((m2*(x2-x3))/r23**3)+(m1*(x1-x3))/r13**3)
    ay3=G*(((m2*(y2-y3))/r23**3)+(m1*(y1-y3))/r13**3)
    az3=G*(((m2*(z2-z3))/r23**3)+(m1*(z1-z3))/r13**3)
    
    
    xf1=x1+vi1x*dt+((1/2)*ax1*dt**2)
    yf1=y1+vi1y*dt+((1/2)*ay1*dt**2)
    zf1=z1+vi1z*dt+((1/2)*az1*dt**2)
    xf2=x2+vi2x*dt+((1/2)*ax2*dt**2)
    yf2=y2+vi2y*dt+((1/2)*ay2*dt**2)
    zf2=z2+vi2z*dt+((1/2)*az2*dt**2)
    xf3=x3+vi3x*dt+((1/2)*ax3*dt**2)
    yf3=y3+vi3y*dt+((1/2)*ay3*dt**2)
    zf3=z3+vi3z*dt+((1/2)*az3*dt**2)
    v1x=vi1x+ax1*dt
    v1y=vi1y+ay1*dt
    v1z=vi1z+az1*dt
    v2x=vi2x+ax2*dt
    v2y=vi2y+ay2*dt
    v2z=vi2z+az2*dt
    v3x=vi3x+ax3*dt
    v3y=vi3y+ay3*dt
    v3z=vi3z+az3*dt
    #actualizaciones
    vi1y=v1y
    vi1x=v1x
    vi1z=v1z
    vi2x=v2x
    vi2y=v2y
    vi2z=v2z
    vi3y=v3y
    vi3x=v3x
    vi3z=v3z
    x1=xf1
    y1=yf1
    z1=zf1
    x2=xf2
    y2=yf2
    z2=zf2
    x3=xf3
    y3=yf3
    z3=zf3
    p1.pos.x=x1
    p1.pos.y=y1
    p1.pos.z=z1
    p2.pos.x=x2
    p2.pos.y=y2
    p2.pos.z=z2
    p3.pos.x=x3
    p3.pos.y=y3
    p3.pos.z=z3
    #print(p1.pos, "PARTICULA 1")
    #print(p2.pos, "PARTICULA 2")
    #print(p3.pos, "PARTICULA 3")
    print("velocidades en cada instante de tiempo partícula de tiempo\n", v1x,v1y,v1z)
    print("velocidades en cada instante de tiempo partícula de tiempo\n", v2x,v2y,v2z)
    print("velocidades en cada instante de tiempo partícula de tiempo\n", v3x,v2y,v3z)
    
    t=t+dt
        
        
  
        
    




