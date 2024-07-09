N, X = map(int, input().split())
A = list(map(int, input().split()))
Flag = False

for i in range(N):
    if A[i] == X:
        Flag = True
        print('Yes')
        break


if Flag == False:
    print('No')