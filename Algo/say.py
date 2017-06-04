d_ones = {'0': '', '1': 'one', '2': 'two', '3': 'three', '4': 'four', '5': 'five', '6': 'six', '7': 'seven',
    '8': 'eight', '9': 'nine'}
d_tens = {'0': '', '1': 'teen', '2': 'twenty', '3': 'thirty', '4': 'forty', '5': 'fifty', '6': 'sixty',
    '7': 'seventy', '8': 'eighty', '9': 'ninety'}
d_units = {1: 'hundred', 2: 'thousand', 3: 'hundred thousand', 4: 'million'}

def say(digit):
    num = str(digit)
    result = []
    unit_count = 0
    while len(num) >= 3:
        to_be_processed = num[-3:]
        num = num[:-3]
        unit_count += 1
        preceding, following = process_chunk(to_be_processed)
        result.append(preceding)
        result.append(' ')
        if preceding:
            result.append(d_units[unit_count])
        result.append('and')
        result.append(following)
    print(num)
    if len(num) == 2:
        preceding, following = (process_chunk('0' + num))
    else:
        preceding, following = (process_chunk('00' + num))
    print(following)
    result.insert(0, following[1:])
    result.insert(1, d_units[unit_count+1])
    return ''.join(result)


# takes three digits as input, returns a preceding unit str and a following str
def process_chunk(chunk):
    preceding = d_ones[chunk[0]]
    n = int(chunk[2::])
    if n == 00:
        following = ''
    elif n == 10:
        following = 'ten'
    elif n == 12:
        following = 'twelve'
    elif n > 12 and n < 20:
        following = d_ones[chunk[2]] + d_tens[chunk[1]]
    else:
        following = d_tens[chunk[1]] + '-' + d_ones[chunk[2]]
    return preceding, following


print(say(1296))
print(say(1001))
