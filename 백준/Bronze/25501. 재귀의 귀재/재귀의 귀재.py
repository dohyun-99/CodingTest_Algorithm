T=int(input())
S=[]
for i in range(T):
    S.append(str(input()))

def recursion(s, l, r, count):
    if l >= r: 
        return 1, count
    elif s[l] != s[r]: 
        return 0, count
    else:
        count+=1 
        return recursion(s, l+1, r-1, count)

def isPalindrome(s):
    return recursion(s, 0, len(s)-1, 1)

for j in S:
    print(isPalindrome(j)[0], isPalindrome(j)[1])