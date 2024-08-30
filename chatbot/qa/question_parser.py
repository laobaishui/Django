from function_tool import chat_wit_ai
from client.clientfactory import Clientfactory
from prompt_templates import get_question_parser_prompt
from purpose_type import purpose_map
from icecream import ic
from purpose_type import userPurposeType

def parse_question(question: str) -> userPurposeType:
    # 在这个函数中我们使用大模型去判断问题类型
    prompt = get_question_parser_prompt(question)
    response = Clientfactory().get_client().chat_with_ai(question)

    if response is None:
        return "其他"
    purpose_type = purpose_map[response]
    ic(purpose_type)

    return purpose_type



    
