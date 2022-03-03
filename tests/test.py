import unittest
import numpy as np
import scipy.stats as scipy_stats
from pyhexdata.pyhexdata.HexData import HexData


class HexData_Test(unittest.TestCase):
    # Values normal
    numpy_value = np.array([158, 63, 152, 5, 253, 234, 57, 135, 44, 141, 62, 65, 160, 214, 144, 196, 20, 62,
                            91, 121, 105, 33, 162, 97, 148, 107, 112, 50, 190, 151, 198, 235, 175, 12, 42, 207,
                            193, 46, 235, 122, 21, 237, 58, 51, 65, 6, 32, 18, 136, 56, 144, 72, 50, 231,
                            106, 5, 88, 247, 93, 248, 242, 202, 54, 142, 116, 192, 65, 48, 176, 236, 151, 90,
                            221, 146, 78, 38, 164, 24, 197, 239, 51, 70, 172, 232, 67, 111, 220, 246, 190, 222,
                            73, 35, 96, 142, 32, 84, 201, 93, 112, 234, 26, 48, 253, 188, 187, 46, 21, 254,
                            255, 31, 216, 147, 25, 56, 226, 177, 58, 176, 63, 46, 180, 67, 35, 8, 23, 154,
                            173, 163])
    int_value = 111125815019327408388141993602375549909825290645250963182571230815758222161610599097341856981961119398420638843875753817458740611451486741552245723353329687395175599284589262074399779130831386320655639292146551623810796546018531646557197490155710779931501105486281349525904742854698101862615651198881645637027
    str_spaced_value = "9e 3f 98 05 fd ea 39 87 2c 8d 3e 41 a0 d6 90 c4 14 3e 5b 79 69 21 a2 61 94 6b 70 32 be 97 c6 eb " \
                       "af 0c 2a cf c1 2e eb 7a 15 ed 3a 33 41 06 20 12 88 38 90 48 32 e7 6a 05 58 f7 5d f8 f2 ca 36 8e " \
                       "74 c0 41 30 b0 ec 97 5a dd 92 4e 26 a4 18 c5 ef 33 46 ac e8 43 6f dc f6 be de 49 23 60 8e 20 54 " \
                       "c9 5d 70 ea 1a 30 fd bc bb 2e 15 fe ff 1f d8 93 19 38 e2 b1 3a b0 3f 2e b4 43 23 08 17 9a ad a3"
    str_value = "9e3f9805fdea39872c8d3e41a0d690c4143e5b796921a261946b7032be97c6ebaf0c2acfc12eeb7a15ed3a33410620128838904" \
                "832e76a0558f75df8f2ca368e74c04130b0ec975add924e26a418c5ef3346ace8436fdcf6bede4923608e2054c95d70ea1a30fd" \
                "bcbb2e15feff1fd8931938e2b13ab03f2eb4432308179aada3"
    bytes_value = b'\x9e?\x98\x05\xfd\xea9\x87,\x8d>A\xa0\xd6\x90\xc4\x14>[yi!\xa2a\x94kp2\xbe\x97\xc6\xeb\xaf\x0c*\xcf' \
                  b'\xc1.\xebz\x15\xed:3A\x06 \x12\x888\x90H2\xe7j\x05X\xf7]\xf8\xf2\xca6\x8et\xc0A0\xb0\xec\x97Z\xdd' \
                  b'\x92N&\xa4\x18\xc5\xef3F\xac\xe8Co\xdc\xf6\xbe\xdeI#`\x8e T\xc9]p\xea\x1a0\xfd\xbc\xbb.\x15\xfe\xff' \
                  b'\x1f\xd8\x93\x198\xe2\xb1:\xb0?.\xb4C#\x08\x17\x9a\xad\xa3'

    # Value padded 4 bytes
    numpy_value_padded_4_bytes = np.array([23, 154, 173, 163])
    int_value_padded_4_bytes = int("179aada3", 16)
    str_spaced_value_padded_4_bytes = "17 9a ad a3"
    str_value_padded_4_bytes = "179aada3"
    bytes_value_padded_4_bytes = b'\x17\x9a\xad\xa3'

    # Value padded 133 bytes
    numpy_value_padded_133_bytes = np.array([0, 0, 0, 0, 0, 158, 63, 152, 5, 253, 234, 57, 135, 44, 141, 62, 65, 160,
                                             214, 144, 196, 20, 62,  91, 121, 105, 33, 162, 97, 148, 107, 112, 50, 190,
                                             151, 198, 235, 175, 12, 42, 207, 193, 46, 235, 122, 21, 237, 58, 51, 65, 6,
                                             32, 18, 136, 56, 144, 72, 50, 231, 106, 5, 88, 247, 93, 248, 242, 202, 54,
                                             142, 116, 192, 65, 48, 176, 236, 151, 90, 221, 146, 78, 38, 164, 24, 197,
                                             239, 51, 70, 172, 232, 67, 111, 220, 246, 190, 222, 73, 35, 96, 142, 32,
                                             84, 201, 93, 112, 234, 26, 48, 253, 188, 187, 46, 21, 254, 255, 31, 216,
                                             147, 25, 56, 226, 177, 58, 176, 63, 46, 180, 67, 35, 8, 23, 154, 173, 163])
    str_spaced_value_padded_133_bytes = "00 00 00 00 00 9e 3f 98 05 fd ea 39 87 2c 8d 3e 41 a0 d6 90 c4 14 3e 5b 79 69 21 a2 61 94 6b 70 32 be 97 c6 eb " \
                       "af 0c 2a cf c1 2e eb 7a 15 ed 3a 33 41 06 20 12 88 38 90 48 32 e7 6a 05 58 f7 5d f8 f2 ca 36 8e " \
                       "74 c0 41 30 b0 ec 97 5a dd 92 4e 26 a4 18 c5 ef 33 46 ac e8 43 6f dc f6 be de 49 23 60 8e 20 54 " \
                       "c9 5d 70 ea 1a 30 fd bc bb 2e 15 fe ff 1f d8 93 19 38 e2 b1 3a b0 3f 2e b4 43 23 08 17 9a ad a3"
    str_value_padded_133_bytes = "00000000009e3f9805fdea39872c8d3e41a0d690c4143e5b796921a261946b7032be97c6ebaf0c2acfc12eeb7a15ed3a33410620128838904" \
                "832e76a0558f75df8f2ca368e74c04130b0ec975add924e26a418c5ef3346ace8436fdcf6bede4923608e2054c95d70ea1a30fd" \
                "bcbb2e15feff1fd8931938e2b13ab03f2eb4432308179aada3"
    bytes_value_padded_133_bytes = b'\x00\x00\x00\x00\x00\x9e?\x98\x05\xfd\xea9\x87,\x8d>A\xa0\xd6\x90\xc4\x14>[yi!\xa2a\x94kp2\xbe\x97\xc6\xeb\xaf\x0c*\xcf' \
                  b'\xc1.\xebz\x15\xed:3A\x06 \x12\x888\x90H2\xe7j\x05X\xf7]\xf8\xf2\xca6\x8et\xc0A0\xb0\xec\x97Z\xdd' \
                  b'\x92N&\xa4\x18\xc5\xef3F\xac\xe8Co\xdc\xf6\xbe\xdeI#`\x8e T\xc9]p\xea\x1a0\xfd\xbc\xbb.\x15\xfe\xff' \
                  b'\x1f\xd8\x93\x198\xe2\xb1:\xb0?.\xb4C#\x08\x17\x9a\xad\xa3'

    # --------------------------------------------------------------------------------------------
    # ------------------------------------- Test HexData -----------------------------------------
    # --------------------------------------------------------------------------------------------
    def test_numpy_array(self):
        HD = HexData(value=self.numpy_value)

        self.assertEqual(HD.to_string(spaces=True), self.str_spaced_value)
        self.assertEqual(HD.to_string(spaces=False), self.str_value)
        self.assertEqual(HD.to_bytes(), self.bytes_value)
        self.assertEqual(HD.to_number(), self.int_value)

    def test_bytes(self):
        HD = HexData(value=self.bytes_value)

        self.assertEqual(HD.to_string(spaces=True), self.str_spaced_value)
        self.assertEqual(HD.to_string(spaces=False), self.str_value)
        self.assertEqual(HD.to_bytes(), self.bytes_value)
        self.assertEqual(HD.to_number(), self.int_value)

    def test_string_with_spaces(self):
        HD = HexData(value=self.str_spaced_value)

        self.assertEqual(HD.to_string(spaces=True), self.str_spaced_value)
        self.assertEqual(HD.to_string(spaces=False), self.str_value)
        self.assertEqual(HD.to_bytes(), self.bytes_value)
        self.assertEqual(HD.to_number(), self.int_value)

    def test_string_without_spaces(self):
        HD = HexData(value=self.str_value)

        self.assertEqual(HD.to_string(spaces=True), self.str_spaced_value)
        self.assertEqual(HD.to_string(spaces=False), self.str_value)
        self.assertEqual(HD.to_bytes(), self.bytes_value)
        self.assertEqual(HD.to_number(), self.int_value)

    def test_integer(self):
        HD = HexData(value=self.int_value)

        self.assertEqual(HD.to_string(spaces=True), self.str_spaced_value)
        self.assertEqual(HD.to_string(spaces=False), self.str_value)
        self.assertEqual(HD.to_bytes(), self.bytes_value)
        self.assertEqual(HD.to_number(), self.int_value)

    def test_padding_smaller(self):
        HD = HexData(value=self.int_value)
        HD.padding(4)

        self.assertEqual(HD.to_string(spaces=True), self.str_spaced_value_padded_4_bytes)
        self.assertEqual(HD.to_string(spaces=False), self.str_value_padded_4_bytes)
        self.assertEqual(HD.to_bytes(), self.bytes_value_padded_4_bytes)
        self.assertEqual(HD.to_number(), self.int_value_padded_4_bytes)

    def test_padding_higher(self):
        HD = HexData(value=self.int_value)
        HD.padding(133)

        self.assertEqual(HD.to_string(spaces=True), self.str_spaced_value_padded_133_bytes)
        self.assertEqual(HD.to_string(spaces=False), self.str_value_padded_133_bytes)
        self.assertEqual(HD.to_bytes(), self.bytes_value_padded_133_bytes)
        self.assertEqual(HD.to_number(), self.int_value)

    def test_rand(self):
        nr_traces = 256_000
        bytes_0 = np.empty(nr_traces, dtype=np.uint8)
        bytes_1 = np.empty(nr_traces, dtype=np.uint8)
        for i in range(nr_traces):
            HD = HexData.rand(2)

            val = HD.get_value()

            bytes_0[i] = val[0]
            bytes_1[i] = val[1]

        # Check statistical test
        unique, counts = np.unique(bytes_0, return_counts=True)
        self.assertTrue(np.all(unique == np.arange(256)))
        statistic, p = scipy_stats.chisquare(counts)
        self.assertTrue(p > 0.05)

        unique, counts = np.unique(bytes_1, return_counts=True)
        self.assertTrue(np.all(unique == np.arange(256)))
        statistic, p = scipy_stats.chisquare(counts)
        self.assertTrue(p > 0.05)


if __name__ == '__main__':
    unittest.main()
