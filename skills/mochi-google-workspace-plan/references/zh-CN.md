# Google办公账户操作规划

明确Google办公账户及资源，区分查询与写入，生成可映射到已有授权工具的操作计划。

## 操作流程

每一步明确使用哪个账户、执行哪种动作、针对哪个资源 ID。先搜索和读取实际对象，再核对写入目的地及变更内容。这里只生成操作计划，不实现 Google 登录或调用接口；实际执行需使用已有授权连接器并检查结果，不能向用户索取刷新令牌。

## 输入示例（虚构）

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

本地处理方法见 runner.md，字段说明见 input.md。仅处理当前工作区，保留原文件，按真实输出核对结果；涉及联网、账户或发布的操作另行执行和验证。
