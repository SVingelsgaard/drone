//code for the arduino uno that controlls the drone.
#include <SPI.h>
#include <nRF24L01.h>
#include <RF24.h>
#include <Servo.h>

//radio stuff
#define CE_PIN 9
#define CSN_PIN 10
const byte thisSlaveAddress[5] = {'R','x','A','A','A'};
RF24 radio(CE_PIN, CSN_PIN);
char dataReceived[12]; // this must match dataToSend in the TX

//hardware
int LFPin = 5;//6
int RFPin = 6;//3
int LBPin = 3;//4
int RBPin = 4;//5

int batteryVoltagePin = A0;

//program variables
Servo LF;
Servo RF;
Servo LB;
Servo RB;

int LFSpeed;
int RFSpeed;
int LBSpeed;
int RBSpeed;

int batteryVoltage;
int batteryPercentage;

String dataRecivedString = "012345678901";

void setup() {
    pinMode(10, OUTPUT);//for radio?
    Serial.begin(9600);
    Serial.println("Drone starting..");
    //radio
    radio.begin();
    radio.setDataRate( RF24_250KBPS );
    radio.openReadingPipe(1, thisSlaveAddress);
    radio.startListening();

    //motors
    LF.attach(LFPin);
    RF.attach(RFPin);
    LB.attach(LBPin);
    RB.attach(RBPin);

    Serial.println("Drone running");
}

void loop() {
    getRadioData();
    getDroneData();
    writeOutput();
}

void getRadioData() {
    if ( radio.available() ) {
        radio.read( &dataReceived, sizeof(dataReceived));
        dataRecivedString = String(dataReceived);
        
        //parsing
        LFSpeed = (String(dataRecivedString.charAt(0)) + String(dataRecivedString.charAt(1)) + String(dataRecivedString.charAt(2))).toInt();
        RFSpeed = (String(dataRecivedString.charAt(3)) + String(dataRecivedString.charAt(4)) + String(dataRecivedString.charAt(5))).toInt();
        LBSpeed = (String(dataRecivedString.charAt(6)) + String(dataRecivedString.charAt(7)) + String(dataRecivedString.charAt(8))).toInt();
        RBSpeed = (String(dataRecivedString.charAt(9)) + String(dataRecivedString.charAt(10)) + String(dataRecivedString.charAt(11))).toInt();
        Serial.println(dataReceived);
    }
}
void getDroneData(){
    batteryVoltage = int((float((analogRead(batteryVoltagePin)))/1023)*14000);//AI after voltage divider(18k and 10k) will be 5V when battery voltage is 14V. in mV for presition calculatiun xd
    batteryPercentage = map(batteryVoltage, 11060, 12600, 10, 100);//maped ish after table from https://blog.ampow.com/lipo-voltage-chart/
}

void writeOutput(){
    LF.write(LFSpeed);
    RF.write(RFSpeed);
    LB.write(LBSpeed);
    RB.write(RBSpeed);
}