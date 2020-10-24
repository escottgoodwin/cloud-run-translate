from transformers import MarianTokenizer, MarianMTModel

def load_model():
    tokenizer = MarianTokenizer.from_pretrained('opus-mt-en-fr')
    model = MarianMTModel.from_pretrained('opus-mt-en-fr')      
    return model, tokenizer

def translate(text):
    model, tokenizer = load_model()
    translated = model.generate(**tokenizer.prepare_seq2seq_batch([text]))
    tgt_text = [tokenizer.decode(t, skip_special_tokens=True) for t in translated]
    return tgt_text[0]