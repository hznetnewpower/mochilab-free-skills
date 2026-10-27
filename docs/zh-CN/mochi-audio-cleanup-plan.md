# 音频响度处理准备

## 能做什么

读取实际ffprobe结果，准备首轮响度分析滤镜，不修改原音频或编造测量值。

## 操作流程

先用目标媒体的 ffprobe JSON 核对音轨，再确认交付响度和真峰值目标。辅助脚本只提出首遍分析滤镜；实际分析后保留 loudnorm 测量值，再准备第二遍处理。输出到新文件并试听安静段、峰值和结尾，响度归一化不等于降噪或修复削波。

## 输入示例（虚构）

```json
{
  "probeFile": "samples/probe.json",
  "targetLufs": -16
}
```

## 输出与核对

在当前工作区生成报告及适用的产物，保留原文件。以返回结果、产物和具体检查范围为准；实时服务、远程账户操作和视觉效果需分别验证。

轻量部署包已默认安装 Skills 助手。在 MochiBot“设置 → MochiLab Skills 账户”验证并连接后，发送：

```text
安装 mochi-audio-cleanup-plan
```

其他环境先[连接 Skills 助手](https://mochilab.bz/Skills/Connect.aspx?lang=zh-CN)。连接成功后不用在聊天里提供密钥。每个工作区分别连接，可使用同一个已授权会员账户。本 Skill 免费，运行本地辅助脚本需要 Python3.10+。
