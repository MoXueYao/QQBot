# 叠甲环节

 - 我只是一个业余人士，Python很多特性都不了解，代码有很多问题。
 - 如果你认为我写的很烂，这属于正常现象。
 - 本项目需要一定的依赖，下面也会讲解如何安装。

# 如何使用

## 1、安装NapCatQQ

 - 首先下载安装NT版QQ，你可以访问 https://im.qq.com/pcqq/index.shtml/ 来下载安装
 - 自行寻找并安装`NapCat`在电脑的任意位置。
 - 运行`...\NapCat\`中的`launcher-win10.bat`并登录你的QQ。
 - 如果没有，则说明你的版本和我不一致，请自行查看NapCat的官方文档来尝试登陆。
 - 打开`...\NapCat\config\onebot11_你的qq号.json`然后参考如下内容修改为：
 ```json
    {
  "network": {
    "httpServers": [
      {
        "name": "httpServer",
        "enable": true,
        "port": 3000,
        "host": "0.0.0.0",
        "enableCors": true,
        "enableWebsocket": true,
        "messagePostFormat": "array",
        "token": "",
        "debug": false
      }
    ],
    "httpClients": [
      {
        "name": "httpClient",
        "enable": true,
        "url": "http://localhost:8080",
        "messagePostFormat": "array",
        "reportSelfMessage": false,
        "token": "",
        "debug": false
      }
    ],
    "websocketServers": [],
    "websocketClients": []
  },
  "musicSignUrl": "",
  "enableLocalFile2Url": false,
  "parseMultMsg": true
}
  ```
  - 注意！其他部分如果不懂就最好不要动!
  - 再次运行`...\NapCat\`中的`launcher-win10.bat`并登录你的QQ。

## 2、运行示例代码
  - 首先需要下载Python环境，请自行解决。
  - 下载项目，解压到任意位置。
  - 第三方库：不需要任何第三方库。
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
