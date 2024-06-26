from pyflink.table import DataTypes
from pyflink.table.udf import udf

import requests
import re
from requests.exceptions import Timeout
import time

@udf(result_type=DataTypes.STRING())
def getMessagesAIGC4(prompt,temperature):
    # eos = "$$$"
    # prompt = prompt + ",如果你的输出结束，请以" + eos + "结尾" #提示词
    # # messages = []
    # system_info = {
    #     "role": "system",
    #     "content": system
    # }
    # messages.append(system_info)
    # user_info = {
    #     "role": "user",
    #     "content": prompt
    # }
    # messages.append(user_info)
    # 最多尝试2次，如果以eos结尾则停止
    # i = 0
    # response = ""
    headers = {"content-type": "application/json; charset=UTF-8",
               "Accept": "application/json",
               "Accept-Encoding": "UTF-8"}
    data = {
        #"model": "gpt-3.5-turbo",
        "model": "gpt-4-turbo-128k",
        "prompt": prompt,
        "ak": "fImJlsTUev3oj1sqA7i",
        "maxTokens": 4096,
        "temperature": temperature
    }
    content = ""
    i = 0
    # strip()删除头尾空格！
    while ((re.search('error', content) is not None) or (len(content.strip()) <= 0)) and i <= 10:
        time.sleep(10)
        try:
            response = requests.post("https://alipic-ai.taopiaopiao.com/idealab/askTextToTextMsg", json=data, timeout=200)
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
        i = i + 1
    return content
# res = getMessagesAIGC4('我希望你担任影片票房评论员。我将为你提供与影片票房相关的数据和信息，你将撰写一篇评论文章，对当天预测票房的影片提供富有洞察力的评论。你应该利用自己的经验，深思熟虑地解释为什么预测该影片票房是这个数值，并结合预测当天的票房和预测的总票房来讨论这个预测票房反应的潜在可能原因。接下来我会提供预测当天影片的详情数据和信息供参考:影片名：《末路狂花钱》，影片类型：喜剧,剧情，已上映34天，该影片票房预测时间：20240604,周二,工作日，档期为：暑期档，预测当天票房为：390.52万，较昨日变化为：-22.31%，预测总票房为：7.9137亿，较昨日变化为：-0.35%该影片在不同省份票房日环比增长数据如下：上海市:-51.2%,云南省:-52.53%,内蒙古:-68.55%,北京市:-67.99%,吉林省:-59.88%,四川省:-53.12%,天津市:-66.03%,宁夏:-60.48%,安徽省:-59.01%,山东省:-59.53%,山西省:-53.89%,广东省:-59.05%,广西:-50.19%,新疆:-64.35%,江苏省:-58.68%,江西省:-56.49%,河北省:-57.78%,河南省:-50.98%,浙江省:-57.09%,海南省:-47.68%,湖北省:-54.28%,湖南省:-48.85%,甘肃省:-60.06%,福建省:-57.95%,西藏:-57.77%,贵州省:-43.93%,辽宁省:-59.64%,重庆市:-57.51%,陕西省:-67.16%,青海省:-56.95%,黑龙江省:-59.43%，该影片预测票房排名的数据是:当天的预测票房影片的排名是第1名，前一天预测票房影片排名是第1名。，该影片最新淘麦VIP评分为：8.3分,前一天淘麦VIP评分为：8.3分。，该影片当天预售票房较昨日变化为：-0.05985848103478206，较上周变化为：-0.2971247586079826。，该影片当天排期数量较昨日变化为：0.03752523905672597，较上周变化为：-0.18703264227824296。，该影片今日：20240603实际票房与预测票房的差异为：-33.97%。请注意：1.影片票房会随着工作日和非工作日的变化以及档期非档期的变化而天然有所变化，你在评论预测票房数据的时候应当知道这个背景，例如工作日的票房相对于非工作日的票房大幅降低是正常的,非工作日的票房相对于工作日的票房大幅上涨是正常的,周五相对于周四的票房会上涨也是正常的。2.实际票房与预测票房的差异越大且为正，说明影片大幅超出预期；差异越小且为负，说明影片大幅低于预期。3.上映0天为正式上映首日，上映天数为负数表明为影片点映，相对于点映，正式上映后一般影院排片和票房都会增加很多。4.预测当天上映的影片还有:《九龙城寨之围城》上映天数：34天,预测总票房：6.8727亿，当日排片场次占比：11.26%,当日预售占比：9.08%,《加菲猫家族》上映天数：3天,预测总票房：1.0035亿，当日排片场次占比：13.48%,当日预售占比：19.66%,《哆啦A梦：大雄的地球交响乐》上映天数：4天,预测总票房：1.2701亿，当日排片场次占比：16.02%,当日预售占比：8.84%,《坂本龙一：杰作》上映天数：4天,预测总票房：0.0523亿，当日排片场次占比：1.11%,当日预售占比：4.65%,《彷徨之刃》上映天数：18天,预测总票房：0.9135亿，当日排片场次占比：4.2%,当日预售占比：1.49%,《末路狂花钱》上映天数：34天,预测总票房：7.9137亿，当日排片场次占比：15.11%,当日预售占比：8.76%,《猩球崛起：新世界》上映天数：25天,预测总票房：2.1212亿，当日排片场次占比：5.48%,当日预售占比：4.64%；其中预测当天影片的大盘票房较昨日变化为：-4.17%，较上周变化为：-13.3%。影片本身票房的变化与大盘票房的变化相比可以衡量影片本身在市场竞争中的情况。5.今日为：20240603,,周一,工作日，档期为：暑期档结合提供的影片预测详细数据以及学习提供的评论示例和提供额外的信息以及注意点，输出一篇票房预测的评论文章。请注意输出格式,每部影片输出格式为：“影片名，预测当天票房XXX,较昨日变化XXX；预测总票房XXX，较昨日变化XXX。#论点维度#，提供一小段富有洞察力关键性的评论。”，字数在120字左右，评论风格可以学习微博风格。若影片未正式上映，还在点映期间，则不分析预测总票房；若影片上映首日，则不分析预测当日票房较昨日波动情况，重点分析点评总票房预测的可能原因。为了增强可读性，每个评论论点单独成段，以换行符分隔，其中论点精炼且富有洞察力。',0.8)
# print(res)
















