import unittest
import numpy as np
import scipy.stats as scipy_stats
from pyhexdata.HexData import HexData


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
    list_value = list([158, 63, 152, 5, 253, 234, 57, 135, 44, 141, 62, 65, 160, 214, 144, 196, 20, 62,
                        91, 121, 105, 33, 162, 97, 148, 107, 112, 50, 190, 151, 198, 235, 175, 12, 42, 207,
                        193, 46, 235, 122, 21, 237, 58, 51, 65, 6, 32, 18, 136, 56, 144, 72, 50, 231,
                        106, 5, 88, 247, 93, 248, 242, 202, 54, 142, 116, 192, 65, 48, 176, 236, 151, 90,
                        221, 146, 78, 38, 164, 24, 197, 239, 51, 70, 172, 232, 67, 111, 220, 246, 190, 222,
                        73, 35, 96, 142, 32, 84, 201, 93, 112, 234, 26, 48, 253, 188, 187, 46, 21, 254,
                        255, 31, 216, 147, 25, 56, 226, 177, 58, 176, 63, 46, 180, 67, 35, 8, 23, 154,
                        173, 163])

    # Value padded 4 bytes
    numpy_value_padded_4_bytes = np.array([23, 154, 173, 163])
    int_value_padded_4_bytes = int("179aada3", 16)
    str_spaced_value_padded_4_bytes = "17 9a ad a3"
    str_value_padded_4_bytes = "179aada3"
    bytes_value_padded_4_bytes = b'\x17\x9a\xad\xa3'
    list_value_padded_4_bytes = list([23, 154, 173, 163])

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
    list_value_padded_133_bytes = list([0, 0, 0, 0, 0, 158, 63, 152, 5, 253, 234, 57, 135, 44, 141, 62, 65, 160,
                                     214, 144, 196, 20, 62,  91, 121, 105, 33, 162, 97, 148, 107, 112, 50, 190,
                                     151, 198, 235, 175, 12, 42, 207, 193, 46, 235, 122, 21, 237, 58, 51, 65, 6,
                                     32, 18, 136, 56, 144, 72, 50, 231, 106, 5, 88, 247, 93, 248, 242, 202, 54,
                                     142, 116, 192, 65, 48, 176, 236, 151, 90, 221, 146, 78, 38, 164, 24, 197,
                                     239, 51, 70, 172, 232, 67, 111, 220, 246, 190, 222, 73, 35, 96, 142, 32,
                                     84, 201, 93, 112, 234, 26, 48, 253, 188, 187, 46, 21, 254, 255, 31, 216,
                                     147, 25, 56, 226, 177, 58, 176, 63, 46, 180, 67, 35, 8, 23, 154, 173, 163])

    # Value right padded 4 bytes
    numpy_value_right_padded_4_bytes = np.array([158, 63, 152, 5])
    int_value_right_padded_4_bytes = int("9e3f9805", 16)
    str_spaced_value_right_padded_4_bytes = "9e 3f 98 05"
    str_value_right_padded_4_bytes = "9e3f9805"
    bytes_value_right_padded_4_bytes = b'\x9e?\x98\x05'
    list_value_right_padded_4_bytes = list([158, 63, 152, 5])

    # Value padded 133 bytes
    numpy_value_right_padded_133_bytes = np.array([158, 63, 152, 5, 253, 234, 57, 135, 44, 141, 62, 65, 160,
                                                   214, 144, 196, 20, 62, 91, 121, 105, 33, 162, 97, 148, 107, 112, 50, 190,
                                                   151, 198, 235, 175, 12, 42, 207, 193, 46, 235, 122, 21, 237, 58, 51, 65, 6,
                                                   32, 18, 136, 56, 144, 72, 50, 231, 106, 5, 88, 247, 93, 248, 242, 202, 54,
                                                   142, 116, 192, 65, 48, 176, 236, 151, 90, 221, 146, 78, 38, 164, 24, 197,
                                                   239, 51, 70, 172, 232, 67, 111, 220, 246, 190, 222, 73, 35, 96, 142, 32,
                                                   84, 201, 93, 112, 234, 26, 48, 253, 188, 187, 46, 21, 254, 255, 31, 216,
                                                   147, 25, 56, 226, 177, 58, 176, 63, 46, 180, 67, 35, 8, 23, 154, 173, 163,
                                                   0, 0, 0, 0, 0])
    str_spaced_value_right_padded_133_bytes = "9e 3f 98 05 fd ea 39 87 2c 8d 3e 41 a0 d6 90 c4 14 3e 5b 79 69 21 a2 61 94 6b 70 32 be 97 c6 eb " \
                                        "af 0c 2a cf c1 2e eb 7a 15 ed 3a 33 41 06 20 12 88 38 90 48 32 e7 6a 05 58 f7 5d f8 f2 ca 36 8e " \
                                        "74 c0 41 30 b0 ec 97 5a dd 92 4e 26 a4 18 c5 ef 33 46 ac e8 43 6f dc f6 be de 49 23 60 8e 20 54 " \
                                        "c9 5d 70 ea 1a 30 fd bc bb 2e 15 fe ff 1f d8 93 19 38 e2 b1 3a b0 3f 2e b4 43 23 08 17 9a ad a3 00 00 00 00 00"
    str_value_right_padded_133_bytes = "9e3f9805fdea39872c8d3e41a0d690c4143e5b796921a261946b7032be97c6ebaf0c2acfc12eeb7a15ed3a33410620128838904" \
                                 "832e76a0558f75df8f2ca368e74c04130b0ec975add924e26a418c5ef3346ace8436fdcf6bede4923608e2054c95d70ea1a30fd" \
                                 "bcbb2e15feff1fd8931938e2b13ab03f2eb4432308179aada30000000000"
    bytes_value_right_padded_133_bytes = b'\x9e?\x98\x05\xfd\xea9\x87,\x8d>A\xa0\xd6\x90\xc4\x14>[yi!\xa2a\x94kp2\xbe\x97\xc6\xeb\xaf\x0c*\xcf' \
                                   b'\xc1.\xebz\x15\xed:3A\x06 \x12\x888\x90H2\xe7j\x05X\xf7]\xf8\xf2\xca6\x8et\xc0A0\xb0\xec\x97Z\xdd' \
                                   b'\x92N&\xa4\x18\xc5\xef3F\xac\xe8Co\xdc\xf6\xbe\xdeI#`\x8e T\xc9]p\xea\x1a0\xfd\xbc\xbb.\x15\xfe\xff' \
                                   b'\x1f\xd8\x93\x198\xe2\xb1:\xb0?.\xb4C#\x08\x17\x9a\xad\xa3\x00\x00\x00\x00\x00'
    list_value_right_padded_133_bytes = list([158, 63, 152, 5, 253, 234, 57, 135, 44, 141, 62, 65, 160,
                                        214, 144, 196, 20, 62, 91, 121, 105, 33, 162, 97, 148, 107, 112, 50, 190,
                                        151, 198, 235, 175, 12, 42, 207, 193, 46, 235, 122, 21, 237, 58, 51, 65, 6,
                                        32, 18, 136, 56, 144, 72, 50, 231, 106, 5, 88, 247, 93, 248, 242, 202, 54,
                                        142, 116, 192, 65, 48, 176, 236, 151, 90, 221, 146, 78, 38, 164, 24, 197,
                                        239, 51, 70, 172, 232, 67, 111, 220, 246, 190, 222, 73, 35, 96, 142, 32,
                                        84, 201, 93, 112, 234, 26, 48, 253, 188, 187, 46, 21, 254, 255, 31, 216,
                                        147, 25, 56, 226, 177, 58, 176, 63, 46, 180, 67, 35, 8, 23, 154, 173, 163,
                                        0, 0, 0, 0, 0])

    # --------------------------------------------------------------------------------------------
    # ------------------------------------- Test HexData -----------------------------------------
    # --------------------------------------------------------------------------------------------
    def test_init(self):
        # Numpy
        HD = HexData(value=self.numpy_value)
        np.testing.assert_array_equal(HD.value, self.numpy_value)
        self.assertEqual(HD.number, self.int_value)
        self.assertEqual(HD.string_spaced, self.str_spaced_value)
        self.assertEqual(HD.string, self.str_value)
        self.assertEqual(HD.bytes, self.bytes_value)
        self.assertEqual(HD.list, self.list_value)

        # Integer
        HD = HexData(value=self.int_value)
        np.testing.assert_array_equal(HD.value, self.numpy_value)
        self.assertEqual(HD.number, self.int_value)
        self.assertEqual(HD.string_spaced, self.str_spaced_value)
        self.assertEqual(HD.string, self.str_value)
        self.assertEqual(HD.bytes, self.bytes_value)
        self.assertEqual(HD.list, self.list_value)

        # String spaced
        HD = HexData(value=self.str_spaced_value)
        np.testing.assert_array_equal(HD.value, self.numpy_value)
        self.assertEqual(HD.number, self.int_value)
        self.assertEqual(HD.string_spaced, self.str_spaced_value)
        self.assertEqual(HD.string, self.str_value)
        self.assertEqual(HD.bytes, self.bytes_value)
        self.assertEqual(HD.list, self.list_value)

        # String without spaced
        HD = HexData(value=self.str_value)
        np.testing.assert_array_equal(HD.value, self.numpy_value)
        self.assertEqual(HD.number, self.int_value)
        self.assertEqual(HD.string_spaced, self.str_spaced_value)
        self.assertEqual(HD.string, self.str_value)
        self.assertEqual(HD.bytes, self.bytes_value)
        self.assertEqual(HD.list, self.list_value)

        # Bytes
        HD = HexData(value=self.bytes_value)
        np.testing.assert_array_equal(HD.value, self.numpy_value)
        self.assertEqual(HD.number, self.int_value)
        self.assertEqual(HD.string_spaced, self.str_spaced_value)
        self.assertEqual(HD.string, self.str_value)
        self.assertEqual(HD.bytes, self.bytes_value)
        self.assertEqual(HD.list, self.list_value)

        # List
        HD = HexData(value=self.list_value)
        np.testing.assert_array_equal(HD.value, self.numpy_value)
        self.assertEqual(HD.number, self.int_value)
        self.assertEqual(HD.string_spaced, self.str_spaced_value)
        self.assertEqual(HD.string, self.str_value)
        self.assertEqual(HD.bytes, self.bytes_value)
        self.assertEqual(HD.list, self.list_value)

    def test_padding(self):
        # Hex data padding 4 bytes init
        HD = HexData(value=self.int_value, padding=4)
        np.testing.assert_array_equal(HD.value, self.numpy_value_padded_4_bytes)
        self.assertEqual(HD.number, self.int_value_padded_4_bytes)
        self.assertEqual(HD.string_spaced, self.str_spaced_value_padded_4_bytes)
        self.assertEqual(HD.string, self.str_value_padded_4_bytes)
        self.assertEqual(HD.bytes, self.bytes_value_padded_4_bytes)
        self.assertEqual(HD.list, self.list_value_padded_4_bytes)

        # Hex data padding 133 bytes init
        HD = HexData(value=self.int_value, padding=133)
        np.testing.assert_array_equal(HD.value, self.numpy_value_padded_133_bytes)
        self.assertEqual(HD.number, self.int_value)
        self.assertEqual(HD.string_spaced, self.str_spaced_value_padded_133_bytes)
        self.assertEqual(HD.string, self.str_value_padded_133_bytes)
        self.assertEqual(HD.bytes, self.bytes_value_padded_133_bytes)
        self.assertEqual(HD.list, self.list_value_padded_133_bytes)

        # Hex data padding 4 bytes
        HD = HexData(value=self.int_value)
        HD.padding(4)
        np.testing.assert_array_equal(HD.value, self.numpy_value_padded_4_bytes)
        self.assertEqual(HD.number, self.int_value_padded_4_bytes)
        self.assertEqual(HD.string_spaced, self.str_spaced_value_padded_4_bytes)
        self.assertEqual(HD.string, self.str_value_padded_4_bytes)
        self.assertEqual(HD.bytes, self.bytes_value_padded_4_bytes)
        self.assertEqual(HD.list, self.list_value_padded_4_bytes)

        # Hex data padding 133 bytes
        HD = HexData(value=self.int_value)
        HD.padding(133)
        np.testing.assert_array_equal(HD.value, self.numpy_value_padded_133_bytes)
        self.assertEqual(HD.number, self.int_value)
        self.assertEqual(HD.string_spaced, self.str_spaced_value_padded_133_bytes)
        self.assertEqual(HD.string, self.str_value_padded_133_bytes)
        self.assertEqual(HD.bytes, self.bytes_value_padded_133_bytes)
        self.assertEqual(HD.list, self.list_value_padded_133_bytes)

    def test_right_padding(self):
        # Hex data padding 4 bytes
        HD = HexData(value=self.int_value)
        HD.right_padding(4)
        np.testing.assert_array_equal(HD.value, self.numpy_value_right_padded_4_bytes)
        self.assertEqual(HD.number, self.int_value_right_padded_4_bytes)
        self.assertEqual(HD.string_spaced, self.str_spaced_value_right_padded_4_bytes)
        self.assertEqual(HD.string, self.str_value_right_padded_4_bytes)
        self.assertEqual(HD.bytes, self.bytes_value_right_padded_4_bytes)
        self.assertEqual(HD.list, self.list_value_right_padded_4_bytes)

        # Hex data padding 133 bytes
        HD = HexData(value=self.int_value)
        HD.right_padding(133)
        np.testing.assert_array_equal(HD.value, self.numpy_value_right_padded_133_bytes)
        self.assertEqual(HD.number, self.int_value<<((133 - self.numpy_value.shape[0])*8))
        self.assertEqual(HD.string_spaced, self.str_spaced_value_right_padded_133_bytes)
        self.assertEqual(HD.string, self.str_value_right_padded_133_bytes)
        self.assertEqual(HD.bytes, self.bytes_value_right_padded_133_bytes)
        self.assertEqual(HD.list, self.list_value_right_padded_133_bytes)

    def test_rand(self):
        nr_traces = 512_000
        bytes_0 = np.empty(nr_traces, dtype=np.uint8)
        bytes_1 = np.empty(nr_traces, dtype=np.uint8)
        for i in range(nr_traces):
            HD = HexData.rand(2)

            val = HD.value

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

    def test_xor(self):
        # A and B same lenght
        A = HexData.rand(4)
        B = HexData.rand(4)
        th_res = A.number ^ B.number
        self.assertEqual((A ^ B).number, th_res)

        # A longer than B
        A = HexData.rand(6)
        B = HexData.rand(4)
        th_res = A.number ^ B.number
        self.assertEqual((A ^ B).number, th_res)

        # A smaller than B
        A = HexData.rand(4)
        B = HexData.rand(7)
        th_res = A.number ^ B.number
        self.assertEqual((A ^ B).number, th_res)

        # Check for all types
        A = HexData(0x53)
        B = HexData(0xA5)
        th_res = A.number ^ B.number
        self.assertEqual((A ^ B).number, th_res)
        self.assertEqual((A ^ B.value).number, th_res)
        self.assertEqual((A ^ B.list).number, th_res)
        self.assertEqual((A ^ B.string).number, th_res)
        self.assertEqual((A ^ B.bytes).number, th_res)
        self.assertEqual((A ^ B.number).number, th_res)

    def test_str(self):
        # A and B same lenght
        A = HexData.rand(4)
        self.assertEqual(str(A), A.string_spaced)

    def test_len(self):
        self.assertEqual(len(HexData.rand(7)), 7)
        self.assertEqual(len(HexData.rand(13)), 13)
        self.assertEqual(len(HexData.rand(3)), 3)

    def test_getitem(self):
        # Set value
        A = HexData("00112233445566778899AABBCCDDEEFF")

        # Integer
        self.assertTrue(A[0] == HexData("00"))
        self.assertTrue(A[1] == HexData("11"))
        self.assertTrue(A[2] == HexData("22"))
        self.assertTrue(A[3] == HexData("33"))
        self.assertTrue(A[4] == HexData("44"))
        self.assertTrue(A[5] == HexData("55"))
        self.assertTrue(A[6] == HexData("66"))
        self.assertTrue(A[7] == HexData("77"))
        self.assertTrue(A[8] == HexData("88"))
        self.assertTrue(A[9] == HexData("99"))
        self.assertTrue(A[10] == HexData("AA"))
        self.assertTrue(A[11] == HexData("BB"))
        self.assertTrue(A[12] == HexData("CC"))
        self.assertTrue(A[13] == HexData("DD"))
        self.assertTrue(A[14] == HexData("EE"))
        self.assertTrue(A[15] == HexData("FF"))

        # Slices
        self.assertTrue(A[3:8] == HexData("3344556677"))
        self.assertTrue(A[:5] == HexData("0011223344"))
        self.assertTrue(A[13:] == HexData("DDEEFF"))

        # Numpy array
        self.assertTrue(A[np.arange(3, 8)] ==  HexData("3344556677"))
        self.assertTrue(A[np.arange(5)] == HexData("0011223344"))
        self.assertTrue(A[np.arange(13, 16)] == HexData("DDEEFF"))

        # List
        self.assertTrue(A[[3, 4, 5, 6, 7]] == HexData("3344556677"))
        self.assertTrue(A[[0, 1, 2, 3, 4]] == HexData("0011223344"))
        self.assertTrue(A[[13, 14, 15]] == HexData("DDEEFF"))

    def test_setitem(self):
        # Integer
        A = HexData(0, padding=16)
        self.assertTrue(A == HexData(0, padding=16))
        A[3] = int("33", 16)
        self.assertTrue(A[3] == HexData("33"))

        # All types test
        B = HexData("11223344")
        # HexData
        A = HexData(0, padding=4)
        A[:4] = HexData("11223344")
        self.assertTrue(A == B)
        # Value
        A = HexData(0, padding=4)
        A[:4] = HexData("11223344").value
        self.assertTrue(A == B)
        # List
        A = HexData(0, padding=4)
        A[:4] = HexData("11223344").list
        self.assertTrue(A == B)
        # String
        A = HexData(0, padding=4)
        A[:4] = HexData("11223344").string
        self.assertTrue(A == B)
        # Bytes
        A = HexData(0, padding=4)
        A[:4] = HexData("11223344").bytes
        self.assertTrue(A == B)
        # Number
        A = HexData(0, padding=4)
        A[:4] = HexData("11223344").number
        self.assertTrue(A == B)

    def test_equal(self):
        A = HexData("00112233445566778899AABBCCDDEEFF")
        B = HexData("00112233445566778899AABBCCDDEEFF")
        self.assertTrue(A == B)
        B = HexData("0011223344556677")
        self.assertTrue(A != B)
        B = HexData("00112233440000008899AABBCCDDEEFF")
        self.assertTrue(A != B)
        A = HexData("00112233")
        B = HexData("00112233445566778899AABBCCDDEEFF")
        self.assertTrue(A != B)

        # All types test
        A = HexData("11223344")
        self.assertTrue(A == HexData("11223344"))
        self.assertTrue(A == HexData("11223344").value)
        self.assertTrue(A == HexData("11223344").list)
        self.assertTrue(A == HexData("11223344").string)
        self.assertTrue(A == HexData("11223344").bytes)
        self.assertTrue(A == HexData("11223344").number)

    def test_add(self):
        A = HexData("00112233")
        B = HexData("445566778899AABBCCDDEEFF")
        C = HexData("00112233445566778899AABBCCDDEEFF")
        self.assertTrue(A+B == C)
        self.assertTrue(A+HexData() == A)

    def test_mul(self):
        A = HexData("00112233")
        B = 0x03
        C = HexData("001122330011223300112233")
        self.assertTrue(A * B == C)
        self.assertTrue(A * 0 == HexData())


if __name__ == '__main__':
    unittest.main
