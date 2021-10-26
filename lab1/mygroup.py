groupmates = [
    {"name": "Николай",
     "surname": "Леонов",
     "exams": ["Информатика","История","Мат. Анализ"],
     "marks": [4,4,4]
        },
        {"name": "Игнат",
     "surname": "Соцков",
     "exams": ["Информатика","История","Мат. Анализ"],
     "marks": [5,5,4]
        },
        {"name": "Иван",
     "surname": "Иванов",
     "exams": ["Информатика","История","Мат. Анализ"],
     "marks": [3,4,3]
        },
        {"name": "Михаил",
     "surname": "Михайлов",
     "exams": ["Информатика","История","Мат. Анализ"],
     "marks": [4,5,5]
        },
        {"name": "Ефим",
     "surname": "Мушаков",
     "exams": ["Информатика","История","Мат. Анализ"],
     "marks": [4,3,4]
        }
]
def print_students(students):
    averageMark = int(input("Введите среднюю оценку"))
    print(u"Имя".ljust(15), u"Фамилия".ljust(10), u"Экзамены".ljust(43), u"Оценки".ljust(20))
    for student in students:
       averageMarkOfStudent = sum(student["marks"])/3
       if (averageMarkOfStudent>=averageMark):
        print(student["name"].ljust(15), student["surname"].ljust(10), str(student["exams"]).ljust(30), str(student["marks"]).ljust(20))
print_students(groupmates)
