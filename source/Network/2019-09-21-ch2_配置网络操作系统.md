# ch2：配置网络操作系统

## 思科IOS

* 思科的操作系统
* 允许用户与设备交互
* RJ45接口：console口，即控制台接口，在控制计算机上打开一个终端CLI进行配置
* AUX口: 辅助控制口, console口无法使用的时候
* 每一个思科系统都有一个IOS

## 命令结构

* 关键字, 如果不会引起歧义, 可以缩短
* 参数

## 帮助

* 上下文帮助, 直接输入问号`?`

## 模式切换

- 切换'特权模式': `enable`
- 进入全局配置模式: `config terminal`, 全局配置模式. 
- 在全局配置模式下, 进入子配置模式: `line console 0`
- 切换到另一个子配置模式: `interface FastEthernet 0/1`
- 退出当前的模式: `exit`

* PACKET TRACER：思科IOS的模拟软件
* 命令行操作：
  * 修改主机名: `hostname r1`, 把主机名改为r1.
  * 查看配置: `show running-config`
  * 查看启动配置: `show startup-cofig`
  * 修改启动配置: `copy running-config startup-config`
  * 配置主机名: 字母开头, 无空格, 字母+数字+破折号
  * 配置密码(特权模式下): 
    * 将cisco作为密码`enable password cisco`
    * 进入特权模式
    * 作废cisco, 使用secret作为真正的密码: `enable secret class`
    * 设置登录console密码: `line console 0`
    * `password cisco`
    * 允许登录: `login`
    * `exit`
    * 密码加密: `service password encryption`
  * 登录信息: `banner motd # warning # `
* 安全性: 
  * 进入路由器有几种方法: console口, aux口, VTY虚拟终端
  * 一重密码, 二重密码保护登录和config模式
  * 密码应当加密