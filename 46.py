#start 6:08pm

def max(a, b):
  if a > b:
    return a
  elif b > a:
    return b
  else:
    return "Those arguments are equal."
    
assert(max(4, 5) == 5)
assert(max(6.2, 32) == 32)
assert(max(20, 20) == "Those arguments are equal.")


def max_of_three(a, b, c):
  args = [a, b, c]
  biggest = 0
  for i in range(3):
    if args[i] > biggest:
      biggest = args[i]
    else:
      pass
  return biggest
    
assert(max_of_three(4, 6, 8) == 8)
assert(max_of_three(3.1, 698.5, 20.0) == 698.5)


def length(str):
  count = 0
  for c in str:
    count += 1
  return count

assert(length("hi") == 2)
assert(length("froggie") == 7)


def vowel(c):
  vowels = ['a', 'e', 'i', 'o', 'u']
  for v in vowels:
    if c == v:
      return True
  return False

assert(vowel('i') == True)
assert(vowel('g') == False)
assert(vowel(' ') == False)


def translate(input):
  output = ''
  for c in input:
    output = output + c
    if c == ' ':
      pass
    elif vowel(c) == False:
      output = output + 'o' + c
  return output
  
assert(translate('this is fun') == 'tothohisos isos fofunon')

#end 6:28


#start 3:42
def sum(values):
  output = 0
  for v in values:
    output += v
  return output

def multiply(values):
  start = values[0]
  mult = values[1:]
  for v in mult:
    start *= v
  return start   
  
assert(sum([1, 2, 3, 4]) == 10)
assert(multiply([1, 2, 3, 4]) == 24)


def reverse(string):
  output = ""
  for c in string:
    output = c + output
  return output
  
assert(reverse("hi") == "ih")
assert(reverse("I am testing") == "gnitset ma I")


def is_palindrome(string):
  if string == reverse(string):
    return True
  else:
    return False
    
assert(is_palindrome("radar") == True)

def is_member(input, list):
  for v in list:
    if v == input:
      return True
  return False
  
assert(is_member(1, [1, 2, 3]) == True)
assert(is_member("o", "gargantuan") == False)


def overlapping(a, b):
  for i in a:
    for v in b:
      if i == v:
        return True
  return False

assert(overlapping([1, 2, 3], [6, 2, 8]) == True)
assert(overlapping(["peach", "pear"], ["orange", "apple"]) == False)
  
#end 4:02 WHEW
  
#start 4:28

def generate_n_chars(n, c):
  output = ""
  i = 0
  while i < n:
    output += c
    i += 1
  return output

assert(generate_n_chars(5, "m") == "mmmmm")
assert(generate_n_chars(1, "h") == "h")


def histogram(ints): ##procedure??
  for i in ints:
    print "*" * i

#histogram([4, 9, 7]) 


def max_in_list(nums):
  best = 0
  for i in nums:
    if i > best:
      best = i
  return best

assert(max_in_list([5, 6, 12, 0, 2, 3, 28]) == 28)
assert(max_in_list([0]) == 0)


def word_lengths(words):
  nums = []
  i = 0
  for word in words:
    nums.insert(i, len(word))
    i += 1
  return nums
  
assert(word_lengths(["hi", "you"]) == [2, 3])
assert(word_lengths(["hi", "you", "silly"]) == [2, 3, 5])
  
#end 4:44 (only did 4 problems)


#start 4:44

def find_longest_word(words):
  best_so_far = 0
  best_word = ""
  for word in words:
    if len(word) > best_so_far:
      best_so_far = len(word)
      best_word = word
  return best_word
  
assert(find_longest_word(["hi", "you", "no"]) == "you")

def filter_long_words(words, n):
  output = []
  for word in words:
    if len(word) > n:
      output.append(word)
  return output
  
assert(filter_long_words(["hi", "you", "no"], 2) == ["you"])
  
def phrase_pal(phrase):
  phrase = phrase.replace(" ", "")
  phrase = phrase.replace("!", "")
  phrase = phrase.replace(",", "")
  phrase = phrase.replace(".", "")
  
  flipped = phrase[::-1]
  if (phrase.lower()) == (flipped.lower()):
    return True
  else:
    return False
    
assert(phrase_pal("Satan, oscillate my metallic sonatas") == True)
 
def pangram(sentence):
  letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
  dict = {}
  sentence = (sentence.replace(" ", "").lower())
  for i in letters:
    dict[i] = False
    
  for c in sentence:
    if dict[c] == False:
      dict[c] = True
    else:
      pass
        
  for key in dict:
    if dict[key] == False:
      return False
  return True
  
assert(pangram("The quick brown fox jumps over the lazy dog") == True)
assert(pangram("Not a pangram") == False)
  
 #end 5:08pm, ended with #18 (only did 4!)
 
 #start 1:34pm
 
def bottles(verse):
  insertion = ""
  for i in range(verse, 0, -1):
    if i == 1:
      insertion = "1 bottle"
      less = "no bottles"
    else:
      insertion = str(i) + " bottles"
      less = str(i-1) + " bottles"
    print insertion + " of beer on the wall, " + insertion + " of beer."
    print "Take one down, pass it around, " + less + "of beer on the wall."
    


def translate(words):
  swe_eng = {"merry":"god", "christmas":"jul", "and":"och", "happy":"gott", "new":"nytt", "year":"ar"} 
  output = []
  for word in words:
    output.append(swe_eng[word])
    
  return output
  
assert(translate(["merry", "christmas", "year"]) == ["god", "jul", "ar"])

def char_freq(s):
  freq = {}
  for c in s:
    try:
      freq[c] += 1
    except:
      freq[c] = 1
  return freq
    
assert(char_freq("hello") == {'h':1, 'e':1, 'l':2, 'o':1})
  
#ended 1:52, completed 3 problems. Ended with #21
  
  
