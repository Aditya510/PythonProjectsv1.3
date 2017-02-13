def sum_pairs(ints, s):
  for item in ints:
    for anotheritem in ints:
      if item+anotheritem == s:
        return[item,anotheritem]
print(sum_pairs([1,2,3,4],7))
