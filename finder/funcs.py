from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from .models import Keyword,SearchResult,Agenda
from django.core.exceptions import ObjectDoesNotExist
from selenium.common.exceptions import NoSuchElementException


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument("user-agent=") # !!! User Agent kodunuzu giriniz


def sel():
    
    
    try:    
        keywords = Keyword.objects.all()
    except ObjectDoesNotExist:
        raise RuntimeError("Anahtar kelime bulunamadı.")
   
    
    browser = webdriver.Chrome(options=chrome_options)

    for key in keywords:
        
        url = f"https://eksisozluk.com/{key.keyword}"
        
        pageCount = 1
        
        try:
            browser.get(url)
            current_url = browser.current_url
        except:
            print("Bu arama için sonuç bulunamadı veya sayfaya erişilemiyor")
            
        
        
        while pageCount <= 3:
            
            newUrl = current_url + f"?p={str(pageCount)}"
            try:        
                browser.get(newUrl)
            except:
                print("Sayfa sayısı geçerli değil veya sayfaya erişilemiyor")
                
            time.sleep(3)
            
            try:
                publishers = browser.find_elements(by="css selector", value=".entry-author")
                contents = browser.find_elements(by="css selector", value=".content")
                publication_date = browser.find_elements(by="css selector", value=".entry-date.permalink")
              
            except NoSuchElementException:
                print("Element bulunamadı")
                  
            finally:
                browser.close()
            pageCount += 1
            
        
        

        for i in range(min(len(publishers), len(contents), len(publication_date))):
            
            
            results = SearchResult.objects.filter(publisher=publishers[i].text, publication_date=publication_date[i].text)
            
            
            
            if results.exists() :
                
                for result in results:
                    if result.newCounter == 4:
                        result.is_new = False
                        result.newCounter += 1
        
                    else:
                        result.newCounter += 1
                    result.save()
            
            else:
            
            
                SearchResult.objects.create(                  
                    
                    keyword = key,
                    publisher = publishers[i].text,
                    content = contents[i].text,
                    publication_date = publication_date[i].text,
                                
                    
            )
        
                    
        time.sleep(2)
        
    browser.close()
    
def cleaner():
    pass
    
def trends():
    
    userID = "" # X Kullanıcı adınızı giriniz
    password = "" # X Şifrenizi giriniz 
    
    browser = webdriver.Chrome(options=chrome_options)
    time.sleep(2)
    
    url = "https://x.com/i/flow/login"
    
    browser.get(url)
    time.sleep(5)
    
    try:
        userIdLayer = browser.find_element(by="css selector", value=".css-175oi2r.r-1roi411.r-z2wwpe.r-rs99b7.r-18u37iz")
        time.sleep(1) 
                                                    
        userIdLayer.send_keys(userID)
        time.sleep(4)
        
        nextButton = browser.find_element(by="xpath", value="//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/button[2]/div")
        time.sleep(1)
        
        nextButton.click()
        time.sleep(5)
        
        
        forclick = browser.find_element(by="css selector", value=".r-4qtqp9.r-yyyyoo.r-dnmrzs.r-bnwqim.r-lrvibr.r-m6rgpd.r-18yzcnr.r-yc9v9c")
        time.sleep(1)
        
        forclick.click()
        time.sleep(1)
        
        passwordLayer = browser.find_element(by="css selector", value=".css-175oi2r.r-z2wwpe.r-rs99b7.r-18u37iz.r-vhj8yc.r-9cip40")
        time.sleep(1)
        
        passwordLayer.send_keys(password)   
        
    except NoSuchElementException:
        print("Element bulunamadı")
    finally:
        browser.close()
    try:
        passwordLayer.send_keys(Keys.ENTER)
        time.sleep(5)
    except:
        print("Element bulunamadı / Hesap adı veya şifre yanlış ")
    finally:
        browser.close()
    
      
    time.sleep(5)
    try:
        browser.get("https://x.com/explore/tabs/keyword")
    except:
        print("URL' nin mevcut olduğundan emin olunuz..")
    time.sleep(5)
    
    try:
        titles = browser.find_elements(by="css selector", value=".css-146c3p1.r-bcqeeo.r-1ttztb7.r-qvutc0.r-37j5jr.r-a023e6.r-rjixqe.r-b88u0q.r-1bymd8e")
        shares = browser.find_elements(by="css selector", value=".css-146c3p1.r-bcqeeo.r-1ttztb7.r-qvutc0.r-37j5jr.r-n6v787.r-1cwl3u0.r-16dba41.r-14gqq1x")
    except NoSuchElementException:
        print("Element bulunamadı")
    finally:
        browser.close() 
    
    time.sleep(2)
        

    for i in range(min(len(titles), len(shares))):
               
        agenda = Agenda.objects.create(                  
                                
                share = shares[i].text,
                title = titles[i].text,
                
        )
        
            
    browser.get("https://x.com/logout")
    time.sleep(5)
    
    logout = browser.find_element(by="css selector", value=".css-175oi2r.r-sdzlij.r-1phboty.r-rs99b7.r-lrvibr.r-16y2uox.r-6gpygo.r-1udh08x.r-1udbk01.r-3s2u2q.r-peo1c.r-1ps3wis.r-cxgwc0.r-1loqt21.r-o7ynqc.r-6416eg.r-1ny4l3l")
    time.sleep(1)
    
    logout.click()
    time.sleep(7)
    
    browser.close()