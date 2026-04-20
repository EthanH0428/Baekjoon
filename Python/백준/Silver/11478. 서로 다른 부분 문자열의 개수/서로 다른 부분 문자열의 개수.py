s = input().strip()
result = set()

for i in range(len(s)): # 부분 문자열의 시작 index
    for j in range(i,len(s)): # 부분 문자열의 stop index
        sub_str = s[i:j+1]
        result.add(sub_str)

print(len(result))