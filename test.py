#python作为载体，javascript作为在android中真正执行代码
import frida, sys
 
#hook代码，采用javascript编写
jscode = """
Java.perform(function () {
        if(Java.available)
        {
            //console.log("",Java.androidVersion);
            //枚举当前加载的所有类
            Java.enumerateLoadedClasses({
                //每一次回调此函数时其参数className就是类的信息
                onMatch: function (className)
                {
                    //输出类字符串
                    console.log("",className);
                },
                //枚举完毕所有类之后的回调函数
                onComplete: function ()
                {
                    //输出类字符串
                    console.log("输出完毕");
                }
            });
        }else{
            console.log("error");
        }
    });
"""
 
#自定义回调函数
def on_message(message, data):
    if message['type'] == 'send':
        print("[*] {0}".format(message['payload']))
    else:
        print(message)
 
#重点的4行代码 别用get_usb_device方法了 改用get_remote_device
process = frida.get_remote_device().attach('酷安')
script = process.create_script(jscode)
script.on('message', on_message)
script.load()
sys.stdin.read()