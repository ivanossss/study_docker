import calendar 
print ('Дорбро пожаловать в календарь, версия 2\n')

year = int (input('Пожалйуста введите год: '))
month = int(input('Введите номер любого месяца'))
print (calendar.month(year, month))

print ('Всего хорошего!')
