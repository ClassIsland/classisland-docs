# 集控策略文件

集控策略文件参考。

您可以使用策略文件来限制 ClassIsland 实例的一些功能，例如禁止编辑档案等，禁止修改设置等。

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

<a id="DisableProfileClassPlanEditing"></a>

## DisableProfileClassPlanEditing

启用此项后，用户将不能创建、删除和编辑课表，同时【从 Excel 表格导入功能】也将被禁用。临时换课和启用临时课表功能不受影响。

<a id="DisableProfileTimeLayoutEditing"></a>

## DisableProfileTimeLayoutEditing

启用此项后，用户将不能创建、删除和编辑时间表，同时【从 Excel 表格导入功能】也将被禁用。

<a id="DisableProfileSubjectsEditing"></a>

## DisableProfileSubjectsEditing

启用此项后，用户将不能创建、删除和编辑科目。

<a id="DisableProfileEditing"></a>

## DisableProfileEditing

启用此项后，用户将不能编辑档案内所有内容，同时【从 Excel 表格导入功能】也将被禁用。临时换课和启用临时课表功能不受影响。

<a id="DisableSettingsEditing"></a>

## DisableSettingsEditing

启用此项后，用户将不能调整应用的设置。但先前调整过的设置在启用此项后不受影响。

<a id="DisableSplashCustomize"></a>

## DisableSplashCustomize

启用此项后，用户将不能自定义启动界面。如果先前调整过启动界面自定义设置，这些设置会被清除。

<a id="DisableDebugMenu"></a>

## DisableDebugMenu

启用此项后，用户将不能进入调试页面。

<a id="AllowExitManagement"></a>

## AllowExitManagement

控制用户是否能主动退出集控。禁用后，用户将无法自行退出集控。
