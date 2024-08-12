class House:
    houses_history = []

    def __new__(cls, *args, **kwargs):
        cls.houses_history.append(args[0])
        print(*cls.houses_history)
        return super().__new__(cls)

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors  # Кол-во этажей

    def go_to(self, new_floor):  # Номер этажа на который нужно приехать
        self.new_floor = new_floor
        floor = 0
        if new_floor < 1 or new_floor > self.number_of_floors:
            print('Такого этажа не существет')
        else:
            for floor in range(new_floor):
                print(floor + 1)

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'

    def __eq__(self, other):
        return self.number_of_floors == other.number_of_floors

    def __lt__(self, other):
        return self.number_of_floors < other.number_of_floors

    def __le__(self, other):
        return self.number_of_floors <= other.number_of_floors

    def __gt__(self, other):
        return self.number_of_floors > other.number_of_floors

    def __ge__(self, other):
        return self.number_of_floors >= other.number_of_floors

    def __ne__(self, other):
        return self.number_of_floors != other.number_of_floors

    def __add__(self, value):
        self.number_of_floors = self.number_of_floors + value
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'

    def __radd__(self, value):
        if isinstance(value, int):
            self.number_of_floors = value + self.number_of_floors
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'

    def __iadd__(self, value):
        if isinstance(value, int):
            self.number_of_floors += value
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'

    def __del__(self):
        print(self.name, "снесён, но останется в истории")

bigband = House('Бигбэнд', 20)
tower = House('Башня', 10)

# bigband.go_to(21)
# tower.go_to(0)
# print(len(bigband))
# print(len(tower))
# print(bigband)
# print(tower)
# print(bigband+5)
# print(tower+10)
# print(5+bigband)
# print(10+tower)
# bigband+=5
# print(bigband)
# tower+=10
# print(tower)
# print(bigband == tower)
# print(bigband<tower)
# print(bigband<=tower)
# print(bigband>tower)
# print(bigband>=tower)
# print(bigband!=tower)
castel = House("Шато де Шамбор", 12)
# print(castel)
del castel
del tower
del bigband
print(House.houses_history)
