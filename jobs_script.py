import numpy as np
import pandas as pd

def format_jobs(x):
	"""
	Inputs: Takes in rows of the JOBS database
	Outputs: Produces a human readable formatting of each job posting
	"""

	#formatted_str must contain name
	formatted_str = f"🤖 {x[3]} - {x[4]}"
	#location
	if str(x[5]) != "nan" and str(x[5]) != "":
		formatted_str += f" - {x[5]}"
	#deadline
	if str(x[6]) != "nan" and str(x[6]) != "":
		formatted_str += f" | {x[6]}"
	#url - using link shortener
	if str(x[2]) != "nan":
		formatted_str += f"\nhttps://link.kszk.eu/jobs{x[0]}"
	#description 
	if str(x[7]) != "nan" and str(x[7]) != "":
		formatted_str += f"\n{x[7]}"
	return formatted_str

def format_events(x):
	"""
	Inputs: Takes in rows of the EVENTS Database
	Outputs: Produces a human readable formatting of each job posting
	"""
	formatted_str = ""
	if x[3] == "WORKSHOP" or x[3] == "TALK":
		formatted_str += "💥 "
	else:
		formatted_str += "📈 "

	formatted_str += f"{x[4]}"
	if str(x[5]) != "nan" and str(x[5]) != "":
		formatted_str += f" - {x[5]}"
	if str(x[6]) != "nan" and str(x[6]) != "":
		formatted_str += f"-{x[6]} "
	if str(x[7]) != "nan" and str(x[7]) != "":
		formatted_str += f"\n{x[7]}"
	if str(x[8]) != "nan" and str(x[8]) != "":
		formatted_str += f"\nNB: {x[8]}"
	if str(x[2]) != "nan" and str(x[2]) != "":
		formatted_str += f"\nhttps://link.kszk.eu/events{x[0]}"
	
	
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
