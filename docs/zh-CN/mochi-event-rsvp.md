# 活动报名与人数核对

## 能做什么

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

## 输出与核对

在当前工作区生成报告及适用的产物，保留原文件。以返回结果、产物和具体检查范围为准；实时服务、远程账户操作和视觉效果需分别验证。

轻量部署包已默认安装 Skills 助手。在 MochiBot“设置 → MochiLab Skills 账户”验证并连接后，发送：

```text
安装 mochi-event-rsvp
```

其他环境先[连接 Skills 助手](https://mochilab.bz/Skills/Connect.aspx?lang=zh-CN)。连接成功后不用在聊天里提供密钥。每个工作区分别连接，可使用同一个已授权会员账户。本 Skill 免费，运行本地辅助脚本需要 Python3.10+。
