# 邮件头证据检查

## 能做什么

检查导出邮件头中的From数量、认证失败标记及路由跳数，不打开正文链接。

## 操作流程

使用原始邮件或邮件头导出，保留 Received 等字段顺序。重复发件字段及路由跳数是调查线索；Authentication-Results 只有来自可信接收边界时才有意义。工具不验证 DKIM 签名、不执行 SPF 查询，也不能直接认定钓鱼邮件，输出中避免泄露地址和正文。

## 输入示例（虚构）

```json
{
  "file": "samples/message.eml"
}
```

## 输出与核对

在当前工作区生成报告及适用的产物，保留原文件。以返回结果、产物和具体检查范围为准；实时服务、远程账户操作和视觉效果需分别验证。

轻量部署包已默认安装 Skills 助手。在 MochiBot“设置 → MochiLab Skills 账户”验证并连接后，发送：

```text
安装 mochi-email-header-inspector
```

其他环境先[连接 Skills 助手](https://mochilab.bz/Skills/Connect.aspx?lang=zh-CN)。连接成功后不用在聊天里提供密钥。每个工作区分别连接，可使用同一个已授权会员账户。本 Skill 免费，运行本地辅助脚本需要 Python3.10+。
