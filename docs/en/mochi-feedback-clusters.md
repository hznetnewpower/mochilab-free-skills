# Customer Feedback Topic Map

## Define an explainable topic vocabulary

Agree on topic names and keyword lists before grouping feedback. Use stable feedback IDs and only the text needed for this analysis. The matching rule is casefolded substring matching, so short keywords can accidentally match unrelated words and one record can require careful interpretation.

### Review ambiguous and unmatched records

Inspect representative items in each topic, records matching several topics and the unclassified group. Refine the vocabulary only when it reflects a real product distinction, and document the change so that period-to-period counts remain comparable.

Topic frequency is not sentiment, customer importance or the number of unique users. This helper does not perform semantic clustering, contact customers or upload their text. Return counts with the vocabulary, cutoff and known false positives. Preserve evidence for product decisions and do not turn a small supplied export into claims about the entire customer base.

## Input example

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

This is transparent keyword grouping, not sentiment analysis or semantic clustering. Review ambiguous examples and false positives before making product decisions. No customer reply or external upload occurs.

The lightweight installer includes the Skills assistant. Connect your Skills account in MochiBot Settings, then send:

```text
Install mochi-feedback-clusters
```

For other deployments, first [connect the helper](https://mochilab.bz/Skills/Connect.aspx?lang=en). Do not provide keys in chat. Each workspace connects separately and authorized users may use the same membership account. This Skill is free; the local helper needs Python3.10+.
