//code for the arduino uno that controlls the non-drone radio module and comunicates with the PC
// SimpleTx - the master or the transmitter
#include <SPI.h>
#include <nRF24L01.h>
#include <RF24.h>


#define CE_PIN 9
#define CSN_PIN 10

const byte slaveAddress[5] = {'R','x','A','A','A'};

const unsigned int MAX_MESSAGE_LENGTH = 12;

RF24 radio(CE_PIN, CSN_PIN); // Create a Radio

String dataToSendString = "000000000000";
//char dataToSend[12] = "000000000000";
int dataToSend = 0;

String serialOutput = "";

String LFSpeed;
String RFSpeed;
String LBSpeed;
String RBSpeed;


unsigned long currentMillis;
unsigned long prevMillis;
unsigned long txIntervalMillis = 10; // send once per second


void setup() {
    pinMode(10, OUTPUT);
    Serial.begin(9600);

    Serial.println("SimpleTx Starting");

    radio.begin();
    radio.setDataRate( RF24_250KBPS );
    radio.setRetries(3,5); // delay, count
    radio.openWritingPipe(slaveAddress);
}

//====================

void loop() {
    dataToSend = 7;
    currentMillis = millis();
    serialRead();//allways check for serial data
    if (currentMillis - prevMillis >= txIntervalMillis) {//sending data on a intervall
        send();
        serialWrite();
        prevMillis = millis();
    }
}

//====================

void send() {
    bool rslt;
    rslt = radio.write( &dataToSend, sizeof(dataToSend) );
        // Always use sizeof() as it gives the size as the number of bytes.
        // For example if dataToSend was an int sizeof() would correctly return 2
    if (not rslt) {
        serialPrint(String("Radio Tx failed"));
    }
}
void serialRead(){
    //Check to see if anything is available in the serial receive buffer
    while (Serial.available() > 0){
        //Create a place to hold the incoming message
        static char message[MAX_MESSAGE_LENGTH];
        static unsigned int message_pos = 0;

        //Read the next available byte in the serial receive buffer
        char inByte = Serial.read();

        //Message coming in (check not terminating character) and guard for over message size
        if ( inByte != '\n' && (message_pos < MAX_MESSAGE_LENGTH-1)){
            //Add the incoming byte to our message
            message[message_pos] = inByte;
            message_pos++;
        } else {//Full message received...
            //Add last byte.
            message[message_pos] = inByte;

            //Print the message (or do other things)
            serialPrint(String(message));
            //dataToSendString = String(message);
        

            //Reset for the next message
            message_pos = 0;
        }
    }
}
void serialPrint(String data){
    serialOutput += data + String("\n");
}

void serialWrite(){
    Serial.println(serialOutput);
    serialOutput = "";
}