
# soup.select('td > th') all TD elements that are directly in a th element.
import tkinter as tk
from tkinter import Tk

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
        dispInput, stickyMan, displayWord = " ", " " , " "

        # ws = WebScrape() # instantiate class
        res = requests.get('http://atcomputingschool.co.uk/dictionary.html')
        res.raise_for_status()

        # bs4 is the web scraper,
        webpage= bs4.BeautifulSoup(res.text ,'html.parser')


        self.scrape(webpage, words, hint)

        self.merge(self, words, hint, gameWords)

        #print( 'Welcome to the Deadly Trap\n'
             # '\nPlay for your Life !!! MUhahahahahahahah\n')
        tries = 0
        #self.playGame(self, words, hint, tries)
        self.display(self,dispInput,stickyMan,displayWord,words, hint)



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







    def playGame(self ,words, hint, tries):





        replay= ""
        playing = True
        # checks to see if the user is in the middle of guessing , if not , pulls a word.
        tries = 0
        randomNum = random.randint(1, 87)
        answer = words[randomNum]

        print(
            '\nyou Get 7 Tries \n'
            '\n1 hint per word \n'
            '\nPress 1:Guess the whole word\n '
            '\nPress 2:Guess by Letter \n'
            '\nPress 3:To skip word \n'
            '\nPress 4 to end game\n'
            '\nnow let us Begin!!\n'
            '\n Default is guess by word')






        while True:

            userAnswer= self.generateWord(self ,words, hint, randomNum)


            if userAnswer =='1':
                replay = self.guessWord(self ,userAnswer, answer ,tries )
                if replay == "y":
                    self.playGame(self, words, hint)
                else:
                    print("Thank you for playing")
                    break
            elif userAnswer =='2':
                replay=self.guessByLetter(self ,answer ,tries)
            elif userAnswer =='3':
                self.playGame(self ,words ,hint, 0)
            elif userAnswer == '4':
                print("Thank you for playing")
                break
            else:
                replay=self.guessWord(self,"1", answer, tries)

            if replay == "n":
                print("THank you for playing . ")
                break







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
        print("Hint:" + hint[randomNum])
        a = words[randomNum]


        userAnswer = input('>')
        return userAnswer

    def guessByLetter(self, answer, tries, DisplayObj):
        # this method user picks a letter
        #  validate letter wheather its a vowel or consonant
        # tells the user if its right and the number of tries.
        # if guessed corectly user wins hangman ,
        # if not man is hanged
        # this needs to be in a while loop
        print("Guess by letter , you have 9 tries, press 0 at any time to guess the whole world. ")
        correctGuess = []
        correctLetters = list(answer)
        totalGuessed =0
        for i in range(len(correctLetters)):
            correctGuess.append(" ")
        while tries < 9:
            letterGuessed = input(">").lower()
            if letterGuessed == "0":
                self.guessWord(self,letterGuessed,answer,tries)



            #find size of correct letter , add enough placeholders to match both dictionary then use the index to update the display dict


            foundLetter = False
            index = -1

            for i in range(len(answer)):
                index += 1
                if correctLetters[i].lower() == letterGuessed:
                    foundLetter = True
                    totalGuessed+=1
                    correctGuess[index] = correctLetters[index]


            # Validates the found letter , add it to
            if foundLetter:
                letters = ""
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

            print("Play again ? y/n")
            replay = input(">")

            return replay


    def display(self,input,stickyMan, displayWord,words,hint):
        root = Tk()
        frame= tk.Frame(root, padx=7, pady=7)
        root.title("Hangman Game")
        frame.grid(column=0, row =0)
        root.grid_columnconfigure(2, weight=1)
        root.grid_rowconfigure(2, weight=1)

        lblRules =tk.Label(frame, text = "awf")
        lblInputName= tk.Label(frame, text=" Input: ")
        lblHintName = tk.Label(frame, text = "Hint: ")
        lblDisplayWord= tk.Label(frame, text=displayWord)
        lblman= tk.Label(frame, text = " Placeholder")
        lblHintExplained = tk.Label(frame, text = "Placeholder")
        entryInput = tk.Entry(frame)





        lblRules.grid(column=1, row=2)
        lblHintName.grid(column=1, row=4)
        lblInputName.grid(column=1, row=5)
        lblDisplayWord.grid(column=2, row = 2)
        lblman.grid(column=2, row=3)
        lblHintExplained.grid(column=2, row=4)
        entryInput.grid(column=2,row=5)
        root.mainloop()

        self.playGame(self,words,hint=[],tries=0)










































