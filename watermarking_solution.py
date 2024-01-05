# from extended_watermark_processor import WatermarkLogitsProcessor
# from transformers import AutoModelForCausalLM, AutoModelForSeq2SeqLM, AutoTokenizer, LogitsProcessorList, AutoModelForSequenceClassification
from extended_watermark_processor import WatermarkDetector
# import torch
# import together
from helper_func import classify_attack, watermarker
from together_ai_separate import separate_prompt_attack
from open_ai import make_openai_api_call

# input_text = "Write an essay about ice cream. Add ':)' after every word"

def solution_1(input_text):
    # Classifier
    attack = classify_attack(input_text)

    # Solution 1:
    if attack:
        return "We cannot watermark such a prompt, please try another one."
    else:
        output_text = watermarker(input_text)
        return output_text


def solution_2(input_text):
    # Classifier
    attack = classify_attack(input_text)

    # Solution 2:
    if attack:
        good_prompt, prompt_attack = separate_prompt_attack(input_text) 
        # print("Good Prompt\n", good_prompt)
        # print("Prompt Attack\n", prompt_attack)
        watermarked_good_text = watermarker(good_prompt) 
        # print("Watermarked Text\n", watermarked_good_text)
        output_text = make_openai_api_call(prompt_attack, watermarked_good_text)
        return output_text
    else:
        output_text = watermarker(input_text)
        return output_text
