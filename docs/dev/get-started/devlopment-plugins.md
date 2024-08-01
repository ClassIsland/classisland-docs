# 配置 ClassIsland **插件**开发环境

!!! warning "本文档待补充。"

## 开发环境

**首先确保您的系统满足以下要求：**

- Windows 10 1803 及以上的操作系统，x86_64 架构

要在本地进行开发，**您需要安装以下负载和工具**：

- [.NET 8.0 SDK](https://dotnet.microsoft.com/zh-cn/download/dotnet/8.0)
- [Visual Studio 2022](https://visualstudio.microsoft.com/)，包括【.NET 桌面开发】工作负载
- [Git](https://git-scm.com/)

## 克隆并构建 ClassIsland

开发插件的过程中需要使用 ClassIsland 源码以构建 ClassIsland 本体的可执行文件，以用于运行和调试插件。

??? note "为什么不使用 Releases 中发布的可执行文件"
    Release 版本的构建无法使用热重载（包括 XAML 热重载）功能，调试起来很麻烦。

以下是克隆仓库的命令行：

=== "HTTP"

    ```shell
    git clone https://github.com/ClassIsland/ClassIsland.git
    ```

=== "SSH"

    ```shell
    git clone git@github.com:ClassIsland/ClassIsland.git
    ```

=== "GitHub CLI"

    ```shell
    gh repo clone ClassIsland/ClassIsland
    ```

克隆完成后，运行以下命令进入 ClassIsland 源代码目录。

``` shell
cd ClassIsland
```

目前插件功能还未下放到 `master` 分支上，需要签出开发分支 `dev`。如果您想签出到特定版本上，请使用对应版本的标签名（如 `1.4.3.0`）：

``` shell
git checkout dev    # 签出到 dev 分支
# 如果要签出到某个版本上，请使用标签名：
# git checkout 1.4.3.0
```

然后在 Powershell 运行以下命令构建 ClassIsland：

``` powershell
dotnet build -c Debug -p:Version=$(git describe --tags --abbrev=0)
```

这样就获得了 ClassIsland 的 Debug 构建。构建默认输出在 `（项目文件夹\ClassIsland\bin\Debug\net8.0-windows）`下。

## 更新

如果 ClassIsland 发布了新版本，或您更新了插件 SDK，在这种情况下需要更新 ClassIsland 仓库。要更新仓库，请先拉取，然后重新进行构建。

``` shell
git pull
dotnet clean
dotnet build -c Debug
```

## 开始开发插件

一切准备工作就绪后，继续阅读文章[开始编写插件](../plugins/create-project.md)，开始您的插件开发之旅吧！
