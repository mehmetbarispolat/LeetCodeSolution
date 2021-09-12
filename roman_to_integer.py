ROMAN_DICT = {
    "I": {
        "numeral": "I",
        "place": ["V", "X"],
        "value": 1
    },
    "V": {
        "numeral": "V",
        "place": [],
        "value": 5
    },
    "X": {
        "numeral": "X",
        "place": ["L", "C"],
        "value": 10
    },
    "L": {
        "numeral": "L",
        "place": [],
        "value": 50
    },
    "C": {
        "numeral": "C",
        "place": ["D", "M"],
        "value": 100
    },
    "D": {
        "numeral": "D",
        "place": [],
        "value": 500
    },
    "M": {
        "numeral": "M",
        "place": [],
        "value": 1000
    }
}
CHECK_LIST = ["I","X", "C"]

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        number = 0
        for i in range(len(s)):
            numeral = s[i]
            numeral_value = ROMAN_DICT[numeral]["value"]

            if numeral in CHECK_LIST:
                try:
                    if s[i+1] in ROMAN_DICT[numeral]["place"]:
                        number -= numeral_value
                    else:
                        number += numeral_value
                except IndexError:
                    number += numeral_value
                    print("End of list")
            else:
                number += numeral_value

        return number

if __name__ == "__main__":
    roman_list = ["III", "IV", "IX", "LVIII", "MCMXCIV"]
    s = Solution()

    for roman in roman_list:
        result = s.romanToInt(roman)

        print(result)