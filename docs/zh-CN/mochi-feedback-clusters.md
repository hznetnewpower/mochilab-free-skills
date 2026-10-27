# 客户反馈主题整理

## 能做什么

按用户指定的关键词主题整理反馈，支持多标签并保留未归类项，不臆测个人属性。

## 操作流程

先约定主题和关键词，再按稳定反馈 ID 处理必要文本。匹配是忽略大小写的子串规则，应抽查多主题命中、误命中和未分类项，并记录词表变更。主题频率不是情绪、客户重要性或独立用户数，不能用少量导出代表所有客户，也不会自动回复或上传反馈。

## 输入示例（虚构）

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

## 输出与核对

在当前工作区生成报告及适用的产物，保留原文件。以返回结果、产物和具体检查范围为准；实时服务、远程账户操作和视觉效果需分别验证。

轻量部署包已默认安装 Skills 助手。在 MochiBot“设置 → MochiLab Skills 账户”验证并连接后，发送：

```text
安装 mochi-feedback-clusters
```

其他环境先[连接 Skills 助手](https://mochilab.bz/Skills/Connect.aspx?lang=zh-CN)。连接成功后不用在聊天里提供密钥。每个工作区分别连接，可使用同一个已授权会员账户。本 Skill 免费，运行本地辅助脚本需要 Python3.10+。
