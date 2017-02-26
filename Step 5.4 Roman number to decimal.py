from unittest import TestCase


def roman_to_decimal(n):
    roman = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
    arabic = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]

    lst = []
    i = 0
    while i < len(n):
        if i == len(n) - 1:
            lst.append(n[i])
            i += 1
        elif roman.index(n[i]) <= roman.index(n[i+1]):
            lst.append(n[i])
            i += 1
        else:
            lst.append(n[i:i+2])
            i += 2
    res = 0
    for num in lst:
        res += arabic[roman.index(num)]

    return res

# print(roman_to_decimal(input()))


class TestRomanToDecimal(TestCase):
    def test_1(self):
        self.assertEquals(roman_to_decimal('MCMLXXXIV'), 1984)

    def test_2(self):
        self.assertEquals(roman_to_decimal('IX'), 9)

    def test_3(self):
        self.assertEquals(roman_to_decimal('III'), 3)


if __name__ == '__main__':
    unittest.main()
