import autogen
from autogen import UserProxyAgent, ConversableAgent
if __name__ == "__main__":
    from user import user_proxy
    from configs import llama_3_1_config
else:
    from .user import user_proxy
    from .configs import llama_3_1_config

critic = autogen.AssistantAgent(
    name = "critic",
    system_message = """
    You are a unit test critic. Your job is to review the newly generated unit tests and give suggestions on how to improve them. 
    Reply with only the suggestions.1
    """,
    llm_config = llama_3_1_config,
    #description=""
)

if __name__ == "__main__":
    user_proxy = UserProxyAgent("user", code_execution_config=False)

    critic.initiate_chat(user_proxy, message="How can I help you today?")