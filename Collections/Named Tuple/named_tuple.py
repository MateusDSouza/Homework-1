# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import namedtuple
number=int(input())
colum=input().split()
grade=0
for i in range(number):
    classe= namedtuple('student',colum)
    x1, x2, x3, x4 = input().split()
    student=classe(x1,x2,x3,x4)
    grade = grade + int(student.MARKS)
print('{:.2f}'.format(grade/number))