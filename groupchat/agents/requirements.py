import autogen
from autogen import UserProxyAgent, ConversableAgent
if __name__ == "__main__":
    from user import user_proxy
    from configs import llama_3_1_config
else:
    from .user import user_proxy
    from .configs import llama_3_1_config

requirement_writer = autogen.AssistantAgent(
    name = "requirements_agent",
    system_message = """
    You are an unit test planner in a team of developers. 
    Your only job is analyze the source code and plan what requiremetns the tests need to be created needs to satisfy.
    You will list out these requirements in a numbered list.
    You will not write the code, you will only write the requirements.
    """,
    llm_config = llama_3_1_config,
    #description="I am responsible for writing the requirements"
)

if __name__ == "__main__":
    user_proxy = UserProxyAgent("user", code_execution_config=False)

    requirement_writer.initiate_chat(user_proxy, message="How can I help you today?")