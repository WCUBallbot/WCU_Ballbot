#include <iostream>
#include <unistd.h>
#include <errno.h>
#include <stdio.h>
#include <stdlib.h>
#include <signal.h>
#include "GPIOClass.h"
#include "AccelStepper.h"
#include <cstdlib>
using namespace std;

AccelStepper stepper1(AccelStepper::DRIVER, 9, 8);
AccelStepper stepper2(AccelStepper::DRIVER, 6, 7);
AccelStepper stepper3(AccelStepper::DRIVER, 10, 11);

float pos1 = 150000;
float pos2 = 150000;
float pos3 = 150000;

int main(void)
{
	atexit(exiting);

	stepper1.setMaxSpeed(100000);   
	stepper1.setAcceleration(50000);

	stepper2.setMaxSpeed(100000);   
	stepper2.setAcceleration(50000);

	stepper3.setMaxSpeed(100000);   
	stepper3.setAcceleration(50000);

	while (1)
	{
		if (stepper1.distanceToGo() == 0){
			pos1 = -pos1;     
			stepper1.moveTo(pos1);
		}
		if (stepper2.distanceToGo() == 0){
			pos2 = -pos2;     
			stepper2.moveTo(pos2);
		}
		if (stepper3.distanceToGo() == 0){
			pos3 = -pos3;     
			stepper3.moveTo(pos3);
		}

		stepper1.run();
		stepper2.run();
		stepper3.run();
	}

	cout << "Exiting....." << endl;
	return 0;
}

void exiting(void) {

}
