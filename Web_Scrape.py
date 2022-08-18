






#soup.select('td > th') all TD elements that are directly in a th element.



class Web_Scrape:
    import requests
    import bs4
    import random



    @classmethod
    def main(self):

        words = []
        hint = []
        gameWords = {}


        #ws = WebScrape() # instantiate class
        res = self.requests.get('http://atcomputingschool.co.uk/dictionary.html')
        res.raise_for_status()

        # bs4 is the web scraper,
        webpage= self.bs4.BeautifulSoup(res.text,'html.parser')


        self.scrape(webpage, words, hint)

        self.merge(self, words, hint, gameWords)

        print('Welcome to the Deadly Trap\n'
              '\nPlay for your Life !!! MUhahahahahahahah\n'
              '\nyou Get 7 Tries \n'
              '\n1 hint per word \n'
              '\nPress 1:Guess the whole word\n '
              '\nPress 2:Guess by Letter \n'
              '\nPress 3:To skip word \n'
              '\nPress 4 to end game\n'
              '\nnow let us Begin!!\n')
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


        return hint,words


    @staticmethod
    def merge(self,words, hint, gameWords ):
        # add values in a dictionary .
        counter=0

        for i in words:
            gameWords.update({i:hint[counter]})
            counter+=1



    def playGame(self,words, hint, tries):


        #checks to see if the user is in the middle of guessing , if not , pulls a word.
        if tries ==0:
            randomNum = self.random.randint(1, 87)
            answer = words[randomNum]
        else:
            pass




        while True:
            userAnswer= self.generateWord(self,words, hint, randomNum)

            if userAnswer =='1':
                replay = self.guessWord(self,userAnswer, answer,tries )
                if replay == "y":
                    self.playGame(self, words, hint)
                else:
                    print("Thank you for playing")
                    break
            elif userAnswer =='2':
                self.guessByLetter(self,answer,tries)
            elif userAnswer =='3':
                self.playGame(self,words,hint, 0)
            elif userAnswer == '4':
                print("Thank you for playing")
                break
            else:
                self.checkUserLetter()


    #this method validates user answer
    def guessWord(self,userAnswer, answer,tries):
        #this method validates the user answer
        # it starts by check if it is correct and if its not correct
        #     it adds to tries and give user the option to restart


        if userAnswer == answer:
            print("Congratulations !! you got it \n Do you want to keep playing (Y/N) ")
            replay= input('>').casefold()

        else:
            # regardless if this is fist atempt or not , the user gets to try again
            tries += 1
            userAnswer = input("Whole Word >")
            if userAnswer == answer:
                print("You got it !!!")
                return
            else:
                tries += 1
                print("Better luck next time\n "
                      "Try again ? (Y/N)")
                replay= input(">").lower()

                while tries <= 8:
                    if replay == "y":
                        print("Try again")
                        userAnswer = input(">")
                        if tries >"8":
                            print("Sorry , you ran out of tries")
                            return
                        else:
                            self.guessWord(self,userAnswer, answer,tries)# user neeeds to try again ,
                    else:
                        break
            return replay





    #generates a word to guess
    def generateWord(self,words, hint, randomNum):
        print("Hint:" + hint[randomNum] + "\n Answer: " + words[randomNum] + "\n" )
        # nAnswer: " + words[randomNum] + "\n")
        userAnswer = input('>')
        return userAnswer


    def guessByLetter(self, answer,tries):
        # this method user picks a letter
        #  validate letter wheather its a vowel or consonant
        # tells the user if its right and the number of tries.
        #if guessed corectly user wins hangman ,
        # if not man is hanged
        #this needs to be in a while loop.


        print("Guess by letter , you have {} triess".format(tries))
        correctGuess= []
        displayWord=""
        while tries < 9:
            letterGuessed = input(">").lower()
            #check agains words.
            correctLetters = list(answer)
            #boolean to check if letter is in list
            foundLetter= False
           #add the correct letter to a list to display the correct letters in order.
            for i in range(len(answer)):
                if correctLetters[i].lower() == letterGuessed and tries <9:
                    print("Tureeeeee")
                    foundLetter = True
                    break
                else:
                    foundLetter= False

#Validates the found letter , add it to
            if foundLetter:
                print("Correct !! : {}".format(correctLetters[i]))
                correctGuess.append(letterGuessed)
            else:
                tries += 1
                print("No Dice \n The man lost {} body parts".format(tries))



            # display the letters guessed in the correct place
            # print correct guess in the correct index. in the index where the worst is not correct add a space

            #populate the end of the list to make it equal to the actual answer
            # check the index and if it not === add a " "
            while (len(correctLetters)) > (len(correctGuess)):
                correctGuess.append(" ")



            count = 0
            letters =""
            displayCorrectLetterGuessed = ""

            for words in correctGuess:
                letters += words





































