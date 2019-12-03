---
title: hexo图片不显示解决方法
categories: hexo
---
---
测试图片

<img src="hexo图片不显示解决方法/image-20191203133639628.png" alt="image-20191203133639628" style="zoom:50%;" />

## 解决方法

1. 下载最新版的typora, 在偏好设置中如下设置

   ![image-20191203133817604](hexo图片不显示解决方法/image-20191203133817604.png)

   这样就会图片就会自动保存在同名文件夹里. 用typora编辑所有md文档.

2.  找到`Hexo`下的`_config.yml`里的`post_asset_folder`，把这个选项从`false`改成`true`. 

3.  `npm install https://github.com/7ym0n/hexo-asset-image --save`(这是个修改过的插件，经测试无问题)

4. 清空缓存并且生成网页

   ```
   hexo cl
   hexo g -d
   ```

5. 打开服务

   ```
   hexo server
   ```

6. 去浏览器`localhost:4000`