# 插件入口类

ClassIsland 的插件需要定义一个插件入口类，插件入口类需要继承`PluginBase`抽象类，并添加`PluginEntrance`属性。下面是一个插件入口的示例：

```csharp title="Plugin.cs"
using ClassIsland.Core.Abstractions;
using ClassIsland.Core.Attributes;
using ClassIsland.Core.Controls.CommonDialog;
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Hosting;

namespace HelloWorldPlugin;

[PluginEntrance]
public class Plugin : PluginBase
{
    public override void Initialize(HostBuilderContext context, IServiceCollection services)
    {
    }
}
```

在上面的代码中，我们定义了一个名为`Plugin`的类，并继承了 `PluginBase`抽象类。同时为`Plugin`类添加了`PluginEntrance`属性，以声明这个类是插件入口类。

这个插件入口类也会在初始化时添加到 IoC 主机上，您可以在插件注册的服务中通过依赖注入获取插件入口类实例。

## 初始化方法

其中的`Initialize`初始化方法会在插件加载后马上执行。您可以在这个方法中完成插件初始化操作。下面的代码会在初始化时显示一个“Hello world!”弹窗。

```csharp title="Plugin.cs" hl_lines="9"
// ...
namespace HelloWorldPlugin;

[PluginEntrance]
public class Plugin : PluginBase
{
    public override void Initialize(HostBuilderContext context, IServiceCollection services)
    {
        CommonDialog.ShowInfo("Hello world!");
    }

    // ...
}
```

初始化方法传入了主机构造时所需的相关参数，注册[组件](../components.md)、提醒提供方、服务等操作需要在这个方法完成。下面的代码会在初始化时注册一个名为 `ExampleSettingsPage` 的设置页面，和一个名为 `ExampleCompent` 的组件。

```cs title="Plugin.cs" hl_lines="11-12"
// ...
namespace PluginWithSettingsPage;

[PluginEntrance]
public class Plugin : PluginBase
{
    public Settings Settings { get; set; } = new();

    public override void Initialize(HostBuilderContext context, IServiceCollection services)
    {
        services.AddSettingsPage<ExampleSettingsPage>();
        services.AddComponent<ExampleComponent>();
    }

}
```

!!! note
    有些注册操作需要在主机启动后进行，由于初始化方法在主机启动前执行，所以可以通过订阅[`AppBase.AppStarted`](../events.md#应用启动完成-appstarted)事件，在应用启动完成后进行注册。

## 获取插件信息

您可以通过访问`Info`来获取这个插件的相关信息，比如插件清单等。您也可以通过访问`PluginConfigFolder`来获取插件配置目录路径。
