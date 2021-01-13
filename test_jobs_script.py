import pandas as pd
from jobs_script import set_header_from_first_row, format_field, JobFormatter, EventFormatter

events_test_df = pd.read_csv("test_data/test_events.csv")
events_test_df = events_test_df[~events_test_df['ID'].isna()]
events_test_df['ID']= events_test_df['ID'].astype(int)

jobs_test_df = pd.read_csv("test_data/test_jobs.csv")
jobs_test_df = jobs_test_df[~jobs_test_df['ID'].isna()]
jobs_test_df['ID']= jobs_test_df['ID'].astype(int)

FIELD_NAMES = ['ID','DATE_ADDED','URL','TYPE',
               'ORGANISATION','NAME','EVENT_START',
               'TIME_START','EVENT_END','TIME_END',
               'DESCRIPTION','NOTES','NEWSLETTER']

def test_set_header_from_first_row_events():
    assert list(events_test_df.values[0]) != FIELD_NAMES

def test_set_header_from_first_row_jobs():
    assert list(events_test_df.values[0]) != FIELD_NAMES
    

def test_event_formatter_text():
    event_formatter = EventFormatter()
    output = "\n\n".join([event_formatter.format_events(x) for x in events_test_df.values])
    true_output = """💥Women in Tech York - Code your way out of a paper bag using Genetic Algorithms - 08/10/2020 18:30:00-20:30:00
NB: An introduction to genetic algorithms which are useful machine learning/evolutionary computing technique for solving problems that take too long to brute force
https://www.eventbrite.co.uk/e/code-your-way-out-of-a-paper-bag-using-genetic-algorithms-tickets-122579607907

💥Flow Traders - Trading Challenge - 06/10/2020 18:30-20:00
https://careers.lse.ac.uk/students/events/Detail/667792/external-event-flow-traders-tr

💥Optiver - Company Presentation - 06/10/2020 17:00-19:00
https://careers.lse.ac.uk/students/events/Detail/666895/company-presentation-with-opti

📈MIT - Energy Hack
https://www.mitenergyhack.org/

📈Facebook - Developer Circles Community Challenge
NB: Challenge to make a tutorial on a Facebook technology - Pytorch, React, Docusaurus etc.
https://developercircles2020.devpost.com/"""
    assert output == true_output

def test_event_formatter_md():
    event_formatter = EventFormatter()
    output = "\n".join([event_formatter.format_events_markdown(x) for x in events_test_df.values])
    print(output)
    true_output = """|💥 Women in Tech York - Code your way out of a paper bag using Genetic Algorithms | TALK | 08/10/2020 - 18:30:00-20:30:00 | https://www.eventbrite.co.uk/e/code-your-way-out-of-a-paper-bag-using-genetic-algorithms-tickets-122579607907 | An introduction to genetic algorithms which are useful machine learning/evolutionary computing technique for solving problems that take too long to brute force | 
|💥 Flow Traders - Trading Challenge | TALK | 06/10/2020 - 18:30-20:00 | https://careers.lse.ac.uk/students/events/Detail/667792/external-event-flow-traders-tr |  | 
|💥 Optiver - Company Presentation | TALK | 06/10/2020 - 17:00-19:00 | https://careers.lse.ac.uk/students/events/Detail/666895/company-presentation-with-opti |  | 
|📈 MIT - Energy Hack | HACKATHON/CHALLENGE |  |https://www.mitenergyhack.org/ |  | 
|📈 Facebook - Developer Circles Community Challenge | HACKATHON/CHALLENGE |  |https://developercircles2020.devpost.com/ | Challenge to make a tutorial on a Facebook technology - Pytorch, React, Docusaurus etc. | """
    assert output == true_output

def test_job_formatter_text():
    job_formatter = JobFormatter()
    output = "\n\n".join([job_formatter.format_jobs(x) for x in jobs_test_df.values])
    true_output = '''🤖 Wood Mackenzie - Research - Internship - London
https://jobs.smartrecruiters.com/Verisk/743999720466699-research-internship-2021-summer-internship-program-cr

🤖 Wood Mackenzie - Data Science - Internship - Edinburgh
https://jobs.smartrecruiters.com/Verisk/743999720481561-data-science-intern-2021-summer-internship-program-cr

🤖 Facebook - Data Engineering - Internship
https://www.facebook.com/careers/jobs/1048869635527518/

🤖 Facebook - Data Scientist-Infrastructure Strategy - Internship
https://www.facebook.com/careers/jobs/2828872594063384/

🤖 Facebook - Data Scientist-Analytics - Internship
https://www.facebook.com/careers/jobs/3733844406643478/'''
    assert output == true_output

def test_job_formatter_md():
    job_formatter = JobFormatter()
    output = "\n".join([job_formatter.format_jobs_markdown(x) for x in jobs_test_df.values])
    true_output = """| 🤖 Wood Mackenzie  - Research | Internship |  London |   |  https://jobs.smartrecruiters.com/Verisk/743999720466699-research-internship-2021-summer-internship-program-cr |
| 🤖 Wood Mackenzie  - Data Science | Internship |  Edinburgh |   |  https://jobs.smartrecruiters.com/Verisk/743999720481561-data-science-intern-2021-summer-internship-program-cr |
| 🤖 Facebook  - Data Engineering | Internship |   |   |  https://www.facebook.com/careers/jobs/1048869635527518/ |
| 🤖 Facebook  - Data Scientist-Infrastructure Strategy | Internship |   |   |  https://www.facebook.com/careers/jobs/2828872594063384/ |
| 🤖 Facebook  - Data Scientist-Analytics | Internship |   |   |  https://www.facebook.com/careers/jobs/3733844406643478/ |"""
    assert output == true_output
