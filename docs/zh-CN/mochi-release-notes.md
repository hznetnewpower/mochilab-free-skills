# 提交记录生成版本说明

## 能做什么

将导出的提交记录按类型整理为版本说明草稿，单列声明的不兼容变更。

## 操作流程

从上一个版本到目标版本的实际提交范围准备记录，保留提交 ID 和必要正文。生成草稿后对照代码差异和测试证据，重大变化需补迁移说明。提交信息本身不能证明功能已修复；发布前删除内部信息，工具不会打标签、构建或发布版本。

## 输入示例（虚构）

```json
{
  "version": "1.1.0",
  "commits": [
    {
      "id": "abc123",
      "subject": "feat!: change interface"
    },
    {
      "id": "def456",
      "subject": "fix: preserve settings"
    }
  ]
}
```

## 输出与核对

在当前工作区生成报告及适用的产物，保留原文件。以返回结果、产物和具体检查范围为准；实时服务、远程账户操作和视觉效果需分别验证。

轻量部署包已默认安装 Skills 助手。在 MochiBot“设置 → MochiLab Skills 账户”验证并连接后，发送：

```text
安装 mochi-release-notes
```

其他环境先[连接 Skills 助手](https://mochilab.bz/Skills/Connect.aspx?lang=zh-CN)。连接成功后不用在聊天里提供密钥。每个工作区分别连接，可使用同一个已授权会员账户。本 Skill 免费，运行本地辅助脚本需要 Python3.10+。
