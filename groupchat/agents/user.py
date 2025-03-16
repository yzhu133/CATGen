import autogen
from autogen import UserProxyAgent, ConversableAgent
import configs

user_proxy = autogen.UserProxyAgent(
    name="User",
    human_input_mode = "ALWAYS",
    code_execution_config=False,
)