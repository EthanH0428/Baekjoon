N, M = map(int, input().split())
num_list = list(map(int, input().split()))

answer = 0
start = 0
end = 0
sum = num_list[0] if N > 0 else 0

while True:

    if sum == M: answer += 1
    if sum <= M:
        end += 1
        if end == N:  
            break
        sum += num_list[end]
    
    else:
        sum -= num_list[start]
        start += 1

print(answer)