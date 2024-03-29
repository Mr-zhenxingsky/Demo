class Person(object):
    """
    return an Person object with given name
    """

    def __init__(self,name):
        self.name = name

    def get_details(self):
        """
        return a String with person's name
        """
        return self.name

class Student(Person):
    """
    return students object , three parameters are adopted : name , branch and year
    """
    def __init__(self,name,branch,year):
        Person.__init__(self,name)
        self.branch = branch
        self.year = year

    def get_details(self):
        """
        return a String with student details
        """
        return "{} studies {} and is in {} year.".format(self.name,self.branch,self.year)

class Teacher(Person):
    """
    return a Teacher object , take a list of stings as arguments
    """
    def __init__(self,name,papers):
        Person.__init__(self,name)
        self.papers = papers

    def get_details(self):
        return "{} teaches {}".format(self.name,','.join(self.papers))

person1 = Person('Sachin')
student1 = Student('Kushal','CSE',2005)
teacher1 = Teacher('Prashad',['C','C++'])

print(person1.get_details())
print(student1.get_details())
print(teacher1.get_details())
