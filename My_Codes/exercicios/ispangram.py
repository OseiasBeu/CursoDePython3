#encoding: utf-8

import string

def isPangram(str1, alphabet=string.ascii_lowercase):
  num = len(alphabet)
  count = 0

  for i in alphabet:
    if i in str1:
      count+=1
  return count == num


print(isPangram("The quick brown fox jumps over the lazy dog"))