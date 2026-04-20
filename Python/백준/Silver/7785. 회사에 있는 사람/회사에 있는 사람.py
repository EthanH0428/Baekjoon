import sys
input = sys.stdin.readline
n = int(input())
in_person = set()

for _ in range(n):
    name, action = input().split()
    if action == 'enter':
        in_person.add(name)
    else:
        in_person.remove(name)

result = sorted(in_person, reverse=True)
for person in result:
    print(person)