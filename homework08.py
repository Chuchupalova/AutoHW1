import pytest
from homework08 import Student, has_h_letter, sum_numbers_from_string

#Students
def test_student_creation():
    s = Student("Daniil", "Kuzmenko", 20, 80)
    assert s.average_grade == 80

def test_student_update_grade():
    s = Student("Anna", "Kuvalenko", 19, 90)
    s.update_grade(100)
    assert s.average_grade == 100

#has_h_letter
def test_has_h_lowercase():
    assert has_h_letter("Hello") is True

def test_has_h_uppercase():
    assert has_h_letter("HELLO") is True

def test_has_no_h():
    assert has_h_letter("python") is False

def test_has_h_empty():
    assert has_h_letter(" ") is False

#sum_numbers_from_string
def test_sum_correct():
    assert sum_numbers_from_string("1, 2, 3") == 6

def test_sum_large():
    assert sum_numbers_from_string("10, 20, 30") == 60

def test_sum_invalid():
    assert sum_numbers_from_string("a, 2, 3") == 0

def test_sum_single_number():
    assert sum_numbers_from_string("5") == 5

