# 基础知识

本文将介绍在进行 ClassIsland 相关开发时需要了解的一部分基础概念。

<a id="xml-namespace"></a>

## XML 命名空间

在 XAML 中使用程序集 `ClassIsland.Core` 下封装的一些控件时，需要引入对应的 XML 命名空间，如下方代码所示：

``` xml hl_lines="3"
<ci:MyWindow x:Class="ClassIsland.Views.FeatureDebugWindow"
        xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation"
        xmlns:ci="http://classisland.tech/schemas/xaml/core">
    <!-- ... -->
</ci:MyWindow >
```

`http://classisland.tech/schemas/xaml/core` 命名空间的前缀默认是 `ci` ，包含了以下的 CLR 命名空间，在引用这个命名空间时会自动包含以下命名空间中的控件。

- ClassIsland.Core
- ClassIsland.Core.Converters
- ClassIsland.Core.Controls
- ClassIsland.Core.Controls.CommonDialog
- ClassIsland.Core.Controls.LessonsControls
- ClassIsland.Core.Controls.IconControl
- ClassIsland.Core.Controls.NavHyperlink
- ClassIsland.Core.Commands
- ClassIsland.Core.Abstractions.Controls

如果您要对 ClassIsland 本体进行修改，在 `ClassIsland` 程序集下的命名空间，需要手动按照 CLR 命名空间进行引用：

``` xml hl_lines="4"
<ci:MyWindow x:Class="ClassIsland.Views.FeatureDebugWindow"
        xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation"
        xmlns:ci="http://classisland.tech/schemas/xaml/core"
        xmlns:controls="clr-namespace:ClassIsland.Controls">
    <!-- ... -->
</ci:MyWindow >
```

<a id="dependency-injection"></a>

## 依赖注入

ClassIsland 使用了依赖注入设计模式。在定义一个服务时，您可以在服务的构造函数参数中指定要引用的服务依赖项，主机会在构造服务时自动传入依赖项。

要了解关于依赖注入的更多内容，请参阅[.NET 依赖项注入](https://learn.microsoft.com/zh-cn/dotnet/core/extensions/dependency-injection)。这篇文档会更详细地介绍 .NET 中依赖注入的相关信息。

如果您正在开发 ClassIsland 的插件，您还应该留意文档[插件基础知识](./plugins/basics.md#依赖注入) 的依赖注入章节中，与在开发应用本体中不同的操作。
