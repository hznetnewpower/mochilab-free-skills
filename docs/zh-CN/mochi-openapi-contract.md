# OpenAPI接口契约检查

## 能做什么

检查OpenAPI3 JSON中的重复操作ID、缺失响应及路径参数声明，生成接口清单。

## 操作流程

先获取目标服务实际使用的 OpenAPI JSON，并记录对应版本。逐项定位报告中的方法和路径，检查重复 operationId、路径参数是否声明为必填、响应定义是否完整。修改标识前核对生成客户端；外部引用、认证方式和完整规范验证需另用专业验证器。

## 输入示例（虚构）

```json
{
  "file": "samples/openapi.json"
}
```

## 输出与核对

在当前工作区生成报告及适用的产物，保留原文件。以返回结果、产物和具体检查范围为准；实时服务、远程账户操作和视觉效果需分别验证。

轻量部署包已默认安装 Skills 助手。在 MochiBot“设置 → MochiLab Skills 账户”验证并连接后，发送：

```text
安装 mochi-openapi-contract
```

其他环境先[连接 Skills 助手](https://mochilab.bz/Skills/Connect.aspx?lang=zh-CN)。连接成功后不用在聊天里提供密钥。每个工作区分别连接，可使用同一个已授权会员账户。本 Skill 免费，运行本地辅助脚本需要 Python3.10+。
