为了能够使用matplotlib画图，必须要使用一个backken,不然显示不出图像。
在centos7中，如果python3是下载源码编译并安装的，那么应该使用：
‵‵‵shell
sudo yum install tkinter
‵‵‵
来安装`tkinter`,然后进入python3源码目录重新编译并安装python3

也可以使用另一种方法：
‵‵‵shell
sudo yum install python3-tkinter
‵‵‵
来安装python3以及tkinter
