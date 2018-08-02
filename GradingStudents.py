def gradingStudents(grades):
    new_grades = []
    for i in grades:
        if i < 38:
            new_grades.append(i)
        else:
            if i % 5 == 0:
                new_grades.append(i)
            else:
                if i % 5 >= 3:
                    x = i + (5 - (i % 5))
                else:
                    x = i
                new_grades.append(x)
    return new_grades


if __name__ == '__main__':
    n = int(input())
    grades = []
    for _ in range(n):
        grades_item = int(input())
        grades.append(grades_item)

    result = gradingStudents(grades)
    print(result)
