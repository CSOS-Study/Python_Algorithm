fix_money, product_money, price = map(int, input().split())

if product_money < price:
    i = fix_money // (price - product_money)
    print(i+1)

else:
    print(-1)
