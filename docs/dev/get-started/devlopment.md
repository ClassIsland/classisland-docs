# 配置 ClassIsland **本体**开发环境

## 开发环境

**首先确保您的系统满足以下要求：**

- Windows 10 1803 及以上的操作系统，x86_64 架构

要在本地进行开发，**您需要安装以下负载和工具**：

- [.NET 8.0 SDK](https://dotnet.microsoft.com/zh-cn/download/dotnet/8.0)
- [Visual Studio 2022](https://visualstudio.microsoft.com/)，包括【.NET 桌面开发】工作负载
- [Git](https://git-scm.com/)

## 拉取代码

您可以在 Fork 了本仓库后，通过 Git 将代码克隆到本地，然后开始开发。

要克隆仓库，您可以直接在 Visual Studio 中克隆，也可以通过命令行克隆。

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

!!! warning "仓库名仅供参考，具体的仓库名请以您的 Fork 为准。"

## 编译与运行

1. 在 Visual Studio 中打开解决方案 `ClassIsland.sln`
2. 将项目 `ClassIsland` 设置为启动项目
3. 点击【启动】即可编译项目，并开始调试。
