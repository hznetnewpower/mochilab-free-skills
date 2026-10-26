# Google办公账户操作规划

## 能做什么

明确Google办公账户及资源，区分查询与写入，生成可映射到已有授权工具的操作计划。

## 如何使用

安装后把具体任务和所需资料交给助手。下面是虚构输入示例，用于了解字段；真实任务请换成自己的文件与参数。

```json
{
  "actions": [
    {
      "kind": "gmail.search",
      "account": "demo@example.com",
      "query": "subject:invoice"
    },
    {
      "kind": "docs.update",
      "account": "demo@example.com",
      "resource": "fictional-document"
    }
  ]
}
```

## 输出与验证

在当前助手工作区生成JSON报告，适用时另有CSV、Markdown或文档产物。源文件保留。包内5项离线测试覆盖功能示例、错误输入、命令行实跑、路径边界和不覆盖输出；不把这些测试写成真实账户、网站或视觉验收。

## 适用边界

明确Google办公账户及资源，区分查询与写入，生成可映射到已有授权工具的操作计划。仅按已提供资料进行本地处理；不自动联网、提交表单、付款或安排任务。涉及实时信息、第三方账户或最终发布时，由助手使用已有授权工具另行执行并核对。详细字段和该功能的限制见包内说明。

轻量部署包已默认安装 Skills 助手。在 MochiBot“设置 → MochiLab Skills 账户”验证并连接后，发送：

```text
安装 mochi-google-workspace-plan
```

其他环境先[连接 Skills 助手](https://mochilab.bz/Skills/Connect.aspx?lang=zh-CN)。连接成功后不用在聊天里提供密钥。每个工作区分别连接，可使用同一个已授权会员账户。本 Skill 免费，运行本地辅助脚本需要 Python3.10+。
