import requests
from bs4 import BeautifulSoup as bs


class Scrapperr:

    def __init__(self,url):

        self.url = url
        self.data = None
        self.soup = None
        
     


    def conteti(self):
        r = requests.get('https://courtesyhealthservices.com/')
        self.soup = bs(r.content , 'html.parser')

           
        #this function gets all web contents typed
        code = r.status_code
        print(self)
        
        if code == 200:
            print("request gotten succesfull")
        else:
            print("process unseccsufull check the site or something else")

        details = self.soup.find_all.prettify1('p')

        for detail in details:
            print(detail.text)
    #this function gets all the links on the website
    #id say subdomains

    def linksFetcher(self):
        for links in self.soup.find_all('a'):
            print(links.get('href'))

       

    def Imagi(self):

        img_list=[]
        images = self.soup.select('img')
        for image in images:
            src =image.get("src")
            alt = image.get('alt')
            img_list.append({"src": src, "alt": alt})
        for image in img_list:
            print(image)

#adding another link for two or more
    def mapeji(self, num_pages):
        for page in range(1, num_pages + 1):
            url = f"{self.url}/{page}"
            r = requests.get(url)
            data = r.content
            pages = bs(data, 'html.parser')
            print("===================================================================================")
            print("===================================================================================")
            print("===================================================================================")

            print(pages)

            print("===================================================================================")
            print("===================================================================================")
            print("===================================================================================")

#url = 'https://courtesyhealthservices.com/'
url = input('please enter the url needed for enumeration :')
scraper =Scrapperr(url)
scraper.conteti()
def option_list(scraper):
    print("1. Fetch Content")
    print("2. Get Links")
    print("3. Get Images")
    print("4. Scrape Multiple Pages")
    print("5. Quit")

    while True:
        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            scraper.conteti()
      
        elif choice == '2':
            scraper.linksFetcher()
        elif choice == '3':
            scraper.Imagi()
        elif choice == '4':
            num_pages = int(input("Enter the number of pages to scrape: "))
            scraper.mapeji(num_pages)
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")


option_list(scraper)