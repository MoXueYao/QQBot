# 叠甲环节

 - 我只是一个业余人士，Python很多特性都不了解，代码有很多问题。
 - 如果你认为我写的很烂，这属于正常现象。
 - 本项目需要一定的依赖，下面也会讲解如何安装。

# 如何使用

## 1、安装NapCatQQ

 - 首先下载安装NT版QQ，你可以访问 https://im.qq.com/pcqq/index.shtml/ 来下载安装
 - 自行寻找并安装`NapCat`在电脑的任意位置。
 - 运行`...\NapCat\`中的`start.ps1`并登录你的QQ。
 - 打开`...\NapCat\config\onebot11_你的qq号.json`然后参考如下方式将HTTP部分修改为：
 ```
    "enable": true,
    "host": "",
    "port": 3000,
    "secret": "",
    "enableHeart": false,
    "enablePost": true,
    "postUrls": ["http://127.0.0.1:8080"]
  ```
  - 注意！其他部分如果不懂就最好不要动!
  - 再次运行`...\NapCat\`中的`start.ps1`并登录你的QQ。

## 2、运行示例代码

  - 将终端定位到项目目录下，键入`python main.py`并回车来运行。
  - 使用手机QQ（或者平板、其他设备）登录任意账号，对该机器人账号发送`你好`既可以看到`Hello World!`的回复
  - 如果想要实现其他功能，请自行阅读代码并编写你的代码。

## 3、编写插件
  - 插件编写请查看的示例代码`plugins\example\`。
  - 下面是一个插件的通常结构：
  ```
    plugins
    └── 插件名
        ├── 其他可能存在的文件
        ├── main.py
        ├── __init__.py
        └── 可能存在的配置文件.后缀
  ```
  - 目前由于技术有限，插件尚不成熟。
