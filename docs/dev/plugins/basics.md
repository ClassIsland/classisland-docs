# 插件基础知识

这里是在 [ClassIsland 开发基础](../basics.md)的基础上，开发插件时还需要知道的事项。

## 程序集隔离

默认情况下，不同的插件会被加载到不同的程序集加载上下文（[AssemblyLoadContext](https://learn.microsoft.com/zh-cn/dotnet/core/dependency-loading/understanding-assemblyloadcontext)）中。因此，不同插件间可以引入相同依赖库的不同版本，而不会产生冲突。

!!! warning
    由于这个特性，当两个插件间包含具有相同名称的类型定义时，它们不是同一类型。当且仅当它们来自同一个 Assembly 实例时，它们的类型相同。详细请见[此文章](https://learn.microsoft.com/zh-cn/dotnet/core/dependency-loading/understanding-assemblyloadcontext#type-conversion-issues)。

## 资源引用

在插件中引用插件程序集内的资源时，需要使用绝对路径，否则会将路径解析至 ClassIsland 本体的程序集。例如：

``` plaintext
pack://application:,,,/程序集名称;;;component/资源路径
pack://application:,,,/ExamplePlugin;;;component/Assets/Image.png
```

## 依赖注入

在 [ClassIsland 开发基础](../basics.md#依赖注入) 所描述的基础上，插件需要在入口点的 `Initialize` 方法内完成相关注册操作。例如：

```csharp
// ...
namespace ClassIsland.ExamplePlugin;

[PluginEntrance]
public class Plugin : PluginBase
{
    public override void Initialize(HostBuilderContext context, IServiceCollection services)
    {
        services.AddSettingsPage<HelloSettingsPage>();
        services.AddSingleton<MyService>();
    }
    // ...
}
```
