def geometry():  
  #installing important files
  import time
  from math import pi
  import math
  
  #Login screen
  print (""" 
  
  
      xxxxxxxxxx Geometry 0.2.0 xxxxxxxxxx
        
        
    """)
  def geo():
    print("""
    Evaluate:
      1. Circle
      2. Sphere
      3. Hemisphere
      4. Cube
      5. Cuboid
      6. Cylinder
      7. Cone
      8. Exit
    """)
    x=input("==> ")
    if x =="1":
      circle()
    elif x =="2":
      sphere()
    elif x=="3":
      hsphere()
    elif x=="4":
      cube()
    elif x=="5":
      cuboid()
    elif x=="6":
      cylinder()
    elif x=="7":
      cone()
    else:
      time.sleep(1)
      print("\n xxx Exiting xxx\n")
      
  #margin line between operations
  def m():
    time.sleep(0.5)
    print("\n |---------------------|\n")
    time.sleep(0.5)
    
  #main menu function
  def back():
    time.sleep(1)
    print("\n xxx Exiting xxx\n")
    time.sleep(1)
    geo()
  
  #error function
  def error():
    time.sleep(1)
    print("\n ERROR!!!!!!!!!!\n")
    time.sleep(1)
  
  #circle
  def circle():
    m()
    def circ():
      r=int(input("\nInput radius ==> "))
      time.sleep(1)
      print("\nCircumference = "+str(2*pi*int(r)))
      time.sleep(1)
      circle()
    def area():
      r=int(input("\nInput radius ==> "))
      time.sleep(1)
      print("\nArea = "+str(pi*int(r)**2))
      time.sleep(1)
      circle()
    print("""
    Find:
      1. Circumference
      2. Area
      3. Back
        """)
    x=input("==> ")
    if x=="1":
      circ()
    elif x=="2":
      area()
    elif x=="3":
      back()
    else:
      error()
      circle()
      
  #sphere
  def sphere():
    m()
    def SA():
      r=int(input("\nInput radius ==> "))
      time.sleep(1)
      print("\nSurface area = "+str(4*pi*int(r)**3))
      time.sleep(1)
      sphere()
    def vol():
      r=int(input("\nInput radius ==> "))
      time.sleep(1)
      print("\nVolume = "+str(4/3*pi*r**3))
      time.sleep(1)
      sphere()
    print("""
    Find:
      1. Surface area
      2. Volume
      3. Back""")
    x=input("==> ")
    if x=="1":
      SA()
    elif x=="2":
      vol()
    elif x=="3":
      back()
    else:
      error()
      sphere()
  
  #hemisphere
  def hsphere():
    m()
    def CSA():
      r=int(input("\nInput radius ==> "))
      time.sleep(1)
      print("\nCurved surface area = "+str(2*pi*r**2))
      time.sleep(1)
      hsphere()
    def TSA():
      r=int(input("\nInput radius ==> "))
      time.sleep(1)
      print("\nTotal surface area = "+str(3*pi*r**2))
      time.sleep(1)
      hsphere()
    def hvol():
      r=int(input("\Input radius ==> "))
      time.sleep(1)
      print("\Volume = "+str(2/3*pi*r**3))
      time.sleep(1)
      hsphere()
    print("""
    Find:
      1. Curved surface area
      2. Total surface area
      3. Volume
      4. Back""")
    x=input("==> ")
    if x=="1":
      CSA()
    elif x=="2":
      TSA()
    elif x=="3":
      hvol()
    elif x=="4":
      back()
    else:
      error()
      hsphere()
  
  #cube
  def cube():
    m()
    def SAC():
      a=int(input("\nInput length of side ==> "))
      time.sleep(1)
      print("\nSurface area = "+str(6*a**2))
      time.sleep(1)
      cube()
    def volC():
      a=int(input("\nInput length of side ==> "))
      time.sleep(1)
      print("\nVolume = "+str(a**3))
      time.sleep(1)
      cube()
    print("""
    Find:
      1. Surface area
      2. Volume
      3. Back""")
    x=input("==> ")
    if x=="1":
      SAC()
    elif x=="2":
      volC()
    elif x=="3":
      back()
    else:
      error()
      cube()
  
  #cuboid
  def cuboid():
    m()
    def SACu():
      l=int(input("\nInput length ==> "))
      h=int(input("Input height ==> "))
      b=int(input("Input breadth ==> "))
      time.sleep(1)
      print("\nSurface area = "+str(2*(l*b+b*h+h*l)))
      time.sleep(1)
      cuboid()
    def volcu():
      l=int(input("\nInput length ==> "))
      h=int(input("Input height ==> "))
      b=int(input("Input breadth ==> "))
      time.sleep(1)
      print("\nVolume = "+str(l*b*h))
      cuboid()
    print("""
    Find:
      1. Surface area
      2. Volume
      3. Back""")
    x=input("==> ")
    if x=="1":
      SACu()
    elif x=="2":
      volcu()
    elif x=="3":
      back()
    else:
      error()
      cuboid
  
  #cylinder
  def cylinder():
    def csacy():
      r=int(input("\nInput radius ==> "))
      h=int(input("Input height ==> "))
      time.sleep(1)
      print("\nCurved surface area = "+str(2*pi*r*h))
      time.sleep(1)
      cylinder()
    def tsacy():
      r=int(input("\nInput radius ==> "))
      h=int(input("Input height ==> "))
      time.sleep(1)
      print("\nTotal surface area = "+str(2*pi*r*(h+r)))
      time.sleep(1)
      cylinder()
    def volcy():
      r=int(input("\nInput radius ==> "))
      h=int(input("Input height ==> "))
      time.sleep(1)
      print("\nVolume = "+str(pi*h*r**2))
      time.sleep(1)
      cylinder()
    print("""
    Find:
      1. Curved surface area
      2. Total surface area
      3. Volume
      4. Back""")
    x=input("==> ")
    if x=="1":
      csacy()
    elif x=="2":
      tsacy()
    elif x=="3":
      volcy()
    elif x=="4":
      back()
    else:
      error()
      cylinder()
  
  #cone
  def cone():
    m()
    def csaco():
      r=int(input("\nInput radius ==> "))
      h=int(input("Input height ==> "))
      y=h**2+r**2
      l=math.sqrt(y)
      time.sleep(1)
      print("\nCurved surface area = "+str(pi*r*l))
      time.sleep(1)
      cone()
    def tsaco():
      r=int(input("\nInput radius ==> "))
      h=int(input("Input height ==> "))
      y=h**2+r**2
      l=math.sqrt(y)
      time.sleep(1)
      print("\nTotal surface area = "+str(pi*r*(l+r)))
      time.sleep(1)
      cone()
    def volco():
      r=int(input("\nInput radius ==> "))
      h=int(input("Input height ==>"))
      y=h**2+r**2
      l=math.sqrt(y)
      time.sleep(1)
      print("\nVolume = "+str(1/3*pi*h*r**2))
      time.sleep(1)
      cone()
    print("""
    Find:
      1. Curved surface area
      2. Total surface area
      3. Volume
      4. Back""")
    x=input("==> ")
    if x=="1":
      csaco()
    elif x=="2":
      tsaco()
    elif x=="3":
      volco()
    elif x=="4":
      back()
    else:
      error()
      cone()
  
  geo()
geometry()
