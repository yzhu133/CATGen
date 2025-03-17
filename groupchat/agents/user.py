import autogen
from autogen import UserProxyAgent, ConversableAgent

user_proxy = autogen.UserProxyAgent(
    name="User",
    human_input_mode = "ALWAYS",
    code_execution_config=False,
)