const int ledPin =  13;      // the number of the LED pin
const int valve1 =  2;
const int valve2 =  3;
const int valve3 =  4;
const int valve4 =  5;
const int valve5 =  6;
const int valve6 =  7;
const int valve7 =  8;
const int valve8 =  9;  
const int pinINT = 10;

int valvepin=2;
int valvestate=0;


byte datard[20] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
int i = 0;
int lim = 0;
int tp = 0;
byte inByte = 0;

int number;
volatile int LEDstate = HIGH;

void ParamPass()     // receive cmd data after flush the buffer, while stopping output pulse
{
  if (Serial.available()) {
	Serial.print(1);
    for (i = 0; i < 20; i++)
    {
      datard[i] = 0;
    }
    i = 0;  
    delay(100);
    while (Serial.available())
    {
      inByte = Serial.read();
      if (i < 20)
      {
        datard[i] = inByte;
        i++;
      }
      else
      {
        while (Serial.available())
        {
          inByte = Serial.read();
        }
        break;
      }
    }
    i = 0;
    while (i <= 19)
    {
      if (datard[i] == 255 && datard[i + 1] == 255) {
        if (datard[i + 2] == 254 && datard[i + 3] == 254) {   // FE FE
          // put a function here
          i=i+4;
        } else if (datard[i + 2] == 239 && datard[i + 3] == 239) {   // EF EF
          i=i+4;
          // put a function here
        } else if (datard[i + 2] == 245 && datard[i + 3] == 245) {   // F5 F5
          valvepin = datard[i + 4];
          valvestate = 1;
          i=i+4;
        } else if (datard[i + 2] == 240 && datard[i + 3] == 240) {   // F5 F5
          valvestate = 0;
          i=i+4;
        } else {
          i=i+10;
          //break;
        }
      } else {
        i++;
      }
    }
  }
}

void SLED()  // serial control the led
{
  LEDstate = !LEDstate;
  digitalWrite(ledPin, LEDstate);
}

void setup() 
{
  Serial.begin(115200);
  Serial.setTimeout(100);
  pinMode(ledPin, OUTPUT);
  pinMode(valve1, OUTPUT);
  pinMode(valve2, OUTPUT);
  pinMode(valve3, OUTPUT);
  pinMode(valve4, OUTPUT);
  pinMode(valve5, OUTPUT);
  pinMode(valve6, OUTPUT);
  pinMode(valve7, OUTPUT);
  pinMode(valve8, OUTPUT);
  pinMode(valvepin, OUTPUT);
  digitalWrite(ledPin, LOW);
  digitalWrite(valve1, LOW);
  digitalWrite(valve2, LOW);
  digitalWrite(valve3, LOW);
  digitalWrite(valve4, LOW);
  digitalWrite(valve5, LOW);
  digitalWrite(valve6, LOW);
  digitalWrite(valve7, LOW);
  digitalWrite(valve8, LOW);
}

void loop() 
{
  // put your main code here, to run repeatedly:
  ParamPass();
  if (valvestate == 1){
    digitalWrite(valvepin, HIGH);
  } else if (valvestate == 0){
    digitalWrite(valvepin, LOW);
  }
  else {
    digitalWrite(ledPin, LOW);
    digitalWrite(valve1, LOW);
    digitalWrite(valve2, LOW);
    digitalWrite(valve3, LOW);
    digitalWrite(valve4, LOW);
    digitalWrite(valve5, LOW);
    digitalWrite(valve6, LOW);
    digitalWrite(valve7, LOW);
    digitalWrite(valve8, LOW);
    delay(100);
    lim = 0;
  }
}
