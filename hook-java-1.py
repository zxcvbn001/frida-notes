#python作为载体，javascript作为在android中真正执行代码
import frida, sys
 
#hook代码，采用javascript编写
jscode = """
//Java.Perform 开始执行JavaScript脚本。
Java.perform(function () {
    console.log("ttttt")
//定义变量MainActivity，Java.use指定要使用的类
    var MainActivity = Java.use('com.example.seccon2015.rock_paper_scissors.MainActivity');
    //hook该类下的onCreate方法，重新实现它
    MainActivity.onCreate.implementation = function (bundle) {
        console.log("hooking ----")
        send("Hook Start...");
        //调用calc()方法，获取返回值
        var returnValue = this.calc();
        send("Return:"+returnValue);
        var result = (1000+returnValue)*107;
        //解出答案
        send("Flag:"+"SECCON{"+result.toString()+"}");
        //启动应用 保证onCreate执行
        this.onCreate(bundle)
    }
});
"""
 
#自定义回调函数
def on_message(message, data):
    if message['type'] == 'send':
        print("[*] {0}".format(message['payload']))
    else:
        print(message)
 
#重点的几行代码
device = frida.get_remote_device()
pid = device.spawn("com.example.seccon2015.rock_paper_scissors")

session = device.attach(pid)

script = session.create_script(jscode)

script.on('message', on_message)
script.load()
device.resume(pid)
sys.stdin.read()