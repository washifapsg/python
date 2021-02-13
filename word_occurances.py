def search(string1):
    splitstring=string1.split()
    list1=[]
    s_word=str(input("enter the word to search"))
    for word in splitstring:
        if word==s_word:
            list1.append(word)
            lengthstring=len(list1)
    return lengthstring
string1=str(input("enter the string"))
a=search(string1)
print("the number of time the word occurs in the string is",a)
