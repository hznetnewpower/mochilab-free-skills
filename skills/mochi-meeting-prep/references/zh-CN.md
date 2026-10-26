# 面向决策的会前准备

整理有明确决策目标的议程，检查时间分配并列出需要补充的问题。

## 使用

先提供本功能需要的文件或参数，由助手按 `input.md` 的字段准备请求。辅助脚本只离线处理当前工作区，报告与新文件保存在 `exports/`。需要实时网页、办公账户或实际发布时，另用已有授权工具执行并核对结果。

## 输入示例（虚构数据）

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

## 验证范围

包内测试验证本地处理、错误输入、路径边界与不覆盖原文件；不表示已完成远程操作、事实核验或视觉检查。具体能力边界以 `input.md` 为准。
