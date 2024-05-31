# from odps.udf import annotate
import  sys
sys.path.insert(0, "work/power_forcasting-depends.tar.gz/__pypackages__")
import requests

# @annotate("string,string,double->string")
class getMessagesAIGC4(object):

    def post_gpt4(self,messages,temperature):
        headers = {"content-type": "application/json; charset=UTF-8",
        "Accept": "application/json",
           "Accept-Encoding": "UTF-8"} 

        data = {
            # "model": "gpt-4-turbo-128k",
            "model": "gpt-3.5-turbo", # 测试用 gpt-4-turbo太贵了
            "messages": messages,
            "ak":"fImJlsTUev3oj1sqA7i",
            "maxTokens":4096,
            "temperature":temperature
            }
        content = "" 
        try:
            response = requests.post("https://alipic-ai.taopiaopiao.com/idealab/askTextToTextMsg", json=data,timeout = 200)
            # response.raise_for_status()  # 如果状态码不是200，将抛出HTTPError
            response = response.json()
            content = ""
            if response['code'] == '200':
                content = response['data']['data']['content']
            else:
                print('Error:', response['code'])
                content = "error"
        except:
            content = "error,调用接口超时。"

        return content

    def post_gpt4_raise_error(self,messages,temperature):
        headers = {"content-type": "application/json; charset=UTF-8",
        "Accept": "application/json",
           "Accept-Encoding": "UTF-8"} 

        data = {
            "model": "gpt-4-turbo-128k",
            "messages": messages,
            "ak":"fImJlsTUev3oj1sqA7i",
            "maxTokens":4096,
            "temperature":temperature
            }
        content = "" 
        response = requests.post("https://alipic-ai.taopiaopiao.com/idealab/askTextToTextMsg", json=data,timeout = 200)
        # response.raise_for_status()  # 如果状态码不是200，将抛出HTTPError
        response = response.json()
        content = ""
        if response['code'] == '200':
            content = response['data']['data']['content']
        else:
            print('Error:', response['code'])
            content = "error"

        return content

    def evaluate(self,system, prompt,temperature):
        eos = "$$$"
        prompt = prompt + ",如果你的输出结束，请以"+eos+"结尾"
        messages = []
        system_info = {
            "role" : "system",
            "content" : system
        }
        messages.append(system_info)

        user_info = {
             "role" : "user",
             "content" : prompt
        }
        messages.append(user_info)
        # 最多尝试2次，如果以eos结尾则停止
        i=0 
        response = ""
        response = self.post_gpt4(messages,temperature)
        return response

