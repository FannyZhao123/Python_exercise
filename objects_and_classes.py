
# create a new type Student
class Student:
    """ a data type representing a student
    
    Instance Attributes: name (str), id_num (int)
    Class Attributes: num_of_students (int)
    """
    num_of_students = 0
    
    # constructor
    def __init__ (self, n, i):
        self.name = n
        self.id_num = i
        Student.num_of_students += 1


def create_student(student_name, student_id):
    """ (str, int) -> Student

    >>> s = create_student("Giulia", 123)
    >>> s.name
    'Giulia'
    >>> s.id_num
    123
    """
    # create a student
    a = Student()
    
    # create two attributes with the values provided as input
    a.name = student_name
    a.id_num = student_id
    
    return a


def get_younger(s1, s2):
    """ (Student, Student) -> str

    >>> s = create_student("Giulia", 123)
    >>> t = Student()
    >>> t.name = "Harry"
    >>> t.id_num = 321
    >>> get_younger(s, t)
    'Harry'
    """
    
    if s1.id_num >= s2.id_num :
        return s1.name
    else:
        return s2.name
    
