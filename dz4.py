n=input()
n=int(n)
if n%2==1:
    print("N нечетное")
elif (n<11) and (n>4):
    print("N четное и принадлежит интервалу [5, 10]")
elif (n>10):
    print("N четное и N > 10")
elif (n<5):
    print("N четное и N < 5")