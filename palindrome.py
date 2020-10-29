word=input("Tell me a random word ")
list1=[]
a=list(word)
for x in a:
    list1.append(x)
    
list2=[]
b=list(word)
b.reverse()
for y in b:
    list2.append(y)
if list1==list2:
    print("it's a palindrome")
else: print("it's not palindrome")