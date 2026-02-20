from sqlalchemy import create_engine, Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

Base = declarative_base()

#Таблица связка many to many
student_course = Table(
'student_course',
    Base.metadata,
    Column('student_id', Integer, ForeignKey('student.id')),
    Column('course_id', Integer, ForeignKey(courses.id))
)

#Модель студент
class Student(Base):
    __tablename__ = 'student'
    id = Column(Integer, primary_key=True)
    name = Column(String)

    courses = relationship("Course", secondary=student_course, back_populates="student")
    def __repr__(self):
        return f"Student(name={self.name})"

#Модель Course
class Course(Base):
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True)
    title = Column(String)

    students = relationship("Student", secondary=student_course, back_populates="course")

    def __repr__(self):
        return f"Course(title={self.title})"

#Подключение к базе
engine = create_engine('sqlite:///school.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

#Создание данных

match = Course(title="Math")
python = Course(title="Python")

student1 = Student(name="Anna")
student2 = Student(name="Ira")

student1 = courses.append(math)
student1 = courses.append(python)

student2.courses.append(python)

session.add_all([student1, student2])
session.commit(python)

print("=== Student and their courses ===")
for student in session.query(Student).all():
    print(student.name, "->", [course.title for course in student.courses])

#Update
student1.name = "Anna"
session.commit()

print("\nAfter update:")
print(session.query(Student).filter_by(id=student1.id).first())

#Delete
session.delete(student2)
session.commit()

print("\nAfter delete:")
for student in session.query(Student).all():
    print(student.name)

