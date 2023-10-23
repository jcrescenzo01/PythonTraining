import copy
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Company:
    def __init__(self, boss, employee):
        self.boss = boss
        self.employee = employee


"""
p1 = Person('Alex', 27)
p2 = p1

p2.age = 28     # both get changed because its not a real copy
print(p2.age)
print(p1.age)
"""
"""
p1 = Person('Alex', 27)
p2 = copy.copy(p1)  # copies p1 into p2 correctly
p2.age = 28
print(p2.age)
print(p1.age)
"""

p1 = Person('Alex', 55)
p2 = Person('Joe', 27)
company = Company(p1, p2)
#company_clone = copy.copy(company)  # only shallow so wont work right
company_clone = copy.deepcopy(company)  # works
company_clone.boss.age = 56
print(company_clone.boss.age)
print(company.boss.age)