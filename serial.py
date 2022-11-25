"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, start=0):
        self.start = self.next = start

    def generate(self):
        """ Increments self.next by 1 each time generate() is run """

        self.next += 1
        return self.next
        
    def reset(self):
        """ Returns the assigned self.start value which was set to start originally """
        return self.start


