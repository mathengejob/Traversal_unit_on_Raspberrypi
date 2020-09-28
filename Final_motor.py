#Importing needed header (support files)
from gpiozero import LED
from gpiozero import Button
from time import sleep

# Delcaring pins for motor and limit switches
#Buttons
limit_top=Button(3)
limit_bottom=Button(2)
#inputs
m_input1= LED(16)
m_input2= LED(17)
home=False 
if limit_top.is_pressed:
    m_input1.off()
    m_input2.on()
   
else:
    m_input1.on()
    m_input2.off()
while (True):
    
    if (home==False):
        if limit_top.is_pressed:
            m_input1.off()
            m_input2.off()
            print("Home ")
            sleep(5)
            home=not home
        else:
            m_input1.on()
            m_input2.off()
            print("Homing")

    else:
        if limit_bottom.is_pressed:
            m_input1.off()
            m_input2.off()
            print ("Dropped")
            sleep(5)
            home=not home
        else:
            m_input1.off()
            m_input2.on()
            print("Dropping")
        
        

    
def toggle():
   global homing
   running = not running

