# 客户端识别

您可以为每个ClassIsland实例自定义一个id，来标识每个实例。您可以将自定义id设置为班级名、教室编号等易于识别的名称。

除了自定义的id外，ClassIsland还会生成一段唯一客户端id（CUID），来标识每个实例。

这些信息可以在访问集控配置数据时，加入到url中。详细请见[url模板](configure.md#url-template)。

<a id="url-template"></a>
## url模板

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
