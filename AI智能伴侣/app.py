import streamlit as st
import os
from openai import OpenAI


#设置页面的配置项
st.set_page_config(
    page_title="周环的AI智能伴侣",
    page_icon="😊",
    layout="wide",
    menu_items={
        "About":"https://www.baidu.com/",
        "Get help":"https://www.cmit.cn/",
        "Report a bug":"https://www.cmit.cn/",
    }
)

# 添加大标题
st.title("周环的AI智能伴侣")

# 设置logo，如果版本报错就注释这一行
# st.logo(".streamlit/古遗迹.png")
# 初始化聊天记录
if "messages" not in st.session_state:
    st.session_state.messages = []
# 展示聊天信息
for message in st.session_state.messages:
    # if message["role"] == "user":
    #     st.chat_message("user").write(message["content"])
    # elif message["role"] == "assistant":
    #     st.chat_message("assistant").write(message["content"])
    st.chat_message(message["role"]).write(message["content"])# 展示聊天信息
#系统提示词
system_prompt = "你是一个温柔的助手，说话很温柔，回答用户的时候一定要以温柔的态度回答"
# 用户输入的提示词
prompt = st.chat_input("请输入您的问题")
if prompt: # 如果用户输入了问题，则进行响应
    st.chat_message("user").write(f"您输入的问题是：{prompt}")
    print("用户输入的问题是：", prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})
    # 调用大模型
    client = OpenAI(
        api_key=os.environ.get('AI1API_API_KEY'),# 从环境变量中获取API密钥
        base_url="https://ai1api.com/v1",  # 使用主域名
    )
    print([
            {"role": "system", "content": system_prompt},
            *st.session_state.messages,
        ])
    response = client.chat.completions.create(
        model="gpt-5.5",
        messages=[
            {"role": "system", "content": system_prompt},
            *st.session_state.messages,
        ],
        stream=True,
    )
    # # 非流式输出方式
    # st.chat_message("assistant").write(response.choices[0].message.content)
    # print("模型的响应是：", response.choices[0].message.content)

    # 流式输出
    response_message = st.empty()
    full_response = ""
    for chunk in response:
        if chunk.choices and len(chunk.choices) > 0: # 如果有choices且长度大于0
            delta = chunk.choices[0].delta # 获取delta对象
            if delta and delta.content is not None: # 如果有delta且内容不为空
                full_response += delta.content # 累加内容
                response_message.write(full_response) # 展示响应内容
    # 保存ai返回的结果
    st.session_state.messages.append({"role": "assistant", "content":full_response})
