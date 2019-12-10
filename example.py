from overdrive import Overdrive
from tkinter import*
from tkinter import messagebox

top = Tk()

def locationChangeCallback(addr, location, piece, speed, clockwise):
    # Print out addr, piece ID, location ID of the vehicle, this print everytime when location changed
    print("Location from " + addr + " : " + "Piece=" + str(piece) + " Location=" + str(location) + " Clockwise=" + str(clockwise))


car = Overdrive("F6:ED:77:8C:70:CA")
car.setLocationChangeCallback(locationChangeCallback) # Set location change callback to function above



car.changeSpeed(750, 1000) # Set car speed with speed = 500, acceleration = 1000
car.changeLaneRight(1000, 1000) # Switch to next right lane with speed = 1000, acceleration = 1000

def StopCar():
    car.changeSpeed(0, 100)
    msg = messagebox.showinfo("Car Stopped", "Car Stop Command Sent")
    
top.geometry("500x500")
B = Button(top, text="Stop Car", command=StopCar)
B.place(x = 50, y = 50)
top.mainloop()
