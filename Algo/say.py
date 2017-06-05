d_ones = {'0': '', '1': 'one', '2': 'two', '3': 'three', '4': 'four', '5': 'five', '6': 'six', '7': 'seven',
    '8': 'eight', '9': 'nine'}
d_tens = {'0': '', '1': 'teen', '2': 'twenty', '3': 'thirty', '4': 'forty', '5': 'fifty', '6': 'sixty',
    '7': 'seventy', '8': 'eighty', '9': 'ninety'}
d_units = {0: '', 1: 'thousand', 2: 'million', 3: 'billion', 4: 'trillion'}

def say(digit):
    num = str(digit)
    if num == '0':
        return "zero"
    result = []
    unit_count = 0
    while len(num) >= 3:
        to_be_processed = num[-3:]
        num = num[:-3]
        processed_chunk = process_chunk(to_be_processed)
        if d_units[unit_count]:
            result.insert(0, processed_chunk + ' ' + d_units[unit_count])
        else:
            result.insert(0, processed_chunk)
        unit_count += 1
    if len(num) == 2:
        processed_chunk = (process_chunk('0' + num))
        if d_units[unit_count]:
            result.insert(0, processed_chunk + ' ' + d_units[unit_count])
        else:
            result.insert(0, processed_chunk)
    elif len(num) == 1:
        processed_chunk = (process_chunk('00' + num))
        if d_units[unit_count]:
            result.insert(0, processed_chunk + ' ' + d_units[unit_count])
        else:
            result.insert(0, processed_chunk)
    return ' '.join(result)


# takes three digits as input, returns a prounced string
def process_chunk(chunk):
    preceding = d_ones[chunk[0]]
    n = int(chunk[1:])
    if n == 0:
        following = ''
    elif n == 10:
        following = 'ten'
    elif n == 11:
        following = 'eleven'
    elif n == 12:
        following = 'twelve'
    elif n > 12 and n < 20:
        following = d_ones[chunk[2]] + d_tens[chunk[1]]
    else:
        if d_tens[chunk[1]] and d_ones[chunk[2]]:
            following = d_tens[chunk[1]] + '-' + d_ones[chunk[2]]
        elif d_tens[chunk[1]]:
            following = d_tens[chunk[1]]
        else:
            following = d_ones[chunk[2]]
    if preceding and following:
        return preceding + ' hundred and ' + following
    elif preceding:
        return preceding + ' hundred'
    elif following:
        return following
    else:
        return 'zero'

print(say(987654321123))
print(say(987654000123))
assert(say(0) == 'zero')
assert(say(14) == 'fourteen')
assert(say(50) == 'fifty')
assert(say(98) == 'ninety-eight')
assert(say(1) == 'one')
assert(say(100) == 'one hundred')
assert(say(1296) == 'one thousand two hundred and ninety-six')
assert(say(987654321123) == "nine hundred and eighty-seven billion "
                                "six hundred and fifty-four million "
                                "three hundred and twenty-one thousand "
                                "one hundred and twenty-three")
