# Uri 导航

ClassIsland 支持通过 Uri 进行应用内导航和从应用外部拉起应用，并提供了相应的命令在界面上处理超链接中的 Uri。

本文将介绍如何通过 `UriNavigationService` 来注册您自定义的 Uri 和导航事件处理方法来处理导航，以及如何在上通过命令和直接调用导航服务进行导航。

ClassIsland 的 Uri 导航协议是 `classisland://`。

## 注册导航

要注册导航，您首先需要获取服务 `ClassIsland.Core.Abstractions.Services.IUriNavigationService`。获取服务的详细方法见[基础知识](basics.md#dependency-injection)。

!!! info
    在本文的代码中，我们假定将获取到的服务存储在了属性 `UriNavigationService` 中。

接下来我们注册路径 `hello_world/hello_world` 的处理程序：

```cs
UriNavigationService.HandlePluginsNavigation(
    "hello_world/hello_world", 
    args => {
        CommonDialog.ShowInfo($"Hello world!");
    }
);
```

在上面的代码中，使用 `HandlePluginsNavigation` 方法注册的 Uri 的主机默认是 `plugins`，也就是专门为插件预留的导航主机。如果要注册到 `app` 或其他主机下，请使用 `HandleAppNavigation` 方法。

!!! note
    `HandleAppNavigation`等方法具有 `internal` 保护，只有从 ClassIsland 内部才能注册到 `app` 和自定义主机下。插件中只能使用 `HandlePluginsNavigation` 方法注册到 `plugins` 主机下。

接下来运行 ClassIsland。当导航到 `classisland://plugins/hello_world/hello_world`时，会弹出对话框“Hello world!”。这代表在上面代码中已经成功注册了 Uri。

## 导航

在导航到某个 Uri 时，ClassIsland 会首先尝试导航到指定的路径下。如果这个路径下没有注册处理方法，会逐步向上级导航，直到根目录。

``` mermaid
flowchart LR
    BeginNavigation["开始导航"] --> IsExist{"目标路径是否存在？"}  -->|"存在"| Navigated["导航成功"] 
    IsExist -->|"不存在"| Back["尝试导航到上级目录"] --> IsRoot{"到达根目录？"} -->|"是"| Failed["导航失败"]
    IsRoot --> |"否"| IsExist
```

!!! example "举个栗子"
    假设我们注册到了路径 `hello_world/hello_world`。当向 `hello_world/hello_world/foo_bar` 导航时，由于这个路径还未被注册，会导航到上一级 `hello_world/hello_world`，并触发对应的事件处理程序。

以下有几种进行导航的方式：

### 通过 `Hyperlink`

!!! info
    待补充。

### 通过后端调用导航方法

调用 `IUriNavigationService.Navigate` 方法可以导航到指定的 Uri。如果要导航的 Uri 协议不是 `classisland://`，ClassIsland 会自动调用系统中最合适的应用处理这个 Uri。

```cs
// 打开导航测试窗口
UriNavigationService.Navigate(new Uri("classisland://app/test"));

// 在系统浏览器中打开 ClassIsland 官网
UriNavigationService.Navigate(new Uri("https://classisland.tech"));
```

### 从外部应用调用

如果 ClassIsland 在系统上注册了 `classisland://` 链接的打开方式，那么在浏览器等地方打开这种协议的链接时，ClassIsland 可以在应用中导航到对应的 Uri 处理程序上。

例如：[classisland://app/test](classisland://app/test)
