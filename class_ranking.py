# WAp to create a class ranking system it should contains two methods like get_student_percentage()
# and get_top_3()


class Ranking_System:

    def __init__(self, students):
        self.students = students

    # Method 1: Calculate percentage
    def get_student_percentage(self, marks):
        total = sum(marks)
        percentage = total / len(marks)
        return percentage

    # Method 2: Get top 3 students
    def get_top_3(self):

        student_percentage = {}

        for name, marks in self.students.items():
            percentage = self.get_student_percentage(marks)
            student_percentage[name] = percentage

        # Sort students based on percentage
        sorted_students = sorted(
            student_percentage.items(),
            key=lambda x: x[1],
            reverse=True
        )

        return sorted_students[:3]


# Student data
students = {
    "Sathish": [85, 90, 88, 92, 87],
    "Rahul": [78, 85, 80, 82, 79],
    "Priya": [95, 92, 94, 96, 93],
    "Kiran": [88, 86, 90, 85, 89],
    "Anjali": [91, 89, 92, 90, 94]
}


# Create object
r = Ranking_System(students)


# Display percentages
print("----- STUDENT PERCENTAGES -----")

for name, marks in students.items():
    percentage = r.get_student_percentage(marks)
    print(name, ":", percentage, "%")


# Display Top 3
print("\n----- TOP 3 STUDENTS -----")

top_3 = r.get_top_3()

for rank, student in enumerate(top_3, start=1):
    print(rank, ".", student[0], "-", student[1], "%")