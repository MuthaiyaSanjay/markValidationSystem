def find(mark):
    if (mark >= 0 and mark <= 100):
        print()
    else:
        print("Enter Valid Mark")
        over()
def result(tamil,english,maths,science,social):
    if(tamil >=35 and english >=35 and maths >=35 and science >=35 and social >=35 ):
        print("You Are pass the Board Exam")
        total = tamil + english + maths + science + social
        print("Your Total Mark is :", total)
    else:
        print("Sorry You are Fail the Board Exam")
        total = tamil + english + maths + science + social
        print("Your Total Mark is :", total)
def over():
    print("---Mark System---")
    tamil=int(input("Enter Tamil Mark\n"))
    mark=tamil
    find(mark)
    english=int(input("Enter English Mark\n"))
    mark=english
    find(mark)
    maths=int(input("Enter Maths Mark\n"))
    mark=maths
    find(mark)
    science=int(input("Enter Science Mark\n"))
    mark=science
    find(mark)
    social=int(input("Enter Social Mark\n"))
    mark=social
    find(mark)
    result(tamil,english,maths,science,social)
over()