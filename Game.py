from calendar import c
import turtle
wn = turtle.Screen()

# Game-plate colours

wn.bgcolor("sky blue")
pl= turtle.Turtle()
pl.color("blue")

# X and O build-functions

def X (a,b):
  pl.color("red")
  pl.goto(a-k,b+k)
  pl.pendown()
  pl.goto(a+k,b-k)
  pl.penup()
  pl.goto(a-k,b-k)
  pl.pendown()
  pl.goto(a+k,b+k)
  
def O (a,b):
  pl.color("green")
  pl.goto(a-2*f,b-f)
  pl.pendown()
  pl.goto(a-2*f,b+f)
  pl.goto(a-f,b+f*2)
  pl.goto(a+f,b+f*2)
  pl.goto(a+f*2,b+f)
  pl.goto(a+f*2,b-f)
  pl.goto(a+f,b-f*2)
  pl.goto(a-f,b-f*2)
  pl.goto(a-f*2,b-f)  
 
# Gameplay function 

def S(x,y):
  global j
  x=int(x+L//2)
  y=int(-(y-H//2-1))
  cn=(x//w)
  rn=(y//h)
  x_O=(-(L-w)//2)
  y_O=(+(H-h)//2)
  x=x_O+cn*w
  y=y_O+(-rn)*h
  j=j*(-1)
  pl.penup()
  if j<0:
    X(x,y)
    D[rn][cn]=1
    if CK(rn,cn,1) == 1:
      print (chr(7),"The winner is X") 
  else:
    O(x,y)
    D[rn][cn]=2
    if CK(rn,cn,2) == 1:
      print (chr(7),"The winner is O")  
       
# Win check function    
   
def CK(rn,cn,n):
  # check -
  g=cn+1
  wc=1
  while g<c  and  D[rn][g]==n:
      wc+=1
      g+=1
  g=cn-1
  while g>=0  and  D[rn][g]==n:
      wc+=1
      g-=1
  if wc >= win :
      return 1
  # check |   
  wc=1     
  g=rn+1     
  while g<r  and  D[g][cn]==n:
      wc+=1
      g+=1
  g=rn-1
  while g>=0  and  D[g][cn]==n:
      wc+=1
      g-=1
  if wc >= win :
      return 1
  # check \ 
  wc=1
  g1=rn-1
  g2=cn-1
  while g1>=0  and  g2>=0  and  D[g1][g2]==n:
      wc+=1
      g1-=1
      g2-=1
  g1=rn+1
  g2=cn+1
  while g1<r  and  g2<c  and  D[g1][g2]==n:
      wc+=1
      g1+=1
      g2+=1
  if wc >= win :
      return 1 
  # check / 
  wc=1
  g1=rn-1
  g2=cn+1
  while g1>=0  and  g2<c  and  D[g1][g2]==n:
      wc+=1
      g1-=1
      g2+=1
  g1=rn+1
  g2=cn-1
  while g1<r  and  g2>=0  and  D[g1][g2]==n:
      wc+=1
      g1+=1
      g2-=1
  if wc >= win :
    return 1

#*******
# main *
#*******
j=1
h=int(input('slot height = '))
w=int(input('slot width = '))
c=int(input('columns number = '))
r=int(input('rows number = '))
win=int(input('winning streak length = '))
L=w*c
H=h*r-1
a=-L//2
b=H//2
if h<=w:
   m=h
else:
   m=w
k=m/3
f=m/5

# Table building

for i in range (r+1):
  pl.penup()
  pl.goto(a,b)
  pl.pendown()   
  pl.forward(L)
  b-=h

pl.right(90)
b=H//2
for i in range (c+1):
  pl.penup()
  pl.goto(a,b)
  pl.pendown()   
  pl.forward(H)
  a+=w

# The computerized table array
   
D=[]
for ir in range(r):
  dr=[]
  for ic in range(c):
    dr.append (0)
  D.append(dr)  
 
wn.onclick(S)   
wn = turtle.Screen()

# Game-plate colours

wn.bgcolor("sky blue")
pl= turtle.Turtle()
pl.color("blue")

# X and O build-functions

def X (a,b):
 pl.color("red")
 pl.goto(a-k,b+k)
 pl.pendown()
 pl.goto(a+k,b-k)
 pl.penup()
 pl.goto(a-k,b-k)
 pl.pendown()
 pl.goto(a+k,b+k)
  
def O (a,b):
 pl.color("green")
 pl.goto(a-2*f,b-f)
 pl.pendown()
 pl.goto(a-2*f,b+f)
 pl.goto(a-f,b+f*2)
 pl.goto(a+f,b+f*2)
 pl.goto(a+f*2,b+f)
 pl.goto(a+f*2,b-f)
 pl.goto(a+f,b-f*2)
 pl.goto(a-f,b-f*2)
 pl.goto(a-f*2,b-f)  
 
# Gameplay function

def S(x,y):
 global j
 x=int(x+L//2)
 y=int(-(y-H//2-1))
 cn=(x//w)
 rn=(y//h)
 x_O=(-(L-w)//2)
 y_O=(+(H-h)//2)
 x=x_O+cn*w
 y=y_O+(-rn)*h
 j=j*(-1)
 pl.penup()
 if j<0:
  X(x,y)
  D[rn][cn]=1
  if CK(rn,cn,1) == 1:
   print (chr(7),"The winner is X") 
 else:
  O(x,y)
  D[rn][cn]=2
  if CK(rn,cn,2) == 1:
   print (chr(7),"The winner is O")  
    
# Win check function   
  
def CK(rn,cn,n):
 # check -
 g=cn+1
 wc=1
 while g<c and D[rn][g]==n:
   wc+=1
   g+=1
 g=cn-1
 while g>=0 and D[rn][g]==n:
   wc+=1
   g-=1
 if wc >= win :
   return 1
 # check |  
 wc=1   
 g=rn+1   
 while g<r and D[g][cn]==n:
   wc+=1
   g+=1
 g=rn-1
 while g>=0 and D[g][cn]==n:
   wc+=1
   g-=1
 if wc >= win :
   return 1
 # check \ 
 wc=1
 g1=rn-1
 g2=cn-1
 while g1>=0 and g2>=0 and D[g1][g2]==n:
   wc+=1
   g1-=1
   g2-=1
 g1=rn+1
 g2=cn+1
 while g1<r and g2<c and D[g1][g2]==n:
   wc+=1
   g1+=1
   g2+=1
 if wc >= win :
   return 1 
 # check / 
 wc=1
 g1=rn-1
 g2=cn+1
 while g1>=0 and g2<c and D[g1][g2]==n:
   wc+=1
   g1-=1
   g2+=1
 g1=rn+1
 g2=cn-1
 while g1<r and g2>=0 and D[g1][g2]==n:
   wc+=1
   g1+=1
   g2-=1
 if wc >= win :
  return 1

#*******
# main *
#*******
j=1
h=int(input('slot height = '))
w=int(input('slot width = '))
c=int(input('columns number = '))
r=int(input('rows number = '))
win=int(input('winning streak length = '))
L=w*c
H=h*r-1
a=-L//2
b=H//2
if h<=w:
  m=h
else:
  m=w
k=m/3
f=m/5

# Table building

for i in range (r+1):
 pl.penup()
 pl.goto(a,b)
 pl.pendown()  
 pl.forward(L)
 b-=h

pl.right(90)
b=H//2
for i in range (c+1):
 pl.penup()
 pl.goto(a,b)
 pl.pendown()  
 pl.forward(H)
 a+=w

# The computerized table array
  
D=[]
for ir in range(r):
 dr=[]
 for ic in range(c):
  dr.append (0)
 D.append(dr)  
 
wn.onclick(S)  
turtle.mainloop()

