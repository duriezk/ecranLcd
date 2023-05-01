import unittest

from lcd import Lcd


class TestLcdClass(unittest.TestCase):

    def test_set_matrix_0(self):
        lcd = Lcd("0")
        self.assertEqual(lcd.number_matrix, [[" _ "], ["| |"], ["|_|"]])

    def test_set_matrix_1(self):
        lcd = Lcd("1")
        self.assertEqual(lcd.number_matrix, [["   "], ["  |"], ["  |"]])

    def test_set_matrix_2(self):
        lcd = Lcd("2")
        self.assertEqual(lcd.number_matrix, [[" _ "], [" _|"], ["|_ "]])

    def test_set_matrix_3(self):
        lcd = Lcd("3")
        self.assertEqual(lcd.number_matrix, [[" _ "], [" _|"], [" _|"]])

    def test_set_matrix_4(self):
        lcd = Lcd("4")
        self.assertEqual(lcd.number_matrix, [["   "], ["|_|"], ["  |"]])

    def test_set_matrix_5(self):
        lcd = Lcd("5")
        self.assertEqual(lcd.number_matrix, [[" _ "], ["|_ "], [" _|"]])

    def test_set_matrix_6(self):
        lcd = Lcd("6")
        self.assertEqual(lcd.number_matrix, [[" _ "], ["|_ "], ["|_|"]])

    def test_set_matrix_7(self):
        lcd = Lcd("7")
        self.assertEqual(lcd.number_matrix, [[" _ "], ["  |"], ["  |"]])

    def test_set_matrix_8(self):
        lcd = Lcd("8")
        self.assertEqual(lcd.number_matrix, [[" _ "], ["|_|"], ["|_|"]])

    def test_set_matrix_9(self):
        lcd = Lcd("9")
        self.assertEqual(lcd.number_matrix, [[" _ "], ["|_|"], ["  |"]])

    def test_display(self):
        lcd = Lcd("9")
        self.assertEqual(lcd.display(), " _ \n|_|\n  |\n")


if __name__ == '__main__':
    unittest.main()
