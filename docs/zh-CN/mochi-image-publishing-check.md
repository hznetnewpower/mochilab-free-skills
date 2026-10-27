# 图片发布资料检查

## 能做什么

核对发布图片的实际文件大小、声明尺寸和替代文字，生成待处理清单。

## 操作流程

先实际查看准备发布的图片，再填写文件路径、尺寸及替代文字，或明确标为装饰图。核对字节数和预算，并用图像解码器确认声明尺寸。信息图不能为消除提示而标为装饰；工具不判断画质、不缩图，也不能确认替代文字是否准确或页面整体是否无障碍。

## 输入示例（虚构）

```json
{
  "assets": [
    {
      "file": "samples/demo.png",
      "width": 1,
      "height": 1,
      "alt": "Fictional one-pixel sample"
    }
  ]
}
```

## 输出与核对

在当前工作区生成报告及适用的产物，保留原文件。以返回结果、产物和具体检查范围为准；实时服务、远程账户操作和视觉效果需分别验证。

轻量部署包已默认安装 Skills 助手。在 MochiBot“设置 → MochiLab Skills 账户”验证并连接后，发送：

```text
安装 mochi-image-publishing-check
```

其他环境先[连接 Skills 助手](https://mochilab.bz/Skills/Connect.aspx?lang=zh-CN)。连接成功后不用在聊天里提供密钥。每个工作区分别连接，可使用同一个已授权会员账户。本 Skill 免费，运行本地辅助脚本需要 Python3.10+。
