#calcuator
def calcu(a, b):
    x = len(b)
    y = len(a)
    j =0
    print("THE ENCODE KEY \n")
    for i in range(x):
        if(j==y):
            j=0
        else:
            asckey =ord(a[j])
            asctext =ord(b[i])
            newasci = asckey*asctext
            print(chr(newasci%127),end='')
            j =j+1
            newasci =0
    
print('''**********Encryptor********** 
**********hope you like it**********
**********★彡( ฿Ɏ Ⱨ₳₵₭ɆⱤ8360 )彡★*********''')



#main block of the function
text = input("enter the text which you want to excute \n")
key = input("enter the key \n")
calcu(key, text)
