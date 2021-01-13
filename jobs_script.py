import numpy as np
import pandas as pd
import time
from time import sleep
from datetime import datetime


def set_header_from_first_row(df):
  df2 = df.copy()
  df2.columns = df2.iloc[0]
  df2 = df2.iloc[1:]
  return df2

def format_field(prepend: str, x: str):
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
        formatted_str += format_field("\n", x[2])
        
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
        formatted_str += f" {format_field('', x[2])} |" #url
        
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
        formatted_str += format_field("\n", x[2])
        
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
        formatted_str += f"{format_field('', x[2])} |" #url
        formatted_str += f"{format_field('',x[10])} {format_field('',x[11])} | " #description - notes
        
        return formatted_str