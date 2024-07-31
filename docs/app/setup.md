# 安装与开始

本文将介绍如何安装与开始使用 ClassIsland。

## 检查系统需求

首先，确保您的设备满足以下推荐需求：

- Windows 10 及以上版本的系统，x86_64 架构
- 已安装 [.NET 8.0 桌面运行时](https://dotnet.microsoft.com/zh-cn/download/dotnet/thank-you/runtime-desktop-8.0.1-windows-x64-installer)
- 4GB 及以上的运行内存

??? note "在 Windows 7 中安装 ClassIsland"
    !!! danger "警告！！！"
        不建议在 Windows 7 中使用 ClassIsland。如果您执意要在 Windows 7 中使用 ClassIsland，请**务必按照以下步骤**完成环境设置等准备工作，否则可能会出现**严重的内存泄漏问题**。（ ClassIsland#91 ）

        此外，在 Windows 10 以下的系统中，部分功能可能不可用。如果您接受这些缺陷，请继续阅读下文。

    1. **安装依赖项**

        您需要按照[此处](https://learn.microsoft.com/zh-cn/dotnet/core/install/windows?tabs=net80#additional-deps)的指引根据您的操作系统版本安装额外的依赖项。

        对于 Windows 7，以下是您需要额外安装的依赖项：

        - Microsoft Visual C++ 2015-2019 Redistributable [64 位](https://aka.ms/vs/16/release/vc_redist.x64.exe) / [32 位](https://aka.ms/vs/16/release/vc_redist.x86.exe)
        - KB3063858 [64 位](https://www.microsoft.com/download/details.aspx?id=47442) / [32 位](https://www.microsoft.com/download/details.aspx?id=47409)

    2. **处理内存泄漏问题**

        .NET 7 以及以上的运行时在 Windows 7 会产生严重的内存泄漏问题。您需要以管理员身份在命令提示符运行以下命令完成修复：

        ``` shell
        setx DOTNET_GCName clrgc.dll
        setx DOTNET_EnableWriteXorExecute 0
        ```

        以上命令设置了以下环境变量。如果命令执行失败，您可以手动设置以下变量。

        | 环境变量 | 值 |
        | --- | --- |
        | `DOTNET_GCName` | `clrgc.dll` |
        | `DOTNET_EnableWriteXorExecute` | `0` |

## 下载应用本体

对于普通用户，可以在以下渠道下载到本软件，请根据自身网络环境选择合适的渠道。

!!! warning

    测试版包含最新的功能，但也可能包含未完善和不稳定的功能，请谨慎使用。

| 下载渠道/通道 | **🚀正式版** <br/>[![GitHub Release](https://img.shields.io/github/v/release/HelloWRC/ClassIsland?style=flat-square&logo=GitHub&color=%233fb950)](https://github.com/HelloWRC/ClassIsland/releases/latest)  | 🚧测试版<br/>[![GitHub Release](https://img.shields.io/github/v/release/HelloWRC/ClassIsland?include_prereleases&style=flat-square&logo=GitHub&label=BETA)](https://github.com/HelloWRC/ClassIsland/releases/) |
| -- | -- | -- |
| GitHub | [**GitHub 下载**](https://github.com/HelloWRC/ClassIsland/releases/latest) | [GitHub 下载](https://github.com/HelloWRC/ClassIsland/releases) |
| AppCenter | [**AppCenter 下载**](https://install.appcenter.ms/users/hellowrc/apps/classisland/distribution_groups/public/releases/latest) | [AppCenter 下载](https://install.appcenter.ms/users/hellowrc/apps/classisland/distribution_groups/publicbeta/releases/latest) |

??? info "高级"

    如果您想体验最新的功能，可以前往[AppVeyor](https://ci.appveyor.com/project/HelloWRC/classisland-yw873/)下载包含最新功能的构建。如果您想自行构建 ClassIsland，请参考[开发文档](../dev/get-started/devlopment.md)。

## 解压软件

下载完成后，将软件压缩包解压到一个您喜欢的地方，运行软件即可开始使用。

!!! warning
    解压时请不要解压到网盘同步文件夹、【下载】文件夹中，否则可能会出现**文件无法读写、文件丢失**等问题。

## 开始使用

首次启动时，会有一个简短的欢迎向导来引导您完成本软件的基本设置，并展示软件的一些基本操作。

您也可以观看[入门教程视频](https://www.bilibili.com/video/BV1fA4m1A7uZ/)来快速上手本软件。如果您要进一步了解本软件，您可以继续阅读本文档。
