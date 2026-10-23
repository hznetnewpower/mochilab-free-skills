# Input contract

read/search: file (relative to current workspace), optional limit 1..200. read accepts start line. search requires query (literal normalized match). Supported text suffixes .txt .md .csv .tsv .json .log, UTF-8, up to 2 MiB. Output gives totalLines, matches, truncation and line-numbered text; long lines are flagged and truncated after 2000 characters.

Currency fields support CNY, USD, EUR, GBP, HKD, SGD, AUD, CAD, CHF and NZD with two decimal places. The sample is fictional. Copy it into an authorized workspace and replace its facts and dates before real use. Current-agent state is stored separately for each workspace. A duplicate requestId with identical input returns the prior result; reusing it with changed data returns an error. A busy lock means another operation is active: wait rather than removing its lock.
