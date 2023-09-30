#  Copyright (c) 2023.
#  @Author Subhrajeet Ghosh
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    marks_list = student_marks[query_name]
    total_marks = 0
    for i in marks_list:
        total_marks += i
    print("{:.2f}".format(total_marks / len(marks_list)))
    print("%.2f" % (total_marks / len(marks_list)))
