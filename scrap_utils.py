from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import threading
import AI_thingies

options = Options()
options.add_argument("--headless")  # makes the browser inivisible wow
flag = False #checking which mode of the HTML it is in

Amazon_base_query = "https://www.amazon.in/s?k={}"
Amazon_base_url = "https://www.amazon.in"

Flipkart_base_query = "https://www.flipkart.com/search?q={}"
Flipkart_base_url = "https://www.flipkart.com"

Blinkit_base_query = "https://blinkit.com/s/?q={}"
Blinkit_base_url = "https://blinkit.com/prn"

Zepto_base_query = "https://www.zeptonow.com/search?query={}"
Zepto_base_url = "https://www.zeptonow.com"

Dunzo_base_query = "https://www.zeptonow.com/search?query={}"
Dunzo_base_url = "https://www.dunzo.com"



#AMAAZONNN DONEEE MFFFFFPGOIWEGOP DON"T TOUCH PLS
def get_amazon(query):
    driver = webdriver.Chrome(options= options)
    URL = Amazon_base_query.format(query)  #creating da URL
    driver.get(URL)
    titles = []
    prices = []
    links = []
    ratings = []
    img_urls = []
            
    result = BeautifulSoup(driver.page_source, "html.parser") #getting the page HTML
    # with open("rm_htmlincase/WHYT.html", "w", encoding="UTF-8") as file:
    #     file.write(str(result))   #writing it to a file for MAYBE mayhapps perhaps even debugging

    TLI = result.findAll('a', attrs={"class":"a-link-normal s-no-outline"}) #for Title, Links, IMG_LINK
    P = result.findAll('a',attrs={"class":"a-link-normal s-no-hover s-underline-text s-underline-link-text s-link-style a-text-normal"}) #for PRICE
    R = result.findAll("div", attrs={"class":"a-row a-size-small"}) #FOR RATINGS

    for tem1 in TLI:
        if "Save up to" not in tem1.find("img").get("alt") and "aax-eu.amazon" not in tem1.get("href"):
            titles.append((tem1.find("img").get("alt")))  #GETTING TITLES FOR EVERYTHING FINALLY
            links.append(Amazon_base_url+tem1.get("href")) #GETTING MATCHING LINKS FOR EVERYTHING FINALLY
            img_urls.append((tem1.find("img").get("src"))) #GETTING MATCHING IMG URLS

    #GETTING MATCHING PRICES GIWHGIOWEGOIHWEGOPIWEGIOWHGIJEIJWEIJOWEGOIJOWEIJOEWIJOEIJOEFJIPWW{}  
    prices = [None] * len(titles)
    for tem2 in P:
        price = tem2.find("span", attrs = {"class":"a-price-whole"})
        hrf = Amazon_base_url+ tem2.get("href")
        for link in links:
            if hrf == link:
                idx = links.index(hrf)
                prices[idx] = price.text

    #OGIWHGIOPWEGPIOWEGPOIWEGOPIWEGHPOWEIGIOPh
    ratings = [None] * len(titles)
    for tem3 in R:
        rating =  ((tem3.find("a", attrs = {"class":"a-popover-trigger a-declarative"}).text).split(" "))[0]
        hrf = Amazon_base_url+tem3.find("a", attrs = {"class":"a-link-normal s-underline-text s-underline-link-text s-link-style"}).get("href").replace("#customerReviews",'')
        for link in links:
            if hrf == link:
                
                idx = links.index(hrf)
                ratings[idx] = rating

    product_list = make_list(zip(titles ,prices ,ratings ,links ,img_urls), "amaflip")           
    print(len(prices),"|",len(titles),"|",len(links),"|",len(ratings),"|",len(img_urls))               

    return product_list    

#it works idk how
def get_flipkart(query):
    driver = webdriver.Chrome(options=options)
    URL = Flipkart_base_query.format(query)  # creating da URL
    driver.get(URL)
    
    titles = []
    prices = []
    links = []
    ratings = []
    img_urls = []

    result = BeautifulSoup(driver.page_source, "html.parser")  # getting the page HTML

    # with open("rm_htmlincase/WHYT.html", "w", encoding="UTF-8") as file:
    #     file.write(str(result))  # writing it to a file for MAYBE mayhapps perhaps even debugging

    if result.findAll("a", attrs={"class": "wjcEIp"}) != []:
        # proices
        prices = [(price.text).replace("₹", "") for price in result.findAll("div", attrs={"class": "Nx9bqj"})]
        # Da name
        titles = [thing.get("title") for thing in result.findAll("a", attrs={"class": "wjcEIp"})]
        # da links from HREF
        links = [(Flipkart_base_url + thing.get("href")) for thing in result.findAll("a", attrs={"class": "wjcEIp"})]
        print("is it coming here")
    else:
        # proices
        prices = [(price.text).replace("₹", "") for price in result.findAll("div", attrs={"class": "Nx9bqj _4b5DiR"})]
        # Da name
        titles = [title.text for title in result.findAll("div", attrs={"class": "KzDlHZ"})]
        # da links from HREF
        links = [(Flipkart_base_url + thing.get("href")) for thing in result.findAll("a", attrs={"class": "CGtC98"})]
        print("OR here")

    # DA ratings
    ratings = [rating.text for rating in result.findAll("div", attrs={"class": "XQDdHH"})]

    img_urls = [thing.get("src") for thing in result.findAll("img", attrs={"class": "DByuf4"})]
    print(len(prices), "|", len(titles), "|", len(links), "|", len(ratings), "|", len(img_urls))

    product_list = make_list(zip(titles ,prices ,ratings ,links ,img_urls), "amaflip")           

    return product_list    

#THIS ALSO WORKSSSSS
def get_zepto(query):
    driver = webdriver.Firefox(options=options)
    URL = Zepto_base_query.format(query)  #creating da URL
    driver.get(URL)
    titles = []
    prices = []
    links = []
    weights = []
    img_urls = [] 

    driver = ZEPTO_LOCATION_BUTTON(driver=driver) #PUTTING THE STUPID LOCATION ONG
    time.sleep(2)
    results = BeautifulSoup(driver.page_source, "html.parser") #getting the page HTML

    titles = [thing.text for thing in results.findAll("div", attrs={"class":"mt-2"})]
    prices = [((thing.text).replace("₹","")).strip() for thing in results.findAll("h4", attrs={"data-testid":"product-card-price"})]
    weights =[(thing.text).replace("g","") for thing in results.findAll("span", attrs={"data-testid":"product-card-quantity"})]
    links = [Zepto_base_url+thing.get('href') for thing in results.findAll("a", attrs={"data-testid":"product-card"})]
    img_urls = [thing.get("src") for thing in results.findAll("img", attrs={"data-testid":"product-card-image"})]

    product_list = make_list(zip(titles, prices, weights, links, img_urls), "zekit")
    print(len(titles),"|",len(prices),"|",len(weights),"|",len(links),"|",len(img_urls))
    
    return product_list

#BLINKIT WORKING
def get_blinkit(query):
    driver = webdriver.Firefox(options=options)
    URL = Blinkit_base_query.format(query)  #creating da URL
    driver.get(URL)
    titles = []
    prices = []
    links = []
    weights = []
    img_urls = [] 

    driver = BLINKIT_LOCATION(driver=driver) #putting the location

    time.sleep(1)
    results = BeautifulSoup(driver.page_source, "html.parser") #getting the page HTML
    with open("rm_htmlincase/WHYT.html", "w", encoding="UTF-8") as file:
        file.write(str(results)) 

    titles = [thing.text for thing in results.findAll("div", attrs={"class":"Product__UpdatedTitle-sc-11dk8zk-9 hxWnoO"})]
    prices = [((thing.text).replace("₹",'')).strip() for thing in results.findAll("div",attrs = {"style":"color: rgb(31, 31, 31); font-weight: 600; font-size: 12px;"})]
    img_urls = [thing.get("src") for thing in results.findAll("img", attrs={"loading":"lazy"})]
    links = [Blinkit_base_url+(thing.get("href")) for thing in results.findAll("a", attrs={"data-test-id":"plp-product"})]

    weights = [(thing.text).replace("g",'') for thing in results.findAll("div", attrs={"style":"align-items: center; display: flex; height: 26px; width: 100%;"})]

    product_list = make_list(zip(titles, prices, weights, links, img_urls),"zekit")
    print(len(titles),"|",len(prices),"|",len(img_urls),"|",len(links),"|", len(weights))
    
    return product_list

#DONE FOR ALL
def make_list(pinfos, website):
    print("entered making list")
    global flag
    info = []
    
    for title ,price ,rating ,link ,img_url in pinfos:
        if price != None:
            temp = {
                "name": title,
                "price": float((price.replace(",", '') if ',' in price else price)),
                "rating":rating,
                "image_url":img_url,
                "prd_link":link,
                "fin_rating":"0",
                "website":website
                }
            info.append(temp)
    print("exiting making list")
    return info

#puts user location
def ZEPTO_LOCATION_BUTTON(driver):

    time.sleep(1)
    for_button = driver.find_element(By.XPATH, "//div[@class='mt-4 flex']")
    buttonfr = for_button.find_element(By.XPATH, "//button[@data-testid = 'manual-address-btn']")
    buttonfrfr = buttonfr.find_element(By.XPATH,"//p[@class = 'font-norms block font-light text-xs !text-sm !font-medium !tracking-[0.5px]']")
    driver.execute_script("arguments[0].click();", buttonfrfr) #normal buttonfrfr.click() won't work idk why 
    print(buttonfr)

    loc_bar = driver.find_element(By.XPATH, "//input[@class = 'focus:outline-none block py-3 mx-2 appearance-none font-subtitle flex-grow font-normal bg-transparent text-md !text-sm']")
    loc_bar.send_keys("banglore")
    pls_click = WebDriverWait(driver,10).until(
        EC.visibility_of_element_located((By.XPATH,"//h4[contains(@class,'font-heading text-lg tracking-wide line-clamp-1 mb-1 capitalize') and text() = 'Bangalore']"))
    )
    pls_click.click()
    
    continue_click = WebDriverWait(driver,10).until(
        EC.visibility_of_element_located((By.XPATH,"//div[contains(@class,'flex items-center justify-center') and text() = 'Confirm & Continue']"))
    )
    time.sleep(1)
    continue_click.click()
    return scroll(driver)

#puts user location
def BLINKIT_LOCATION(driver):
    loc = driver.find_element(By.NAME, "select-locality")
    loc.send_keys("banglore")
    time.sleep(1)
    loc.send_keys(Keys.BACK_SPACE)
    dropdown = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//div[contains(@class, 'LocationSearchList__LocationLabel') and text()='Bangalore, Karnataka, India']"))
    )
    dropdown.click()
    return scroll(driver)

#scrolls to get more content
def scroll(driver):
    i = 0
    for i in range(0,3):
        driver.execute_script("window.scrollBy(0, 2000);")
        time.sleep(0.5)
    return driver


