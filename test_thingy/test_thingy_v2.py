
import string

letters = string.ascii_uppercase

class Question:
    def __init__(self, question:str, answer:list[str]|str, case_strict:bool=False):
        self.question = question
        self.answer = self.set_answer(answer)
        self.case_strict = case_strict

    def identify(self, answer:str) -> bool:
        if not self.case_strict and not isinstance(self, MultipleChoice):
            answer = answer.lower()
            answer = answer.strip()

        if type(self.answer) == list:
            if answer in self.answer:
                return True
            else:
                return False
        elif type(self.answer) == str:
            if answer == self.answer:
                return True
            else:
                return False

    def set_answer(self, answer):
        if isinstance(self, MultipleChoice) and len(answer) > 1 and type(answer) is not list:
            raise ValueError(f"MultipleChoice Class answer must only have one character only.")

        return answer

class Identification(Question):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class MultipleChoice(Question):
    def __init__(self, choices:list, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.choices = choices

class Test:
    def __init__(self, questions:list[Question]):
        self.questions = questions
        self.answers = []
        self.result = []
        self.corrects = 0
        self.length = len(self.questions)

    def get_score(self):
        return f"{self.corrects}/{self.length}"

    def take_test(self):
        for idx, q in enumerate(self.questions):
            print(idx+1, ") ", q.question, sep="")

            if type(q) == MultipleChoice:
                for idx, c in enumerate(q.choices):
                    import string
                    uppercase_alphabet = string.ascii_uppercase
                    print("\t" + letters[idx] + ") " + c)

            answer = input("> ")
            print()
            self.answers.append(answer)

    def assess(self):
        for q, a in zip(self.questions, self.answers):
            self.result.append(q.identify(a))

        self.corrects = self.result.count(True)


if __name__ == "__main__":
    questions = []

    questions.append(MultipleChoice(
        question    = "Who is our National Hero?",
        answer      = "b", 
        choices     = [
            "Dr. Hosei Rizaru",
            "Ronaldo Baldador",
            "\"FunNy\"",
            "Whitebeard",
        ]
    ))
    questions.append(MultipleChoice(
        question    = "Who is the colonizeristerator of the Philippines in 21st century?",
        answer      = "a", 
        choices     = [
            "Gen. Ronarudo Barudadooru",
            "Whitebeard Pirates",
            "Avengers",
            "AestheticerzxcxzXZXZXz",
        ]
    ))
    questions.append(MultipleChoice(
        question    = "Who is our RIIL campus dean?",
        answer      = "a",
        choices     = [
            "Kim Atienza",
            "Kim Taehyung",
            "Jackie-san",
            "Pekora",
        ]
    ))
    questions.append(MultipleChoice(
        question    = "What happened on September 16, 2022 in World LIT messenger that impacted students' lives?",
        answer      = "a",
        choices     = [
            "Nothing",
            "Handsomes did the \"Sign of the Pogi\"",
            "Rats fighting on a soup",
            "Your Mom",
        ]
    ))
    questions.append(MultipleChoice(
        question    = "Who is the person behind Darna's mask?",
        answer      = "d",
        choices     = [
            "Tectone",
            "Narda",
            "Jane De Leon",
            "Mayor Ange",
        ]
    ))
    questions.append(MultipleChoice(
        question    = "How to properly compliment someone as Pinoy?",
        answer      = "d",
        choices     = [
            "Literally say a compliment",
            "Tap them on the back",
            "Say \"Ataya! Maayuja jud nimo baysts!\"",
            "Get jealous and make fake accusasions",
        ]
    ))
    questions.append(MultipleChoice(
        question    = "Cats are evil",
        answer      = "c",
        choices     = [
            "True",
            "Tralse",
            "Cats are cute",
            "False",
        ]
    ))
    questions.append(MultipleChoice(
        question    = "Is the One Piece Real?",
        answer      = "a",
        choices     = [
            "THE ONE PIECE IS REAAAAAAL",
            "Can we get much higher",
            "Baldador",
            "Idk, ask my BBF/GBF",
        ]
    ))
    questions.append(MultipleChoice(
        question    = "Am I (the coder) handsome?",
        answer      = ["a", "b", "c", "d"],
        choices     = [
            "Yes",
            "Yes",
            "Yes",
            "Yes",
        ]
    ))
    questions.append(MultipleChoice(
        question    = "Scenario: Your student made a slight grammatical error. What should you do?",
        answer      = "d",
        choices     = [
            "Kick them from the group.",
            "Make drama about it.",
            "Be sarcastic AF, yo!",
            "All of the above",
        ]
    ))

    test = Test(questions)
    test.take_test()
    test.assess()
    print(test.get_score())
