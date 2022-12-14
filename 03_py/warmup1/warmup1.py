'''
The parameter weekday is True if it is a weekday, and
the parameter vacation is True if we are on vacation.
We sleep in if it is not a weekday or we're on vacation.
Return True if we sleep in.
'''

def sleep_in(weekday, vacation):
  return (not weekday or vacation)

print("=====SLEEP IN=====")
print(sleep_in(False, False))
print("...should be True")
print(sleep_in(True, False))
print("...should be False")

'''
We have two monkeys, a and b, and the parameters a_smile and b_smile indicate if each is smiling.
We are in trouble if they are both smiling or if neither of them is smiling.
Return True if we are in trouble.
'''

def monkey_trouble(a_smile, b_smile):
  return (a_smile and b_smile) or (not a_smile and not b_smile)

print("=====MONKEY TROUBLE=====")
print(monkey_trouble(True, True))
print("...should be True")
print(monkey_trouble(False, False))
print("...should be True")

'''
Given two int values, return their sum.
Unless the two values are the same, then return double their sum.
'''

def sum_double(a, b):
  if (a == b):
    return (4*a)
  return (a + b)

print("=====SUM DOUBLE=====")
print(sum_double(1, 2))
print("...should be 3")
print(sum_double(3, 2))
print("...should be 5")

'''
Given an int n, return the absolute difference between n and 21,
except return double the absolute difference if n is over 21.
'''

def diff21(n):
  if (n > 21):
    return (2*(n-21))
  return (21-n)

print("=====DIFF21=====")
print(diff21(19))
print("...should be 2")
print(diff21(10))
print("...should be 11")

'''
We have a loud talking parrot.
The "hour" parameter is the current hour time in the range 0..23.
We are in trouble if the parrot is talking and the hour is before 7 or after 20.
Return True if we are in trouble.
'''

def parrot_trouble(talking, hour):
  return (talking and (hour < 7 or hour > 20))

print("=====PARROT TROUBLE=====")
print(parrot_trouble(True, 6))
print("...should be True")
print(parrot_trouble(True, 7))
print("...should be False")

'''
Given 2 ints, a and b,
return True if one if them is 10 or if their sum is 10.
'''

def makes10(a, b):
  return ((a == 10) or (b == 10) or (a + b == 10))

print("=====MAKES10=====")
print(makes10(9, 10))
print("...should be True")
print(makes10(9, 9))
print("...should be False")

'''
Given an int n, return True if it is within 10 of 100 or 200.
Note: abs(num) computes the absolute value of a number.
'''

def near_hundred(n):
  return ( (abs(100-n) <= 10) or (abs(200-n) <= 10) )

print("=====NEAR HUNDRED=====")
print(near_hundred(93))
print("...should be True")
print(near_hundred(90))
print("...should be True")

'''
Given 2 int values, return True if one is negative and one is positive.
Except if the parameter "negative" is True, then return True only if both are negative.
'''

def pos_neg(a, b, negative):
  if (not negative):
    return (a*b < 0)
  return (a < 0 and b < 0)

print("=====POS NEG=====")
print(pos_neg(1, -1, False))
print("...should be True")
print(pos_neg(-1, 1, False))
print("...should be True")

'''
Given a string, return a new string where "not " has been added to the front.
However, if the string already begins with "not", return the string unchanged.
'''

def not_string(str):
  if (str[0:3] == "not"):
    return (str)
  return ("not " + str)

print("=====NOT STRING=====")
print(not_string('candy'))
print("...should be not candy")
print(not_string('x'))
print("...should be not x")

'''
Given a non-empty string and an int n,
return a new string where the char at index n has been removed.
The value of n will be a valid index of a char in the original string
(i.e. n will be in the range 0..len(str)-1 inclusive).
'''

def missing_char(str, n):
  return (str[0:n] + str[n+1:len(str)])

print("=====MISSING CHAR=====")
print(missing_char('kitten', 1))
print("...should be not ktten")
print(missing_char('kitten', 0))
print("...should be not itten")

'''
Given a string,
return a new string where the first and last chars have been exchanged.
'''

def front_back(str):
  if (len(str) > 2):
    return (str[len(str)-1] + str[1:len(str)-1] + str[0])
  elif (len(str) == 2):
    return (str[1] + str[0])
  return (str)

print("=====FRONT BACK=====")
print(front_back('code'))
print("...should be not eodc")
print(front_back('a'))
print("...should be not a")

'''
Given a string, we'll say that the front is the first 3 chars of the string.
If the string length is less than 3, the front is whatever is there.
Return a new string which is 3 copies of the front.
'''

def front3(str):
  if (len(str) > 2):
    return (str[0:3] * 3)
  return (str*3)

print("=====FRONT3=====")
print(front3('Java'))
print("...should be not JavJavJav")
print(front3('Chocolate'))
print("...should be not ChoChoCho")
