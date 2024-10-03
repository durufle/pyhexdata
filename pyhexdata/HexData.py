import numpy as np
import math


class HexData:
    """
    HexData class
    """

    def __init__(self, value=None, padding=None):
        """
        The function __init__ initialize the object HexData from a integer value or a hexdecimal string value with or
        without spaces or a numpy array dtyped np.uint8.
        The final value is stored in a numpy array format inside the class.

        @param value (int, str or numpy array, optional): the value to pass to HexData
        @param padding (int, optional): the number of bytes to keep (could be higher or smaller than the real number
           of bytes)
        """
        self._data = np.array([])
        if not(value is None):
            if isinstance(value, np.ndarray):
                self._data = value.astype(np.uint8)
            elif isinstance(value, list):
                self._data = np.array(value, dtype=np.uint8)
            elif isinstance(value, bytes):
                self._data = np.array(np.frombuffer(value, dtype=np.uint8))
            elif isinstance(value, bytearray):
                self._data = np.array(np.frombuffer(value, dtype=np.uint8))
            elif isinstance(value, np.uint8):
                self._data = np.array([value], dtype=np.uint8)
            elif isinstance(value, str):
                value = value.replace(" ", "")

                if len(value) % 2 == 1:
                        value = "0" + value

                # String read
                byte_value = bytes.fromhex(value)
                self._data = np.array(np.frombuffer(byte_value, dtype=np.uint8))
            elif isinstance(value, int) or isinstance(value, int):
                nr_bytes = max(1, math.ceil(value.bit_length() / 8.))

                # Integer read
                byte_value = value.to_bytes(nr_bytes, "big", signed=False)
                self._data = np.array(np.frombuffer(byte_value, dtype=np.uint8))
            else:
                raise TypeError("This type is not allowed")

        if padding is not None:
            self.padding(padding)

    @property
    def value(self):
        """
        This property methods returns the value of the numpy array

        @return: numpy array
        """
        return self._data

    @property
    def list(self) -> list:
        """
        This property methods returns the list value

        @return: list
        """
        return self._data.tolist()

    @property
    def string(self):
        """
        This property methods returns the string value without spaces

        @return: str hexadecimal
        """
        if len(self) > 0:
            return "".join(["{:02x}".format(x) for x in self._data])
        return ""

    @property
    def string_spaced(self):
        """
        This property methods returns the string value with spaces

        @return: str hexadecimal
        """
        if len(self) > 0:
            return " ".join(["{:02x}".format(x) for x in self._data])
        return ""

    @property
    def bytes(self):
        """
        This property methods returns the bytes value

        @return: bytes
        """
        return self._data.tobytes()

    @property
    def bytearray(self):
        """
        This property methods returns the bytes value

        @return: bytes
        """
        return bytearray(self._data)

    @property
    def number(self):
        """
        This property methods returns the integer value (could be big integer)

        @return: int
        """
        if len(self) > 0:
            return int.from_bytes(self._data.tobytes(), "big", signed=False)
        return 0

    def padding(self, nr_bytes):
        """
        This function forces the left padding of the _data attribute internally. This does not affect the represented
        integer value.

        @param nr_bytes: the number of bytes of the _data attribute
        @return:
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
        This function forces the left padding of the _data attribute internally. This does affect the represented
        integer value.

        @param nr_bytes: the number of bytes of the _data attribute
        @return:
        """
        diff = nr_bytes - self._data.shape[0]
        if diff > 0:
            self._data = np.concatenate((self._data, np.zeros(diff, dtype=np.uint8)))
        elif diff < 0:
            self._data = self._data[:nr_bytes]
        else:
            pass

    @staticmethod
    def rand(nr_bytes):
        """
        This function generates a random bytes array composed by nr_bytes. Note that, the padding is automatically
        performed. The random can starts by 00

        @param nr_bytes: number of bytes of the random to generate.
        @return: HexData object with random bytes
        """
        data = np.array(np.frombuffer(np.random.bytes(nr_bytes), dtype=np.uint8))

        return HexData(value=data)

    def __xor__(self, other):
        """
        Override method to xor One HexData object with another value (all HexData allowed types).

        @param other (al allowed type for HexData): HexData object to use for the xor
        @return: xor of two values
        """
        if not isinstance(other, HexData):
            try:
                other = HexData(other)
            except:
                raise ValueError("The type of the second parameter for XOR is not allowed")

        # Check len are same
        if len(self) != len(other):
            max_len = max(len(self), len(other))

            if len(self) != max_len:
                self.padding(max_len)

            if len(other) != max_len:
                other.padding(max_len)

        return HexData(np.bitwise_xor(self._data, other._data))

    def __str__(self):
        """
        Override method to returns string_spaced

        @return: string_spaced
        """
        return self.string_spaced

    def __len__(self):
        """
        Override method to returns the object length in bytes

        @return: length in bytes
        """
        return self._data.shape[0]

    def __getitem__(self, index):
        """
        Override method for getitem.

        E.g:
        A = HexData("00112233445566778899")
        B = A[3]   #0x33
        C = A[5:8] #0x556677

        @param index: index(es) to get. It could be list, np.ndarray, slice and int)
        @return: HexData[index]
        """
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
        """
        Override method for getitem.

        E.g:
        A = HexData("00112200440000008899")
        A[3] = 0x33
        A[5:8] = "556677"
        A will be equals to A = HexData("00112233445566778899")

        @param index: index(es) to get. It could be list, np.ndarray, slice and int)
        @param value: value(es) to set. It could be all HexData allowed types.
        @return:
        """
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
        if not isinstance(value, HexData):
            try:
                value = HexData(value)
            except:
                raise ValueError("The type of the second parameter for XOR is not allowed")

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

        self._data[index] = value.value

    def __eq__(self, other):
        """
        Override method to for equals condition test. Check that self and other are equals in value and length.

        @param other: Value to compare. It could be all HexData allowed types.
        @return: conditional test comparison
        """
        if not isinstance(other, HexData):
            try:
                other = HexData(other)
            except:
                raise ValueError("The type of the second parameter for XOR is not allowed")

        # Perform comparison
        if len(self) != len(other):
            return False
        return np.all(np.equal(self.value, other.value))

    def __add__(self, other):
        """
        Override method for adding two HexData object. This corresponds to the concatenation of the two objects.

        @param other: HexData object to add
        @return: Concatenation of the two objects
        """

        if not isinstance(other, HexData):
            raise ValueError("The second parameter is not a HexData object")
        return HexData(np.concatenate((self.value, other.value)))

    def __mul__(self, other):
        """
        Override method to reproduce the HexData object as many times as other value. This will corresponds to the
        concatenation of itself as many times as the other value.

        @param other: integer to reproduce the HexData object
        @return: Reproduction of the HexData value. This will corresponds to the concatenation of itself as many times
        as the other value
        """
        if not isinstance(other, int):
            raise ValueError("The second parameter is not an integer")
        return HexData(np.tile(self.value, other))
