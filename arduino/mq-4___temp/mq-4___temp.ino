/*
 Arduino MQ4 gas sensor - Geekstips.com
 This example is to calculate the gas concentration using the R0
 calculated in the example above
 Also a OLED SSD1306 screen is used to display data, if you do not
 have such a display, just delete the code used for displaying
*/



#include <SPI.h> //Library for SPI interface 
#include <Wire.h> //Library for I2C interface 




int gas_sensor = A1; //Sensor pin
float m = -0.318; //Slope
float b = 1.133; //Y-Intercept
float R0 = 18.16; //Sensor Resistance in fresh air from previous code
float temp;
int pin = A5;

void setup() {
  Serial.begin(9600); //Baud rate

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
  Serial.print("ratio");
  Serial.print(ratio);

  double ppm_log = (log10(ratio) - b) / m; //Get ppm value in linear scale according to the the ratio value
  double ppm = pow(10, ppm_log); //Convert ppm value to log scale
  Serial.print("       ppm");
  Serial.print(ppm);
  //Serial.print("\t");
  
  
  double percentage = ppm / 10000; //Convert to percentage
  //Serial.print("\t");
  //Serial.print(percentage); //Load screen buffer with percentage value
  //Serial.println("%"); //Load screen buffer with "%"
  delay(2000);
  

  //TEMPERATURE

    // put your main code here, to run repeatedly:
    temp = analogRead(pin);
    temp = temp*500/1024;
    temp = (temp-32)*5/9;
    Serial.print("temp =  ");
    Serial.println(temp);
    delay(2000);

  
  return 0;
}
