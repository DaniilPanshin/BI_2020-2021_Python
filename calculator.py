print('''Калькулятор 
 Поддерживаемые операции:
 Сложение +
 Вычитанеи -
 Деление /
 Умножение *''')
while True:
  a = float(input('Введите первое число: '))
  c = input('Введите операцию')
  b = float(input('Введите второе число: '))
  if c == '-':
    print (a - b)
  elif c == '/' and b == 0:
    print ('На ноль делить нельзя!')
  elif c == '+':
    print (a + b)
  elif  c == '/':
    print (a / b)
  elif c == '*':
    print (a * b)
