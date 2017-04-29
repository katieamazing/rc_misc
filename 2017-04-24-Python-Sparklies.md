---
layout: post
title: "I Coded in Python for a Year Without Knowing These Ten Things"
date: TODO
---

Forgive me for my clickbait title.

**1. in**

Now, I was familiar with in from for loops, so don't despair of me entirely! But using in alone as a test for membership had not occurred to me in my first year of Python programming. If you have a collection (like a list, or a string) and you'd like to see if that collection contains (or does not contain) a value, you can use:

{% highlight python %}
classes = ['English', 'Math', 'Science']
if 'Math' in classes:
  print('Yay, Math!')
if 'History' not in classes:
  print('Doomed to repeat your mistakes.')
{% endhighlight %}

**2. sets**

I had done many practice problems that could have gone better with [sets](https://docs.python.org/3/library/stdtypes.html#set) before I learned about this Python data structure. Sets are data structures that contain unique values. They are also super fast at that checking for membership thing above. I'll come back to that in a moment after we take a look at a simple set example:

TODO fix this a lot (add a list comp, add join), consider moving whole example later in list
{% highlight python %}
string = "hello world"
set_of_chars = set()
for char in string:
  set_of_chars.add(char)
print('There are ' + len(set_of_chars) + ' unique characters in ' + string)
{% endhighlight %}

You can make a set by calling set(), which can take one iterable argument (see below), or by directly listing values in what looks like a list, but with curly braces: my_set = {2, 4, 5, 8}

So, why are sets faster at checking for membership than the strategy we used above with the list of course subjects? Because sets are a dictionary underneath, which also means they are a hash table underneath. And hash tables are fast. But if you're thinking that all that heavyweight stuff under the hood of sets makes them bigger, you'd be right. Sets trade more space in memory for fast membership tests (O(1)). Lists are smaller space-wise, but are more like O(n) to look through each element and test for membership.

Another flavor of set that Python supports as a core data structure is a frozenset(). This is the same kind of thing as a set, but it is immutable. You might find this useful if you are using constants that can be structured in a set, or if you'd like to use a set as a dictionary key.

One other cool thing I've learned is that you can spread iterable objects directly into a set. So:

{% highlight python %}
string = 'buttercup'
buttercup_set = set(string)
{% endhighlight %}

Evaluates to a set like this: buttercup_set = {'b', 'u', 't', 'e', 'r', 'p'}

*Bonus:* Python somewhat obfuscates another set-related data structure, which is more generally referred to as a bag in computer science. You might also find these called multisets. Python has these stuffed down in the collections module under the name [Counter](https://docs.python.org/3/library/collections.html#collections.Counter). If you're looking for this data structure, it exists in the language! No need to implement your own bag data structure unless that sounds fun to you.

**3. enumerate()**

Oftentimes, you want to loop through a list and have the item and its index available in the body of the loop. You can use [enumerate(iterable)](https://docs.python.org/3/library/functions.html#enumerate) to accomplish this:

{% highlight python %}
fruits = ['apple', 'orange', 'banoonoo']
for index, fruit in enumerate(fruits):
  print(index, fruit)
{% endhighlight %}

Under the hood, enumerate returns a tuple for each iteration containing the index integer and the item data, which is then unpacked into the index and item variables for use in the loop body.

One neat thing is that enumerate() will take iterable objects, such as [sequences](https://docs.python.org/3.1/library/stdtypes.html#typesseq) (like string, lists, tuples, and ranges) and [iterators](https://docs.python.org/3/tutorial/classes.html#iterators) (streams of data).

*Bonus:* You might be wondering how enumerate() works on dictionaries, which do not guarantee positional data order the way sequences do. And you're right to raise an eyebrow, enumerate() does not work on dictionaries. In Python 3, you can unpack key and value with:

{% highlight python %}
veggies = {2: carrot, 1: onion, 5: broccoli}
for number, veggie in veggies.items():
  print(number, veggie)
{% endhighlight %}

Note that you still guarantee the order in which the dictionary is looped over, but this syntax will give you both sides of each dict entry.

Enumerate() is an operation that I didn't know how much I wanted until I started Lua. In Lua, key, value unpacking of tables (THE Lua data structure) is just a given! It was only when I came back to Python after a few months off that I was really needing this operation.



join instead of +
for ... else
iter()
defaultdict
zip
list comprehensions
repr v str
