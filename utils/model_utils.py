from transformers import GPT2LMHeadModel, GPT2Tokenizer

def load_model_and_tokenizer(model_dir):
    model = GPT2LMHeadModel.from_pretrained(model_dir)
    tokenizer = GPT2Tokenizer.from_pretrained(model_dir)
    return model, tokenizer
