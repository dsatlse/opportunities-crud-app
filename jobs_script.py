import numpy as np
import pandas as pd
import time
from time import sleep
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

def set_header_from_first_row(df):
  df2 = df.copy()
  df2.columns = df2.iloc[0]
  df2 = df2.iloc[1:]
  return df2

def format_field(prepend: str, x : str):
    x = ' '.join(str(x).split()) #strip whitespace and coerce to string
    if x != "nan" and x != "":  #if not empty add
        return prepend + x
    return ""

class JobFormatter:
    @staticmethod
    def format_jobs(x):
        """
        Inputs: Takes in rows of the JOBS Database
        Outputs: Produces a human readable formatting of each job posting
        """
        formatted_str = f"🤖 {x[3]}" #organisation name, emoji
        formatted_str += format_field(" - ", x[4]) #post name
        formatted_str += format_field(" - ", x[5]) #level
        formatted_str += format_field(" - ", x[6]) #location
        formatted_str += format_field("- Deadline: ",x[7]) #deadline
        formatted_str += format_field("\n",x[8]) #description
        formatted_str += format_field("\nhttps://link.kszk.eu/jobs", x[0])
        
        return formatted_str

    @staticmethod
    def format_jobs_markdown(x):
        """
        Inputs: Takes in rows of the JOBS Database
        Outputs: Produces a markdown table each job posting
        """
        formatted_str = ""
        formatted_str += f"| 🤖 {x[3]} {format_field(' - ', x[4])} | " #organisation
        formatted_str += f"{format_field('', x[5])} | " #level
        #date and time
        formatted_str += f" {format_field('', x[6])} | " #location
        formatted_str += f" {format_field('', x[8])} | " #description
        formatted_str += f" {format_field('https://link.kszk.eu/jobs', x[0])} |" #url
        
        return formatted_str


class EventFormatter:
    def __init__(self):
        self.events_emoji_map = {"WORKSHOP":u"💥", "TALK":u"💥", "HACKATHON/CHALLENGE": u"📈"}
        return

    def format_events(self, x):
        """
        Inputs: Takes in rows of the EVENTS Database
        Outputs: Produces a human readable formatting of each event posting
        """
        formatted_str = self.events_emoji_map.get(x[3], u"💥") #emoji
        formatted_str += format_field("", x[4]) #organisation
        formatted_str += format_field(" - ", x[5]) #title
        
        formatted_str += format_field(" - ", x[6]) #date start
        formatted_str += format_field(" ", x[7]) #time start
        if x[6] != x[8]:
            formatted_str += format_field("-", x[8]) #date end
            formatted_str += format_field(" ", x[9]) #time end
        else:
            formatted_str += format_field("-", x[9]) #time end
        
        formatted_str += format_field("\n",x[10]) #description
        formatted_str += format_field("\nNB: ",x[11]) #notes
        formatted_str += format_field("\nhttps://link.kszk.eu/events", x[0])
        
        return formatted_str

    def format_events_markdown(self, x):
        """
        Inputs: Takes in rows of the EVENTS Database
        Outputs: Produces a markdown table for the event posting
        """
        formatted_str = ""
        formatted_str += f"|{self.events_emoji_map.get(x[3], u'💥')} {format_field('', x[4])}{format_field(' - ', x[5])} | " #organisation - title
        formatted_str += f"{format_field('', x[3])} | " #type
        #date and time
        formatted_str += f"{format_field('', x[6])}{format_field(' - ', x[7])}"
        if x[6] != x[8]:
            formatted_str += f"{format_field('-', x[8])}{format_field(' ', x[9])} |"
        else:
            formatted_str += f"{format_field('-', x[9])} | "
        formatted_str += f"{format_field('https://link.kszk.eu/events', x[0])} |" #url
        formatted_str += f"{format_field('',x[10])} {format_field('',x[11])} | " #description - notes
        
        return formatted_str
        

def auto_add(config : dict, urls : list, prepend: str):
    assert("username" in config)
    assert("password" in config)

    options = webdriver.ChromeOptions()
    # options.add_argument('--headless')
    # options.add_argument('--no-sandbox')
    # options.add_argument('--disable-dev-shm-usage')
    # open it, go to a website, and get results
    driver = webdriver.Chrome('chromedriver',options=options)
    driver.get("https://link.kszk.eu/admin/")
    
    #login into portal
    try:
        element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "username")))
        element.clear()
        element.send_keys(config["username"])
    except:
        print("Failed to put username")
    try:
        element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "password")))
        element.clear()
        element.send_keys(config["password"])
        element.send_keys(Keys.RETURN)
    except:
        print("Failed to put password")

    for url in urls:
        try:
            element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "add-url")))
            element.clear()
            element.send_keys(url[0])
        except:
            print(f"Failed to put url: {url[0]}")
        try:
            element2 = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "add-keyword")))
            element2.clear()
            element2.send_keys(prepend + url[1])
            element2.send_keys(Keys.RETURN)
        except:
            print(f"Failed to put shortened name: {url[1]}")
        #timeout between urls
        time.sleep(1.5)
    driver.quit()
    return