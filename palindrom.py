num = int(input("enter your number : "))
og=num
rev = 0
while (num > 0):
    dig = num%10
    rev = rev*10 + dig
    num=num//10
if og == rev :
    print("number{og} is palindrom")
else:
    print("number{num} is not palindrom")