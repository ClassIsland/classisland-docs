# 客户端识别

您可以为每个 ClassIsland 实例自定义一个 id，来标识每个实例。您可以将自定义 id 设置为班级名、教室编号等易于识别的名称。

除了自定义的 id 外，ClassIsland 还会生成一段唯一客户端 id（CUID），来标识每个实例。

这些信息可以在访问集控配置数据时，加入到 url 中。详细请见[url 模板](configure.md#url-template)。

<a id="url-template"></a>

## url 模板

在调用集控清单中的 url 时，ClassIsland 可以根据客户端的信息，将对应信息填入 url 模板中，实现为每个 ClassIsland 实例分配特定的对象。

ClassIsland 支持以下模板：

| 模板 | 说明 |
| -- | -- |
| `{id}` | 客户端的 ID |
| `{cuid}` | 客户端的唯一客户端 ID |

在发起请求时，url 中的模板会直接被替换为对应信息，例如：

``` plaintext
https://example.com/client/{id}/policy.json -> https://example.com/client/TEST_ID/policy.json
https://example.com/client/{cuid}/policy.json -> https://example.com/client/9f5ab079-83c7-aeba-db2f-db39a0009845/policy.json
```
