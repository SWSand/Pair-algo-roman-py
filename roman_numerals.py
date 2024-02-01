def to_roman(num):
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

print(to_roman(6))