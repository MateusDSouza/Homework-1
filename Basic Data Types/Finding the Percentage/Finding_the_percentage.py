if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    if query_name in student_marks:
        media=student_marks[query_name]
        mm=(sum(media))/len(media)
        mmm="{:.2f}".format(mm)
        print(mmm)