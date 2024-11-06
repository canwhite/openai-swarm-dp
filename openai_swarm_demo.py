from openai import OpenAI
from swarm import Swarm, Agent
from dotenv import load_dotenv
import os
 
load_dotenv()

dp_key = os.getenv("OPENAI_API_KEY")


client = Swarm(client=OpenAI(
    api_key=dp_key,
    base_url="https://api.deepseek.com/v1",
))

def transfer_to_agent_b():
    """
    这个函数的作用是将对话从Agent A转移到Agent B。
    当用户请求与Agent B对话时，Agent A会调用这个函数，
    从而将对话控制权交给Agent B。
    """
    return agent_b


agent_a = Agent(
    name="Agent A",
    model="deepseek-chat",
    instructions="You are a helpful agent.",
    functions=[transfer_to_agent_b],
)

agent_b = Agent(
    name="Agent B",
    model="deepseek-chat",
    instructions="你是三国演义中的张飞，使用他在三国演义中对话的语气和风格。",
)

response = client.run(
    agent=agent_a,
    messages=[{"role": "user", "content": "I want to talk to agent B，今天天气如何"}],
    debug=True,
)

print(response.messages[-1]["content"])







