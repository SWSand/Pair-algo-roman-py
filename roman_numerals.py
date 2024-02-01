def to_roman_lazy(num):
    roman_numerals = {
    'M' : 1000,
    'D' : 500,
    'C' : 100,
    'L' : 50,
    'X' : 10,
    'V' : 5,
    'I' : 1,
    }
    # for loop through dictionary values and compare to num
    ans = ""

    for x in roman_numerals :
        if num >= roman_numerals[x] :
            ans += x * (num//roman_numerals[x])
            num = (num % roman_numerals[x])
    return ans

def to_roman(num):
    roman_numerals = {
    'M' : 1000,
    'CM': 900,
    'D' : 500,
    'CD' : 400,
    'C' : 100,
    'XC' : 90,
    'L' : 50,
    'XL' : 40,
    'X' : 10,
    'IX' : 9,
    'V' : 5,
    'IV': 4,
    'I' : 1,
    }
    # for loop through dictionary values and compare to num
    ans = ""

    for x in roman_numerals :
        if num >= roman_numerals[x] :
            ans += x * (num//roman_numerals[x])
            num = (num % roman_numerals[x])
    return ans

# print(to_roman_lazy(909))
# print(to_roman(909))


