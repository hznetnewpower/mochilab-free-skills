# UTM推广链接整理

## 能做什么

生成规范编码的UTM推广链接，保留普通查询参数，拒绝明显带密钥的地址。

## 操作流程

先统一 source、medium、campaign 的命名，保留原链接中语言或商品等功能参数。生成后解码检查主机、路径及参数是否正确，中文和空格也需核对。公开参数不要放姓名、邮箱、客户 ID 或密钥；生成链接不代表已发布活动或已部署统计采集。

## 输入示例（虚构）

```json
{
  "links": [
    {
      "url": "https://example.com/page?lang=en",
      "utm_source": "newsletter",
      "utm_medium": "email",
      "utm_campaign": "demo launch"
    }
  ]
}
```

## 输出与核对

在当前工作区生成报告及适用的产物，保留原文件。以返回结果、产物和具体检查范围为准；实时服务、远程账户操作和视觉效果需分别验证。

轻量部署包已默认安装 Skills 助手。在 MochiBot“设置 → MochiLab Skills 账户”验证并连接后，发送：

```text
安装 mochi-utm-campaigns
```

其他环境先[连接 Skills 助手](https://mochilab.bz/Skills/Connect.aspx?lang=zh-CN)。连接成功后不用在聊天里提供密钥。每个工作区分别连接，可使用同一个已授权会员账户。本 Skill 免费，运行本地辅助脚本需要 Python3.10+。
