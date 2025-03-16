# Hello there!


import autogen

llm_config = {
    "config_list": [
        {
            "model": "llama3-groq-tool-use",
            "base_url": "http://localhost:11434/v1",
            "api_key": "ollama",
        }
    ]
}

# llm_config = {
#     "config_list": [
#         {
#             "model": "gemma3",
#             "base_url": "http://localhost:11434/v1",
#             "api_key": "ollama",
#         }
#     ]
# }

engineer = autogen.AssistantAgent(
    name="Engineer",
    llm_config=llm_config,
    system_message="""
    I'm Engineer. I'm expert in python programming. I'm executing code tasks required by Admin.
    """,
)

user_proxy = autogen.UserProxyAgent(
    name="Admin",
    human_input_mode="ALWAYS",
    code_execution_config=False,
)

groupchat = autogen.GroupChat(
    agents=[engineer, user_proxy],
    messages=[],
    max_round=500,
    speaker_selection_method="round_robin",
    enable_clear_history=True,
)
manager = autogen.GroupChatManager(groupchat=groupchat, llm_config=llm_config)


from typing_extensions import Annotated

default_path = "backend_dir/"


@user_proxy.register_for_execution()
@engineer.register_for_llm(description="List files in choosen directory.")
def list_dir(directory: Annotated[str, "Put the path to the Directory to check here."]):
    files = os.listdir(directory)
    return 0, files


@user_proxy.register_for_execution()
@engineer.register_for_llm(description="Check the contents of a chosen file.")
def see_file(filename: Annotated[str, "Put the path of file to check here."]):
    with open(filename, "r") as file:
        lines = file.readlines()
    formatted_lines = [f"{i+1}:{line}" for i, line in enumerate(lines)]
    file_contents = "".join(formatted_lines)

    return 0, file_contents


@user_proxy.register_for_execution()
@engineer.register_for_llm(description="Replace old piece of code with new one. Proper indentation is important.")
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
@engineer.register_for_llm(description="Create a new file with code.")
def create_file_with_code(
    filename: Annotated[str, "Put the name and path of file to create here."], code: Annotated[str, "Put the code to write in the file here."]
):
    with open(filename, "w") as file:
        file.write(code)
    return 0, "File created successfully"



chat_result = user_proxy.initiate_chat(
    manager,
    message="""
You will need to modify extend the functionality of a script. For now, check out all the files, try to understand it and wait for next instructions.
""",
)