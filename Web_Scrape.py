
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





        toDisplay= self.guessByLetter(self, answer, tries,toDisplay)
        return toDisplay




    # this method validates user answer
    def guessWord(self,entry, toDisplay, answer, frame):

        wonGame=False

        if entry == answer:
            askokcancel(title="Winner", message = " Congratulations Winner")
            wonGame
        else:
            askokcancel(title="Loser", message="Loooooserrrrr")



    # generates a word to guess
    def generateWord(self, words, hint, randomNum):

        a = words[randomNum]

    def guessByLetter(self, entry,toDisplay, answer, frame):
        letters = " "
        correctGuess = []
        correctLetters = list(answer)
        totalGuessed =0
        for i in range(len(correctLetters)):
            correctGuess.append(" ")


            foundLetter = False
            index = -1
            # checks found letter against the correct lettrs.
            for i in range(len(answer)):
                index += 1
                if correctLetters[i].lower() == entry:
                    foundLetter = True
                    totalGuessed+=1
                    correctGuess[index] = correctLetters[index]


            # Further validation
            if foundLetter:
                for j in correctGuess:
                    letters += j
                print("Correct !! : {}".format(letters))

            if totalGuessed == len(correctLetters) :
                print("Congrats you Won or" )

            return correctGuess


    def display(self,words,hint):
        toDisplay = [] # list to take in items that i will dynamically show.
        tries=0

        randomNum = random.randint(1, 87)
        answer = words[randomNum]
        hints = hint[randomNum]

        root = Tk()

        toDisplay.append("        ")  # initialize
        frame= tk.Frame(root, padx=7, pady=7)

        root.title("Hangman Game")
        frame.grid(column=0, row =0)
        root.grid_columnconfigure(2, weight=1)
        root.grid_rowconfigure(2, weight=1)




        lblInputName= tk.Label(frame, text=" Input: ")
        lblHintName = tk.Label(frame, text = "Hint: ")
        lblDisplayWord= tk.Label(frame, text=toDisplay[0])
        lblman= tk.Label(frame, text = " ")


        lblHintExplained = tk.Label(frame, text = hint[randomNum] )
        entryInput = tk.Entry(frame)
        btnSkip = tk.Button(frame, text="Skip", command=lambda : self.skip(self, words, hint, randomNum))
        btnMode = tk.Button(frame, text = "Whole word", command= lambda :self.mode(self, btnMode, frame ))



        mode = btnMode.cget("text")
        btnSubmit = tk.Button(frame, text = "Submit", background="Green", command=lambda : self.validate(self, entryInput,toDisplay,answer, frame,mode))
        btnQuit = tk.Button(frame, text="Quit", background = "Red")
        btnShowRules = tk.Button(frame, text="Rules")

        #pass what i need to change which is the man , the user guessed letters , and
        #list of TK objects

        btnQuit.bind('<Button-1>', self.quitGame)
        btnShowRules.bind('<Button-1>', self.showRules)
        #btnSubmit.bind('<Button-1>', self.validate(self,entryInput))
        btnSkip.bind('<1>', self.skip)



        lblHintName.grid(column=1, row=4)
        lblInputName.grid(column=1, row=5)
        lblDisplayWord.grid(column=2, row = 2)
        lblman.grid(column=2, row=3)
        lblHintExplained.grid(column=2, row=4)
        entryInput.grid(column=2,row=5)



        btnSkip.grid(column=2, row=6)
        btnSubmit.grid(column = 3, row = 6)
        btnQuit.grid(column=4, row = 6)
        btnShowRules.grid(column=1, row=0)
        btnMode.grid(column=1, row=1)








        # Events

        root.mainloop()

    def mode(self, btnMode, frame):
        textMode = btnMode.cget("text")

        if textMode == "Whole word":
            btnMode.config(text="By Letter")
            mode = "By letter"
        else:
            btnMode.config(text="Whole word")

        return textMode

    def quitGame(self):
        askokcancel(title="Quit game", message="Quit doenst work yet")

    def validate(self, entryInput,toDisplay,answer, frame,mode):
        askokcancel(message=mode)
        entry = entryInput.get()
        if mode == "By Letter":
           toDisplay[0]=self.guessByLetter(self,entry,toDisplay, answer, frame)
        else:
          toDisplay[0]=self.guessWord(self, entry, toDisplay, answer, frame)
        return toDisplay[0]






    def skip(self, word, hint, randomNum):
        print(" waiting to code")



    def showRules(self):
        answer= askokcancel(
            title = " Rules",
            message = '\nyou get 7 Tries \n'
            '\n1 hint per word \n'
            '\nPress 1:Guess the whole word\n '
            '\nPress 2:Guess by Letter \n'
            '\nPress 3:To skip word \n'
            '\nPress 4 to end game\n'
            '\nnow let us Begin!!\n'
            '\n Default is guess by word\n'
            "Press 0 to guess by the letter"
        )















































