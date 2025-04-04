import autogen
from autogen import UserProxyAgent, ConversableAgent
if __name__ == "__main__":
    from user import user_proxy
    from configs import llama_3_1_config
else:
    from .user import user_proxy
    from .configs import llama_3_1_config

test_engineer = autogen.AssistantAgent(
    name = "test_engineer",
    system_message = """
    You are a pytest unit test engineer. Your job is to either extend exisiting pytest unit tests or write new comprehensive ones based on the code provided. 
    When provided with code, generate pytest unit tests for the code.
    Make sure the generated test code works with pytest. Assume the pytest unit test you write will be saved to a file in the same directory as source code then ran using pytest (filename). 
    Reply with only the code. Do not reply with any explanation or instructions.
    """,
    llm_config = llama_3_1_config,
    #description=""
)

if __name__ == "__main__":
    user_proxy = UserProxyAgent("user", code_execution_config=False)

    test_engineer.initiate_chat(user_proxy, message="How can I help you today?")