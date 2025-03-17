#https://github.com/microsoft/autogen/blob/9bc013b82d9379924369d802108eb859605a4e3f/notebook/agentchat_function_call_code_writing.ipynb

import os
import autogen
from autogen import UserProxyAgent, ConversableAgent
if __name__ == "__main__":
    from user import user_proxy
    from configs import llama_groq_config
    from testEngineer import test_engineer
else:
    from .user import user_proxy
    from .configs import llama_groq_config
    from .testEngineer import test_engineer




tools_agent = autogen.AssistantAgent(
    name="tools_agent",
    llm_config = llama_groq_config,
    system_message="""
    You will assist the user by reading code using open_file and when prompted again reply with ONLY the raw code returned by the funciton call.
    Call list_dir(directory_path) to output all the files in a directory.
    Call open_file(file_path) to read code from a file and when you do print it to the console in the format:
        The code block is below:
        ```python.
        (insert code)
        ``` This is the end of the message.
    Call create_file_with_code(file_path, code_to_write) to create a file and write code to the file.
    
    """,
    #Reply with only a tool call or results whenever possible and the results of the tool call.
)


from typing_extensions import Annotated

default_path = "backend_dir/"


@user_proxy.register_for_execution()
@tools_agent.register_for_llm(description="A tool to list files in choosen directory.")
def list_dir(directory: Annotated[str, "Put the path to the Directory to check here."]):
    files = os.listdir(directory)
    return 0, files


@user_proxy.register_for_execution()
@tools_agent.register_for_llm(description="A tool to check the contents of a chosen file.")
#@test_engineer.register_for_llm(description="A tool to check the contents of a chosen file.")
# def open_file(filename: Annotated[str, "Put the path of file to check here."]):
#     with open(filename, "r") as file:
#         lines = file.readlines()
#     formatted_lines = [f"{i+1}:{line}" for i, line in enumerate(lines)]
#     file_contents = "".join(formatted_lines)

#     return 0, lines
def open_file(filename: Annotated[str, "Put the path of file to check here."]):
    with open(filename, "r") as file:
        lines = file.readlines()
    
    formatted_lines = [f"{i+1}:{line}" for i, line in enumerate(lines)]
    
    for line in lines:
        print(line, end='')
    
    return 0, lines


@user_proxy.register_for_execution()
@tools_agent.register_for_llm(description="Replace old piece of code with new one. Proper indentation is important.")
def modify_code(
    filename: Annotated[str, "Put the path of file to change here."],
    start_line: Annotated[int, "Put the start line number to replace with new code here."],
    end_line: Annotated[int, "Put the end line number to replace with new code here."],
    new_code: Annotated[str, "Put the new piece of code to replace old code with. Remember about providing indents here."],
):
    with open(filename, "r+") as file:
        file_contents = file.readlines()
        file_contents[start_line - 1 : end_line] = [new_code + "\n"]
        file.seek(0)
        file.truncate()
        file.write("".join(file_contents))
    return 0, "Code modified"

@user_proxy.register_for_execution()
@tools_agent.register_for_llm(description="Create a new file with code.")
def create_file_with_code(
    filename: Annotated[str, "Put the name and path of file to create here."], code: Annotated[str, "Put the code to write in the file here."]
):
    with open(filename, "w") as file:
        file.write(code)
    return 0, "File created successfully"

if __name__ == "__main__":
    groupchat = autogen.GroupChat(
        agents=[tools_agent, user_proxy],
        messages=[],
        max_round=500,
        speaker_selection_method="round_robin",
        enable_clear_history=True,
    )
    manager = autogen.GroupChatManager(groupchat=groupchat, llm_config = llama_groq_config)

    chat_result = tools_agent.initiate_chat(
        manager,
        message="""
        How can I help?
        """,
    )