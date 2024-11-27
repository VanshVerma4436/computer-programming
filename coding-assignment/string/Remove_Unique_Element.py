#WAP To Remove Unique Element From Given String:
st = input("Write Any Fruit:")
c = ''
for i in st:
    if st.count(i) > 1:
     if i not in c:
        c += i
for i in c:
   print(i,end='')        
