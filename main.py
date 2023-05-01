import sys

from lcd import Lcd


def main(number):
    lcd = Lcd(number)
    print(lcd.display())


if __name__ == "__main__":
    input_value = int(sys.argv[1])
    main(number=sys.argv[1])
