
//const int Pauseswitch = 52;
//const int Refillswitch = 50;

int PW = 20000; // Microsecond
int Freq = 1; // Hz
int RePW = 10000; // Microsecond
int DeTi = 0; // Millisecond   delay time between refill and print
//float ReRa = 0.5;  // Refill Pulse Width Ratio
int pulsecount = 10;

const int ledPin =  13;      // the number of the LED pin
const int valveP = 2;  // for Printing
const int valveP2 = 3;  // for Refill
//const int valve3 =  ;
const int buttonPin = 7;     // the number of the pushbutton pin
const int pinINT = 10;

int buttonState = 0;
int PbuttonState = 0;         // variable for reading the P pushbutton status
int P2buttonState = 0;         // variable for reading the R pushbutton status
int pulseswitch = 0;

int AlwaysOn = 0;
int valvepin=3;
int valvestate=0;
int valve2_state = 0;
int valve3_state = 0;

//int pinINTERUPT = 2;

byte datard[20] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
//int datard0[]={0,0,0,0,0,0,0,0,0,0,0,0};
int i = 0;
int lim = 0;
int tp = 0;
byte inByte = 0;

int number;
volatile int LEDstate = HIGH;

void ParamPass()     // receive cmd data after flush the buffer, while stopping output pulse
{
  //digitalWrite(valveP, HIGH);
  //digitalWrite(valveR, HIGH);
  if (Serial.available()) {
    for (i = 0; i < 20; i++)
    {
      datard[i] = 0;
    }
    i = 0;  
    delay(100);
    while (Serial.available())
    {
      inByte = Serial.read();
      //Serial.print(inByte, HEX);
      //Serial.print(255, HEX);
      //Serial.write(255);
      //Serial.write(inByte);
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
          pulseswitch = 0;
          i=i+4;
        } else if (datard[i + 2] == 239 && datard[i + 3] == 239) {   // EF EF
          pulseswitch = 1;
          i=i+4;
        } else if (datard[i + 2] == 245 && datard[i + 3] == 245) {   // F5 F5
          valvepin = datard[i + 4];
          valvestate = 1;
          i=i+4;
        } else if (datard[i + 2] == 240 && datard[i + 3] == 240) {   // F5 F5
          valvestate = 0;
          i=i+4;
        } else {
          Freq = datard[i + 2];
          tp = 1000 / Freq;
          PW = datard[i + 4] * 256 + datard[i + 3];
          RePW = datard[i + 6] * 256 + datard[i + 5];
          pulsecount = datard[i + 8] * 256 + datard[i + 7];
          AlwaysOn = datard[i + 9];
          i=i+10;
          //break;
        }
      } else {
        i++;
      }
    }
    //Serial.write(Freq);
    //Serial.write(PW/1000);
    //Serial.write(pulsecount);
    //Serial.write(pulseswitch);
  }
}

void SLED()  // serial control the led
{
  //delay(500);
  LEDstate = !LEDstate;
  digitalWrite(ledPin, LEDstate);
}

void setup() {
  Serial.begin(115200);
  Serial.setTimeout(100);
  //Serial.flush();
  // put your setup code here, to run once:
  pinMode(ledPin, OUTPUT);
  pinMode(valveP, OUTPUT);
  pinMode(valveP2, OUTPUT);
  pinMode(valvepin, OUTPUT);
  //pinMode(valve3, OUTPUT);
  pinMode(buttonPin, INPUT_PULLUP);
  //pinMode(pinINTERUPT,INPUT);
  //pinMode(pinINT,OUTPUT);
  //digitalWrite(pinINT, HIGH);
  digitalWrite(ledPin, LOW);
  //pinMode(Pauseswitch, INPUT_PULLUP);
  //pinMode(Refillswitch, INPUT_PULLUP);
  tp = 1000 / Freq;
  //attachInterrupt(1,ParamPass,FALLING);
  //attachInterrupt(0, SPort, FALLING);
  //Serial.write(Freq);
  //Serial.write(PW / 1000);
  //Serial.write(RePW / 1000);
  //Serial.write(pulsecount);
  //Serial.write(pulseswitch);
}

void loop() {
  // put your main code here, to run repeatedly:
  ParamPass();
  if (pulseswitch == 1 and AlwaysOn == 0){
    digitalWrite(ledPin, LOW);
    if (lim < pulsecount) {
      digitalWrite(valveP2, HIGH);
      delay(RePW);
      digitalWrite(valveP2, LOW);
      delay(DeTi);
      digitalWrite(valveP, HIGH);
      delay(PW);
      digitalWrite(valveP, LOW);
      delay(tp - PW - RePW - DeTi);
    } else {
      digitalWrite(ledPin, LOW);
      digitalWrite(valveP, LOW);
      digitalWrite(valveP2, LOW);
      pulseswitch = 0;
      delay(100);
    }
    lim += 1;
  } else if (pulseswitch == 1 and AlwaysOn == 1) {
    digitalWrite(ledPin, LOW);
    if (lim < pulsecount) {
      digitalWrite(valveP2, HIGH);
      delay(RePW);
      delay(DeTi);
      digitalWrite(valveP, HIGH);
      delay(PW);
      digitalWrite(valveP, LOW);
      delay(tp - PW - RePW - DeTi);
    } else {
      digitalWrite(ledPin, LOW);
      digitalWrite(valveP, LOW);
      digitalWrite(valveP2, LOW);
      pulseswitch = 0;
      delay(100);
    }
    lim += 1;
    
  } else if (pulseswitch == 0 and valvestate == 1){
    digitalWrite(valvepin, HIGH);
    if (valvepin == 2) {
      valve2_state = 1;
    }
    else if (valvepin == 3) {
      valve3_state = 1;
    }
  } else if (pulseswitch == 0 and valvestate == 0 and (valve2_state ==1 or valve3_state==1) ){
    digitalWrite(valvepin, LOW);
    if (valvepin == 2) {
      valve2_state = 0;
    }
    else if (valvepin == 3) {
      valve3_state = 0;
    }
  }
  else {
    digitalWrite(ledPin, LOW);
    digitalWrite(valveP, LOW);
    digitalWrite(valveP2, LOW);
    delay(100);
    lim = 0;
  }
}
