#!/user/bin/evn python3
# -*- coding: utf-8 -*-
import urllib.request

answer = True

def getRobotReply(question):
    '''
    函数功能：对于特定问题进行特定回复，对于非特定的问题进行智能回复
    参数描述：
    question 聊天内容或问题

    返回值：str，回复内容
    '''
    if "你叫什么名字" in question: #成员运算符 in 
        answer = "我是君哥"
    elif "你多少岁" in question:
        answer = "18"
    elif "我还有多少钱" in question:
        answer = "5块钱"
    elif "你是GG还是MM" in question:
        answer = "GG"
    else:
        try:
            # 调用NLP接口实现智能回复
            params = urllib.parse.urlencode({'msg': question}).encode() # 接口参数需要进行URL编码
            req = urllib.request.Request("http://api.itmojun.com/chat_robot", params, method="POST") # 创建请求，参数是一个字典
            answer = urllib.request.urlopen(req).read().decode() # 调用接口（即向目标服务器发出HTTP请求，并获取服务器响应）
        except Exception as e:
            answer = "AI机器人出现故障（原因：%s ）" % e
    return answer

def duihua():
        while True:
            question = input("\n我说：")
            answer = getRobotReply(question)
            print("\n小魔仙说：%s" %answer)
        


if __name__ == '__main__':
    # 测试
    duihua()




