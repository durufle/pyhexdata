
import numpy as np
import math


class HexData:
    """
    HexData class
    """

    version = "0.1.0"
    __version__ = version

    def __init__(self, value=None, padding=None):
        """
        The function __init__ initialize the object HexData from a integer value or a hexdecimal string value with or
        without spaces or a numpy array dtyped np.uint8.
        The final value is stored in a numpy array format inside the class.

        Input:
           - value (int, str or numpy array, optional): the value to pass to HexData
           - padding (int, optional): the number of bytes to keep (could be higher or smaller than the real number
           of bytes)
        Output:
           - None
        """
        if not(value is None):
            if isinstance(value, np.ndarray):
                self._data = value.astype(np.uint8)
            elif isinstance(value, bytes):
                self._data = np.frombuffer(value, dtype=np.uint8)
            elif isinstance(value, str):
                value = value.replace(" ", "")

                if len(value) % 2 == 1:
                        value = "0" + value

                # String read
                byte_value = bytes.fromhex(value)
                self._data = np.frombuffer(byte_value, dtype=np.uint8)
            elif isinstance(value, int):
                nr_bytes = math.ceil(value.bit_length() / 8.)

                # Integer read
                byte_value = value.to_bytes(nr_bytes, "big", signed=False)
                self._data = np.frombuffer(byte_value, dtype=np.uint8)
            else:
                self._data = None

        if padding is not None:
            self.padding(padding)

    def get_value(self):
        """
        This function get the value of the numpy array

        Input:
           - None
        Output:
           - None
        """
        return self._data

    def to_string(self, spaces=True):
        """
        This function converts the numpy array to string with spaces

        Input:
           - spaces (bool; optional): if True, spaces between each byte, without spaces either
        Output:
           - None
        """
        if not(self._data is None):
            if spaces:
                return " ".join(["{:02x}".format(x) for x in self._data])
            else:
                return "".join(["{:02x}".format(x) for x in self._data])
        return None

    def to_bytes(self):
        """
        This function converts the numpy array to string with spaces

        Input:
           - spaces (bool; optional): if True, spaces between each byte, without spaces either
        Output:
           - None
        """
        if not(self._data is None):
            return self._data.tobytes()
        return None

    def to_number(self):
        """
        This function converts the numpy array into the integer value represented by the entire array

        Input:
           - None
        Output:
           - None
        """
        if not (self._data is None):
            return int.from_bytes(self._data.tobytes(), "big", signed=False)
        return None

    def padding(self, nr_bytes):
        """
        This function forces the padding of the _data attribute internally

        Input:
           - nr_bytes (int): the number of bytes of the _data attribute
        Output:
           - None
        """
        diff = nr_bytes - self._data.shape[0]
        if diff > 0:
            self._data = np.concatenate((np.zeros(diff, dtype=np.uint8), self._data))
        elif diff < 0:
            self._data = self._data[-diff:]
        else:
            pass

    @staticmethod
    def rand(nr_bytes):
        """
        This function generates a random bytes array composed by nr_bytes

        Input:
           - nr_bytes (int): number of bytes of the random to generate.
        Output:
           - None

        Note that, the padding is automatically performed. The random can starts by 00
        """
        data = np.frombuffer(np.random.bytes(nr_bytes), dtype=np.uint8)

        return HexData(value=data)
