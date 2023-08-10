from ai import generate_text
from trans_v_to_t import speech_to_text
from vits_generator import generate_audio
from IPython.display import Audio




while(True):
    #語音轉文字
    text = speech_to_text()
    #chatgpt
    prompt_text = text
    generated_text = generate_text(prompt_text)
    #輸出
    print(generated_text)
    generate_audio(output_path="/content/VITS-fast-fine-tuning",
               model_path="/content/drive/MyDrive/继续训练Anny300/G_latest.pth",
               config_path="/content/drive/MyDrive/继续训练Anny300/finetune_speaker.json",
               language="English",
               text=generated_text,
               spkid=0,
               noise_scale=0.667,
               noise_scale_w=0.6,
               length_scale=1,
               output_name="output")
    output_audio_path = "/content/VITS-fast-fine-tuning/output.wav"  # 将路径替换为实际的音频文件路径
    Audio(output_audio_path)
    
    
    




