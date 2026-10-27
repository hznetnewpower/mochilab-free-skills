# 事件证据时间线

## 能做什么

按含时区的时间整理有来源的事件记录，计算间隔并导出证据时间线。

## 操作流程

为每个事件记录唯一 ID、带时区时间、简述和来源，区分事件发生时间与后来观察到它的时间。对照原始日志、监控和人员报告核对时钟差异、缺失时段及矛盾证据；时间相近不证明因果。工具仅整理已有证据，不查询监控、不推断根因、不删日志或执行修复。

## 输入示例（虚构）

```json
{
  "events": [
    {
      "id": "b",
      "at": "2026-10-27T10:05:00Z",
      "summary": "Recovered",
      "source": "synthetic monitor"
    },
    {
      "id": "a",
      "at": "2026-10-27T10:00:00Z",
      "summary": "Failure observed",
      "source": "synthetic log"
    }
  ]
}
```

## 输出与核对

在当前工作区生成报告及适用的产物，保留原文件。以返回结果、产物和具体检查范围为准；实时服务、远程账户操作和视觉效果需分别验证。

轻量部署包已默认安装 Skills 助手。在 MochiBot“设置 → MochiLab Skills 账户”验证并连接后，发送：

```text
安装 mochi-incident-timeline
```

其他环境先[连接 Skills 助手](https://mochilab.bz/Skills/Connect.aspx?lang=zh-CN)。连接成功后不用在聊天里提供密钥。每个工作区分别连接，可使用同一个已授权会员账户。本 Skill 免费，运行本地辅助脚本需要 Python3.10+。
