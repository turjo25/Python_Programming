n = input()
for i in range(int(n)):
    try:
        a,b = map(int,input().split())
        print(a//b)
    except Exception as e:
        print("Error Code:",e)