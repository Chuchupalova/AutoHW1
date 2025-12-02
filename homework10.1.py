class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

class Developer(Employee):
    def __init__(self, name, salary, programing_language):
        super().__init__(name, salary)
        self.programing_language = programing_language

class TeamLead(Manager, Developer):
    def __init__(self, name, salary, department, programing_language, team_size):
        Manager.__init__(self, name, salary, department)
        Developer.__init__(self, name, salary, programing_language)
        self.team_size = team_size

#attribute

def test_team_lead_attributes():
    team_lead = TeamLead("", 2000, "Python", "Python")
    assert hasattr(team_lead, "name")
    assert hasattr(team_lead, "salary")
    assert hasattr(team_lead, "department")
    assert hasattr(team_lead, "team_size")
    assert hasattr(team_lead, "programing_language")

#Task2

from abc import ABC, abstractmethod
class Figure (ABC):
    @abstractmethod
    def figure(self):
        pass
    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Figure):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height
    def perimeter(self):
        return 2 * self.width + self.height

import math
class Circle(Figure):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return math.pi * self.radius * self.radius
    def perimeter(self):
        return 2 * math.pi * self.radius * self.radius

#обьект и цикл вівода

figures = [
    Rectangle(4, 6),
    Circle(5)
]
 for figure in figures:
     print(figure.__class__.__name__)