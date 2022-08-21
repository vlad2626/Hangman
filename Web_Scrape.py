
# soup.select('td > th') all TD elements that are directly in a th element.
from tkinter import Tk


class Web_Scrape:
    import requests
    import bs4
    import random
    from tkinter import ttk



    #create grint and frame
    root= Tk()
    frame = ttk.Frame(root, padding=(4,4,10,100))
    frame.grid(column=4, row = 4)
    root.grid_columnconfigure(0)
    root.grid_rowconfigure((0))



    @classmethod
    def main(self):

        words = []
        hint = []
        gameWords = {}

        # ws = WebScrape() # instantiate class
        res = self.requests.get('http://atcomputingschool.co.uk/dictionary.html')
        res.raise_for_status()

        # bs4 is the web scraper,
        webpage= self.bs4.BeautifulSoup(res.text ,'html.parser')


        self.scrape(webpage, words, hint)

        self.merge(self, words, hint, gameWords)

        print( 'Welcome to the Deadly Trap\n'
              '\nPlay for your Life !!! MUhahahahahahahah\n')
        tries = 0
        self.playGame(self, words, hint, tries)



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

        print(
              '\nyou Get 7 Tries \n'
              '\n1 hint per word \n'
              '\nPress 1:Guess the whole word\n '
              '\nPress 2:Guess by Letter \n'
              '\nPress 3:To skip word \n'
              '\nPress 4 to end game\n'
              '\nnow let us Begin!!\n'
            '\n Default is guess by word')

        # checks to see if the user is in the middle of guessing , if not , pulls a word.
        tries = 0
        randomNum = self.random.randint(1, 87)
        answer = words[randomNum]






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
                self.guessByLetter(self ,answer ,tries)
            elif userAnswer =='3':
                self.playGame(self ,words ,hint, 0)
            elif userAnswer == '4':
                print("Thank you for playing")
                break
            else:
                self.guessWord(self,"1", answer, tries)

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
                    elif replay == "y" and tries <= 9:
                            self.guessWord(self, userAnswer, answer, tries)  # user neeeds to try again ,
                    else:
                        break
            return replay

    # generates a word to guess
    def generateWord(self, words, hint, randomNum):
        print("Hint:" + hint[randomNum] + "\n Answer: " + words[randomNum] + "\n")
        # nAnswer: " + words[randomNum] + "\n")
        userAnswer = input('>')
        return userAnswer

    def guessByLetter(self, answer, tries):
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
                print("Correct !! : {}".format(correctGuess))
            else:
                tries += 1
                print("No Dice \n The man lost {} body parts".format(tries))
            if totalGuessed == len(correctLetters) :
                print("Congrats you Won or" )
            elif tries == 9:
                print("Ran out of tries!!!!")


            # display the letters guessed in the correct place
            # print correct guess in the correct index. in the index where the worst is not correct add a space
            # populate the end of the list to make it equal to the actual answer
            # check the index and if it not === add a " "

    root.mainloop()






































