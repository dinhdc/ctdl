def romanToInt(s):
    map_to = {
        1: "I",
        4: "IV",
        5: "V",
        9: "IX",
        10: "X",
        40: "XL",
        50: "L",
        90: "XC",
        100: "C",
        400: "CD",
        500: "D",
        900: "CM",
        1000: "M"
    }
    reverser_map = {}
    checked = []
    for _ in range(len(s)):
        checked.append(False)
    for key, value in map_to.items():
        reverser_map[value] = key
    index = 0
    res = 0
    for index in range(len(s)-1):
        roman = s[index]
        roman_2 = s[index] + s[index+1]
        if roman_2 in reverser_map and checked[index+1] is False and checked[index] is False:
            res += reverser_map[roman_2]
            checked[index] = True
            checked[index+1] = True
        elif checked[index] is False:
            checked[index] = True
            res += reverser_map[roman]
    if checked[-1] == False:
        res += reverser_map[s[-1]]
    return res


print(romanToInt("MCMXCIV"))
