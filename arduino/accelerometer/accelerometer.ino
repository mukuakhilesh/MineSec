#include <Wire.h>
#define accel_module (0x53)
byte values[6] ;
char output[512];
const float g=0.0037;
float net,net1,tot;
void setup() {
Wire.begin();
Serial.begin(9600);
Wire.beginTransmission(accel_module);
Wire.write(0x2D);
Wire.write(0);
Wire.endTransmission();
Wire.beginTransmission(accel_module);
Wire.write(0x2D);
Wire.write(16);
Wire.endTransmission();
Wire.beginTransmission(accel_module);
Wire.write(0x2D);
Wire.write(24);
Wire.endTransmission();
Wire.beginTransmission(accel_module);
Wire.write(0x31);
Wire.write(0);
Wire.endTransmission();

}

void loop() {
  int xyzregister = 0x32;
float x, y, z;

Wire.beginTransmission(accel_module);
Wire.write(xyzregister);
Wire.endTransmission();

Wire.beginTransmission(accel_module);
Wire.requestFrom(accel_module, 6);

int i = 0;
while(Wire.available()){
values[i] = Wire.read();
i++;
}
Wire.endTransmission();
net1=net;
x = (((int)values[1])<<8)|values[0];
y = (((int)values[3])<<8)|values[2]; 
z = (((int)values[5])<<8)|values[4];
x*=g;y*=g;z*=g;
 net=(x*x+y*y+z*z);
 tot=fabs(net-net1)*100;


  Serial.print(tot);
Serial.println("  ");
delay(600);



 
//if(fabs(net-net1)>0.07)
  //delay(2000); 
Serial.write(10);
delay(100); 
}
