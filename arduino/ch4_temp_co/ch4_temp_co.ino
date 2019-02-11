float R0_co = 2.08;

int gas_sensor = A1; //Sensor pin
float a = 1041.333;
float b = -2.729007;
float R0 = 18.16; //Sensor Resistance in fresh air from previous code
float temp;
int pin = A4;

void setup() {
    Serial.begin(9600);

    pinMode(gas_sensor, INPUT);
}

void loop() {
    float sensor_volt_co = 0;
    float RS_gas_co = 0;
    float ratio_co = 0;
    float sensorValue_co = 0;
    //float sensor_volt = 0;
    float a_co = 64.86 ;
    float b_co = -1.4;

    //----------------------------------------------------------------------------------------
    float sensor_volt; //Define variable for sensor voltage
    float RS_gas; //Define variable for sensor resistance
    float ratio; //Define variable for ratio
//-------------------------------------------------------------------------------------------------------
    //Heather 5v 60 s
    analogWrite(A2, 1023);
    delay(60000);

    //Heather 1.4 V 90 s
    analogWrite(A2, (1023/5)*1.4 );
    for(int i = 0; i<9000; i++){
        sensorValue_co = analogRead(A0);
        float sensor_volt_co = sensorValue_co/1024*5.0;
        RS_gas_co = (5.0-sensor_volt_co)/sensor_volt_co;
      //  Serial.print("rs = ");
      //  Serial.print(RS_gas);
        ratio_co = RS_gas_co/R0_co; //Replace R0 with the value found using the calibration code
       // Serial.print("        ratio =");
       // Serial.print(ratio);
       
        float z_co = pow(ratio_co , b_co);
     //    Serial.print("    z =");
      //  Serial.print(z);

        float ppm_co = a_co*z_co ;//Formula for co 2 concentration
       // Serial.print("\t");
    //----------------------------------------------------------------------------------------------------------
        float sensorValue = analogRead(gas_sensor); //Read analog values of sensor
        sensor_volt = sensorValue * (5.0 / 1023.0); //Convert analog values to voltage
        RS_gas = ((5.0 * 10.0) / sensor_volt) - 10.0; //Get value of RS in a gas
        ratio = RS_gas / R0;

        double ppm = a*pow(ratio , b);
  
  
        double percentage = ppm / 10000;
    //------------------------------------------------------------------------------------
          temp = analogRead(pin);
          temp = temp*5000/1024;
          temp = (temp - 500)/10;
    
       //------------------------------------------------------------------------------------------
        Serial.print(ppm);
        Serial.print("  ");
        Serial.print(temp);
        Serial.print("  ");
        Serial.println(ppm_co);
        
        
        delay(10);
    }
}
