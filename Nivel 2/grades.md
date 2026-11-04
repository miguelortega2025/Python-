# Exercise Level 3 — Functions and Lists

## 🎯 Goal

Practice functions (with parameters and return values), lists, and combining both to organize code properly.

## 📝 Task — "Student Grade Manager"

Create a program called `grades.py` that manages a list of students and their grades. All logic must be inside functions — no long blocks of code at the top level.

### Data structure

Use a list of dictionaries, for example:

```python
students = [
    {"name": "Ana", "grade": 8.5},
    {"name": "Luis", "grade": 6.0},
    {"name": "Marta", "grade": 9.2},
]
```

### Required functions

- **`show_students(students)`**
  Prints all students and their grades in a readable format.

- **`average_grade(students)`**
  Returns the average grade of all students (a float). Handle the case of an empty list (return 0).

- **`best_student(students)`**
  Returns the name of the student with the highest grade. If the list is empty, return `None`.

- **`add_student(students, name, grade)`**
  Adds a new student to the list. If the grade is not between 0 and 10, print an error and don't add the student.

- **`passed_students(students)`**
  Returns a new list with only the names of students whose grade is ≥ 6.

### Main program

At the bottom, write a small `main()` function that:

1. Calls `show_students()`
2. Prints the average
3. Prints the best student
4. Adds a new student
5. Prints the list of passed students

Wrap everything in `if __name__ == "__main__": main()`

## ✅ Base solution

```python
def show_students(students):
    print("--- Students ---")
    for s in students:
        print(f"{s['name']}: {s['grade']}")

def average_grade(students):
    if not students:
        return 0
    return sum(s["grade"] for s in students) / len(students)

def best_student(students):
    if not students:
        return None
    best = students[0]
    for s in students:
        if s["grade"] > best["grade"]:
            best = s
    return best["name"]

def add_student(students, name, grade):
    if grade < 0 or grade > 10:
        print(f"Invalid grade for {name} ❌")
        return
    students.append({"name": name, "grade": grade})
    print(f"{name} added ✅")

def passed_students(students):
    return [s["name"] for s in students if s["grade"] >= 6]

def main():
    students = [
        {"name": "Ana", "grade": 8.5},
        {"name": "Luis", "grade": 6.0},
        {"name": "Marta", "grade": 9.2},
    ]

    show_students(students)
    print(f"Average: {average_grade(students):.2f}")
    print(f"Best student: {best_student(students)}")

    add_student(students, "Pedro", 7.5)
    add_student(students, "Sofia", 12)  # invalid

    print(f"Passed: {passed_students(students)}")

if __name__ == "__main__":
    main()
```

## 🚀 Extra challenges (pick one or more)

1. **Interactive menu:** replace `main()` with a `while True` menu that lets the user choose: show / add / average / best / passed / exit — reusing the same functions.
2. **Sorting:** add a function `sort_by_grade(students)` that returns a new list sorted from highest to lowest (hint: `sorted(students, key=lambda s: s["grade"], reverse=True)`).
3. **Save to file:** add `save_to_file(students, filename)` that writes each student to a `.txt` file, one per line (`Ana,8.5`).
4. **Refactor:** rewrite `best_student` using `max()` with a lambda and check both versions give the same result.

## 🧑‍💻 My solution (with extra challenges)

```python
# Exercise Level 3 --- Functions and Lists

""" Practice functions (with parameters and return values), lists, and combining
both to organize code properly """


def show_students(students):
    print(" --- Students ---")
    for s in students:
        print(f"{s["name"]}: {["grade"]}")

def average_grade(students):
    if not students: 
        return 0
    return sum(s["grade"] for s in students) / len(students)


def best_student(students):
    if not students: 
        return None
    best = students[0]
    for s in students:
        if s["grade"] > best["grade"]:
            best = s
    return best["name"]

def add_student(students, name, grade):
    if grade < 0 or grade > 10: 
        print(f"Invalid grade for {name} X")
        return
    students.append({"name":name, "grade": grade })
    print(f"{name} added ")

def passed_students(students):
    return [s["name"] for s in students if s["grade"] >= 6]

def sort_by_grade(students):
    return sorted(students,key=lambda s: s["grade"],reverse=True)

# Guardar estudiantes en un txt
def save_to_file(students, filename): 
    with open(filename, "w") as file:
        for s in students:
            file.write(f"{s["name"]},{s["grade"]}\n")


# Version 2: 
def best_student_v2(students):
    if not students: 
        return None

    best = max(students,key=lambda s: s["grade"])


    




def main():
    students = [
        {"name": "Ana", "grade": 8.5},
        {"name": "Luis", "grade": 6.0},
        {"name": "Marta", "grade": 9.2}
    ]

    while True: 

        save_to_file(students, "students.txt")
        print(best_student_v2(students))





        print("\n === MENU ===")
        print("1. Show students")
        print("2. Add student")
        print("3. Average")
        print("4. Best student")
        print("5. Passed students")
        print("6. Exit")

        option = input("Choose: ")

        if option == "1":
            show_students(students)
        elif option == "2":
            name = input("Name: ")
            grade = float(input("Grade: "))
            add_student(students, name, grade)
        elif option == "3": 
            print(f"Average: {average_grade(students):.2f}")

        elif option == "4": 
            print(f"Best student: {best_student(students)} ")

        elif option == "5": 
            print(passed_students(students))

        elif option == "6": 
            print("Goodbye!")
            break
        else: 
            print("Invalid option")


 

if __name__ == "__main__": 
    main()
```
