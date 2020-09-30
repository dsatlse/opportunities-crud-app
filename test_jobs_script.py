import pandas as pd
from jobs_script import *

if __name__ == '__main__':
    #test for events
    events_test_df = pd.read_csv("test_data/test_events.csv")
    events_test_df = events_test_df[~events_test_df['ID'].isna()]
    events_test_df['ID']= events_test_df['ID'].astype(int)
    # print(events_test_df)
    event_formatter = EventFormatter()
    print("\n\n".join([event_formatter.format_events(x) for x in events_test_df.values]))
    print("\n\n")
    print("\n".join([event_formatter.format_events_markdown(x) for x in events_test_df.values]))

    #test for jobs
    jobs_test_df = pd.read_csv("test_data/test_jobs.csv")
    jobs_test_df = jobs_test_df[~jobs_test_df['ID'].isna()]
    jobs_test_df['ID']= jobs_test_df['ID'].astype(int)
    job_formatter = JobFormatter()
    print("\n\n".join([job_formatter.format_jobs(x) for x in jobs_test_df.values]))
    print("\n\n")
    print("\n".join([job_formatter.format_jobs_markdown(x) for x in jobs_test_df.values]))
