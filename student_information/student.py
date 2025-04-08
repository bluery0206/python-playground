"""
student
"""

from person import Person

class Student(Person):
    """ Student """
    def __init__ (self, name:str, age:int, address:str, gender:str, id_num:int, course:str) -> None:
        super().__init__(name, age, address, gender)
        self._id_num=id_num
        self._course=course

    @property
    def id_num(self) -> int:
        """ Student's ID number """
        return self._id_num

    @id_num.setter
    def id_num(self, new_id_num: int) -> None:
        self._id_num = new_id_num

    @property
    def course(self) -> str:
        """ Student's Course """
        return self._course

    @course.setter
    def course(self, new_course: str) -> None:
        self._course = new_course

    @property
    def details(self) -> str:
        return f"id:{self._id_num} " + super().details + f", course:{self._course}"


if __name__ == "__main__":
    student_1 = Student("Mark Paul", 20, "Pob. Norte Clarin", "Male", 1111, "BSCS 2A")
    print(student_1.details)
