# Атрибуты и методы объекта.

class House:
    # Вунтри класса House определим метод __init__, в который передадим название и кол-во этажей
    def __init__(self, name, number_of_floors):
        self.name = name # Инициализация атрибута name
        self.number_of_floors = number_of_floors # Инициализация атрибута number_of_floors


# Создаем метод go_to с параметром new_floor
    def go_to(self, new_floor):
        if 0 < new_floor <= self.number_of_floors:
            for i in range(1, new_floor+1):
                print(i)
        else:
            print(f'Такого этажа не существует')

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'



# Создаем объект класса House с произвольным названием и количеством этажей
h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)
print(h1)
print(h2)
print(len(h1))
print(len(h2))
# Вызываем метод go_to у этого объекта с произвольным числом этажей
# h1.go_to(5)
# h2.go_to(10)
# print(h1.name, h1.number_of_floors)
# print(h2.name, h2.number_of_floors)



