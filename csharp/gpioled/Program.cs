// code based on the kitt-leds.py, but written in c-sharp

using System.Device.Gpio;

// initial state 
int blink = 1;

// define pins as variables
int redLed = 16;
int yellowLed = 20;
int greenLed = 21;


// setup output for pins
using GpioController controller = new GpioController();
controller.OpenPin(redLed, PinMode.Output);
controller.OpenPin(yellowLed, PinMode.Output);
controller.OpenPin(greenLed, PinMode.Output);

while (true)
{
	switch (blink)
	{
		case 1:
			controller.Write(redLed, PinValue.Low);
			controller.Write(yellowLed, PinValue.High);
			controller.Write(greenLed, PinValue.Low);
			blink = 2;
			break;

		case 2:
			controller.Write(redLed, PinValue.Low);
			controller.Write(yellowLed, PinValue.Low);
			controller.Write(greenLed, PinValue.High);
			blink = 3;
			break;

		case 3:
			controller.Write(redLed, PinValue.High);
			controller.Write(yellowLed, PinValue.Low);
			controller.Write(greenLed, PinValue.Low);
			blink = 1;
			break;

	}

	await Task.Delay(TimeSpan.FromSeconds(1));
}
