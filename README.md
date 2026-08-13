# xiaobai skill(小白)

一个用于优化 AI 输出方式的 Claude Code SKILL:避免一次性输出长文,改为小步交互。

- **分步指导模式**:指导用户完成工作时,先给简要路线图,然后一步一步带着做,每步可实操、可验证,根据用户反馈继续。
- **QA 快问快答模式**:完成复杂工作后,不输出冗长报告,而是结论先行 + 推荐问题,通过快问快答帮用户逐步理解全貌。
- **HTML 优先的汇报展示**:做汇报或内容展示时,优先生成带图表、可交互的 HTML 页面替代大段文字;阐述软件系统的内容、变更、设计时,推荐配合 [archify](https://github.com/tt-a1i/archify) 生成交互式系统架构报告。

## 安装

把本仓库链接(或复制)到 Claude Code 的 skills 目录:

```bash
# 全局生效(所有项目)
ln -s "$(pwd)" ~/.claude/skills/xiaobai

# 或只对某个项目生效
ln -s "$(pwd)" <project>/.claude/skills/xiaobai
```

重启 Claude Code 会话后生效。可通过 `/xiaobai` 手动调用,也会在指导类/汇报类任务中自动触发。

## 维护

SKILL 的全部内容在 [SKILL.md](SKILL.md),改完提交推送即可。
