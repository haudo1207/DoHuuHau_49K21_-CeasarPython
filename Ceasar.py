import string
Plaintext = "do huu hau"
key= 8
a=list(string.ascii_lowercase)  # Tạo danh sách chữ cái từ a đến z
b=a[key:]+a[:key]
print("Ten sau khi duoc ma hoa: ",end='')
for i in Plaintext:
    if i in a:
        print(b[a.index(i)],end='')
    else:
        print(i,end="")

