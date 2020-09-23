import numpy as np
import pandas as pd

def set_header_from_first_row(df):
  df2 = df.copy()
  df2.columns = df2.iloc[0]
  df2 = df2.iloc[1:]
  return df2

def format_field(prepend: str, x : str):
    x = ' '.join(x.split()) #strip whitespace
    if str(x) != "nan" and str(x) != "":  #if not empty add
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


class EventFormatter:
    def __init__(self):
        self.events_emoji_map = {"WORKSHOP":u"💥", "TALK":u"💥", "HACKATHON": u"📈"}
        return

    def format_events(self, x):
        """
        Inputs: Takes in rows of the EVENTS Database
        Outputs: Produces a human readable formatting of each job posting
        """
        formatted_str = events_emoji_map.get(x[3], u"💥") #emoji
        formatted_str += format_field("", x[4]) #organisation
        formatted_str += format_field(" - ", x[5]) #title
        formatted_str += format_field(" - ", x[6]) #date start
        if x[6][:14] == x[7][:14]:
            formatted_str += format_field("-", x[7][15:]) #date end
        else:
            formatted_str += format_field("-", x[7])
        formatted_str += format_field("\n",x[8]) #description
        formatted_str += format_field("\nNB: ",x[9]) #notes
        formatted_str += format_field("\nhttps://link.kszk.eu/events", x[0])
        
        return formatted_str

if __name__ == '__main__':
    #test for events
    events_test_df = pd.read_csv("test_data/Opportunities post - EVENTS.csv")
    events_test_df = events_test_df[~events_test_df['ID'].isna()]
    events_test_df['ID']= events_test_df['ID'].astype(int)
    print("\n\n".join([format_events(x) for x in events_test_df.values]))

    #test for jobs
    jobs_test_df = pd.read_csv("test_data/Opportunities post - JOBS.csv")
    jobs_test_df = jobs_test_df[~jobs_test_df['ID'].isna()]
    jobs_test_df['ID']= jobs_test_df['ID'].astype(int)
    print("\n\n".join([format_jobs(x) for x in jobs_test_df.values]))
