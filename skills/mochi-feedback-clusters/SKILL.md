---
name: mochi-feedback-clusters
description: "Apply user-defined keyword topic labels to selected feedback and expose unmatched records without inferring private traits."
license: MIT-0
metadata: {"openclaw": {"requires": {"anyBins": ["python3", "python"]}}, "homepage": "https://mochilab.bz", "version": "1.0.1"}
---

# Customer Feedback Topic Map

Apply user-defined keyword topic labels to selected feedback and expose unmatched records without inferring private traits.

## Define an explainable topic vocabulary

Agree on topic names and keyword lists before grouping feedback. Use stable feedback IDs and only the text needed for this analysis. The matching rule is casefolded substring matching, so short keywords can accidentally match unrelated words and one record can require careful interpretation.

### Review ambiguous and unmatched records

Inspect representative items in each topic, records matching several topics and the unclassified group. Refine the vocabulary only when it reflects a real product distinction, and document the change so that period-to-period counts remain comparable.

Topic frequency is not sentiment, customer importance or the number of unique users. This helper does not perform semantic clustering, contact customers or upload their text. Return counts with the vocabulary, cutoff and known false positives. Preserve evidence for product decisions and do not turn a small supplied export into claims about the entire customer base.

## Reproducible request

topics: nonempty name-to-keyword-list map. feedback: id,text records. Matching is casefolded substring matching.

The following is fictional fixture data, not a live service result.

```json
{
  "topics": {
    "speed": [
      "slow",
      "latency"
    ],
    "billing": [
      "invoice"
    ]
  },
  "feedback": [
    {
      "id": "f1",
      "text": "slow response"
    },
    {
      "id": "f2",
      "text": "invoice question"
    },
    {
      "id": "f3",
      "text": "thanks"
    }
  ]
}
```

Use the [runner instructions](references/runner.md) to create and inspect real local outputs. The [input contract](references/input.md) records the supported fields. [中文操作说明](references/zh-CN.md) is separate; answer users in their own language.
