






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
              '\nPress 2:To skip word \n'
              '\nPress 3 to end game\n'
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
                self.playGame(self,words,hint)
            elif userAnswer == '3':
                break
            else:
                self.checkUserLetter()

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
                replay= input(">").casefold()

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






    def generateWord(self,words, hint, randomNum):
        print("Hint:" + hint[randomNum] + " \nAnswer: " + words[randomNum] + "\n")
        userAnswer = input('>')
        return userAnswer












