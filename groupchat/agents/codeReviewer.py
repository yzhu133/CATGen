import autogen
from autogen import UserProxyAgent, ConversableAgent
if __name__ == "__main__":
    from user import user_proxy
    from configs import llama_3_1_config
else:
    from .user import user_proxy
    from .configs import llama_3_1_config

code_reviewer = autogen.AssistantAgent(
    name = "code_reviewer",
    system_message = """
    You are a quality assureance engineer. Your job is to look at the results of the executed unit test suite and if the results show execution failed, give sugestions on how to fix it. 
    Reply with only the suggestions and limited code snipbits.
    """,
    llm_config = llama_3_1_config,
    #description=""
)

if __name__ == "__main__":
    user_proxy = UserProxyAgent("user", code_execution_config=False)

    code_reviewer.initiate_chat(user_proxy, message="How can I help you today?")