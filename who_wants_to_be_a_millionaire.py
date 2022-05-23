import random # needed for randomized weighted choices (see below)

# Introduction
name = input("Enter your name: ")
print()
print(f"Welcome to \"Who wants to be a millionaire?\", {name}! \nFifteen questions are ahead, if you want to win the million! \nIf you answer the fifth question correctly, 500 $ is guaranteed for you. \nIf you answer the tenth question correcty, 16000 $ is guaranteed for you.")
print("If you don\'t know the answer, you can use a lifeline: 50:50, Phone a Friend or Ask the Audience. You can use each only once.")
print()
print("Let\'s start with question number one!")
print()
input("Press ENTER to continue.")
print()

# Class for questions
class Question:
    def __init__(self, name, question, answer1, answer2, answer3, answer4, level, correct_answer, fifty_answer, weighted_phone, weighted_audience):
        self.name = name
        self.question = question
        self.answer1 = answer1
        self.answer2 = answer2
        self.answer3 = answer3
        self.answer4 = answer4
        self.level = level
        self.correct_answer = correct_answer
        self.fifty_answer = fifty_answer
        self.weighted_phone = weighted_phone
        self.weighted_audience = weighted_audience
        self.next = None

# Counter for lifelines. They can be used only once.
fifty_count = 0
phonefriend_count = 0
audience_count = 0

# initiates questions, specifies correct and wrong answers
def pose_question(self):
    print(f"The {self.level}$-question: \n{self.question}")
    print(f"A: {self.answer1}")
    print(f"B: {self.answer2}")
    print(f"C: {self.answer3}")
    print(f"D: {self.answer4}")
    print(f"E: I want to use a lifeline")
    print(f"F: Quit")
    print()
    choice = input("Choose one answer (A, B, C, D, E or F): ").upper()
    print()
    if choice == "A" or choice == "B" or choice == "C" or choice == "D" or choice == "E" or choice == "F":
        if choice == "F":
            quit()
        elif choice == "E":
            if fifty_count == 1 and phonefriend_count == 1 and audience_count == 1:
                print("No lifelines left.")
                print()
                input("Press ENTER to continue.")
                pose_question(self)  
            else: 
                lifeline(self)
        elif choice == self.correct_answer:
            if self.level == 1000000:
                print(f"You won the million, {self.name}! You did it! Congratulations!")
                print ("*   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *   *")
                print("Game over.")
                quit()
            else:
                print(f"Correct answer! You won {self.level} $.")
                print()
                input("Press ENTER to continue.")
                print()
                pose_question(self.next)
        else:
            print("Wrong answer.")
            if 1000 <= self.level <= 16000:
                print("Game over. But you can go home with 500 $!")
                quit()
            if 32000 <= self.level <= 1000000:
                print("Game over. But you can go home with 16000 $!")
                quit()
            quit()
    else:
        print("Incorrect input.")
        print()
        input("Press ENTER to continue.")
        print()
        pose_question(self)

# initiates lifelines
def lifeline(self):
    while True: 
        global fifty_count
        global phonefriend_count
        global audience_count     
        print("You can choose: ")
        if fifty_count == 0:
            print("1) 50:50")
        if phonefriend_count == 0:
            print("2) Phone a Friend")
        if audience_count == 0:
            print("3) Ask the Audience")
        lifeline_var = input("Enter the number: ")
        print()
        if lifeline_var == "1":
            if fifty_count == 0:
                fifty_count += 1
                fifty(self)
            else:
                print("You already used this lifeline.")
        elif lifeline_var == "2":
            if phonefriend_count == 0:
                phonefriend_count += 1                
                phonefriend(self)
            else:
                print("You already used this lifeline.")
        elif lifeline_var == "3":
            if audience_count == 0:
                audience_count += 1
                audience(self)
            else:
                print("You already used this lifeline.")
        else:
            print("Incorrect input.")

# enforces the 50:50-lifeline
def fifty(self):
    while True: 
        print("You choose the 50:50-lifeline.")
        print()
        print(f"Two wrong questions are removed. The remaining two are:")
        if self.correct_answer < self.fifty_answer:
            print(self.correct_answer)
            print(self.fifty_answer)
        else:
            print(self.fifty_answer)   
            print(self.correct_answer)
        choice_remaining = input("Which answer do you choose? ").upper()
        if choice_remaining == self.correct_answer:
            print()
            print(f"Correct answer! You won {self.level} $.")
            print()
            input("Press ENTER to continue.")
            print()
            pose_question(self.next)
        elif choice_remaining == self.fifty_answer:
            if 1000 < self.level < 16000:
                print("Wrong answer. Game over. But you can go home with 500 $!")
                quit()
            elif 32000 < self.level < 1000000:
                print("Wrong answer. Game over. But you can go home with 16000 $!")
                quit()
            else:
                print("Wrong answer. Game over.")
                quit()     
        elif choice_remaining != "A" or "B" or "C" or "D" or "E" or "F": 
            print("Incorrect input.")

# enforces the Phone a Friend-lifeline
def phonefriend(self):
    print("You choose the Phone a Friend-lifeline. Who yo you want to call?")
    friend = input("I want to call my friend: ")
    print(f"Rrrring. Hello {friend}! {self.name} now reached the {self.level}$-question.")
    print()
    print(f"The {self.level}$-question: \n{self.question}")
    print(f"A: {self.answer1}")
    print(f"B: {self.answer2}")
    print(f"C: {self.answer3}")
    print(f"D: {self.answer4}")
    print()
    print(f"What answer do you choose, {friend}?")
    print()
    print(f"{friend}: I would say answer {self.weighted_phone} is correct!")
    print()
    print(f"Thank you, {friend}! So, {name}, what do you say? Which answer do you choose? Do you follow the advice of {friend}?")
    print()
    input("Press ENTER to continue.")
    print()
    pose_question(self)
    print()

# enforces the Ask the Audience-lifeline
def audience(self):
    print("You choose the Ask the Audience-lifeline.")
    print()
    print("Dear spectators of our show, please vote now, which of the four answer possibilites you think is correct.")
    print("...")
    print(f"The majority voted for: {self.weighted_audience}!")
    print()
    print(f"Thank you, dear audience! So, {name}, what do you say? Which answer do you choose? Do you follow the advice of the audience?")
    print()
    input("Press ENTER to continue.")
    print()
    pose_question(self)

# needed for weighting the answers
answers = ["A", "B", "C", "D"]

# the questions (objects of the class Question) with their attributes
head_weighted_phone = (random.choices(answers, weights=(10, 10, 60, 20), k=1)) # weighted answers for Phone a Friend
head_weighted_audience = (random.choices(answers, weights=(5, 5, 75, 10), k=1)) # weighted answers fpr Ask the Audience
head = Question(name, "What sort of animal is Walt Disney's Dumbo?", "Deer", "Rabbit", "Elephant", "Donkey", 50, "C", "D", *head_weighted_phone, *head_weighted_audience) # 50 $

second_question_weighted_phone = (random.choices(answers, weights=(10, 10, 60, 20), k=1))
second_question_weighted_audience = (random.choices(answers, weights=(5, 5, 75, 10), k=1))
second_question = Question(name, "Which Disney character famously leaves a glass slipper behind at a royal ball?", "Pocahontas", "Sleeping Beauty", "Cinderella", "Elsa", 100, "C", "D", *second_question_weighted_phone, *second_question_weighted_audience) # 100 $

third_question_weighted_phone = (random.choices(answers, weights=(20, 10, 10, 60), k=1))
third_question_weighted_audience = (random.choices(answers, weights=(10, 5, 5, 75), k=1))
third_question = Question(name, "Which is the largest city in the USA's largest state?", "Dallas", "Los Angeles", "New York", "Anchorage", 200, "D", "C", *third_question_weighted_phone, *third_question_weighted_audience) # 200 $ 

fourth_question_weighted_phone = (random.choices(answers, weights=(10, 60, 10, 20), k=1))
fourth_question_weighted_audience = (random.choices(answers, weights=(5, 75, 5, 10), k=1))
fourth_question = Question(name, "The hammer and sickle is one of the most recognisable symbols of which political ideology?", "Republicanism", "Communism", "Conservatism", "Liberalism", 300, "B", "C", *fourth_question_weighted_phone, *fourth_question_weighted_audience) # 300 $

fifth_question_weighted_phone = (random.choices(answers, weights=(10, 60, 10, 20), k=1))
fifth_question_weighted_audience = (random.choices(answers, weights=(5, 75, 5, 10), k=1))
fifth_question = Question(name, "In the UK, the abbreviation NHS stands for National what Service?", "Humanity", "Health", "Honour", "Household", 500, "B", "C", *fifth_question_weighted_phone, *fifth_question_weighted_audience) # 500 $ 

sixth_question_weighted_phone = (random.choices(answers, weights=(60, 10, 10, 20), k=1))
sixth_question_weighted_audience = (random.choices(answers, weights=(75, 5, 5, 10), k=1))
sixth_question = Question(name, "Obstetrics is a branch of medicine particularly concerned with what?", "Childbirth", "Broken bones", "Heart conditions", "Old age", 1000, "A", "B", *sixth_question_weighted_phone, *sixth_question_weighted_audience) # 1000 $

seventh_question_weighted_phone = (random.choices(answers, weights=(10, 60, 10, 20), k=1))
seventh_question_weighted_audience = (random.choices(answers, weights=(5, 75, 5, 10), k=1))
seventh_question = Question(name, "What does the word loquacious mean?", "Angry", "Chatty", "Beautiful", "Shy", 2000, "B", "C", *seventh_question_weighted_phone, *seventh_question_weighted_audience) # 2000 $ 

eigth_question_weighted_phone = (random.choices(answers, weights=(10, 10, 20, 60), k=1))
eigth_question_weighted_audience = (random.choices(answers, weights=(10, 5, 5, 75), k=1))
eigth_question = Question(name, "Which city will host the 2028 Olympic Games?", "Beijing", "Paris", "Tokyo", "Los Angeles", 4000, "D", "B", *eigth_question_weighted_phone, *eigth_question_weighted_audience) # 4000 $

nineth_question_weighted_phone = (random.choices(answers, weights=(60, 10, 10, 20), k=1))
nineth_question_weighted_audience = (random.choices(answers, weights=(75, 5, 5, 10), k=1))
nineth_question = Question(name, "How many million miles away is the sun from the Earth?", "93 million", "12 million", "136 million", "200 million", 8000, "A", "B", *nineth_question_weighted_phone, *nineth_question_weighted_audience) # 8000 $ 

tenth_question_weighted_phone = (random.choices(answers, weights=(60, 10, 10, 20), k=1))
tenth_question_weighted_audience = (random.choices(answers, weights=(75, 5, 5, 10), k=1))
tenth_question = Question(name, "At the closest point, which island group is only 50 miles south-east of the coast of Florida?", "Bahamas", "US Virgin Islands", "Turks and Caicos Islands", "Bermuda", 16000, "A", "B", *tenth_question_weighted_phone, *tenth_question_weighted_audience) # 16000 $

eleventh_question_weighted_phone = (random.choices(answers, weights=(10, 10, 60, 20), k=1))
eleventh_question_weighted_audience = (random.choices(answers, weights=(5, 5, 75, 10), k=1))
eleventh_question = Question(name, "What was the only painting sold by Vincent van Gogh during his lifetime?", "Sunflower", "The Starry Night", "The Red Vineyard", "The Yellow House", 32000, "C", "D", *eleventh_question_weighted_phone, *eleventh_question_weighted_audience) # 32000 $ 

twelveth_question_weighted_phone = (random.choices(answers, weights=(10, 10, 60, 20), k=1))
twelveth_question_weighted_audience = (random.choices(answers, weights=(5, 5, 75, 10), k=1))
twelveth_question = Question(name, "From which author's work did scientists take the word \"quark\"?", "Lewis Carroll" , "Edward Lear", "James Joyce", "Aldous Huxley", 64000, "C", "D", *twelveth_question_weighted_phone, *twelveth_question_weighted_audience) # 64000 $

thirteenth_question_weighted_phone = (random.choices(answers, weights=(20, 10, 10, 60), k=1))
thirteenth_question_weighted_audience = (random.choices(answers, weights=(10, 5, 5, 75), k=1))
thirteenth_question = Question(name, "Construction of which of these famous landmarks was completed first?", "Empire State Building", "Royal Albert Hall", "Eiffel Tower", "Big Ben Clock Tower", 125000, "D", "B", *thirteenth_question_weighted_phone, *thirteenth_question_weighted_audience) # 125000 $ 

fourteenth_question_weighted_phone = (random.choices(answers, weights=(10, 10, 60, 20), k=1))
fourteenth_question_weighted_audience = (random.choices(answers, weights=(5, 5, 75, 10), k=1)) 
fourteenth_question = Question(name, "Oberon is the satellite of which planet?", "Mercury", "Neptune", "Uranus", "Mars", 500000, "C", "D", *fourteenth_question_weighted_phone, *fourteenth_question_weighted_audience) # 500000 $

fifteenth_question_weighted_phone = (random.choices(answers, weights=(10, 60, 10, 20), k=1))
fifteenth_question_weighted_audience = (random.choices(answers, weights=(5, 75, 5, 10), k=1))
fifteenth_question = Question(name, "In 1718, which pirate died in battle off the coast of what is now North Carolina?", "Calico Jack", "Blackbeard", "Bartholomew Roberts", "Captain Kidd", 1000000, "B", "C", *fifteenth_question_weighted_phone, *fifteenth_question_weighted_audience) # 1000000 $ 

# the simply linked list
head.next = second_question
second_question.next = third_question
third_question.next = fourth_question
fourth_question.next = fifth_question
fifth_question.next = sixth_question
sixth_question.next = seventh_question
seventh_question.next = eigth_question
eigth_question.next = nineth_question
nineth_question.next = tenth_question
tenth_question.next = eleventh_question
eleventh_question.next = twelveth_question
twelveth_question.next = thirteenth_question
thirteenth_question.next = fourteenth_question
fourteenth_question.next = fifteenth_question

# initiating the game
pose_question(head)

# python who_wants_to_be_a_millionaire.py