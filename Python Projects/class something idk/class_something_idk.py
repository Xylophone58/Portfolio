import csv

def main():
    students = []
    with open('Test 1.csv', 'r') as f:
        first = True
        reader = csv.reader(f)
        for row in reader:
            if first:
                first = False
                row.append('Average')
                headers = row
            else:
                students.append(row[:2] + [int(x) for x in row[2:]])

    for n in range(len(students[0]) - 2):
        max_score = max([student[n + 2] for student in students])
        if max_score < 90:
            for student in students:
                student[n + 2] += 90 - max_score

    for student in students:
        average = sum(student[2:]) / (len(student) - 2)
        student.append(average)
        '''
                average = sum(int(x) for x in row[2:]) / (len(row) - 2)
                row.append(f"{average:.2f}")
                students.append(row)
                '''
    with open('grades_averaged.csv', 'w') as f:
        writer = csv.writer(f, lineterminator='\n')
        writer.writerow(headers)
        for student in students:
            writer.writerow(student)

main()