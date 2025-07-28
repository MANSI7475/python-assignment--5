student_marks={'mansi':50,
              'kartik':60,
              'darshan':70,
              'dev':60}
student_name=input("enter the student name:")
if student_name in student_marks:
    mark=student_marks[student_name]
    print("the mark of {} is {}".format(student_name,mark))
else:
    print("student name not found")


