from fileinput import filename
import os

products = []

# 讀取檔案
def read_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            if '商品,價格' in line:
                continue
            name, price = line.strip().split(',')
            products.append([name, price])
    return products

# 讓使用者輸入
def user_input(products):
    while True:
        name = input('請輸入商品名稱: ')
        if name =='q':
            break
        price = input('請輸入商品價格: ')
        # p = []
        # p.append(name)
        # p.append(price)
        # p = [name, price]
        products.append([name, price])
    print(products)
    return products
# 印出所有商品
def print_products(products):
    for product in products:
        print(product[0], '的價格是$', product[1])

# 寫入檔案
def white_file(filename, products):
    with open(filename, 'w', encoding='utf-8') as f:
        f.write('商品,價格\n')
        for p in products:
            f.write(p[0] + ',' + p[1] + '\n')

def main():
    filename = 'products.csv'
    if os.path.isfile(filename):
        print('Yes')
        products = read_file(filename)
    else:
        print('No')
    products = user_input(products)
    print_products(products)
    white_file(filename, products)

main()