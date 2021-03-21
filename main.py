###solution to exercise 78 from ben stephenson's 'the python workbook'.

num = int(input('Enter an integer:'))

result = ''
while num > 0:
  r = num % 2
  result = str(r) + result
  num = num // 2

print(f'The binary equivalent is: {result}.')
