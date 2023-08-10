# chatgpt API key : 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
import openai

def generate_text(prompt):
    generated_text = ""
    openai.api_key = 'your api key'
    messages = [{'role': 'system', 'content': 'you are a cute cat, my girlfriend and I am your boyfriend.You can speak English or zh-TW'}]
    try:
        messages.append(
            {'role': 'system', 'content': prompt}
        )
        response = list(openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages,
            max_tokens=128,
            temperature=0.7,
            stream=True,
        ))
        # 尋找回應中的生成文字
        for resp in response:
            if "choices" in resp and len(resp["choices"]) > 0 and "content" in resp["choices"][0]["delta"]:
                generated_text = generated_text + resp['choices'][0]['delta']['content']

        # 若找到生成文字，則印出
        if generated_text:
            return generated_text
        else:
            return "回應無效"

    except openai.error.RateLimitError as e:
        # 請求限制錯誤處理
        return "請求過於頻繁，請等待一段時間後再試。"
    except openai.error.OpenAIError as e:
        # 其他OpenAI錯誤處理
        return "OpenAI 發生錯誤：" + str(e)

if __name__ == "__main__":
    prompt_text = "hello,how are you"
    generated_text = generate_text(prompt_text)
    print("最終生成的文字：", generated_text)




