if __name__ == '__main__':
    # Input :
    n = int(input())
    studentsEng = set(input().strip().split())

    b = int(input())
    studentsFrn = set(input().strip().split())


    studentsBoth = studentsEng & studentsFrn
    noStudentsBoth = len(studentsBoth)

    # Output :
    print(noStudentsBoth)
