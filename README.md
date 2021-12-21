# frida-notes
断断续续学了点，汇总下

# frida安装

```
电脑：
python -m pip install frida
如果出现ERROR: Failed building wheel for frida 就去下面的链接下载一个对应的egg文件到当前用户目录 比如c:\users\administrator\，然后再执行上面的命令
https://pypi.org/project/frida/#files

坑点：要对应python版本 不然会报dll找不到 目前最高3.8（2021.12）

然后
python -m pip install frida-tools
```

![image-20211221142820025](README.assets/image-20211221142820025-16400693457831.png)

![image-20211221143712999](README.assets/image-20211221143712999-16400693457832.png)

```
手机或者模拟器：
先看手机架构
```

![image-20210826095823033](README.assets/image-20210826095823033-16400693457833.png)

下载对应版本 对应架构的frida-server：

![image-20210826100052140](README.assets/image-20210826100052140-16400693457844.png)

```
解压，重命名为frida-server 用adb复制到手机中 并且执行
adb push frida-server /data/local/tmp
adb shell "chmod 755 /data/local/tmp/frida-server"
adb shell "/data/local/tmp/frida-server &"

然而夜神模拟器这个安卓5.1版本的会报错，改成7.1版本的了
```

![image-20210826102614164](README.assets/image-20210826102614164-16400693457845.png)



# frida-dexdump（脱壳测试）

```
python -m pip install frida-dexdump
frida-dexdump -h
```

![image-20210826102752551](README.assets/image-20210826102752551-16400693457846.png)

```
先用frida-ps -U找到要导出的进程
frida 14统一用的包名，15开始有部分就是中文了 用中文那个
4126  酷安
```

![image-20210826103500438](README.assets/image-20210826103500438-16400693457847.png)

```
frida-dexdump -p 4126
```

![image-20210826104423990](README.assets/image-20210826104423990-16400693457848.png)

```
目标是 X-App-Token 编码过程

可疑dex：
0x94a87000.dex
0x9606f000.dex
```

![image-20210826111607140](README.assets/image-20210826111607140-16400693457849.png)

```

String replace = new Regex("\\r\\n|\\r|\\n|=").replace(sb3, "");
String as = AuthUtils.getAS(this.f5974, replace);

```

![image-20210826111633903](README.assets/image-20210826111633903-164006934578410.png)

![image-20210826112745220](README.assets/image-20210826112745220-164006934578511.png)

疑似在这里

![image-20210826113616930](README.assets/image-20210826113616930-164006934578512.png)



