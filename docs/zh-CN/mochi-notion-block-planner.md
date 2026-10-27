# Notion内容块草稿

## 能做什么

把本地简单标题、列表和段落转换为可审核的Notion内容块JSON，先预览后上传。

## 操作流程

先检查 Markdown 是否属于支持的标题、列表和段落范围，表格、代码及行内格式需另定映射。生成后按原文顺序核对 notion-blocks.json 及长文本切片。实际上传前读取目标页面、避免重复追加，并按连接器限制分批写入；本地生成不代表 Notion 已接收。

## 输入示例（虚构）

```json
{
  "file": "samples/note.md"
}
```

## 输出与核对

在当前工作区生成报告及适用的产物，保留原文件。以返回结果、产物和具体检查范围为准；实时服务、远程账户操作和视觉效果需分别验证。

轻量部署包已默认安装 Skills 助手。在 MochiBot“设置 → MochiLab Skills 账户”验证并连接后，发送：

```text
安装 mochi-notion-block-planner
```

其他环境先[连接 Skills 助手](https://mochilab.bz/Skills/Connect.aspx?lang=zh-CN)。连接成功后不用在聊天里提供密钥。每个工作区分别连接，可使用同一个已授权会员账户。本 Skill 免费，运行本地辅助脚本需要 Python3.10+。
