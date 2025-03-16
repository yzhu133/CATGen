import autogen
from autogen import UserProxyAgent, ConversableAgent
import configs

critic = autogen.AssistantAgent(
    name = "critic",
    system_message = """
    You are a unit test critic. Your job is to review the newly generated unit tests and give suggestions on how to improve them. 
    Reply with only the suggestions.
    """,
    llm_config = configs.gemma3_config,
    #description=""
)

if __name__ == "__main__":
    user_proxy = UserProxyAgent("user", code_execution_config=False)

    critic.initiate_chat(user_proxy, message="How can I help you today?")