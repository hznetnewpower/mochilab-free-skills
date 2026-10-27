# JSON数据契约检查

## 能做什么

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

## 输出与核对

在当前工作区生成报告及适用的产物，保留原文件。以返回结果、产物和具体检查范围为准；实时服务、远程账户操作和视觉效果需分别验证。

轻量部署包已默认安装 Skills 助手。在 MochiBot“设置 → MochiLab Skills 账户”验证并连接后，发送：

```text
安装 mochi-json-schema-check
```

其他环境先[连接 Skills 助手](https://mochilab.bz/Skills/Connect.aspx?lang=zh-CN)。连接成功后不用在聊天里提供密钥。每个工作区分别连接，可使用同一个已授权会员账户。本 Skill 免费，运行本地辅助脚本需要 Python3.10+。
