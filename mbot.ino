#include "MeMegaPi.h"
#include "src/MeNewRGBLed.h"

int incomingByte = 0; // for incoming serial data
int prevByte=10;

MeMegaPiDCMotor motor1(PORT1A);
MeMegaPiDCMotor motor2(PORT1B);
MeMegaPiDCMotor motor3(PORT2A);
MeMegaPiDCMotor motor4(PORT2B);

uint8_t motorSpeed = 155;

MeNewRGBLed rgbled_67(67,4);
MeNewRGBLed rgbled_68(68,4);

float light_1 =236;
float light_2 = 0;
float light_3 =117;

void setup() {
  Serial.begin(115200);
  rgbled_67.setColor(0, light_1, light_2, light_3);
  rgbled_67.show();

  rgbled_68.setColor(0, light_1, light_2, light_3);
  rgbled_68.show();
}



void loop() {
  // send data only when you receive data:
  if (Serial.available() > 0) {
    // read the incoming byte:
    incomingByte = Serial.read();
    Serial.println(incomingByte, DEC);

    
    if ( incomingByte==119){
      motor1.run(motorSpeed*1); /* value: between -255 and 255. */
      motor2.run(motorSpeed*1); /* value: between -255 and 255. */
      motor3.run(motorSpeed*-1);
      motor4.run(motorSpeed*-1);
      delay(10);
    }
    if ( incomingByte==115){
      motor1.run(motorSpeed*-1); /* value: between -255 and 255. */
      motor2.run(motorSpeed*-1); /* value: between -255 and 255. */
      motor3.run(motorSpeed*1);
      motor4.run(motorSpeed*1);
      delay(10);
    }
    if ( incomingByte==100){
      motor1.run(motorSpeed*-1); /* value: between -255 and 255. */
      motor2.run(motorSpeed*1); /* value: between -255 and 255. */
      motor3.run(motorSpeed*1);
      motor4.run(motorSpeed*-1);
      delay(10);
    }
     if ( incomingByte==97){
      motor1.run(motorSpeed*1); /* value: between -255 and 255. */
      motor2.run(motorSpeed*-1); /* value: between -255 and 255. */
      motor3.run(motorSpeed*-1);
      motor4.run(motorSpeed*1);
      delay(10);
    }
    if ( incomingByte==101){
      motor1.run(motorSpeed*-1); /* value: between -255 and 255. */
      motor2.run(motorSpeed*-1); /* value: between -255 and 255. */
      motor3.run(motorSpeed*-1);
      motor4.run(motorSpeed*-1);
      delay(10);
    }
    if ( incomingByte==113){
      motor1.run(motorSpeed*1); /* value: between -255 and 255. */
      motor2.run(motorSpeed*1); /* value: between -255 and 255. */
      motor3.run(motorSpeed*1);
      motor4.run(motorSpeed*1);
      delay(10);
    }

    if ( incomingByte==49){
      motorSpeed=55;
      delay(5);
    }
    else if ( incomingByte==50){
      motorSpeed=155;
      delay(5);
    }
    else if ( incomingByte==51){
      motorSpeed=255;
      delay(5);
    }
  
     motor1.stop();
     motor2.stop();
     motor3.stop();
     motor4.stop();   
      
     prevByte=incomingByte;
     
    }
  }
