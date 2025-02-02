import os

import qianfan

# 【推荐】使用安全认证AK/SK鉴权，通过环境变量初始化认证信息
# 替换下列示例中参数，安全认证Access Key替换your_iam_ak，Secret Key替换your_iam_sk
os.environ["QIANFAN_ACCESS_KEY"] = ""
os.environ["QIANFAN_SECRET_KEY"] = ""

chat_comp = qianfan.ChatCompletion()


def llm(content):
    return chat_comp.do(model="Yi-34B-Chat", messages=[{
        "role": "user",
        "content": "假如你是一个美食推荐专家，对食堂中的美食进行个性化推荐，可选食堂包括"
                   "{学一食堂，学二食堂，学三食堂，学四食堂，学五食堂，沙西第一食堂，沙西第二食堂，学院路清真食堂，沙河清真食堂，教工食堂，沙东一层食堂，沙东二层食堂，鼓瑟轩，新北地下一层食堂，新北二层食堂，新北三层食堂}。"
                   "接下来给你一个样例，提供格式参考，但不要完全根据样例给出内容，样例为{user: 我今天想吃香锅。agent：如果您想吃香锅的，可以选择新北二层食堂的麻辣香锅或者学三食堂的成都冒菜，两个的口味都非常不错。+再简要介绍一下香锅}（总共约100字）"
                   "现在，用户的询问为：" + content,
    }])


def getLLMresponse(content: str):
    resp = llm(content)
    answer = resp["body"]["result"]

    return answer


if __name__ == "__main__":
    print(getLLMresponse("猪脚"))
