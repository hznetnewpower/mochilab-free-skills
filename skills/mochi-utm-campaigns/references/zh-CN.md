# UTM推广链接整理

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

本地处理方法见 runner.md，字段说明见 input.md。仅处理当前工作区，保留原文件，按真实输出核对结果；涉及联网、账户或发布的操作另行执行和验证。
