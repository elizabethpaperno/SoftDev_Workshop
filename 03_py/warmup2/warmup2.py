def string_times(str, n):
  return (str*n)

def front_times(str, n):
  if (len(str) > 2):
    return (str[0:3] * n)
  return (str*n)

def string_bits(str):
  new = ""
  for index in range(len(str)):
    if (index % 2 == 0):
      new += str[index]
  return (new)

def string_splosion(str):
  new = ""
  for index in range(len(str)+1):
    new += str[0:index]
  return (new)

def last2(str):
  last = str[len(str)-2:len(str)]
  count = 0
  for index in range(len(str)-2):
    if (str[index:index+2] == last):
      count+=1
  return count
