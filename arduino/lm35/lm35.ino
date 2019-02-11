float temp;
int pin = A4;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);

}

void loop() {
  // put your main code here, to run repeatedly:
temp = analogRead(pin);
temp = temp*5000/1024;
temp = (temp - 500)/10;

Serial.print("temp =  ");
Serial.println(temp);
delay(2000);
}
