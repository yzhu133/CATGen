#https://microsoft.github.io/autogen/0.2/docs/tutorial/code-executors/

import tempfile

from autogen import ConversableAgent
from autogen.coding import LocalCommandLineCodeExecutor

# Create a temporary directory to store the code files.
temp_dir = tempfile.TemporaryDirectory()

# Create a local command line code executor.
executor = LocalCommandLineCodeExecutor(
    timeout=10,  # Timeout for each code execution in seconds.
    work_dir=temp_dir.name,  # Use the temporary directory to store the code files.
)

# Create an agent with code executor configuration.
code_executor_agent = ConversableAgent(
    "code_executor_agent",
    llm_config=False,  # Turn off LLM for this agent.
    code_execution_config={"executor": executor},  # Use the local command line code executor.
    human_input_mode="ALWAYS",  # Always take human input for this agent for safety.
)
if __name__ == "__main__":
    message_with_code_block = """This is a message with code block.
    The code block is below:
    ```python
    for i in range(5):
        print("Hello there this is time i.")
    ```
    This is the end of the message.
    """

    # Generate a reply for the given code.
    reply = code_executor_agent.generate_reply(messages=[{"role": "user", "content": message_with_code_block}])
    print(reply)