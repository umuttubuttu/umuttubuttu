#include <DHT.h>
#define kirmizi D5
#define yesil D6
#define mavi D7
#define DHTTYPE DHT11   
float sicaklik;
const int DHTPin = D4;

DHT dht(DHTPin,DHTTYPE);

void setup() {

  dht.begin();
  pinMode(kirmizi,OUTPUT);
  pinMode(yesil,OUTPUT);
  pinMode(mavi,OUTPUT);
}

void loop() {
sicaklik=dht.readTemperature(false);

if(int(sicaklik)<=5)
{
  digitalWrite(kirmizi,LOW);
  digitalWrite(yesil,HIGH);
  digitalWrite(mavi,HIGH);
}
else if(int(sicaklik)<=20)
{
  digitalWrite(kirmizi,HIGH);
  digitalWrite(yesil,LOW);
  digitalWrite(mavi,HIGH);
}
else
{
  digitalWrite(kirmizi,HIGH);
  digitalWrite(yesil,HIGH);
  digitalWrite(mavi,LOW);
}
}
