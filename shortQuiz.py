import time
expanded_mcq_dictionary = {
    "What is the largest organ in the human body?\n\nA) Heart\nB) Liver\nC) Skin\nD) Lungs": "C",

    "How many legs does a spider typically have?\n\nA) 6\nB) 8\nC) 10\nD) 12": "B",

    "Which country is famous for the Pyramids of Giza?\n\nA) Greece\nB) Italy\nC) Egypt\nD) Mexico": "C",

    "What is the chemical symbol for water?\n\nA) CO2\nB) H2O\nC) O2\nD) NaCl": "B",

    "Which season comes after winter?\n\nA) Summer\nB) Autumn\nC) Spring\nD) Monsoon": "C",

    "What is the name of the fairy tale character who loses her glass slipper?\n\nA) Snow White\nB) Cinderella\nC) Sleeping Beauty\nD) Rapunzel": "B",

    "Which of these shapes has three sides?\n\nA) Square\nB) Triangle\nC) Rectangle\nD) Circle": "B",

    "What is the main ingredient in a traditional omelet?\n\nA) Potatoes\nB) Eggs\nC) Flour\nD) Rice": "B",

    "Which star is closest to the Earth?\n\nA) Alpha Centauri\nB) Polaris\nC) Sirius\nD) The Sun": "D",

    "How many core senses do humans have?\n\nA) 3\nB) 4\nC) 5\nD) 6": "C",

    "What do bees collect from flowers to make honey?\n\nA) Nectar\nB) Mud\nC) Sap\nD) Seeds": "A",

    "Which instrument has black and white keys?\n\nA) Guitar\nB) Flute\nC) Piano\nD) Drums": "C",

    "What is the currency used in Japan?\n\nA) Dollar\nB) Euro\nC) Yen\nD) Won": "C",

    "Which gas do humans need to breathe in to survive?\n\nA) Carbon Dioxide\nB) Nitrogen\nC) Hydrogen\nD) Oxygen": "D",

    "In which direction does the sun rise?\n\nA) North\nB) South\nC) East\nD) West": "C",

    "Who is the author of the 'Harry Potter' book series?\n\nA) J.R.R. Tolkien\nB) J.K. Rowling\nC) Roald Dahl\nD) C.S. Lewis": "B",

    "What is the tallest mammal on Earth?\n\nA) Elephant\nB) Giraffe\nC) Blue Whale\nD) Moose": "B",

    "Which of these is a primary food source for giant pandas?\n\nA) Eucalyptus\nB) Bamboo\nC) Bananas\nD) Fish": "B",

    "How many colors are there in a standard rainbow?\n\nA) 5\nB) 6\nC) 7\nD) 8": "C",

    "What is the hard, protective outer layer of a tree trunk called?\n\nA) Leaves\nB) Bark\nC) Roots\nD) Twigs": "B"
}
while True:
    playOrNot = input("Do You want to answer some simple question?y/n  ")
    if playOrNot == 'y':
        point = 0
        wrong_dic = {}
        start_time = time.perf_counter()
        for key in expanded_mcq_dictionary.keys():
            ans = input(f"{key}   ")
            value = expanded_mcq_dictionary.get(key)
            if ans.upper() == value:
                point = point+10
            else:
                point = point-10
                wrong_dic.update({key: value})
        end_time = time.perf_counter()
        if wrong_dic:
            print(f"Time taken : {end_time - start_time}")
            print("You've got some wrong answers")
            time.sleep(0.5)

            if input("Do you want to see the answers? y/n ") == 'y':
                for k, v in wrong_dic.items():
                    time.sleep(0.3)
                    print(f"{k} right answer is {v}")

        else:
            print("You've got it all right! Congratulation")

        print(f"Thanks for playing the game you got {point} points out of 200")
        break
    else:
        print("Your freaking choice!! ")
        break
