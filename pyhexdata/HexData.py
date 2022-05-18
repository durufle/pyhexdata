
import numpy as np
import math


class HexData:
    """
    HexData class
    """

    version = "0.3.0"
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
        self._data = np.array([])
        if not(value is None):
            if isinstance(value, np.ndarray):
                self._data = value.astype(np.uint8)
            elif isinstance(value, list):
                self._data = np.array(value, dtype=np.uint8)
            elif isinstance(value, bytes):
                self._data = np.frombuffer(value, dtype=np.uint8)
            elif isinstance(value, np.uint8):
                self._data = np.array([value], dtype=np.uint8)
            elif isinstance(value, str):
                value = value.replace(" ", "")

                if len(value) % 2 == 1:
                        value = "0" + value

                # String read
                byte_value = bytes.fromhex(value)
                self._data = np.frombuffer(byte_value, dtype=np.uint8)
            elif isinstance(value, int) or isinstance(value, int):
                nr_bytes = max(1, math.ceil(value.bit_length() / 8.))

                # Integer read
                byte_value = value.to_bytes(nr_bytes, "big", signed=False)
                self._data = np.frombuffer(byte_value, dtype=np.uint8)
            else:
                raise TypeError("This type is not allowed")

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

    def to_list(self):
        """
        This function get the value of the numpy array

        Input:
           - None
        Output:
           - None
        """
        return self._data.tolist()

    def to_string(self, spaces=True):
        """
        This function converts the numpy array to string with spaces

        Input:
           - spaces (bool; optional): if True, spaces between each byte, without spaces either
        Output:
           - None
        """
        if len(self) > 0:
            if spaces:
                return " ".join(["{:02x}".format(x) for x in self._data])
            else:
                return "".join(["{:02x}".format(x) for x in self._data])
        return ""

    def to_bytes(self):
        """
        This function converts the numpy array to string with spaces

        Input:
           - spaces (bool; optional): if True, spaces between each byte, without spaces either
        Output:
           - None
        """
        return self._data.tobytes()

    def to_number(self):
        """
        This function converts the numpy array into the integer value represented by the entire array

        Input:
           - None
        Output:
           - None
        """
        if len(self) > 0:
            return int.from_bytes(self._data.tobytes(), "big", signed=False)
        return 0

    def padding(self, nr_bytes):
        """
        This function forces the padding of the _data attribute internally

        Input:
           - nr_bytes (int): the number of bytes of the _data attribute
        Output:
           - None
        """
        diff = nr_bytes - len(self)
        if diff > 0:
            self._data = np.concatenate((np.zeros(diff, dtype=np.uint8), self._data))
        elif diff < 0:
            self._data = self._data[-diff:]
        else:
            pass

    def right_padding(self, nr_bytes):
        """
        This function forces the padding of the _data attribute internally

        Input:
           - nr_bytes (int): the number of bytes of the _data attribute
        Output:
           - None
        """
        diff = nr_bytes - self._data.shape[0]
        if diff > 0:
            self._data = np.concatenate((self._data, np.zeros(diff, dtype=np.uint8)))
        elif diff < 0:
            self._data = self._data[:-diff]
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

    def __xor__(self, other):
        if isinstance(other, int) or isinstance(other, str):
            other = HexData(other)
            if len(other) != 1:
                raise ValueError("The second parameter for XOR is not a byte")

        return HexData(np.bitwise_xor(self._data, other._data))

    def __str__(self):
        return self.to_string(spaces=False)

    def __len__(self):
        return self._data.shape[0]

    def __getitem__(self, index):
        # Check type index
        if isinstance(index, list):
            pass
        elif isinstance(index, np.ndarray):
            pass
        elif isinstance(index, slice):
            pass
        elif isinstance(index, int):
            pass
        else:
            raise ValueError("This type is not allowed")

        return HexData(self._data[index])

    def __setitem__(self, index, value):
        # Check type index
        if isinstance(index, list):
            pass
        elif isinstance(index, np.ndarray):
            pass
        elif isinstance(index, slice):
            pass
        elif isinstance(index, int):
            pass
        else:
            raise ValueError("This type is not allowed")

        # Check type value
        if isinstance(value, list):
            value = HexData(value)
        elif isinstance(value, np.ndarray):
            value = HexData(value)
        elif isinstance(value, int):
            value = HexData(value)
        elif isinstance(value, HexData):
            pass
        else:
            raise ValueError("This type is not allowed")

        # Check sizes are equal
        if isinstance(index, list) or isinstance(index, np.ndarray):
            if len(index) != len(value):
                raise ValueError("The sizes of index and values must be the same")
        elif isinstance(index, int):
            if len(value) != 1:
                raise ValueError("The sizes of index and values must be the same")
        elif isinstance(index, slice):
            size_slice = len(range(*index.indices(self._data.shape[0])))
            if size_slice != len(value):
                raise ValueError("The sizes of index and values must be the same")

        self._data[index] = value.get_value()

    def __eq__(self, other):
        if isinstance(other, HexData):
            if len(self) != len(other):
                return False
            return np.alltrue(np.equal(self.get_value(), other.get_value()))
        else:
            return self.to_number() == HexData(other).to_number()

    def __add__(self, other):
        if not isinstance(other, HexData):
            raise ValueError("One parameter is not a HexData object")
        return HexData(np.concatenate((self.get_value(), other.get_value())))
