class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors  # Кол-во этажей

    # def go_to(self, new_floor):  # Номер этажа на который нужно приехать
    #     self.new_floor = new_floor
    #     floor = 0
    #     if new_floor < 1 or new_floor > self.number_of_floors:
    #         print('Такого этажа не существет')
    #     else:
    #         for floor in range(new_floor):
    #             print(floor + 1)

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        string = str(f'Название: {self.name}, кол-во этажей: {self.number_of_floors}')
        return string

bigband = House('Бигбэнд', 21)
tower = House('Башня', 99)
# bigband.go_to(21)
# tower.go_to(0)
print(len(bigband))
print(len(tower))
print(bigband)
print(tower)