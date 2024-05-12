# 教程：手动编写集控配置文件

!!! warning "这个教程还没写完"

本教程将指引您手动编写集控配置文件，并将其静态托管到网上。

每当你看见👉️符号，就说明你应该做一些事情。而其余的只供您参考和更深入的理解。


## 在开始之前

您可以用任何文本编辑器来编辑这些配置文件，如[VS Code](https://code.visualstudio.com/)、[GitHub Codespaces](https://github.dev)，甚至是记事本。我们建议您安装一个带有json语法检查和高亮功能的编辑器。如果您安装了其它的编辑器，可以跳过这一步。

**👉️从[这里](https://code.visualstudio.com/)下载并安装VS Code。**

## 开始

我们需要新建一个文件夹，来存放接下来我们要用到的文件。

**👉️新建一个文件夹。**

**👉️进入刚刚创建的文件夹。**

集控文件包含了要拉取的集控相关文件的信息和组织的相关信息，相当于一个索引文件。ClassIsland在加入集控后，会拉取这个文件，并根据此文件中的配置来拉取相关的文件。

**👉️新建一个文件，并命名为`manifest.json`，并用文本编辑器打开。**

**👉️将以下文本粘贴到`manifest.json中`**

```json
{
    "ServerKind": 0,
    "OrganizationName": "Hello"
}
```

这就是一个最基础的清单文件了。这个文件说明了服务器类型是静态托管的，并且说明了组织名称。我们之后会逐渐完善这个文件。

接下来我们要把这个文件静态托管到网上。您可以选择您喜欢的托管平台，我们这里以GitHub为例。如果您使用其它的托管平台，部分操作可能会与文档所述略有差异。

**👉️在GitHub上新建一个公开仓库，并将该文件夹中的文件上传到GitHub仓库中。**

上传完成后，我们就能在GitHub上看到我们的文件了。接下来我们需要指向这个文件内容的**直接链接**。

**👉️进入`manifest.json`文件，点击`Raw`按钮。**

**👉️在刚刚打开的标签页中，复制地址栏的地址。**

接下来回到本地，我们在刚才的目录中新建一个集控配置文件，来告诉ClassIsland实例应该从哪里拉取集控清单。

**👉️在文件夹中新建一个文件，并命名为`ManagementPreset.json`，并用文本编辑器打开。**

**👉将以下文本粘贴到`ManagementPreset.json`中，并将`ManifestUrlTemplate`字段替换成你刚刚复制的链接。**

```json
{
    "ManagementServerKind": 0,
    "ManagementServer": "",
    "ManifestUrlTemplate": "（你刚刚复制的链接）",
}
```

编辑好集控配置后，我们就可以将这个文件导入到ClassIsland实例中了。

**👉将文件`ManagementPreset.json`复制到ClassIsland程序目录下，然后运行ClassIsland。**

如果您是第一次运行ClassIsland，此时ClassIsland会弹出欢迎向导。

**👉同意许可协议，然后点击【加入集控】按钮。**

此时会弹出集控加入界面，并自动加载了我们刚刚放置在应用目录下的`ManagementPreset.json`文件。您可以点击【浏览】按钮选择其它的配置文件。

**👉在ID一栏填入`TEST`**

ID在此处可以标识ClassIsland实例。在后续您可以将自定义id设置为班级名、教室编号等易于识别的名称。

**👉点击【连接】按钮。**

此时应用会下载集控清单文件，速度因网络环境而异。在下载完成后，应用会弹出最后的集控加入确认窗口。

**👉在弹出的确认提示框上，点击【加入】按钮。**

**👉在弹出的加入成功提示框上，点击【确定】按钮。**

此时应用会重新启动。在重新启动后，进入【应用设置】，您可以看到右上角出现了【由贵单位管理】徽章。

## 