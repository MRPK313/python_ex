

class Student:
    """ The Student class creates a new Student object with the given name and age then get scores and calculate average

    """

    

    def __init__(self, name: str, age: int) -> None:
        """initialize the Student object with the given name and age

        Args:
            name (str): name of the Student
            age (int): age of the Student
        """

        self.name = name
        self.age = age
        self.scores = {}

    def add_score(self) -> str:
        """add a scores of the Student in the dictionary {'lesson':'score'}

        Returns:
            str: scores
        """

        while True:
            lesson = input("enter Lesson name to add or 0 to exit: ")
            if lesson == "0":
                return "\nadded sucssesful\n"+self.__str__()

            score = float(input(f"Enter score for {lesson}: "))
            print()

            if lesson and score :
                self.scores[lesson] = score

    

    def average(self) -> str:
        """calculate averagee of scores in dictonary

        Returns:
            str: averagee
        """

        if not self.scores:
            answer = "No scores added\n"
        
        avg_scores = sum(self.scores.values()) / len(self.scores)

        answer = f"Average score: {avg_scores}\n"
        answer += self.__str__()
        return answer
    
    def __str__(self) -> str:
        """show info after print object

        Returns:
            str: info
        """

        return f"Student Name: {self.name}, Age: {self.age}\nscores added : {self.scores}\n"
    

    def __repr__(self) -> str:
        """reperesentation method for developers

        Returns:
            str: __repr__ method
        """

        return f"{self.__class__.__name__}({self.name!r}, {self.age!r})"
    

ali = Student("ali",12)

print(ali)
ali.add_score()

print(ali.average())

print(ali)
print(repr(ali))  # representations for developers