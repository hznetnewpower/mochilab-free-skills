# 面向决策的会前准备

## 能做什么

整理有明确决策目标的议程，检查时间分配并列出需要补充的问题。

## 操作流程

按需要达成的决定设计议题，为每项分配分钟数，并核对总时长是否超额。超时要提出删减或书面跟进方案，背景信息应有资料依据。检查生成的会前简报是否明确讨论材料、决定和负责人；它不是会议纪要，也不会获取参会者私有资料或发邀请。

## 输入示例（虚构）

```json
{
  "title": "Fictional planning review",
  "minutes": 30,
  "agenda": [
    {
      "topic": "Choose next milestone",
      "minutes": 20,
      "decision": "Select one option"
    },
    {
      "topic": "Open questions",
      "minutes": 15
    }
  ]
}
```

## 输出与核对

在当前工作区生成报告及适用的产物，保留原文件。以返回结果、产物和具体检查范围为准；实时服务、远程账户操作和视觉效果需分别验证。

轻量部署包已默认安装 Skills 助手。在 MochiBot“设置 → MochiLab Skills 账户”验证并连接后，发送：

```text
安装 mochi-meeting-prep
```

其他环境先[连接 Skills 助手](https://mochilab.bz/Skills/Connect.aspx?lang=zh-CN)。连接成功后不用在聊天里提供密钥。每个工作区分别连接，可使用同一个已授权会员账户。本 Skill 免费，运行本地辅助脚本需要 Python3.10+。
