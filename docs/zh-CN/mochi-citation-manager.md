# 参考文献去重与导出

## 能做什么

按规范化DOI或标题去重用户提供的文献，保留来源信息并导出BibTeX。

## 操作流程

收集可追溯的记录 ID、标题、作者、年份和 DOI，并到出版方核对最终元数据。检查规范化去重后保留了哪条记录，不要误删不同版本、译本、勘误或撤稿信息。导出 BibTeX 后核对引用键；工具不检索论文、不解析 DOI，也不能证明文献支持某个论点。

## 输入示例（虚构）

```json
{
  "records": [
    {
      "id": "demo1",
      "title": "Fictional report",
      "authors": [
        "Example Author"
      ],
      "year": 2026,
      "doi": "https://doi.org/10.0000/demo"
    },
    {
      "id": "demo2",
      "title": "Same record",
      "doi": "10.0000/demo"
    }
  ]
}
```

## 输出与核对

在当前工作区生成报告及适用的产物，保留原文件。以返回结果、产物和具体检查范围为准；实时服务、远程账户操作和视觉效果需分别验证。

轻量部署包已默认安装 Skills 助手。在 MochiBot“设置 → MochiLab Skills 账户”验证并连接后，发送：

```text
安装 mochi-citation-manager
```

其他环境先[连接 Skills 助手](https://mochilab.bz/Skills/Connect.aspx?lang=zh-CN)。连接成功后不用在聊天里提供密钥。每个工作区分别连接，可使用同一个已授权会员账户。本 Skill 免费，运行本地辅助脚本需要 Python3.10+。
