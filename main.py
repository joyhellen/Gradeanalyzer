def grade_analyzer(student_grades, operation):
    if operation not in ["average", "highest", "lowest"]:
        raise ValueError("Invalid operation.")

    if not student_grades:
        raise ValueError("The students grade list is empty.")
    
    result = None
    
    if operation == "average":
        total_grades = sum(grade for _, grade in student_grades)
        result = total_grades / len(student_grades)
        return result
    elif operation == "highest":
        highest_grade = float('-inf')
        for _, grade in student_grades:
            if grade > highest_grade:
                highest_grade = grade
            result = highest_grade
        
    elif operation == "lowest":
        lowest_grade = float('inf')
        for _, grade in student_grades:
            if grade < lowest_grade:
                lowest_grade = grade
            result = lowest_grade

    return result


student_grades = [("Amanda", 100), ("Sharon", 98), ("Fauzia", 88), ("Joy", 90), ("Koome", 68), ("Kaburu", 56)]
operation = "highest"
highest = grade_analyzer(student_grades, operation)
print("Highest grade: {}".format(highest))

operation = "average"
average = grade_analyzer(student_grades, operation)
print("Average grade: {}".format(average))

operation = "lowest"
lowest = grade_analyzer(student_grades, operation)
print("Lowest grade: {}".format(lowest))