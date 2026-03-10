n = int(input())

min_discount = float('inf')
product = ""

for i in range(n):
    name,price,discount = input().split(",")
    price = int(price)
    discount = int(discount)

    amount = price*discount/100

    if amount < min_discount:
        min_discount = amount
        product = name

print(product)