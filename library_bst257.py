import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008
#The Adafruit MCP3008 and GPIO libraries are provided "Without Restriction"
#As noted in their respective library files


def detect_eeprom():
    filename = "/proc/device-tree/hat/product_id"
    file = open(filename, "r")
    product_id = str(file.read())
    if "0x4313" in product_id:
        return True
    return False

def read_sliders():
    SPI_PORT   = 0
    SPI_DEVICE = 0
    mcp = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))
    #The above 3 lines are same used to initialize the SPI device in the
    #example software provided with the MCP3008 library
    values = [0, 0, 0, 0]
    for i in range(4):
        values[i] = mcp.read_adc(i)
    return values
