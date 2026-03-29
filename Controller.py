import dashscope


def request_API(single_content, video_head, video_source, video_attitude):
    if video_attitude == 1:
        response = dashscope.Generation.call(model=dashscope.Generation.Models.qwen_turbo,
                                             prompt='# 角色设定:你现在是一名文本情感分析打分专家。'
                                                    '# 任务:你需要对这条短视频的评论进行分析，判断评论是否支持生育。'
                                                    '# 分析要求:'
                                                    f'## 使用以下评分标准对这条短视频下的这个评论，{single_content}，进行评分'
                                                    '0表示反对生育; 1表示支持生育; 5表示中立'
                                                    '(必须且仅只能回复0 或者1 或者5 这样的整数) '
                                                    '# 特殊情况: '
                                                    '## 如果评论中包含符号或表情，请根据视频标题，视频态度等上下文具体情况分析其情感分数。'
                                                    '## 如果评论中出现“赞同”、“支持”、“羡慕”、“有道理”、“说的真对”、“明白”、“想生”、'
                                                    '“想要生一个娃”、“想结婚”、“自私自利” 、“中药” 等词汇，'
                                                    '故应判断为支持生育，回答1。'
                                                    '## 如果评论中出现“理解”、“尊重”、“无所谓”、“不关我事”、'
                                                    '“个人选择”、“自己决定”等词汇，故应判断为中立，回答5。'
                                                    '## 如果评论中出现“不结婚”、“不生”、“不敢生”、“没必要”、“不婚不育保平安”、“不嫁人”、“单身快乐”、'
                                                    '“清醒”、“压力大”、“不需要”，故应判断为反对生育，回答 0'
                                                    f'# 待分析评论: {single_content}'
                                                    '# 输出格式:仅输出“支持度分数为  ?')

        if response.output and response.output.get('text') is not None:
            print(response.output['text'])
        else:
            response.output = {'text': 'No Response'}
            print('********************* No Response *********************')
        return response.output['text']

    elif video_attitude == 0:
        response = dashscope.Generation.call(model=dashscope.Generation.Models.qwen_turbo,
                                             prompt='# 角色设定:你现在是一名文本情感分析打分专家。'
                                                    '# 任务:你需要对这条短视频的评论进行分析，判断评论是否支持生育。'
                                                    '# 分析要求:'
                                                    f'## 使用以下评分标准对这条短视频下的这个评论，{single_content}，进行评分'
                                                    '0表示反对生育; 1表示支持生育；5表示中立'
                                                    '(必须且仅只能回复0 或者1 或者5 这样的整数) '
                                                    '# 特殊情况: '
                                                    '## 如果评论中包含符号或表情，请根据视频标题，视频态度等上下文具体情况分析其情感分数。'
                                                    '## 如果评论中出现“赞同”、“支持”、“羡慕”、“有道理”、“说的真对”、“明白”、'
                                                    '“不结婚”、“不生”、“不敢生”、“没必要”、“不婚不育保平安”、“不嫁人”、“单身快乐”、'
                                                    '“清醒”、“压力大”、“不需要”等词汇，'
                                                    '故应判断为反对生育，回答0。'
                                                    '## 如果评论中出现“理解”、“尊重”、“不关我事”、“无所谓”、“不关我事”、“个人选择”、“自己决定”、“这个社会，想结就结，'
                                                    '不想结就不结。任何一条路都有辛酸有幸福“ 等词汇，故应判断为中立，回答5。'
                                                    '## 如果评论中出现“想生”、“想要生一个娃”、“想结婚”、“自私自利” 、“中药”，故应判断为支持生育， 回答 1。'
                                                    f'# 待分析评论: {single_content}'
                                                    '# 输出格式:仅输出“支持度分数为  ?')

        if response.output and response.output.get('text') is not None:
            print(response.output['text'])
        else:
            response.output = {'text': 'No Response'}
            print('********************* No Response *********************')
        return response.output['text']
    else:
        print('********************* ERROR ERROR ERROR *********************')
