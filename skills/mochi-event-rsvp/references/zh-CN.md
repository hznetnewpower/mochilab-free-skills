# 活动报名与人数核对

根据明确报名状态核对实际参加人数、同行人数及餐食数量，提示超出容量。

## 操作流程

用稳定人员 ID 和明确截止时间核对 yes、no、maybe、pending 状态。肯定回复应按 partySize 计算座位，不能把一家人的回复当成一人。确认人数与容量、餐食分别核对，待定回复单列；公开汇总不要暴露联系方式、个人饮食身份或完整名单，也不会自动催回复。

## 输入示例（虚构）

```json
{
  "capacity": 2,
  "people": [
    {
      "id": "a",
      "status": "yes",
      "partySize": 2,
      "meal": "standard"
    },
    {
      "id": "b",
      "status": "yes",
      "meal": "vegetarian"
    },
    {
      "id": "c",
      "status": "maybe"
    }
  ]
}
```

本地处理方法见 runner.md，字段说明见 input.md。仅处理当前工作区，保留原文件，按真实输出核对结果；涉及联网、账户或发布的操作另行执行和验证。
