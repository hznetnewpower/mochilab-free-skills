# Input contract

add: date, title, detail, status done|in-progress|blocked, evidence [source references], optional minutes 0..1440. report: from,to inclusive. Output includes selected records, grouped sections, recordedMinutes and recordsWithoutDuration. Add requires requestId.

Currency fields support CNY, USD, EUR, GBP, HKD, SGD, AUD, CAD, CHF and NZD with two decimal places. The sample is fictional. Copy it into an authorized workspace and replace its facts and dates before real use. Current-agent state is stored separately for each workspace. A duplicate requestId with identical input returns the prior result; reusing it with changed data returns an error. A busy lock means another operation is active: wait rather than removing its lock.
