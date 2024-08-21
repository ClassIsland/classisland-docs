# 常见问题

这些是用户通常可以自行解决的问题，您可以通过下方的目录或搜索功能快速检索您遇到的问题。

[TOC]

## 安装

安装时遇到的问题。

### 提示“You must install or update .NET to run this application.”

![1723087458369](image/faq/1723087458369.png)

出现这种弹窗一般是没安装 .NET 8 运行时。请点击【Download it now】或从[本链接](https://dotnet.microsoft.com/zh-cn/download/dotnet/thank-you/runtime-desktop-8.0.7-windows-x64-installer)下载 .NET 运行时，并运行下载的安装程序安装 .NET 运行时。完成后重新打开本软件即可。

### 在 Windows 7 中启动后出现内存占用极高的问题

解决方法见[在 Windows 7 中安装 ClassIsland](./setup.md#检查系统需求)。

## 系统

与系统相关的问题。

### 设置开机自启后，开机时 ClassIsland 无法正常自启动

这可能是因为 ClassIsland 的自启动项被禁用了，或者被安全软件拦截。您可以在安全软件的相关功能页面检查是否拦截了 ClassIsland 的自启动项目，或者在任务管理器的【启动应用】页面检查相关启动项目是否被禁用。

## 配置文件

### 正常使用时，电脑/大屏重启后配置文件丢失/回档

这种情况可能是电脑意外断电，导致配置文件没有完全保存导致的。目前 ClassIsland 已尝试通过定期备份等方式尽量减小意外断电对配置文件的影响。如果您的配置文件不幸丢失，可以在应用目录下的`Backups`文件夹内找到定期创建的备份，并进行恢复。详细请参阅[应用数据备份](./backup.md#恢复备份)文章。
