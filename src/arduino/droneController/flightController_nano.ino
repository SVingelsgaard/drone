//code for the arduino uno that controlls the drone.
// SimpleRx - the slave or the receiver
#include <SPI.h>
#include <nRF24L01.h>
#include <RF24.h>

#define CE_PIN 9
#define CSN_PIN 10

const byte thisSlaveAddress[5] = {'R','x','A','A','A'};

RF24 radio(CE_PIN, CSN_PIN);

char dataReceived[12]; // this must match dataToSend in the TX
bool newData = false;

//program variables
String dataRecivedString = "012345678901";
int LF;
int RF;
int LB;
int RB;


//===========

void setup() {
    pinMode(10, OUTPUT);
    Serial.begin(9600);

    Serial.println("Drone starting..");
    radio.begin();
    radio.setDataRate( RF24_250KBPS );
    radio.openReadingPipe(1, thisSlaveAddress);
    radio.startListening();
    Serial.println("Drone running");
}

//=============

void loop() {
    getData();

}

//==============

void getData() {
    if ( radio.available() ) {
        radio.read( &dataReceived, sizeof(dataReceived));
        dataRecivedString = String(dataReceived);
        
        parseData();
    }
}

void parseData() {
    LF = (String(dataRecivedString.charAt(0)) + String(dataRecivedString.charAt(1)) + String(dataRecivedString.charAt(2))).toInt();
    RF = (String(dataRecivedString.charAt(3)) + String(dataRecivedString.charAt(4)) + String(dataRecivedString.charAt(5))).toInt();
    LB = (String(dataRecivedString.charAt(6)) + String(dataRecivedString.charAt(7)) + String(dataRecivedString.charAt(8))).toInt();
    RB = (String(dataRecivedString.charAt(9)) + String(dataRecivedString.charAt(10)) + String(dataRecivedString.charAt(11))).toInt();
    
    Serial.println(LF);
    Serial.println(RF);
    Serial.println(LB);
    Serial.println(RB);
}
