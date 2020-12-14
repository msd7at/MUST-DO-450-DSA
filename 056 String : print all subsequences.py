#https://www.youtube.com/watch?v=KCEPvdLqlYI
s=input()
o=""
def alls(s,o):
    if s=="":
        print(o)
        return 
    alls(s[1:],o)
    alls(s[1:],o+s[0])
alls(s,o)
