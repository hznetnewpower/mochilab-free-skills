# 参考文献去重与导出

按规范化DOI或标题去重用户提供的文献，保留来源信息并导出BibTeX。

## 使用

先提供本功能需要的文件或参数，由助手按 `input.md` 的字段准备请求。辅助脚本只离线处理当前工作区，报告与新文件保存在 `exports/`。需要实时网页、办公账户或实际发布时，另用已有授权工具执行并核对结果。

## 输入示例（虚构数据）

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

## 验证范围

包内测试验证本地处理、错误输入、路径边界与不覆盖原文件；不表示已完成远程操作、事实核验或视觉检查。具体能力边界以 `input.md` 为准。
