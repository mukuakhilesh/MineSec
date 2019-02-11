import serial

ser2 = serial.Serial("/dev/ttyACM1" , 9600)

ser2.flush()
b=ser2.readline()
print("p1")
print(b)
b=b.decode("UTF-8")
print("p2")
print(b)
if b>0:
    co = float(b)  