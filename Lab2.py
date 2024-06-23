n = 3
length = n*4 -3
data = []
result = []
for i in range (97,123):
    data.append(chr(i))
for i in range(n):
    str1 = data[n-1:i:-1]
    str2 = data[i:n]
    str3 = "-".join(str1+str2)
    str4 = "-" * ((length - len(str3))//2)
    result.append(str4 + str3 + str4)
for i in result[::-1]:
    print(i)
for i in result[1:]:
    print(i)
