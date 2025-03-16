import autogen
from autogen import UserProxyAgent, ConversableAgent
import configs

test_engineer = autogen.AssistantAgent(
    name = "test_engineer",
    system_message = """
    You are a unit test engineer. Your job is to either extend exisiting unit tests or write new comprehensive ones based on the code provided. 
    Make sure the generated test code works with pytest. 
    Reply with only the code. Do not reply with any explanation or instructions.
    """,
    llm_config = configs.gemma3_config,
    #description=""
)

if __name__ == "__main__":
    user_proxy = UserProxyAgent("user", code_execution_config=False)

    test_engineer.initiate_chat(user_proxy, message="How can I help you today?")