# 社交内容批次核对

## 能做什么

按用户提供的平台限制检查一批社交内容的字数与附件，保留为待发布草稿。

## 操作流程

每篇草稿保留唯一 ID、目标平台、最终文字和素材引用，并提供该平台当前字数限制。工具按 Unicode 码点计数，实际平台可能对网址、字符和账户类型采用不同规则。临界稿需在真实编辑器核对，精简不能改变事实或去掉必要出处；工具不登录、排期或发布。

## 输入示例（虚构）

```json
{
  "platformLimits": {
    "demo": 5
  },
  "posts": [
    {
      "id": "p1",
      "platform": "demo",
      "text": "hello"
    },
    {
      "id": "p2",
      "platform": "demo",
      "text": "too long"
    }
  ]
}
```

## 输出与核对

在当前工作区生成报告及适用的产物，保留原文件。以返回结果、产物和具体检查范围为准；实时服务、远程账户操作和视觉效果需分别验证。

轻量部署包已默认安装 Skills 助手。在 MochiBot“设置 → MochiLab Skills 账户”验证并连接后，发送：

```text
安装 mochi-social-batch-plan
```

其他环境先[连接 Skills 助手](https://mochilab.bz/Skills/Connect.aspx?lang=zh-CN)。连接成功后不用在聊天里提供密钥。每个工作区分别连接，可使用同一个已授权会员账户。本 Skill 免费，运行本地辅助脚本需要 Python3.10+。
