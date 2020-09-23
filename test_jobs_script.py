import job_scripts

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
