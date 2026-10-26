# UTM推广链接整理

生成规范编码的UTM推广链接，保留普通查询参数，拒绝明显带密钥的地址。

## 使用

先提供本功能需要的文件或参数，由助手按 `input.md` 的字段准备请求。辅助脚本只离线处理当前工作区，报告与新文件保存在 `exports/`。需要实时网页、办公账户或实际发布时，另用已有授权工具执行并核对结果。

## 输入示例（虚构数据）

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

## 验证范围

包内测试验证本地处理、错误输入、路径边界与不覆盖原文件；不表示已完成远程操作、事实核验或视觉检查。具体能力边界以 `input.md` 为准。
