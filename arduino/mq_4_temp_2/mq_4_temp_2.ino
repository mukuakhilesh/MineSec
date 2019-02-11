/*
 Arduino MQ4 gas sensor - Geekstips.com
 This example is to calculate the gas concentration using the R0
 calculated in the example above
 Also a OLED SSD1306 screen is used to display data, if you do not
 have such a display, just delete the code used for displaying
*/ 
#define accel_module (0x53)
#include <Wire.h> //Library for I2C interface 
#include <math.h>



int gas_sensor = A1; //Sensor pin
float m = -0.318; //Slope
//float b = 1.133; //Y-Intercept
float R0 = 18.16; //Sensor Resistance in fresh air from previous code
float temp;
int pin = A5;
float a = 1041.333;
float b = -2.729007;
byte values[6] ;
char output[512];
const float g=0.0037;
float net,net1,tot,tot1,final;

void setup() {
Serial.begin(9600); //Baud rat
Wire.begin();
Wire.beginTransmission(accel_module);
Wire.write(0x2D);
Wire.write(24);
Wire.endTransmission();
Wire.beginTransmission(accel_module);
Wire.write(0x31);
Wire.write(0);
Wire.endTransmission();


  pinMode(gas_sensor, INPUT); //Set gas sensor as input
}

void loop() {
  
  float sensor_volt; //Define variable for sensor voltage
  float RS_gas; //Define variable for sensor resistance
  float ratio; //Define variable for ratio
  float sensorValue = analogRead(gas_sensor); //Read analog values of sensor
  sensor_volt = sensorValue * (5.0 / 1023.0); //Convert analog values to voltage
  RS_gas = ((5.0 * 10.0) / sensor_volt) - 10.0; //Get value of RS in a gas
  ratio = RS_gas / R0;   // Get ratio RS_gas/RS_air
  //Serial.print("ratio");
  //Serial.print(ratio);


 // double ppm_log = (log10(ratio) - b) / m; //Get ppm value in linear scale according to the the ratio value
 // double ppm = pow(10, ppm_log); //Convert ppm value to log scale
  double ppm = a*pow(ratio , b);
  
  
  double percentage = ppm / 10000; //Convert to percentage
  //Serial.print("\t");
  //Serial.print(percentage); //Load screen buffer with percentage value
  //Serial.println("%"); //Load screen buffer with "%"
  delay(200);
  

  //TEMPERATURE

    // put your main code here, to run repeatedly:
    temp = analogRead(pin);
    temp = temp*500/1024;
    temp = (temp-32)*5/9;
    
    delay(100);
    //accelerometer
//for(int j=0;j<10;j++){ 
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
tot1=tot;
x = (((int)values[1])<<8)|values[0];
y = (((int)values[3])<<8)|values[2]; 
z = (((int)values[5])<<8)|values[4];
x*=g;y*=g;z*=g;
 net=(x*x+y*y+z*z);
 tot=fabs(net-net1);
//if(fabs(net-net1)>0.07)
/// if(tot>tot1)
  //final=tot;
Serial.write(10); 
delay(1); 
//}



    //prints
    //Serial.print("ppm = ");
    Serial.print(ppm);
    Serial.print("  ");
    Serial.print(temp);
    Serial.print("  ");
    Serial.print(tot);
    Serial.println("  ");
    delay(1000);
  
}

 
