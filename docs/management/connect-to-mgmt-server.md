# 连接/退出集控

在部署好配置文件/集控服务器后，您还需要将 ClassIsland 实例连接到集控服务器。


<a id="from-settings"></a>
## 从设置中加入

ClassIsland 从[集控配置文件](configure.md#mgmt-configure)加载集控的相关设置。在编写好集控配置文件后，在【应用设置】->【更多选项（右上角三个点）】->【加入管理…】即可加载配置文件并连接到集控服务。

![image](https://github.com/HelloWRC/ClassIsland/assets/55006226/07d32ffc-a7a7-45e2-844e-58ae3f998d47)

![image](https://github.com/HelloWRC/ClassIsland/assets/55006226/b8013062-1b71-4a10-9e52-12f15928fb4c)



<a id="from-wizard"></a>
## 在初始化应用时加入


您也可以在首次运行应用时，点击欢迎向导首页右下角【加入管理】按钮打开加入集控的界面。

![image](https://github.com/HelloWRC/ClassIsland/assets/55006226/6e0f2c6d-5bff-4677-bf3a-caa4319a990e)

!!! tip "将集控配置后重命名为`ManagementPreset.json`，并放置于应用目录下，即可在加入集控时自动选择并加载集控配置文件。"



<a id="exit"></a>
## 退出集控

要退出集控，点击【应用设置】->【更多选项（右上角三个点）】->【退出集控…】即可退出集控。

![image](https://github.com/HelloWRC/ClassIsland/assets/55006226/b354b1fa-7347-4204-9546-effe0045c56e)

!!! note "如果要禁用集控退出功能，可以在集控策略中将`AllowExitManagement`设置为`false`。[详细信息]()"