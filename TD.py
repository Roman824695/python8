#Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt. Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.

# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в текстовом файле
# 3. Пользователь может ввести одну из характеристик для поиска определенной записи(Например имя или фамилию человека)
# 4. Использование функций. Ваша программа не должна быть линейной
   
# 17th: 
# 1. Открыть файл
# 2. Сохранить файл
# 3. Показать контакты
# 4. Добавить контакт
# 5. Изменить контакт
# 6. Найти контакт
# 7. Удалить контакт
# 8 Выход
phone_book = []
print('Это телефонный справочник. Выполните нужное действие :')

# Меню работы со справочником. 
def print_menu():
    print('_____________________ \n'
        '1. Открыть файл. \n'
        '2. Сохранить файл. \n'
        '3. Показать контакты. \n'
        '4. Добавить контакт. \n'
        '5. Изменить контакт. \n'
        '6. Найти контакт. \n'
        '7. Удалить контакт. \n'
        '8 Выход. \n'    
        '______________________ \n'
     )
    data = int(input('>> Введите номер необходимого действия <<\n'))
    return data

#Открыть файл
def open_phone_book():
   with open('phone_book.txt', 'r', encoding = 'utf-8') as data:
     phone_book = data.readlines()
     print('\n >> Файл готов к работе << \n')
     return phone_book     
       
# Сохранить файл
def save_phone_book():
    with open('phone_book.txt', 'w', encoding = 'utf-8') as data:
       for i in phone_book:
           data.write(str(i))

# Показать контакты
def show_phone_book(file):
   
    if len(file) == 0:
      print('>> Вы не открыли файл, либо файл пуст <<') 
    else:
       for i in file:
         print('\n' + ' ' .join(i.split(';')))       
   
# Добавить контакт
def add_phone_book():
    user_info = input('>> Введите данные нового контакта <<\n')
    print(f'>> Контакт {user_info} добавлен <<')
    user_info = ';'.join(user_info.split(' '))
    phone_book.append( user_info + '\n')
    
    
# Изменить контакт
def change_phone_book():
    user_info = input('>> Введите номер контакта который хотите изменить <<\n')
    for i in range(len(phone_book)):
        if user_info in phone_book[i]:
          print(phone_book[i])
          
          new_user_info = input('>> Введите новый номер телефона <<\n')
          print(f'>> Номер {new_user_info} присвоен <<')
          phone_book[i] = phone_book[i].replace(user_info, new_user_info)

# Найти контакт
def search_phone_book():
    user_info = input('>> Введите информацию контакта который хотите найти <<\n')
    for i in range(len(phone_book)):
        if user_info in phone_book[i]:
          print(' ' .join(phone_book[i].split(';')))


# Удалить контакт
def delete_phone_book():
    user_info = input('>> Введите информацию контакта который хотите удалить <<\n')
    for i in range(len(phone_book)):
        if user_info in phone_book[i]:
          log = ' '.join(phone_book[i].split(';'))
          print(f'>> Вы точно хотите удалить контакт {log}<<\n')
          delete = input('>> ДА - 1, НЕТ - 0 <<\n')
          if delete == 1:
           phone_book.pop(i)
           break
          else:
             print_menu()
             

while True:
    user_choice = print_menu()
    match user_choice:
     case 1: 
      phone_book = open_phone_book()
     case 2: 
      save_phone_book()  
     case 3: 
      show_phone_book(phone_book) 
     case 4: 
      add_phone_book() 
     case 5: 
        change_phone_book()
     case 6: 
        search_phone_book()   
     case 7: 
        delete_phone_book()
     case 8: 
        print('Выход.') 
        break








