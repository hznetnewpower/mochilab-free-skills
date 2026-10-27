# 转录文稿章节整理

## 能做什么

把拟定的视频章节与转录片段ID关联，检查时间范围并导出时间戳章节表。

## 操作流程

先取得授权转写及带唯一 ID 的时间段，标题必须依据实际文本。每个章节关联存在的片段 ID，并按真实话题转折检查边界和时间顺序。导出后对照音视频核对最后时间点；引用关系通过不等于摘要准确，工具不会获取视频、生成转写或发布章节。

## 输入示例（虚构）

```json
{
  "segments": [
    {
      "id": "s1",
      "start": 0,
      "end": 60
    },
    {
      "id": "s2",
      "start": 60,
      "end": 120
    }
  ],
  "chapters": [
    {
      "start": 0,
      "title": "Opening",
      "sourceIds": [
        "s1"
      ]
    },
    {
      "start": 60,
      "title": "Example",
      "sourceIds": [
        "s2"
      ]
    }
  ]
}
```

## 输出与核对

在当前工作区生成报告及适用的产物，保留原文件。以返回结果、产物和具体检查范围为准；实时服务、远程账户操作和视觉效果需分别验证。

轻量部署包已默认安装 Skills 助手。在 MochiBot“设置 → MochiLab Skills 账户”验证并连接后，发送：

```text
安装 mochi-transcript-chapters
```

其他环境先[连接 Skills 助手](https://mochilab.bz/Skills/Connect.aspx?lang=zh-CN)。连接成功后不用在聊天里提供密钥。每个工作区分别连接，可使用同一个已授权会员账户。本 Skill 免费，运行本地辅助脚本需要 Python3.10+。
