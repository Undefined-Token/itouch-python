# 测试已发布的 itouch-auto 包
# 安装: pip install itouch-auto
# 导入: from itouch import client as itclient

from itouch import client as itclient
import time

def test():
    print('开始测试连接...')
    
    # 创建客户端实例，连接到 192.168.31.15
    client = itclient({
        'host': '192.168.31.15',
        'port': 23188
    })

    # 注册 device:online 事件监听器
    client.on('device:online', lambda data: print('收到 device:online 事件:', data))

    # 注册 device:offline 事件监听器
    client.on('device:offline', lambda data: print('收到 device:offline 事件:', data))

    print('正在连接到 ws://192.168.31.15:23188...')
    client.connect()
    print('连接成功!')
    print('等待 device:online 和 device:offline 事件...')

    # 测试 sendKey 命令
    print('测试 sendKey 命令...')
    result = client.invoke("sendKey", {
        'deviceId': 'P60904DC8D3F',
        'key': 'h',
        'fnkey': 'COMMAND'
    })
    print('sendKey 调用结果:', result)

    # 测试 getScreenShot 命令
    print('测试 getScreenShot 命令...')
    screenshot_result = client.invoke("getScreenShot", {
        'deviceId': 'P60904DC8D3F'
    })
    
    # 如果返回的是二进制数据，直接保存到文件
    if screenshot_result:
        with open('screenshot.png', 'wb') as f:
            f.write(screenshot_result)
        print('截图已保存到 screenshot.png (直接二进制)')
    
    # client.destroy()
    
    print('客户端已销毁')

if __name__ == '__main__':
    test()

    while True:
        time.sleep(1)
