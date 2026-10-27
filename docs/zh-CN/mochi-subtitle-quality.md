# 字幕时间与阅读速度检查

## 能做什么

检查SRT或简单WebVTT字幕的时长、重叠及可配置阅读速度，保留原字幕。

## 操作流程

使用带毫秒时间戳的 UTF-8 SRT 或 WebVTT，按受众和语言设定阅读速度阈值。对异常字幕结合前后段及真实音频判断，不能为了降速删掉重要意思。工具不听音频、不校准同步、不验证翻译，复杂 WebVTT 布局需专用编辑器，原文件应保留。

## 输入示例（虚构）

```json
{
  "file": "samples/subtitles.srt",
  "maxCharsPerSecond": 20
}
```

## 输出与核对

在当前工作区生成报告及适用的产物，保留原文件。以返回结果、产物和具体检查范围为准；实时服务、远程账户操作和视觉效果需分别验证。

轻量部署包已默认安装 Skills 助手。在 MochiBot“设置 → MochiLab Skills 账户”验证并连接后，发送：

```text
安装 mochi-subtitle-quality
```

其他环境先[连接 Skills 助手](https://mochilab.bz/Skills/Connect.aspx?lang=zh-CN)。连接成功后不用在聊天里提供密钥。每个工作区分别连接，可使用同一个已授权会员账户。本 Skill 免费，运行本地辅助脚本需要 Python3.10+。
