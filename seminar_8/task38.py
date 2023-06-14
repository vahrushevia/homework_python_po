# Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных. Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал для изменения и удаления данных
import csv

phone_book = {}  # Создаем пустой телефонный справочник

def load_phone_book():
    with open('seminar_8/phone_book.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            name = row[0]
            phone_number = row[1]
            phone_book[name] = phone_number

def save_phone_book():
    with open('seminar_8/phone_book.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        for name, phone_number in phone_book.items():
            writer.writerow([name, phone_number])

def add_contact():
    name = input("Введите имя контакта: ")
    phone_number = input("Введите номер телефона: ")
    phone_book[name] = phone_number
    save_phone_book()
    print("Контакт успешно добавлен!")

def update_contact():
    name = input("Введите имя контакта, который хотите изменить: ")
    if name in phone_book:
        new_phone_number = input("Введите новый номер телефона: ")
        phone_book[name] = new_phone_number
        save_phone_book()
        print("Контакт успешно обновлен!")
    else:
        print("Контакт не найден!")

def delete_contact():
    name = input("Введите имя контакта, который хотите удалить: ")
    if name in phone_book:
        del phone_book[name]
        save_phone_book()
        print("Контакт успешно удален!")
    else:
        print("Контакт не найден!")

load_phone_book()

while True:
    print("\nТелефонный справочник")
    print("1. Добавить контакт")
    print("2. Изменить контакт")
    print("3. Удалить контакт")
    print("4. Выйти")
    choice = input("Выберите действие: ")

    if choice == '1':
        add_contact()
    elif choice == '2':
        update_contact()
    elif choice == '3':
        delete_contact()
    elif choice == '4':
        break
    else:
        print("Неверный выбор. Попробуйте снова.")