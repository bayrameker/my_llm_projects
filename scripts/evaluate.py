from transformers import GPT2LMHeadModel, GPT2Tokenizer, pipeline

def main():
    # Model ve tokenizer'ı yükleyin
    model = GPT2LMHeadModel.from_pretrained('./models/my_model')
    tokenizer = GPT2Tokenizer.from_pretrained('./models/my_model')

    # Değerlendirme pipeline'ını oluşturun
    nlp = pipeline('text-generation', model=model, tokenizer=tokenizer)

    # Test metni üzerinde modeli değerlendirin
    test_text = "Bu bir deneme metnidir. "
    result = nlp(test_text, max_length=50, num_return_sequences=1, truncation=True)
    print(result)

if __name__ == "__main__":
    main()
