# opportunities
A  CRUD web app to record opportunities (careers events, jobs, hackathons) posted in the society


This is an example table, there are two: JOBS and EVENTS which store a list of jobs posting and relevant events, and their associated information

![example table](docs/example_table.png)

The ```jobs_script.py``` produces formatted output from the table (ideally it should support a SELECT WHERE DATE_POSTED > x query) which can be posted in Zulip / Newsletter

![formatted output](docs/format_output.png)

The next step currently is a link shortener service, which will allow us to log number of clicks. currently each link needs to be added manually, with the user specificying the namespace (ideally it should be a hash instead of something like "events1")

![link shortener](docs/link_shortener.png)

## Development

Ideally the whole workflow should be integrated, an end user should be able to add a new events / job posting to the database via a front-end interface or API, the shortened link should be made automatically and there should be a ```/format_output``` method to print the unposted postings