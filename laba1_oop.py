class Worker:
    def __init__(self, name, surname, age):
        self.__name = name
        self.__surname = surname
        self.__age = age

    @property
    def name(self):
        return self.__name

    @property
    def surname(self):
        return self.__surname

    @property
    def age(self):
        return self.__age

    def __str__(self):
        return f"{self.name} {self.surname}, Возраст: {self.age}"

class Director:
    def __init__(self, name, surname, age):
        self.__name = name
        self.__surname = surname
        self.__age = age

    @property
    def name(self):
        return self.__name

    @property
    def surname(self):
        return self.__surname

    @property
    def age(self):
        return self.__age

    def __str__(self):
        return f"{self.name} {self.surname}, Возраст: {self.age}"

class Firm:
    def __init__(self, name_of_firm):
        self.__name_of_firm = name_of_firm
        self.__director = None
        self.__workers = []

    @property
    def name_of_firm(self):
        return self.__name_of_firm

    @property
    def director(self):
        return self.__director

    @property
    def workers(self):
        return self.__workers

    def make_director(self, director):
        self.__director = director

    def make_worker(self, worker):
        self.__workers.append(worker)

    def __str__(self):
        director_str = f"Директор: {self.director}" if self.director else "Директор не назначен"
        workers_str = "\n".join(str(worker) for worker in self.workers)
        return f"Фирма: {self.name_of_firm}\n{director_str}\nСотрудники:\n{workers_str}"

def create_firm():
    name_of_firm = input("Введите название фирмы: ")
    return Firm(name_of_firm)

def create_director():
    while True:
        name = input("Введите имя директора: ")
        if name.isalpha():
            break
        else:
            print("Ошибка. Имя должно состоять из букв. Введите корректное имя. ")
    surname = input("Введите фамилию директора: ")

    while True:
        age = input("Введите возраст директора: ")
        try:
            age = int(age)
            break  # Если возраст успешно преобразован в целое число, завершаем цикл
        except ValueError:
            print("Ошибка: Возраст должен быть числом. Попробуйте снова.")

    return Director(name, surname, age)

def create_worker():
    while True:
        name = input("Введите имя сотрудника: ")
        if name.isalpha():
            break
        else:
            print("Ошибка. Имя должно состоять из букв. Введите корректное имя. ")
    surname = input("Введите фамилию сотрудника: ")

    while True:
        age = input("Введите возраст сотрудника: ")
        try:
            age = int(age)
            break  # Если возраст успешно преобразован в целое число, завершаем цикл
        except ValueError:
            print("Ошибка: Возраст должен быть числом. Попробуйте снова.")

    return Worker(name, surname, age)

def menu():
    firm = None
    director = None

    while True:
        print("Главное меню:")
        print("1. Создать фирму.")
        print("2. Создать директора(количество - 1).")
        print("3. Создать сотрудника.(количество - не ограничено)")
        print("4. Вывести информацию о сотруднике.")
        print("5. Вывести информацию о директоре.")
        print("6. Вывести информацию о фирме.")
        print("7. Выход из программы ")

        choose = input("Выберите пункт меню: ")

        if choose == "1":
            pass
        elif choose == "2":
            pass
        elif choose == "3":
            pass
        elif choose == "4":
            pass
        elif choose == "5":
            pass
        elif choose == "6":
            pass
        elif choose == "7":
            pass

if __name__ == "__main__":
    menu()
