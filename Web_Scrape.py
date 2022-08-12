






#soup.select('td > th') all TD elements that are directly in a th element.
class Web_Scrape:
    import requests, bs4
    words = []
    hint  = []

    @classmethod
    def main(self):


        #ws = WebScrape() # instantiate class
        res = self.requests.get('http://atcomputingschool.co.uk/dictionary.html')
        res.raise_for_status()

        # bs4 is the web scraper,
        webpage= self.bs4.BeautifulSoup(res.text,'html.parser')

        self.scrape(webpage)



    @staticmethod
    def scrape(webpage):
        global words
        global hint
        words = []
        hint = []

        # find the tag by attribute value.
        name= webpage.select('th[scope="row"]')
        answer = webpage.select("tr > td")

        for i in range(len(name)):
            words.append(name[i].getText(strip=True))

        for j in  range (len(answer)):
            hint.append(answer[j].getText())






