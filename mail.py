def add_item(shopping_list):
    name = input("Введіть надву товару")
    quantity = int(input("Введіть кількість"))
    price = float(input("Введіть ціну"))

    item = {
        "name": name,
        "quantity": quantity,
        "price": price
    }
    shopping_list.append(item)

    print(f"✅ {name} додано до списку!")
def  show_list():
    pass

def count_total():
    pass

def save_to_file():
    pass

def load_from_fike():
    pass 

def main():
    print("🛒 Вітаю у менеджері покупок! Меню:")
    shopping_list = []

    while True:
        print('''
    Meню:
    1. Додати покупку
    2. Переглянути список
    3. Порахувати загальну суму
    4. Зберегти у файл
    5. Завантажити з файлу
    6. Вихід
            ''')
        choice = int(input("Ваш вибір: "))
        match choice:
            case 1:
                add_item(shopping_list)
            case 2:
                show_list()
            case 3:
                count_total()
            case 4:
                save_to_file()
            case 5:
                load_from_fike()
            case 6:
                print("See you!!")
                break
            case _:
                print("Error! Enter number 1-6!")

main()