from elastalert.enhancements import BaseEnhancement
import re


class Extract_Requestid(BaseEnhancement):

    # The enhancement is run against every match
    # The match is passed to the process function where it can be modified in any way
    # ElastAlert will do this for each enhancement linked to a rule
    def process(self, match):
        # 定义正则表达式模式
        pattern = r"\b[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}\b"

        # 检查 'message' 字段是否存在于match中
        if 'message' in match:
            log_message = match['message']
            match_obj = re.search(pattern, log_message)
            if match_obj:
                match['extract_requestid'] = match_obj.group(0)
            else:
                match['extract_requestid'] = "request id not found"
