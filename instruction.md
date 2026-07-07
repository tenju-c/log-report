There is an Apache-style access log file named `access.log` in the working directory. Analyze the log and create a JSON report containing a summary of the traffic.

Write the completed report to exactly:

`/app/report.json`

The report must be a valid JSON file containing the requested summary information.

Success criteria:

1. A JSON report is created at `/app/report.json`.

2. The report contains a `total_requests` field whose value is the total number of requests recorded in `access.log`.

3. The report contains a `unique_clients` field whose value is a list of all unique client IP addresses that appear in `access.log`.

4. The report contains a `popular_pages` field whose value is an object mapping requested page paths to the number of times each path appears in `access.log`.