'''
Author: 周强
Date: 2023-01-27 15:42:09
LastEditTime: 2023-01-27 16:14:39
LastEditors: LAPTOP-LB76IECS
Description: In User Settings Edit
FilePath: /python-project/python-100-days/Day01-15/day09-面向对象进阶.py
'''

class Person(object):
    def __init__(self, name, age):
        self._name = name
        self._age = age
    
    # 访问器
    @property
    def name(self):
        return self._name
    
    @property
    def age(self):
        return self._age
    
    # 修改器
    @age.setter
    def age(self, age):
        self._age = age
        
    def play(self):
        if self._age < 16:
            print(f"{self.name}正在玩飞行棋")
        else:
            print(f"{self.name}正在玩斗地主")

# 继承
class Student(Person):
    
    def __init__(self, name, age, grade):
        super().__init__(name=name, age=age)
        self._grade = grade
        
    @property
    def grade(self):
        return self._grade
    
    @grade.setter
    def grade(self, grade):
        self._grade = grade
        
    def study(self, course):
        print(f'{self.grade}的{self.name}正在学习{course}')
        
class Teacher(Person):
    def __init__(self, name, age, title):
        super().__init__(name=name, age=age)
        self._title = title
        
    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, title):
        self._title = title
        
    def teach(self, course):
        print(f'{self.title}{self.name}正在讲{course}')
        
# 多态之子类对象重写父类对象的方法
from abc import ABCMeta, abstractmethod

# 如果没有metaclass=ABCMeta，则Pet仍然可以实例化
# 但是我们的Pet包含了抽象方法，因此Pet是抽象类
# 加上metaclass = ABCMeta，保证抽象类不能实例化
class Pet(object, metaclass=ABCMeta):
    def __init__(self, nickname):
        self._nickname = nickname
        
    @property
    def nickname(self):
        return self._nickname
        
    @abstractmethod
    def make_voice(self):
        pass
    
class Dog(Pet):
    
    def make_voice(self):
        print(f'{self.nickname}:汪.. 汪.. 汪..')
        
class Cat(Pet):
    
    def make_voice(self):
        print(f'{self.nickname}:喵.. 喵.. 喵..')

def main():
    person = Person(name='周强', age=24)
    person.play()
    person.age = 12
    person.play()
    print(f"{person.name}的年龄是{person.age}")
    # person.name = '周冠强'    # AttributeError: can't set attribute
    
    stu = Student('周强', 24, "硕士二年级")
    stu.study("编程")
    
    tea = Teacher('李永乐' ,34, '教授')
    tea.teach('数学')
    
    pets = [Dog("旺财"), Cat("花卷")]
    for pet in pets:
        pet.make_voice()
        
    pet = Pet('宠物')
    

if __name__ == '__main__':
    main()