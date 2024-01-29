binary = input()

decimal = 0
for b in binary:
    decimal = decimal*2 + int(b)

decimal *= 17

binary2 = ''
while decimal >0:
    decimal,k = divmod(decimal, 2)
    binary2 = str(k) + binary2

print(binary2)