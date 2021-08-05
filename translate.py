from transformers import MarianTokenizer, MarianMTModel
from config import *

model_name = f'opus-mt-{SOURCE_LANG}-{TARGET_LANG}'

def load_model():
    tokenizer = MarianTokenizer.from_pretrained(model_name)
    model = MarianMTModel.from_pretrained(model_name)      
    return model, tokenizer

def translate(text):
    model, tokenizer = load_model()
    translated = model.generate(**tokenizer.prepare_seq2seq_batch([text]))
    tgt_text = [tokenizer.decode(t, skip_special_tokens=True) for t in translated]
    return tgt_text[0]