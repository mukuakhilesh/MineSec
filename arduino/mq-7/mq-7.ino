float R0 = 2.08;
void setup() {
    Serial.begin(9600);
}

void loop() {
    float sensor_volt = 0;
    float RS_gas = 0;
    float ratio = 0;
    float sensorValue = 0;
    //float sensor_volt = 0;
    float a = 64.86 ;
    float b = -1.4;


    //Heather 5v 60 s
    analogWrite(A2, 1023);
    delay(60000);

    //Heather 1.4 V 90 s
    analogWrite(A2, (1023/5)*1.4 );
    for(int i = 0; i<900; i++){
        sensorValue = analogRead(A0);
        float sensor_volt = sensorValue/1024*5.0;
        RS_gas = (5.0-sensor_volt)/sensor_volt;
        Serial.print("rs = ");
        Serial.print(RS_gas);
        ratio = RS_gas/R0; //Replace R0 with the value found using the calibration code
        Serial.print("        ratio =");
        Serial.print(ratio);
       
        float z = pow(ratio , b);
         Serial.print("    z =");
        Serial.print(z);

        float ppm = a*z ;//Formula for co 2 concentration
        Serial.print("\t");
        Serial.println(ppm);
        delay(100);
    }
}
