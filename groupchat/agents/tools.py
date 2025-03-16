import os
import autogen
from autogen import UserProxyAgent, ConversableAgent
import configs
import user



tools_agent = autogen.AssistantAgent(
    name="tools_agent",
    llm_config = configs.llama_groq_config,
    system_message="""
    You will assist the user by making tool calls only.
    Call list_dir(directory_path) to output all the files in a directory."
    Call open_file(file_path) to read code from a file.
    Reply with only a tool call whenever possible and the results of the tool call.
    """,
)


from typing_extensions import Annotated

default_path = "backend_dir/"


@user.user_proxy.register_for_execution()
@tools_agent.register_for_llm(description="A tool to list files in choosen directory.")
def list_dir(directory: Annotated[str, "Put the path to the Directory to check here."]):
    files = os.listdir(directory)
    return 0, files


@user.user_proxy.register_for_execution()
@tools_agent.register_for_llm(description="A tool to check the contents of a chosen file.")
def open_file(filename: Annotated[str, "Put the path of file to check here."]):
    with open(filename, "r") as file:
        lines = file.readlines()
    formatted_lines = [f"{i+1}:{line}" for i, line in enumerate(lines)]
    file_contents = "".join(formatted_lines)

    return 0, file_contents


@user.user_proxy.register_for_execution()
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

@user.user_proxy.register_for_execution()
@tools_agent.register_for_llm(description="Create a new file with code.")
def create_file_with_code(
    filename: Annotated[str, "Put the name and path of file to create here."], code: Annotated[str, "Put the code to write in the file here."]
):
    with open(filename, "w") as file:
        file.write(code)
    return 0, "File created successfully"

if __name__ == "__main__":
    groupchat = autogen.GroupChat(
        agents=[tools_agent, user.user_proxy],
        messages=[],
        max_round=500,
        speaker_selection_method="round_robin",
        enable_clear_history=True,
    )
    manager = autogen.GroupChatManager(groupchat=groupchat, llm_config = configs.llama_groq_config)

    chat_result = tools_agent.initiate_chat(
        manager,
        message="""
        How can I help?
        """,
    )