#I just learned basic python aand I was bored so I also made a python version of this test thingy :)

def Software():
    print("\nReady to take the test? Yes/No:")
    cnfrm = input()

    answers = ["Null", ]
    yesList = ["Yes", "yes"]
    noList = ["No", "no"]
    name = []


    if cnfrm in yesList:
        print('''
Input your first and last name, department, year and section:''')

        def login():
            name = input().split()
            if len(name) < 4:
                name.clear()
                print("\nPlease input correctly...")
                login()
            else:
                num1 = input('''
Instruction: Input the capital letter of the chosen answer.
1. Who is our National Hero?
(A) Dr. Hosei Rizaru
(B) Ronaldo Baldador
(C) \"FunNy\"
(D) Whitebeard
Enter here: ''')
                if num1 != "B":
                    num1 = "X"
                elif num1 == "B":
                    num1 = "Correct"
                answers.append(num1)

                num2 = input('''
2. Who is the colonizeristerator of the Philippines in 21st century?
(A) Gen. Ronarudo Barudadooru
(B) Whitebeard Pirates
(C) Avengers
(D) AestheticerzxcxzXZXZXz
Enter here: ''')
                if num2 != "A":
                    num2 = "X"
                elif num2 == "A":
                    num2 = "Correct"
                answers.append(num2)

                num3 = input('''
3. Who is our RIIL campus dean?
(A) Kim Atienzan
(B) Kim Taehyung
(C) Jackie-san
(D) Pekora
Enter here: ''')
                if num3 != "A":
                    num3 = "X"
                elif num3 == "A":
                    num3 = "Correct"
                answers.append(num3)

                num4 = input('''
4. What happened on September 16, 2022 in World LIT messenger that impacted students' lives?
(A) Nothing
(B) Handsomes did the \"Sign of the Pogi\"
(C) Rats fighting on a soup
D) Your Mom
Enter here: ''')
                if num4 != "A":
                    num4 = "X"
                elif num4 == "A":
                    num4 = "Correct"
                answers.append(num4)

                num5 = input('''
5. Who is the person behind Darna's mask?
(A) Tectone
(B) Narda
(C) Jane De Leon
(D) Mayor Ange
Enter here: ''')
                if num5 != "D":
                    num5 = "X"
                elif num5 == "D":
                    num5 = "Correct"
                answers.append(num5)

                num6 = input('''
6. How to properly compliment someone as Pinoy?
(A) Literally say a compliment
(B) Tap them on the back
(C) Say \"Ataya! Maayuja jud nimo baysts!\"
(D) Get jealous and make fake accusasions
Enter here: ''')
                if num6 != "D":
                    num6 = "X"
                elif num6 == "D":
                    num6 = "Correct"
                answers.append(num6)

                num7 = input('''
7. Cats are evil
(A) True
(B) Tralse
(C) Cats are cute
(D) False
Enter here: ''')
                if num7 != "C":
                    num7 = "X"
                elif num7 == "C":
                    num7 = "Correct"
                answers.append(num7)

                num8 = input('''
8. Is the One Piece Real?
(A) THE ONE PIECE IS REAAAAAAL
(B) Can we get much higher
(C) Baldador
(D) Idk, ask my BBF/GBF
Enter here: ''')
                if num8 != "A":
                    num8 = "X"
                elif num8 == "A":
                    num8 = "Correct"
                answers.append(num8)

                imangry = ["Di", "Dile", "di", "dile"]
                compliment = ["Gwapa ko", "gwapa ko", "Gwapo ko", "gwapo ko"]
                choices = ["A", "B", "C", "D"]

                num9 = input('''
9. Am I (the coder) handsome?
(A) Yes
(B) Yes
(C) Yes
(D) Yes
Enter here: ''')
                if num9 in imangry:
                    answers.append("X... Ako'y magbuot.")
                elif num9 in compliment:
                    answers.append("Awh... Syempre! 'Sa man...")
                elif num9 in choices:
                    num9 = "Correct"
                    answers.append(num9)
                else:
                    answers.append("X")

                num10 = input('''
10. Scenario: Your student made a slight grammatical error. What should you do?
(A) Kick them from the group.
(B) Make drama about it.
(C) Be sarcastic AF, yo!
(D) All of the above
Enter here: ''')
                if num10 != "D":
                    num10 = "X"
                elif num10 == "D":
                    num10 = "Correct"
                answers.append(num10)


                print("\nYour answers:")
                for i in range(1, len(answers)):
                    print("%d. %s" % (i, answers[i]))


                correctAns = answers.count("Correct")
                print("\nScore: ", correctAns,"/", (len(answers) - 1))


                passing_score = ((len(answers) - 1) * .75)

                if correctAns == len(answers) - 1:
                    print(f"Wow! You got a perfect score, {name[0]}! Keep it up!")
                elif correctAns == 0:
                    print(f"Well, that was unexpected. Nice try though, {name[0]}.")
                elif float(correctAns) < passing_score:
                    print(f"You did well, {name[0]}! Study harder next time!")
                elif float(correctAns) > passing_score:
                    print(f"You passed! Good job, {name[0]}!")

                retry = input("\nDo you want to retake test? Yes/No: ")
                if retry in yesList:
                    login()
                elif retry in noList:
                    exit()


        login()



    elif cnfrm == "No":
        print("\nWelp... There's always tomorrow! :)")
        areyousure = input()
        if areyousure != None:
            Software()
    else:
        Software()#I just learned basic python aand I was bored so I also made a python version of this test thingy :)

Software()