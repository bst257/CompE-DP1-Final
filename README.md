# CompE-DP1-Final

Brief Specifications
	Basic Functionality:
	My add-on board is meant to be used as a form of input for the Raspberry Pi. It can read the values of four sliding potentiometers and return them as a value from 0 to 1023 and is meant to feature a system that can read a gesture input in one of four directions: up, down, left, or right.  However, the latter subsystem was unable to be implemented in time for the submission of the project.
	Power:
	My add-on board does not require a seperate power supply. The manual control subsystem only requires the 3.3V power that the Pi can supply and the gesture control system would be powered by the 5V power supply on the Pi. 
	Current:
	The ID EEPROM of the add-on board requires 1.7 mA of current, drawn from the 3.3V power supply of the Pi. The four potentiometers have a resistance of 10kΩ each so they draw 0.33 mA each for a total of 1.32 mA. The ADC IC used in the manual control system draws current on the order of µA. It is impossible to tell how much current would be drawn by the gesture control system without properly constructing it, as it would need to be measured with a multimeter.
	GPIO Pins/Communication buses:
	The add-on board uses BCM pins 0 and 1 for identification of the ID EEPROM.  The ADC IC of the manual control system uses SPI bus 0 and chip enable 0 so the same bus could be used with other chip enable lines.
	
Assembling and using the board
	https://i.imgur.com/OONl408.png
	I could not find a proper footprint for the sliders used in my project, but chose the footprint of another potentiometer to hold its place.

Installing and using the library
	Because I was only able to implement the manual control subsystem of my add-on board, my software library is rather simple.  It relies on the Adafuri_Python_GPIO and Adafruit_Python_MCP3008 libraries that can be obtained at https://github.com/adafruit/Adafruit_Python_GPIO and https://github.com/adafruit/Adafruit_Python_MCP3008 (It seems that as of yesterday the latter library is no longer supported, but it should still work for the purposes of this project).  The two function available for my project are detect_eeprom() which returns True if the hat is attached and False otherwise and read_sliders() which returns a list of the 4 values of the ADC as an integer in the range of 0-1023 based on the position of the sliders.
