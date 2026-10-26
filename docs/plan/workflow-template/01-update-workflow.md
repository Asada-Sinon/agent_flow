# 精简规约并补齐工作流模板

> 历史记录：本文件保留当时的要求与验证结果；小修改计划、记录时机等规则已由当前 [AGENTS.md](../../../AGENTS.md) 及 [效率调整规格](../../spec/agent-efficiency/spec.md) 更新，不作为现行规范。

**status**: done
**来源**: [工作流模板精简与补全](../../spec/workflow-template/spec.md#验收标准)

## 目标与验收项

落实已确认的模板调整方案，覆盖 AC-01 至 AC-06；本文件也是完整执行记录示例。

## 实施步骤

- [x] 保存本次修改的 spec 和 plan。
- [x] 集中通用规约，明确任务分级、澄清与计划调整边界。
- [x] 更新 spec 模板并新增 plan 模板，补齐验收、执行结果和交接字段。
- [x] 精简 README，清理重复索引及日志占位文件，调整忽略规则。
- [x] 验证文档链接、规则场景和忽略行为，将实际结果写回本文件。

## 验证方法

| 验收项 | 方法 | 通过条件 |
|---|---|---|
| AC-01、AC-04 | 检查 Markdown 本地链接，并搜索旧规则与删除文件的引用 | 本地文件和锚点有效；入口引用同一份规约，无旧规则残留 |
| AC-02 | 逐项走查调查、小修改、完整功能、计划调整、中断接续场景 | 每种场景都有对应规则，既能推进也能识别需要确认的问题 |
| AC-03 | 检查两个模板及本示例的字段与验收映射 | 字段完整，验收项可追溯，未验证不计为完成 |
| AC-05 | 在临时 Git 仓库复制忽略规则，使用 git check-ignore 和 git ls-files 检查代表路径 | 本地文件被忽略，应入库文件可被识别 |
| AC-06 | 检查 README 的准备方式、填写项和示例入口，核对实际验证输出 | 复用步骤完整，证据与实际检查一致 |

## 执行结果与证据

全部验收项通过。以下为本次实际执行的检查，未运行不存在的业务测试或应用。

### 文档、模板与入口（AC-01、AC-03、AC-04）

使用一次性 Python 检查读取全部 Markdown，核对本地链接及锚点、两个模板的必需字段、6 个验收项的映射，并确认已删除文件和旧规则引用没有残留。结果：

```text
Markdown links: PASS (7 files, 11 local links, 1 anchor)
Entry point and removed-rule references: PASS
Template fields and acceptance mapping: PASS (6 acceptance items)
```

CLAUDE.md 使用 `@AGENTS.md` 引入通用规约，语法已对照 [Claude Code 官方导入说明](https://code.claude.com/docs/en/memory#import-additional-files)。本次检查了入口内容和目标文件，未启动 Claude Code 会话验证加载行为。

### 流程走查（AC-02）

对照 AGENTS.md、README 和两个模板逐项人工走查：

| 场景 | 实际检查结果 |
|---|---|
| 阅读和排查现有实现 | 可直接调查和运行本地检查；需要修改代码、脚本或配置时才补计划 |
| 边界明确的小修改 | 用简短文件计划保存请求摘要、步骤、验收和结果，可省略 spec |
| 新功能或跨模块改动 | 先明确关键问题，创建 spec 及编号验收项，再用一个或多个计划实施 |
| 调整实现方式 | 目标、范围和验收不变时先更新计划后继续；尚未授权的范围、兼容性、成本或数据处理变化先确认 |
| 会话中断和外部阻塞 | 普通中断保留 in-progress 并写下一步；外部阻塞记录解除条件，恢复时核对文件现状后继续 |

五种场景均有对应规则，纯文档调整的豁免和验证失败时不得标记 done 的要求一致。

### 忽略行为（AC-05）

在自动清理的临时目录初始化 Git 并复制 .gitignore，为每个代表路径创建无敏感内容的测试文件。逐项执行 `git check-ignore --no-index -q -- <路径>`，再用 `git ls-files --others --exclude-standard` 核对完整可入库集合：

```text
Git ignore rules: PASS (28 ignored, 20 eligible for version control)
```

覆盖根目录数据、日志及旧快照路径、产物、临时文件；根目录及子目录的本地环境配置、依赖和缓存均被排除。规约、模板、环境示例、测试样例、交付文档和依赖锁文件可入库；`tests/fixtures/data/sample.csv` 不受根目录 data 规则影响。

### 使用方式（AC-06）

在另一自动清理的临时目录复制两个模板，逐段用 `bash -eu -c` 执行 README 的三段 shell 示例，检查工作目录、复制文件内容和完整任务的来源路径；同时核对项目填写项：

```text
README quick start: PASS (3 shell blocks, 5 local directories, 3 copied templates)
Workspace Git initialization: unchanged (temporary repositories only)
```

当前工作目录的 Git 未初始化，检查仅在临时目录创建版本库；未添加业务依赖或自动化脚本。

## 变更记录

- 初始计划：按用户确认的方案实施，使用本次修改作为真实示例，不额外创建模拟业务示例。
- 文档走查：将“执行前核对计划”明确限定为需要计划的任务，避免与直接调查、纯文档豁免冲突；spec 模板使用“仓库根目录”指引，避免复制进任务子目录后相对路径失效。目标、范围和验收不变。

## 阻塞与下一步

- 阻塞：无。
- 下一步：无，计划已完成。
