#include "MeMegaPi.h"
#include "src/MeNewRGBLed.h"

int incomingByte = 0; // for incoming serial data
int prevByte=10;

MeMegaPiDCMotor motor1(PORT1A);
MeMegaPiDCMotor motor2(PORT1B);
MeMegaPiDCMotor motor3(PORT2A);
MeMegaPiDCMotor motor4(PORT2B);

// m4 m1
// m3 m2

float motor1Scale = 0.8;
float motor2Scale = 0.8;
float motor3Scale = 0.8;
float motor4Scale = 0.8;

uint8_t motorSpeed = 155;
uint8_t motorSpeedLevel1 = 55;
uint8_t motorSpeedLevel2 = 155;
uint8_t motorSpeedLevel3 = 255;

MeNewRGBLed rgbled_67(67,4);
MeNewRGBLed rgbled_68(68,4);

float light1 =236;
float light2 = 0;
float light3 =117;

byte forward = 119;
byte left = 97;
byte backward = 115;
byte right = 100;
byte rotateLeft = 113;
byte rotateRight = 101;
byte n1 = 49;
byte n2 = 50;
byte n3 = 51;

byte colorCheckByte = 99;

void setup() {
  Serial.begin(115200);

  changeLEDColor(light1, light2, light3);
}

void changeLEDColor(float red, float green, float blue) {
  rgbled_67.setColor(0, red, green, blue);
  rgbled_67.show();

  rgbled_68.setColor(0, red, green, blue);
  rgbled_68.show();
  Serial.println("change light");
}

bool colorCheckLoop;
int colorCheckCount;
void loop() {
  // send data only when you receive data:
  if (Serial.available() > 0) {
    // read the incoming byte:
    incomingByte = Serial.read();
    Serial.println(incomingByte, DEC);

    if(colorCheckLoop) {
      if(colorCheckCount == 0) {
        light1 = (float)incomingByte;
      } else if(colorCheckCount == 1) {
        light2 = (float)incomingByte;
      } else if(colorCheckCount == 2) {
        light3 = (float)incomingByte;
        changeLEDColor(light1, light2, light3);
        // reset count
        colorCheckCount = 0;
        colorCheckLoop = false;
        Serial.println("-----color changed-----");
        return;
      }
      colorCheckCount++;
      return;
    }
    if(incomingByte == colorCheckByte) {
      colorCheckLoop = true;
      Serial.println("---waiting color input----");
      return;
    }
    
    if (incomingByte == forward){
      motorRun(1, 1, -1, -1);
    }
    if (incomingByte == backward){
      motorRun(-1, -1, 1, 1);
    }
    if (incomingByte == right){
      motorRun(-1, 1, 1, -1);
    }
     if (incomingByte == left){
      motorRun(1, -1, -1, 1);
    }
    
    if (incomingByte == rotateRight){
      motorRun(-1, -1, -1, -1);
    }
    if (incomingByte == rotateLeft){
      motorRun(1, 1, 1, 1);
    }

    if (incomingByte == n1){
      motorSpeed = motorSpeedLevel1;
      delay(5);
    }
    else if (incomingByte == n2){
      motorSpeed = motorSpeedLevel2;
      delay(5);
    }
    else if (incomingByte == n3){
      motorSpeed = motorSpeedLevel3;
      delay(5);
    }
  
     motor1.stop();
     motor2.stop();
     motor3.stop();
     motor4.stop();   
      
     prevByte=incomingByte;   
  }
}

void motorRun(int motor1Dir, int motor2Dir, int motor3Dir, int motor4Dir) {
  motor1.run(motorSpeed * motor1Dir * motor1Scale); /* value: between -255 and 255. */
  motor2.run(motorSpeed * motor2Dir * motor2Scale); /* value: between -255 and 255. */
  motor3.run(motorSpeed * motor3Dir * motor3Scale);
  motor4.run(motorSpeed * motor4Dir * motor4Scale);
  delay(10);
}
