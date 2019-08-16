# this is learning python's   list[] map(key:value)
n = int(input("Enter the number of students: "))
data = {} #Dictionary variables used to store data
Subjects = ('Physics','Maths','History') #all the subjects
for a in range(0,n):
    name = input("Enter the name of the student {}: ".format(a+1))
    marks = []
    for x in Subjects:
        marks.append(int(input('Enter marks of {}:'.format(x))))
    data[name] = marks
for x,y in data.items():
    total = sum(y)
    print("{}'s total marks {}".format(x,total))
    if total < 120:
        print(x,"failed :")
    else:
        print(x,"passed :")
# when the program through the dictionary the output is a disorderly
# if you want through the dictionary you should use the function of .item()
# when we add data to the dictionary ,we should determine if an element exists,we can
# use dict.setdefault(key , value) for example  date.setdefault('name', []).append('python')
