# 代码仓库上手地图

## 能做什么

根据指定仓库文件清单定位技术栈、上手文档和测试入口，先理解再操作。

## 操作流程

从用户指定的仓库和版本导出文件名清单，包含隐藏文件及相关子项目。先读 AGENTS.md、README、依赖清单、锁文件和 CI 配置，再判断真实构建路径。文件名推断要标明依据，单仓多项目需分别梳理；发现安装脚本不等于已获准执行它。

## 输入示例（虚构）

```json
{
  "files": [
    "package.json",
    "README.md",
    "AGENTS.md",
    "tests/basic.test.js"
  ]
}
```

## 输出与核对

在当前工作区生成报告及适用的产物，保留原文件。以返回结果、产物和具体检查范围为准；实时服务、远程账户操作和视觉效果需分别验证。

轻量部署包已默认安装 Skills 助手。在 MochiBot“设置 → MochiLab Skills 账户”验证并连接后，发送：

```text
安装 mochi-repo-onboarding
```

其他环境先[连接 Skills 助手](https://mochilab.bz/Skills/Connect.aspx?lang=zh-CN)。连接成功后不用在聊天里提供密钥。每个工作区分别连接，可使用同一个已授权会员账户。本 Skill 免费，运行本地辅助脚本需要 Python3.10+。
