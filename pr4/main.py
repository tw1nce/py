class User:
    """Класс содержащий name, login, password, grade"""
    count = 0

    def __init__(self, name, login, password, grade=0):
        if isinstance(grade, int):
            """проверим, что grade int, иначе выдадим ошибку.
               Остальные строки. Всё преобразуем в строку."""
            self._name = str(name)
            self._login = str(login)
            self._password = str(password)
            self._grade = grade
            User.count += 1
        else:
            raise ValueError('grade должно быть int!')

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = str(new_name)

    @property
    def login(self):
        return self._login

    @login.setter
    def login(self, new_login):
        print("Невозможно изменить логин!")

    @property
    def password(self):
        return "********"

    @password.setter
    def password(self, new_password):
        self._password = str(new_password)

    @property
    def grade(self):
        return "Неизвестное свойство grade!"

    @grade.setter
    def grade(self, new_grade):
        print("Неизвестное свойство grade!")

    def show_info(self):
        print (f"Name: {self._name}, Login: {self._login}")

    @classmethod
    def verified(cls, other):
        """"метод для проверки, является ли сравниваемый операнд объектом класса User"""
        if not isinstance(other, User):
            raise TypeError("Сравниваемый правый операнд должен принадлежать классу User")
        return other

    def __eq__(self, other):
        """функция для сравнения ==.
        Для != нет необходимости, т.к. произойдет обратное сравнение"""
        other = self.verified(other)
        return self._grade == other._grade

    def __lt__(self, other):
        """функция для сравнения на <.
        Нет необходимости писать на >, т.к. произойдет
        подмена операндов"""
        other = self.verified(other)
        return self._grade < other._grade

    def __le__(self, other):
        """функция для сравнения на <=.
                Нет необходимости писать на >=, т.к. произойдет
                подмена операндов"""
        other = self.verified(other)
        return self._grade <= other._grade


class SuperUser(User):
    """класс наследник от User с атрибутом role"""

    count = 0#Переопредлеим count для нового счётчика

    def __init__(self, name, login, password, role, grade):
        super().__init__(name, login, password, grade)
        self._role = str(role)
        SuperUser.count += 1

    @property
    def role(self):
        return self._role

    @role.setter
    def role(self, new_role):
        self._role = str(new_role)




user1 = User('Paul McCartney', 'paul', '1234', 3)
user2 = User('George Harrison', 'george', '5678', 2)
user3 = User('Richard Starkey', 'ringo', '8523', 3)
admin = SuperUser('John Lennon', 'john', '0000', 'admin', 5)

user1.show_info()
admin.show_info()
print()
users = User.count
admins = SuperUser.count

print(f'Всего обычных пользователей: {users}')
print(f'Всего супер-пользователей: {admins}\n')

print(user1 < user2)
print(admin > user3)
print(user1 == user3,"\n")

user3.name = 'Ringo Star'
user1.password = 'Pa$$w0rd'

print(user3.name)
print(user2.password)
print(user2.login)

user2.login = 'geo'

print(user1.grade)
admin.grade = 10
