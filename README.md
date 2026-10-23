# MochiLab Free Skills

免费的 MochiLab Skills，含源码、示例和测试。仅发布免费部分，付费包不在本仓库。

Free, self-contained MochiLab Skills for OpenClaw. Paid packages, website backend code, customer data and credentials are excluded. Existing MochiPay and Mochi Crypto Intelligence publications are independent and are not modified by this repository.

## Skills

| Skill | Slug | Version |
|---|---|---|
| [MochiLab Skills assistant](skills/mochilab-skills) | `mochilab-skills` | 1.0.0 |
| [My Daily Brief](skills/mochi-daily-brief) | `mochi-daily-brief` | 1.0.0 |
| [Web Research Notes](skills/mochi-web-notes) | `mochi-web-notes` | 1.0.0 |
| [Translation and Proofreading](skills/mochi-translation-qa) | `mochi-translation-qa` | 1.0.0 |
| [Website Availability and Basic SEO Check](skills/mochi-site-check) | `mochi-site-check` | 1.0.0 |
| [Reply Drafts](skills/mochi-reply-drafts) | `mochi-reply-drafts` | 1.0.0 |
| [Meeting Minutes and Action Items](skills/mochi-meeting-actions) | `mochi-meeting-actions` | 1.0.0 |
| [Study Cards with Source References](skills/mochi-learning-cards) | `mochi-learning-cards` | 1.0.0 |
| [File Organization Plan and Duplicate Report](skills/mochi-file-organizer) | `mochi-file-organizer` | 1.0.0 |
| [CSV Cleaning and Analysis](skills/mochi-csv-workbench) | `mochi-csv-workbench` | 1.0.0 |
| [Content Repurposing Workbench](skills/mochi-content-workbench) | `mochi-content-workbench` | 1.0.0 |

## Everyday Skills / 日常常用 Skills

Nine additional free Skills, with local helpers, examples and executable tests.

| Skill | Slug | Version |
|---|---|---|
| [提醒与定时任务 / Reminders and Scheduled Tasks](skills/mochi-reminders) | `mochi-reminders` | 1.0.0 |
| [菜谱与买菜清单 / Meal Planner and Grocery List](skills/mochi-meal-planner) | `mochi-meal-planner` | 1.0.0 |
| [随手记与待办 / Quick Notes and Tasks](skills/mochi-quick-notes) | `mochi-quick-notes` | 1.0.0 |
| [每日计划与复盘 / Daily Planner and Review](skills/mochi-daily-planner) | `mochi-daily-planner` | 1.0.0 |
| [日常记账与预算 / Expense Tracker and Budgets](skills/mochi-expense-tracker) | `mochi-expense-tracker` | 1.0.0 |
| [学习陪练与错题复习 / Study Coach and Mistake Review](skills/mochi-study-coach) | `mochi-study-coach` | 1.0.0 |
| [文件阅读与重点问答 / Document Reading and Questions](skills/mochi-document-reader) | `mochi-document-reader` | 1.0.0 |
| [工作日报与周报 / Daily and Weekly Work Reports](skills/mochi-work-reports) | `mochi-work-reports` | 1.0.0 |
| [购物比较助手 / Shopping Comparison](skills/mochi-shopping-compare) | `mochi-shopping-compare` | 1.0.0 |

## Install and use

Install the chosen Skill from ClawHub once its listing is available, or copy one folder from `skills/` into your current OpenClaw workspace's `skills/` directory. Preserve the folder name and its supporting files. Run `openclaw skills info SKILL_SLUG`, then start a fresh conversation. Each SKILL.md describes its exact inputs, outputs and boundaries.

The nineteen standalone task Skills do not need a MochiLab key. The optional `mochilab-skills` catalogue assistant uses your private account connection only when downloading packages from the MochiLab website; it never includes paid packages in this repository.

Most task scripts require Node.js 24+. The catalogue assistant requires Node.js 24.16+ or 26.1+. The agent's configured model and any external services may charge separately. Installing a Skill does not itself configure a model, create a timer, or prove a task has completed.

## 中文说明

选择一个免费 Skill 的目录安装即可，不需要先下载整个网站，也不要把全部目录当成一个 Skill。安装后先检查就绪状态，再新建对话使用。各包中的说明包含输入格式、工具权限、运行方法和示例。

这里的独立免费包无需 MochiLab 访问密钥。MochiLab Skills 助手本身也是免费的，但通过它从站点下载内容时仍需在自己的终端连接账户；以后出现的付费内容不会自动同步到本仓库。

## License

All files in this public release are provided under MIT-0 (MIT No Attribution). This permits modification, redistribution and commercial use without mandatory attribution. Links to MochiLab identify the source, not an additional license restriction.

Website: https://mochilab.bz/ · Connection guide: https://mochilab.bz/Skills/Connect.aspx
