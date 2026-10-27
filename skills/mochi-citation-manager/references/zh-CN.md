# 参考文献去重与导出

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

本地处理方法见 runner.md，字段说明见 input.md。仅处理当前工作区，保留原文件，按真实输出核对结果；涉及联网、账户或发布的操作另行执行和验证。
