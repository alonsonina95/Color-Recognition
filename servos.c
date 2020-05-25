// This is the code used to reset all the servos to 90 degrees out of 0-180

#include <Servo.h>

// Define our Servos

Servo servo1;
Servo servo2;
Servo servo3;
Servo servo4;
Servo servo5;
Servo servo6;
Servo servo7;
Servo servo8;
Servo servo9;
Servo servo10;
Servo servo11;
Servo servo12;

void setup(){
	servo1.attach(8);
	servo2.attach(9);
	servo3.attach(10);
	servo4.attach(11);
	servo5.attach(12);
	servo6.attach(13);
}

//Reset servos to 90 degrees
// Right now only servos 1-3 are connected

void loop() {
	servo1.write(90);
	servo2.write(90);
	servo3.write(90);
	servo4.write(90);
	servo5.write(90);
	servo6.write(90);
}
