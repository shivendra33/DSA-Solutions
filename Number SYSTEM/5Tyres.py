# number of dealerships
n = int(input())

for i in range(1, n+1):
    cars, bikes = map(int, input().split())

    tyres = (cars * 4) + (bikes * 2)

    print(tyres)