






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

        self.playGame(self, words, hint, gameWords)



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



    def playGame(self,words, hint, gameWords):


        tries = 0
        #for i in range(8):


        #while True:
        randomNum = self.random.randint(1, 87)
        print('Welcome to the Deadly Trap\n'
              'Play for your Life !!! MUhahahahahahahah'
              '\nyou Get 7 Tries '
              '\n1 hint per word '
              '\nif you want to guess the whole word , press 1.'
              '\nTo skip word pres 2'
              '\nPress 3 to end game'
              '\nnow let us Begin!!')


        answer = words[randomNum]

        print("Hint:" + hint[randomNum] +" \nAnswer: " + words[randomNum])








