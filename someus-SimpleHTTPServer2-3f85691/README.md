SimpleHTTPServer2
=================

改善python的SimpleHTTPServer模块，使得其在windows下支持中文路径


##基本使用
python自带SimpleHTTPServer模块以实现一个简单的服务器，例如：

	cd /home/www
	python -m SimpleHTTPServer

使用浏览器访问`http://127.0.0.1:8000`，即可访问/home/www下的内容。

在windows下也可以使用，但是对中文路径支持欠佳，这也就是SimpleHTTPServer2诞生的原因。SimpleHTTPServer2其实就是对SimpleHTTPServer略作些改动。

##安装SimpleHTTPServer2.py
以windows为例，假设python2.7安装路径为c:\python27\，将SimpleHTTPServer2.py放入c:\python27\Lib\下即可。

在使用时候可以这样：

	python -m SimpleHTTPServer2
	
也可以作为一个模块，整合到自己的程序中，server.py就是一个示例。

##关于server.py
server.py是一个使用了SimpleHTTPServer2.py的示例，其在运行时绑定了环回地址127.0.0.1，而非0.0.0.0。运行server.py后，其所在目录的内容将能够被浏览器通过`http://127.0.0.1:8000`访问。
