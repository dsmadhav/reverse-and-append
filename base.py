def a(i):
    i=i[::-1]
    return i
#no. of words in the meme
n=int(input())
string[n]
#take str input and append it to pre-existant str
for i in range(n):
    string[i]=input()
    if(i>0):
        string[i]=string[i]+string[i-1]
#print
print(string)
