---
name: unity-csfile-organize
description: Reorder one Unity C# file without changing behavior.
disable-model-invocation: true
---

# Unity C# File Organize

## 目录

- [目标](#目标)
- [终止条件](#终止条件)
- [工作流程](#工作流程)
- [排序规则](#排序规则)
- [保护规则](#保护规则)
- [验证清单](#验证清单)
- [输出要求](#输出要求)

## 目标

整理单个已有 Unity C# 代码文件的结构顺序. 只调整完整成员, 类型, `using`, 注释, attribute, 或 region 内代码块的位置. 不修改函数体内容, 命名, 行为逻辑, API 语义, 初始化语义, Inspector 展示意图, 或菜单和 UI 操作顺序.

默认不删除 `using`. 只有用户明确要求, 或已经完成可靠编译验证并确认安全时, 才能删除未使用 `using`.

如果保护已有逻辑, Inspector 体验, 初始化顺序, region 结构, 或调用语义需要妥协排序规则, 执行后必须向用户说明具体妥协点和原因.

## 终止条件

在执行任何文件修改前, 必须确认目标文件明确且是 Unity C# 文件. 如果无法确定目标文件, 目标不是单个文件, 文件扩展名不是 `.cs`, 或文件内容无法确认属于 Unity C# 项目, 立刻终止任务并向用户报告具体原因.

判断 Unity C# 文件时, 优先使用路径和内容证据, 例如文件位于 Unity 项目的 `Assets`, `Packages`, 或 Unity package 目录下, 或文件包含 `using UnityEngine`, `using UnityEditor`, `MonoBehaviour`, `ScriptableObject`, `Editor`, `AssetPostprocessor`, `InitializeOnLoadMethod`, `SerializeField`, `MenuItem` 等 Unity 相关 API. 如果证据不足, 不要猜测, 直接终止并说明需要用户提供明确的 Unity C# 文件.

## 工作流程

1. 执行终止条件检查. 未通过时立刻停止, 不做修改.
2. 阅读目标文件和项目局部规则. 如果修改 C# 或需要 Git 操作, 先读取项目要求的对应 rule module.
3. 识别文件主类型, 顶层类型, nested type, 常量, 字段, UI 成员, 生命周期入口, asset 回调, 普通函数, 注释, attribute, region, partial 边界.
4. 只移动完整代码块. 移动成员时带走紧贴该成员的 XML summary, attribute, 普通说明注释, 空行上下文中明确属于该成员的分隔注释.
5. 优先在现有 region 内整理. 不要为了排序新建 region. 必须跨 region 移动时, 先确认 region 语义确实阻碍整理, 并在结果中说明.
6. 对 `partial` 类型只整理当前文件内成员. 不跨 partial 文件移动成员, 不假设其他 partial 文件布局.
7. 完成后检查 diff, 确认没有成员重复, 遗漏, 半截残留, 注释错位, 或括号失衡.

## 排序规则

### using 顺序

普通 `using` 在前, 被宏包裹的 `using` 作为独立整块放在普通 `using` 之后, `using Alias = Namespace.Type;` 再后, `using static Namespace.Type;` 最后.

普通 `using` 分组顺序:

1. `.NET` 命名空间, 即 `System` 系列.
2. Unity 命名空间, 顺序为 `UnityEngine`, `UnityEditor`, 其他 `Unity.*`.
3. 第三方命名空间.
4. 用户项目命名空间.

同组内部按字母序排列. 保留宏包裹块内部原有条件语义, 只在不会改变条件编译结构时整理块内顺序.

### 同级类型顺序

1. 文件主类型优先. 文件名对应的 `class`, `struct`, `enum`, 或 `interface` 视为主类型.
2. 与主类型强绑定的辅助类型紧随主类型之后. 推荐顺序为 `enum`, `class`, `struct`, `interface`, `delegate`. 例如主类型专用的 options, settings, context, result, state. 如果这些类型只被主类型使用, 可以提示它们适合 nested type, 但默认不做嵌套化重构.
3. 其他同级类型先排 public API 类型, 再排 internal 或 private 辅助类型.
4. 同一语义组内按依赖方向排序. 被更多类型依赖的基础类型在前, 使用方在后, 例如 enum, config, result 在 processor, runner, helper 前.
5. 没有明显主次关系或依赖关系时, 按字母序.

### 类内大顺序

1. 类型定义, 包括 `enum`, nested `class`, nested `struct`, nested `interface`, `delegate`.
2. 全局常量, `public const` 在前, `private const` 在后.
3. static 字段, `public static` 在前, `private static` 在后.
4. public 实例字段.
5. private 实例字段.
6. Odin UI 暴露成员和 UI 入口函数.
7. `OnValidate`.
8. `InitializeOnLoadMethod` 等初始化入口.
9. Unity 生命周期函数.
10. Asset postprocessor 或 asset modification processor 相关回调.
11. 普通函数, 按语义分组排列.

### UI 和生命周期顺序

带有 `Button`, `ButtonGroup`, `ShowInInspector`, `PropertyOrder`, `Title`, `MenuItem` 等 UI 或编辑器入口属性的成员归入 UI 组. UI 组内部必须保持 Inspector, 菜单, 用户操作顺序不变.

`OnValidate` 放在 UI 组之后, 生命周期组之前. `InitializeOnLoadMethod` 放在 `OnValidate` 之后, Unity 生命周期函数之前.

Unity 生命周期函数建议顺序为 `Reset`, `Awake`, `OnEnable`, `Start`, `Update`, `LateUpdate`, `OnDisable`, `OnDestroy`. 如果项目已有固定顺序, 优先沿用项目顺序.

### Asset 回调顺序

Asset postprocessor 和 asset modification processor 回调放在生命周期组之后, 普通函数之前. 同类资源管线回调保持成组, 不要散进普通 helper 区.

常见回调包括 `OnPreprocessTexture`, `OnPostprocessTexture`, `OnPreprocessModel`, `OnPostprocessModel`, `OnPreprocessAnimation`, `OnPostprocessAnimation`, `OnPostprocessAllAssets`, `OnWillMoveAsset`, `OnWillDeleteAsset`, `OnWillSaveAssets`.

### 普通函数语义顺序

普通函数不要机械按调用顺序排列. 优先按语义重要性排列:

1. 与当前类功能最紧密的核心逻辑和算法函数.
2. 核心算法的直接 helper.
3. 输入校验, 上下文构建, 数据准备函数.
4. 接口实现和 override 函数, 保持同一接口或基类语义成组.
5. 事件, delegate, callback 处理函数.
6. Coroutine 和 async 相关函数, 放在调用它们的功能组附近.
7. 资产读写, 材质处理, 序列化, 文件路径等副作用函数.
8. 场景辅助, 状态恢复, 临时对象管理等局部 helper.
9. 通用工具函数, 例如字符串清洗, prefab 判断, 路径安全处理等.

核心逻辑或算法函数指真正完成该类主要工作的函数. 校验函数和准备函数即使在调用链上更早发生, 也应排在核心算法之后. 同组内部可以按主流程, 被直接调用 helper, 更底层 helper 排列.

## 保护规则

字段排序必须谨慎. Unity 序列化字段, Odin 暴露字段, public 配置字段经常共同决定 Inspector 顺序. static 字段, readonly 字段, lazy 初始化字段, Unity 序列化字段, Odin 显示字段, 以及带 attribute 的字段都可能受初始化顺序或显示顺序影响.

如果字段排序可能影响 Inspector 顺序或初始化语义, 保持原顺序并说明. 不要为了满足字面排序破坏用户在 Inspector, MenuItem, ButtonGroup, PropertyOrder, 或 attribute 组合中表达的使用顺序.

注释和 attribute 必须跟随主体移动. 不要留下孤儿注释, 空的分隔注释, 或和下一段代码错位的说明.

## 验证清单

- `using` 顺序符合规则.
- 同级类型顺序符合规则.
- 类型, 常量, static 字段, public 实例字段, private 实例字段顺序正确.
- Odin UI 和 `MenuItem` 顺序没有破坏.
- `OnValidate` 位置正确.
- `InitializeOnLoadMethod` 和 Unity 生命周期函数位置正确.
- Asset postprocessor 或 modification processor 回调成组.
- 核心算法函数在校验和准备函数之前.
- interface, override, callback 没有被拆散.
- coroutine 和 async 函数仍靠近相关功能组.
- 注释和 attribute 没有丢失或错位.
- 没有重复成员.
- 没有遗漏成员.
- 旧位置没有残留半截代码.
- 括号数量平衡.
- 原有逻辑没有改变.

## 输出要求

完成后简短说明整理后的主要顺序和验证结果. 如果因保护已有逻辑而没有完全按规则排序, 必须说明具体妥协点和原因.
