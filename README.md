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
| [提醒与定时任务 / Reminders and Scheduled Tasks](skills/mochi-reminders) | `mochi-reminders` | 1.1.0 |
| [菜谱与买菜清单 / Meal Planner and Grocery List](skills/mochi-meal-planner) | `mochi-meal-planner` | 1.1.0 |
| [随手记与待办 / Quick Notes and Tasks](skills/mochi-quick-notes) | `mochi-quick-notes` | 1.1.0 |
| [每日计划与复盘 / Daily Planner and Review](skills/mochi-daily-planner) | `mochi-daily-planner` | 1.1.0 |
| [日常记账与预算 / Expense Tracker and Budgets](skills/mochi-expense-tracker) | `mochi-expense-tracker` | 1.1.0 |
| [学习陪练与错题复习 / Study Coach and Mistake Review](skills/mochi-study-coach) | `mochi-study-coach` | 1.1.0 |
| [文件阅读与重点问答 / Document Reading and Questions](skills/mochi-document-reader) | `mochi-document-reader` | 1.1.0 |
| [工作日报与周报 / Daily and Weekly Work Reports](skills/mochi-work-reports) | `mochi-work-reports` | 1.1.0 |
| [购物比较助手 / Shopping Comparison](skills/mochi-shopping-compare) | `mochi-shopping-compare` | 1.1.0 |

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

## File tools and web subscriptions / 文件工具与网页订阅

| Skill | Version | What it does |
|---|---|---|
| [批量图片处理](skills/mochi-image-batch) | 1.0.0 | Batch resize, crop, pad, compress, convert and watermark images, with contact sheets and downloadable results. |
| [PDF 文件工具箱](skills/mochi-pdf-toolbox) | 1.0.0 | Merge, split, select, reorder, rotate and compress PDFs; convert images, render previews and inspect blank pages. |
| [网页变化订阅](skills/mochi-web-watch) | 1.0.0 | Watch selected webpage regions, retain baselines, filter noise, record differences and connect scheduled checks with chat delivery. |

## Workbenches / 综合工作台

| Skill | Version | What it does |
|---|---|---|
| [Excel 业务分析工作台](skills/mochi-sheet-studio) | 1.0.0 | Combine XLSX/CSV sources, clean mapped fields, deduplicate, reconcile sales, refunds and expenses, and export currency-separated monthly reports with source rows. |
| [音视频内容加工台](skills/mochi-media-workbench) | 1.0.0 | Inspect media, extract audio, cut clips and frames, and export SRT/VTT subtitles locally, with optional local speech recognition and resumable chunk caches. |
| [龙虾维护与迁移管家](skills/mochi-claw-maintenance) | 1.0.0 | Inspect one selected OpenClaw instance and its agent bindings, create verified private snapshots, compare changes and rehearse restoration in a new directory. |

## Mail, dates and daily workflows / 邮箱、日子与日常工作台

- [Multi-account Email Desk / 多邮箱邮件工作台](skills/mochi-email-desk): Connect IMAP/SMTP/POP3 accounts, sync and search mail, extract attachments, prepare and send messages, and track new-mail notifications.
- [Important Dates and Holidays / 重要日子与节日管家](skills/mochi-important-dates): Track Gregorian and lunar birthdays, anniversaries and sourced annual holidays, with advance alerts, time zones, leap-day policies and calendar export.
- [Calendar and Agenda Desk / 日程日历工作台](skills/mochi-calendar-desk): Import ICS calendars, expand recurring events, inspect conflicts, create meeting files and transfer CalDAV resources with version checks.
- [WebDAV Cloud File Desk / WebDAV 网盘工作台](skills/mochi-cloud-files): Connect a WebDAV drive, list and compare a directory, upload or download files, check versions and produce integrity hashes.
- [Contacts and Follow-up Desk / 联系人与跟进工作台](skills/mochi-contact-desk): Import CSV/vCard contacts, review email and phone duplicates, merge records, track follow-ups and export an address book.
- [RSS Subscription and Reading Hub / RSS 订阅与阅读中心](skills/mochi-feed-hub): Subscribe to RSS/Atom, import and export OPML, retain read state, search saved entries and queue new-content notifications.
- [Document Templates and Batch Output / 文档模板与批量出稿](skills/mochi-document-templates): Generate notices, certificates and business documents from DOCX, text or HTML templates, validate fields and retain Word run formatting.
- [Subscription and Renewal Desk / 订阅续费与账单管家](skills/mochi-subscription-desk): Track software, memberships and service renewals, calculate cancellation deadlines, forecast costs by currency and queue due notices.
- [Git Project Review and Snapshots / Git 项目检查与快照](skills/mochi-git-desk): Inspect a selected Git project and commit history, distinguish staged changes and create verified private working snapshots.
- [Archive and Integrity Toolbox / 压缩归档与完整性工具箱](skills/mochi-archive-desk): Inspect ZIP/TAR contents, extract into new folders, create ZIPs from selected files and report per-file integrity hashes.
