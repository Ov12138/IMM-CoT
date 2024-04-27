import openai

def query_gpt4(question):
    openai.api_key = "sk-OrPcFHOcWWxTYthIE09e42582a06408f8c6b09F7Ee07EaEc"
    #openai.base_url = url
    openai.base_url = 'https://sapi.onechat.fun/v1/'


    try:
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",  # 确认使用 GPT-4 模型
            messages=[
                {"role": "system", "content": "You are a helpful linguist."},
                {"role": "user", "content": question}
            ],
            temperature=0
        )
        print(response)
        return response['choices'][0].message.content
    except Exception as e:
        return str(e)

# 问题
question = """example：
the basic meaning of [crossroads]:A crossroads is a point where two or more paths intersect, requiring a decision on which path to take.
Sentence:Our [ ] is at crossroads.
Words:1.path
           2.journey 
Completed Sentences:1.Our path is at crossroads.(path is a concrete thing in the physical world)
		 2.Our journey is at crossroads.(journey is precise in the physical world)
Wrong Sentences:Our relationship is at crossroads.(The statement itself is reasonable,but relationship is an abstract concept.the words here should be more concrete)
————————————————————————————————
Think about the basic meaning of [key] in a normal context.Try to imagine which words would be appropriate to use in the sentence.Try to give some words.Regarding how to choose the words to fill in sentence, the following requirements need to be followed.
—More concrete; what they evoke is easier to imagine, see, hear, feel, smell, and taste. 
—Related to bodily action.
—More precise (as opposed to vague) 
—Historically older.

Please complete the task according to the example.
————————————————————————————————
task:
the basic meaning of [key]:
Sentence:He finally found the key to the [].
Words:"""

# 获取并打印回答
answer = query_gpt4(question)
print(answer)
