
# soup.select('td > th') all TD elements that are directly in a th element.
import tkinter as tk
from tkinter import Tk
from tkinter.messagebox import askokcancel
from typing import List

import requests
import bs4
import random
from DisplayPages import Display






class Web_Scrape:
    import tkinter
    from tkinter import ttk











    @classmethod
    def main(self):

        words = []
        hint = []
        gameWords = {}


        # ws = WebScrape() # instantiate class
        res = requests.get('http://atcomputingschool.co.uk/dictionary.html')
        res.raise_for_status()

        # bs4 is the web scraper,
        webpage= bs4.BeautifulSoup(res.text ,'html.parser')
        self.scrape(webpage, words, hint)
        self.merge(self, words, hint, gameWords)
        self.display(self,words, hint)



    @staticmethod
    def scrape(webpage, words, hint):



        # find the tag by attribute value.
        name= webpage.select('th[scope="row"]')
        answer = webpage.select("tr > td")

        for i in range(len(name)):
            words.append(name[i].getText(strip=True))

        for j in  range (len(answer)):
            hint.append(answer[j].getText())


        return hint ,words


    @staticmethod
    def merge(self ,words, hint, gameWords ):
        # add values in a dictionary .
        counter =0

        for i in words:
            gameWords.update({i :hint[counter]})
            counter +=1







    def playGame(self ,words, hint, tries,toDisplay):


        # word to be displayed , random num , stickman


        replay= ""
        playing = True
        # checks to see if the user is in the middle of guessing , if not , pulls a word.
        tries = 0
        randomNum = random.randint(1, 87)
        answer = words[randomNum]

        toDisplay.append(answer)
        toDisplay.append(randomNum)

        #while true
        # self.generateWord(self ,words, hint, randomNum)
        # if userAnswer =='1':
        #      self.guessWord(self ,userAnswer, answer ,tries )
        # elif userAnswer =='2':
        #     self.guessByLetter(self ,answer ,tries,toDisplay)
        # elif userAnswer =='3':
        #     self.playGame(self ,words ,hint, 0)
        # elif userAnswer == '4':
        #     print("Thank you for playing")

        toDisplay= self.guessByLetter(self, answer, tries,toDisplay)
        return toDisplay




    # this method validates user answer
    def guessWord(self ,userAnswer, answer ,tries):
        # this method validates the user answer
        # it starts by check if it is correct and if its not correct
        #     it adds to tries and give user the option to restart


        if userAnswer == answer:
            print("Congratulations !! you got it \n Do you want to keep playing (Y/N) ")
            replay= input('WholeWord>').lower()

            return replay

        else:
            # regardless if this is fist atempt or not , the user gets to try again
            print("Guess the word , press 0 at anytime to guess by letter")
            tries += 1
            userAnswer = input("Whole Word >").lower()
            if userAnswer == answer:
                print("You got it !!!")
                tries = 0
                print("Try again ? (Y/N)")
                replay = input("Whole Word>").lower()
                replay = replay.strip()
                return replay
            elif userAnswer == "0":
                self.guessByLetter(self, answer, tries)
            else:
                tries += 1
                print("Better luck next time\n "
                      "Try again ? (Y/N)")
                replay= input("Whole Word>").lower()
                replay = replay.strip()

                while tries <= 9:
                    if replay != "y" or tries == 9:
                        print("End of game")
                        break
                    elif replay == "y" and tries <= 9:
                            self.guessWord(self, userAnswer, answer, tries)  # user neeeds to try again ,
                    else:
                        break
            return replay



    # generates a word to guess
    def generateWord(self, words, hint, randomNum):

        a = words[randomNum]

    def guessByLetter(self, answer, tries, toDisplay):
        # this method user picks a letter
        #  validate letter wheather its a vowel or consonant
        # tells the user if its right and the number of tries.
        # if guessed corectly user wins hangman ,
        # if not man is hanged
        # this needs to be in a while loop

        letters = ""
        print("Guess by letter , you have 9 tries, press 0 at any time to guess the whole world. ")
        correctGuess = []
        correctLetters = list(answer)
        totalGuessed =0
        for i in range(len(correctLetters)):
            correctGuess.append(" ")
        while tries < 9:
            letterGuessed = " "
            if letterGuessed == "0":
                self.guessWord(self,letterGuessed,answer,tries)



            #find size of correct letter , add enough placeholders to match both dictionary then use the index to update the display dict


            foundLetter = False
            index = -1
            # checks found letter against the correct lettrs.
            for i in range(len(answer)):
                index += 1
                if correctLetters[i].lower() == letterGuessed:
                    foundLetter = True
                    totalGuessed+=1
                    correctGuess[index] = correctLetters[index]


            # Further validation
            if foundLetter:

                for j in correctGuess:
                    letters += j
                print("Correct !! : {}".format(letters))
            else:
                tries += 1
                print("No Dice \n The man lost {} body parts".format(tries))
            if totalGuessed == len(correctLetters) :
                print("Congrats you Won or" )
            elif tries == 9:
                print("Ran out of tries!!!!")
                break

            # print("Play again ? y/n")
            # replay = input(">")
            # toDisplayLetter = ""
            # for i in correctGuess:
            #     toDisplayLetter += i
            # toDisplay[] = toDisplayLetter # update index 1 to show the letters

            return toDisplay


    def display(self,words,hint):
        toDisplay = [] # list to take in items that i will dynamically show.
        tries=0

        root = Tk()


        frame= tk.Frame(root, padx=7, pady=7)

        root.title("Hangman Game")
        frame.grid(column=0, row =0)
        root.grid_columnconfigure(2, weight=1)
        root.grid_rowconfigure(2, weight=1)

        toDisplay = self.playGame(self, words, hint,tries, toDisplay)
        print(toDisplay)


        lblInputName= tk.Label(frame, text=" Input: ")
        lblHintName = tk.Label(frame, text = "Hint: ")
        lblDisplayWord= tk.Label(frame, text=toDisplay[0])
        lblman= tk.Label(frame, text = " ")

        num=(toDisplay[1])
        num2 =int(toDisplay[1])
        print(num2)
        lblHintExplained = tk.Label(frame, text = hint[num2] )
        entryInput = tk.Entry(frame)
        btnSubmit = tk.Button(frame, text = "Save", background="Green")
        btnQuit = tk.Button(frame, text="Quit", background = "Red")
        btnShowRules = tk.Button(frame, text="Rules", command=self.show_rules)

        #pass what i need to change which is the man , the user guessed letters , and
        #list of TK objects







        lblHintName.grid(column=1, row=4)
        lblInputName.grid(column=1, row=5)
        lblDisplayWord.grid(column=2, row = 2)
        lblman.grid(column=2, row=3)
        lblHintExplained.grid(column=2, row=4)
        entryInput.grid(column=2,row=5)
        btnSubmit.grid(column = 3, row = 6)
        btnQuit.grid(column=4, row = 6)
        btnShowRules.grid(column=1, row=0)


        btnQuit.bind('<Button-1>', quit)
        btnShowRules.bind('<Button-3>',self.show_rules(self))



        # Events

        root.mainloop()

    def quit(event):
        SystemExit()

    def show_rules(self):
        answer= askokcancel(
            title = " Rules",
            message = '\nyou Get 7 Tries \n'
            '\n1 hint per word \n'
            '\nPress 1:Guess the whole word\n '
            '\nPress 2:Guess by Letter \n'
            '\nPress 3:To skip word \n'
            '\nPress 4 to end game\n'
            '\nnow let us Begin!!\n'
            '\n Default is guess by word'
        )















































