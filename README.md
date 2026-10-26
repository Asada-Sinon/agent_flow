# flow

面向 agent 开发的可复用工作流模板。以完成并验证任务的总成本为优先：简单任务直接推进，复杂任务保留必要的计划和验收，长任务留下可接续的进度。

通用规则统一维护在 [AGENTS.md](AGENTS.md)，Claude Code 通过 [CLAUDE.md](CLAUDE.md) 引入。开始任务时只读取当前工作需要的内容。

## 开始使用

采用到新项目时：

1. 填写下方项目目标、环境、运行和验证命令，补充技术栈的忽略规则。
2. 删除 `docs/spec/`、`docs/plan/` 中模板自身的任务目录（保留 `_template.md`），并移除 README 中对应的示例链接；如需保留，移到明确的示例目录并修复相对链接。所有保留记录中的目标、授权、仓库地址和环境信息只属于当时的任务，不适用于新项目。
3. 根据新项目的实际请求开始首个任务，仅在需要时创建 spec 或 plan。

本地工作目录按需创建：

```bash
mkdir -p data log output temp script
```

按 [任务分级](AGENTS.md#开始任务) 选择流程。局部明确修改无需文件计划；需要持久计划时使用以下示例。`refactor-import` 是示例任务名，请替换为实际 slug；目标文件已存在时停止，继续已有任务或换用新 slug：

```bash
(
set -eu
task_slug=refactor-import
target="docs/plan/$task_slug/01-refactor-import.md"
mkdir -p "docs/plan/$task_slug"
if ! (set -C; cat docs/plan/_template.md > "$target"); then
  printf '无法创建 %s；若已存在，请继续已有任务或使用新 slug。\n' "$target" >&2
  exit 1
fi
)
```

需要 spec 的任务，再创建同名规格：

```bash
(
set -eu
task_slug=refactor-import
target="docs/spec/$task_slug/spec.md"
mkdir -p "docs/spec/$task_slug"
if ! (set -C; cat docs/spec/_template.md > "$target"); then
  printf '无法创建 %s；若已存在，请继续已有任务或使用新 slug。\n' "$target" >&2
  exit 1
fi
)
```

填写适用内容，删除空的可选章节。上述 plan 若关联 spec，来源链接使用 `../../spec/refactor-import/spec.md#验收标准`。任务步骤按实际需要命名，不要求预先创建所有目录或文档。

## 项目入口与验证

采用模板后尽早填写，避免每次会话重新探索环境与命令。目前包含工作流文档与标准库检查脚本，没有业务运行时或应用测试。在项目根目录运行：

```bash
python3 script/check_workflow.py
```

脚本检查当前 Markdown 内联本地链接、标题锚点、模板关键字段，并在临时目录执行 README 创建示例及重复执行保护检查。检查不联网、不修改项目文件；规约语义仍需人工或 agent 审阅。

| 项目项 | 当前值 / 采用后填写 |
|---|---|
| 项目目标 | 当前为工作流模板；采用后填写业务目标 |
| 环境与安装 | 检查脚本需要 Python 3.8+ 与 Bash，无第三方包；采用后填写业务环境及安装命令 |
| 运行入口 | 当前无应用；采用后填写启动命令及工作目录 |
| 最小验证 | `python3 script/check_workflow.py`；采用后补充业务改动的相关检查命令 |
| 完整验证及触发条件 | 工作流、模板或检查脚本修改时运行上述命令并走查受影响的规则场景；采用后填写业务完整测试/构建命令及触发条件 |
| 外部依赖与耗时 | 本地文档检查无需外部服务；发布需 GitHub 访问及 Git 写权限。采用后标明慢检查、服务需求及预期耗时 |
| 源码与测试位置 | 按技术栈填写；需入库的小型样例放在 `tests/fixtures/` |
| 配置方式 | 本地环境配置默认忽略，提供不含凭据的 `.env.example` 或 `.env.<环境>.example` |

## 模板与示例

下列任务记录仅展示本模板的历史工作，不能作为新项目的需求或操作授权。

- [spec 模板](docs/spec/_template.md)：需求、边界及可验证的验收项。
- [plan 模板](docs/plan/_template.md)：目标、进度、验证及必要的接续信息。
- 效率调整任务的 [spec](docs/spec/agent-efficiency/spec.md)、[实施计划](docs/plan/agent-efficiency/01-simplify-workflow.md) 与 [发布记录](docs/plan/agent-efficiency/02-publish-repository.md)：真实工作示例。
- 早期模板调整的 [spec](docs/spec/workflow-template/spec.md) 与 [plan](docs/plan/workflow-template/01-update-workflow.md)：历史记录，部分流程已被当前规约替代。
- [采用与验证修复记录](docs/plan/workflow-review/01-fix-adoption.md)：创建保护、检查脚本和采用说明的验证记录。

## 目录

| 路径 | 用途 |
|---|---|
| `docs/spec/`、`docs/plan/` | 规格、计划及模板 |
| `data/`、`log/`、`output/`、`temp/` | 按需创建的本地工作数据，默认不入库 |
| `script/` | 需要保留的辅助脚本 |
| `tests/fixtures/`、`docs/deliverables/` | 按需创建的小型测试样例、交付文档 |

业务源码与测试布局随技术栈确定，并更新上表。版本管理保留源码、依赖锁文件和必要记录；可再生成的数据与产物留在本地工作目录。
