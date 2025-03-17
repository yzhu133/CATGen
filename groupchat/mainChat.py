from autogen import AssistantAgent, UserProxyAgent, GroupChat, GroupChatManager
from agents import configs
from agents import user, testEngineer, tools, codeExecutor, requirements, critic

agents = [user.user_proxy, tools.tools_agent, testEngineer.test_engineer, codeExecutor.code_executor_agent, requirements.requirement_writer, critic.critic]


group_chat = GroupChat(
    agents=agents,
    messages=[],
    max_round=20,
    speaker_selection_method="manual",
    allow_repeat_speaker=None,
    speaker_transitions_type="allowed",
    )

manager = GroupChatManager(
    groupchat=group_chat,
    llm_config=configs.gemma3_config,
    is_termination_msg=lambda x: x.get("content", "") and x.get("content", "").rstrip().endswith("TERMINATE"),
    code_execution_config=False,
)

user.user_proxy.initiate_chat(
    manager,
    message="Make a tool call to view the contents of the file located in testings/mainTest.py then reply with the code.",
    clear_history=True
)
