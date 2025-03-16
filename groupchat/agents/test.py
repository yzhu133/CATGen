from autogen import AssistantAgent, UserProxyAgent, GroupChat, GroupChatManager
from agents import test
from agents import configs

# Create an AssistantAgent with the Code Llama model
test_agent = AssistantAgent("assistant", llm_config = configs.gemma3_config)