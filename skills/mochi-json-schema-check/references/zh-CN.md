# JSON数据契约检查

按明确支持的schema子集验证JSON，逐项指出错误及不支持的关键字，避免假通过。

## 操作流程

把 schema 和待校验 value 放在同一请求中。区分请求格式错误、数据违反支持规则、不支持关键字导致检查不完整这三类结果。保留失败字段位置，不自动把字符串转成数字。涉及引用、组合规则或格式校验时，改用项目的完整规范验证器。

## 输入示例（虚构）

```json
{
  "schema": {
    "type": "object",
    "required": [
      "count"
    ],
    "properties": {
      "count": {
        "type": "integer",
        "minimum": 1
      }
    },
    "additionalProperties": false
  },
  "value": {
    "count": 2
  }
}
```

本地处理方法见 runner.md，字段说明见 input.md。仅处理当前工作区，保留原文件，按真实输出核对结果；涉及联网、账户或发布的操作另行执行和验证。
