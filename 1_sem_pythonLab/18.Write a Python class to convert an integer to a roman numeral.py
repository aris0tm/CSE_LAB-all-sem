class IntegerToRoman:
    def __init__(self):
        self.int_to_roman_map = {
            1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X',
            40: 'XL', 50: 'L', 90: 'XC', 100: 'C',
            400: 'CD', 500: 'D', 900: 'CM', 1000: 'M'
        }

    def int_to_roman(self, num):
        if num <= 0:
            return "Invalid number"

        result = ''
        for value, numeral in sorted(self.int_to_roman_map.items(), reverse=True):
            while num >= value:
                result += numeral
                num -= value
        return result


# Test the class
converter = IntegerToRoman()
number = int(input("Enter an integer: "))
print("Roman numeral:", converter.int_to_roman(number))
