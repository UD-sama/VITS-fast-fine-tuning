from ai import generate_text
from trans_v_to_t import speech_to_text
from t_to_v import text_to_speech
from yating import aitts




while(True):
    #語音轉文字
    text = speech_to_text()
    #chatgpt
    prompt_text = text
    generated_text = generate_text(prompt_text)
    #輸出
    print(generated_text)
    aitts(generated_text)
    #tts_fn(model, hps, speaker_ids)


