Read the Apache-style access log at /app/access.log and write the summary to
/app/report.json. Do not modify the input log.

1. The output must be a valid JSON object with exactly three keys. total_requests
   and unique_ips must be integers, and top_path must be a string.
2. total_requests must equal the number of nonempty log records. unique_ips must
   equal the number of distinct client IP addresses in the first column.
3. top_path must equal the request-target path that appears most often in the log.

You have 120 seconds to complete this task. Do not cheat by using online solutions or hints specific to this task.
