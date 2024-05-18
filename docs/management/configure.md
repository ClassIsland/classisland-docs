# 集控配置文件

ClassIsland集控配置文件的参考文档。

## 目录

### 类型

| 类型 | 说明 |
| -- | -- |
| [`ReVersionString`](#reversionstring) | 一种存储了字符串和其版本信息的类型。 |

### 配置文件

| 文件 | 说明 |
| -- | -- |
| [集控配置](#mgmt-configure) | 客户端集控配置，存储了集控服务器/集控清单url的相关信息。 |
| [集控清单](#mgmt-manifest) | 包含了要拉取的集控相关文件的信息和组织的相关信息。 |
| [策略文件](#mgmt-policy) | 控制ClassIsland行为的各个策略。 |
| 应用设置 | ClassIsland的设置。 |
| [课表、时间表与科目文件](#mgmt-profile) | 存储课表、时间表与科目信息的文件。 |

<a id="ReVersionString"></a>
## ReVersionString

`ReVersionString`是一种存储了字符串和其版本信息的类型。

### 成员

| 属性 | 类型 | 必填？ | 说明 | 示例 |
| -- | -- | -- | -- | -- |
| `Version` | `int` | **是** | 当前字符串的版本序号 | `1` |
| `Value` | `string?` | 否 | 字符串内容 | `Hello world!` |

### 示例

```json
{
    "Version": 1,
    "Value": "Hello world!"
}
```

<a id="mgmt-configure"></a>
## 集控配置

客户端集控配置，存储了集控服务器/集控清单url的相关信息。

### 属性

| 属性 | 类型 | 必填？ | 说明 | 示例 |
| -- | -- | -- | -- | -- |
| `ManagementServerKind` | `int` | **是** | 集控服务器类型。（`0`：静态托管的配置文件；`1`：集控服务器） | `0` |
| `ManagementServer` | `string` | 仅当`ManagementServerKind`为1时必填 | 集控服务器地址 | `https://example.com:23333` |
| `ManifestUrlTemplate` | `string` | 仅当`ManagementServerKind`为0时必填 | 集控清单url模板 | `https://example.com/manifest.json` |
| `ClassIdentity` | `string` | 否 | 班级标识符 | `1-101` |

<a id="url-template"></a>
### url模板

在调用集控清单中的url时，ClassIsland可以根据客户端的信息，将对应信息填入url模板中，实现为每个ClassIsland实例分配特定的对象。

ClassIsland支持以下模板：

| 模板 | 说明 |
| -- | -- |
| `{id}` | 客户端的ID |
| `{cuid}` | 客户端的唯一客户端ID |

在发起请求时，url中的模板会直接被替换为对应信息，例如：

```
https://example.com/client/{id}/policy.json -> https://example.com/client/TEST_ID/policy.json
https://example.com/client/{cuid}/policy.json -> https://example.com/client/9f5ab079-83c7-aeba-db2f-db39a0009845/policy.json
```

### 示例

```json
{
    "ManagementServerKind": 0,
    "ManagementServer": "",
    "ManifestUrlTemplate": "https://example.com/manifest.json",
    "ClassIdentity": "TEST"
}
```

<a id="mgmt-manifest"></a>
## 集控清单

包含了要拉取的集控相关文件的信息和组织的相关信息。

如果您正在手动修改此文件，请务必在修改了`ReVersionString`类型的属性后更新该属性的版本序号，否则ClassIsland实例可能不会更新相关信息。

### 属性

| 属性 | 类型 | 必填？ | 说明 | 示例 |
| -- | -- | -- | -- | -- |
| `ServerKind` | `int` | **是** | 服务器类型（`0`：静态托管的配置文件；`1`：集控服务器） | `0` |
| `OrganizationName` | `string` | 否 | 组织名称| `⌈黑塔⌋空间站`
| `ClassPlanSource` | [`ReVersionString`](#ReVersionString) | 否 | 课表文件url模板 | -- |
| `TimeLayoutSource` | [`ReVersionString`](#ReVersionString) | 否 | 时间表文件url模板 | -- |
| `SubjectsSource` | [`ReVersionString`](#ReVersionString) | 否 | 科目文件url模板 | -- |
| `DefaultSettingsSource` | [`ReVersionString`](#ReVersionString) | 否 | 应用设置url模板 | -- |
| `PolicySource` | [`ReVersionString`](#ReVersionString) | 否 | 策略文件url模板 | -- |

### 示例

```json
{
    "ClassPlanSource": {
        "Value": "https://example.com/ClassPlan.json",
        "Version": 1
    },
    "TimeLayoutSource": {
        "Value": "https://example.com/TimeLayout.json",
        "Version": 1
    },
    "SubjectsSource": {
        "Value": "https://example.com/Subjects.json",
        "Version": 1
    },
    "DefaultSettingsSource": {
        "Value": "https://example.com/settings.json",
        "Version": 1
    },
    "PolicySource": {
        "Value": "https://example.com/policy.json",
        "Version": 2
    },
    "ServerKind": 0,
    "OrganizationName": "Test Organization"
}
```

<a id="mgmt-policy"></a>
## 策略文件

控制ClassIsland行为的各个策略，详见[策略文件](policy.md)。

<a id="mgmt-profile"></a>
## 课表、时间表与科目文件

存储课表、时间表与科目信息的文件，格式为档案文件格式。

您可以直接将含有这些信息的档案文件导出，并直接在清单引用这些文件。
