# MochiPay 支付接入

[English](../en/integrate-mochipay.md)

协助选择官方商城插件和开发示例，实现收银台、回调、重试恢复与支付状态核验，附离线配置检查。

## 功能与用法

协助选择官方商城插件和开发示例，实现收银台、回调、重试恢复与支付状态核验，附离线配置检查。

```text
帮我检查这个商城应使用哪个 MochiPay 官方插件版本。
```

```text
根据官方 API 文档设计异步通知与幂等履约流程，先用模拟数据测试。
```

```text
检查脱敏的接入配置，列出缺失项，不发起真实订单。
```

原始发布者为 MochiPay；本页分发 1.2.15 原版安装包，保留原作者说明和 MIT-0 许可。[官方说明](https://mochi.bz/Developers/Skill.aspx)与[API 文档](https://mochi.bz/Developers/Reference.aspx)。技能免费；MochiPay 服务、商户权限及外部 AI 工具费用另计。离线检查不证明真实付款或生产接入已通过。

## 运行要求

具备文件和代码能力的 AI 客户端；可选离线检查需要 Python 3 标准库。

## 安装与开始使用

先[连接 MochiLab Skills 助手](https://mochilab.bz/Skills/Connect.aspx?lang=zh-CN)，再发送：

```text
安装 integrate-mochipay
```

也可领取 ZIP 后放入目标助手工作区的 skills/，开启新对话。不同 BOT 分别连接自己的 MochiLab 账户。

## 详细操作说明

[查看原版技能操作契约](https://github.com/hznetnewpower/mochipay-plugins/blob/main/skills/integrate-mochipay/SKILL.md)。命令、字段名和文件路径保留原样；按当前助手工作区执行，先核对依赖，再检查实际输出。
