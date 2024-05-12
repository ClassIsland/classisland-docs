# 集控策略文件

集控策略文件参考。

您可以使用策略文件来限制ClassIsland实例的一些功能，例如禁止编辑档案等，禁止修改设置等。

## 示例

```json
{
    "DisableProfileClassPlanEditing": true,
    "DisableProfileTimeLayoutEditing": true,
    "DisableProfileSubjectsEditing": true,
    "DisableProfileEditing": true,
    "DisableSettingsEditing": false,
    "DisableSplashCustomize": true,
    "DisableDebugMenu": true,
    "AllowExitManagement": true
}
```

## 目录

| 属性名 | 类型 | 说明 | 默认值 |
| -- | -- | -- | -- |
| [`DisableProfileClassPlanEditing`](#DisableProfileClassPlanEditing) | `bool` | 禁止编辑课表。 | `false` |
| [`DisableProfileTimeLayoutEditing`](#DisableProfileTimeLayoutEditing) | `bool` | 禁止编辑时间表。 | `false` |
| [`DisableProfileSubjectsEditing`](#DisableProfileSubjectsEditing) | `bool` | 禁止编辑科目。 | `false` |
| [`DisableProfileEditing`](#DisableProfileEditing) | `bool` | 禁止编辑档案。 | `false` |
| [`DisableSettingsEditing`](#DisableSettingsEditing) | `bool` | 禁止编辑应用设置。 | `false` |
| [`DisableSplashCustomize`](#DisableSplashCustomize) | `bool` | 禁止自定义启动加载界面。 | `false` |
| [`DisableDebugMenu`](#DisableDebugMenu) | `bool` | 禁用调试菜单。 | `false` |
| [`AllowExitManagement`](#AllowExitManagement) | `bool` | 允许退出集控。 | `true` |

## DisableProfileClassPlanEditing

## DisableProfileTimeLayoutEditing

## DisableProfileSubjectsEditing

## DisableProfileEditing

## DisableSettingsEditing

## DisableSplashCustomize

## DisableDebugMenu

## AllowExitManagement