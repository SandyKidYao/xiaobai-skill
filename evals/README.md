# evals

`evals.json` 是本 skill 的测试用例;`fixtures/` 是测试用的示例项目。

跑测试时的注意事项:**给每个 fixture 副本 `git init` 并提交一个初始 commit**。前两轮评测的副本没有 git,agent 只能落盘生成 diff 文件送审,反向养成了"有 git 也生成 diff 文件"的习惯——skill 现已明确"有 git 时让搭档自行 `git diff`",测试环境要能支撑这个行为。
