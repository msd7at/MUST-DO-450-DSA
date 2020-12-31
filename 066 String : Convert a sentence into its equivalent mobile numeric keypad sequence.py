t=int(input())
a=['2','22','222','3','33','333','4','44','444','5','55','555','6','66','666','7','77','777','7777','8','88','888','9','99','999','9999']
for q in range(t):
    s=input()
    ans=""
    for i in range(len(s)):
        if s[i]==" ":
            ans+="0"
        else:
            position = ord(s[i]) - ord('A') 
            ans = ans + a[position] 
    print(ans)
