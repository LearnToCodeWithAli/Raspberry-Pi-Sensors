// See https://aka.ms/new-console-template for more information
// Console.WriteLine("Hello, World!");

using System.Device.Gpio;

int blink = 1;

int redLed = 16;
int yellowLed = 20;
int greenLed = 21;

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

