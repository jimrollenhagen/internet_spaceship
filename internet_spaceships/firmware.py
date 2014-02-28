import logging
from internet_spaceships import base


class Firmware(base.BaseFirmware):
    def input(self):
        """ Implement your code here. This will be called on every tick after
        the class data has been set up from the JSON. Look at debug.log to
        see the debugging information.
        """
        if self.throttle > 100:
            self.throttle -= 40
        else:
            self.throttle += 5
            
        self.heading = (self.heading + 5) % 360


if __name__ == "__main__":
    """ This sets up your firmware when you run "firmware.py" with some JSON
    input.
    """
    firmware = Firmware()
    firmware.start()
