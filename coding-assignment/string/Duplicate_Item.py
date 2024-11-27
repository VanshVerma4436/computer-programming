#WAP to find the duplicate item in given string:
str = input("Enter Any Sentence:")
empty_str = ''
for i in str:
    if str.count(i) > 1:
      if i not in empty_str:
        empty_str += i
for i in empty_str:
   print(i)        

