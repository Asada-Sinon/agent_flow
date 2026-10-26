# flow

面向 agent 开发的可复用工作流模板。以完成并验证任务的总成本为优先：简单任务直接推进，复杂任务保留必要的计划和验收，长任务留下可接续的进度。

通用规则统一维护在 [AGENTS.md](AGENTS.md)，Claude Code 通过 [CLAUDE.md](CLAUDE.md) 引入。开始任务时只读取当前工作需要的内容。

## 开始使用

复制模板后，优先填写下方项目入口与验证信息，补充所选技术栈的忽略规则。本地工作目录按需创建：

```bash
mkdir -p data log output temp script
```

按 [任务分级](AGENTS.md#开始任务) 选择流程。局部明确修改无需文件计划；需要持久计划时：

```bash
task_slug=refactor-import
mkdir -p "docs/plan/$task_slug"
cp docs/plan/_template.md "docs/plan/$task_slug/01-refactor-import.md"
```

需要 spec 的任务，再创建同名规格：

```bash
task_slug=refactor-import
mkdir -p "docs/spec/$task_slug"
cp docs/spec/_template.md "docs/spec/$task_slug/spec.md"
```

填写适用内容，删除空的可选章节。上述 plan 若关联 spec，来源链接使用 `../../spec/refactor-import/spec.md#验收标准`。任务步骤按实际需要命名，不要求预先创建所有目录或文档。

## 项目入口与验证

采用模板后尽早填写，避免每次会话重新探索环境与命令。目前仅包含工作流文档，没有业务运行时或应用测试。

| 项目项 | 当前值 / 采用后填写 |
|---|---|
| 项目目标 | 当前为工作流模板；采用后填写业务目标 |
| 环境与安装 | 当前无业务依赖；采用后填写语言、版本、包管理器及安装命令 |
| 运行入口 | 当前无应用；采用后填写启动命令及工作目录 |
| 最小验证 | 当前为受影响文档的链接、示例与规则一致性检查；采用后填写可直接执行的相关检查命令 |
| 完整验证及触发条件 | 当前在工作流或模板联动修改时检查相关入口、复制示例和规则场景；采用后填写完整测试/构建命令及何时必须运行 |
| 外部依赖与耗时 | 本地文档检查无需外部服务；发布需 GitHub 访问及 Git 写权限。采用后标明慢检查、服务需求及预期耗时 |
| 源码与测试位置 | 按技术栈填写；需入库的小型样例放在 `tests/fixtures/` |
| 配置方式 | 本地环境配置默认忽略，提供不含凭据的 `.env.example` 或 `.env.<环境>.example` |

## 模板与示例

- [spec 模板](docs/spec/_template.md)：需求、边界及可验证的验收项。
- [plan 模板](docs/plan/_template.md)：目标、进度、验证及必要的接续信息。
- 本次效率调整的 [spec](docs/spec/agent-efficiency/spec.md)、[实施计划](docs/plan/agent-efficiency/01-simplify-workflow.md) 与 [发布记录](docs/plan/agent-efficiency/02-publish-repository.md)：真实工作示例。
- 早期模板调整的 [spec](docs/spec/workflow-template/spec.md) 与 [plan](docs/plan/workflow-template/01-update-workflow.md)：历史记录，部分流程已被当前规约替代。

## 目录

| 路径 | 用途 |
|---|---|
| `docs/spec/`、`docs/plan/` | 规格、计划及模板 |
| `data/`、`log/`、`output/`、`temp/` | 按需创建的本地工作数据，默认不入库 |
| `script/` | 需要保留的辅助脚本 |
| `tests/fixtures/`、`docs/deliverables/` | 按需创建的小型测试样例、交付文档 |

业务源码与测试布局随技术栈确定，并更新上表。版本管理保留源码、依赖锁文件和必要记录；可再生成的数据与产物留在本地工作目录。
