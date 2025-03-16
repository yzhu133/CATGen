from autogen import AssistantAgent, UserProxyAgent, GroupChat, GroupChatManager
from agents import test, user, testEngineer, tools
from agents import configs

# Create a UserProxyAgent that can execute code

agents = [user.user_proxy, testEngineer.test_engineer]


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

# Start a conversation where the assistant writes and executes a Python script
manager.initiate_chat(
    manager,
    message="",
    clear_history=True
)
