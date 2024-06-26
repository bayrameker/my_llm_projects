from transformers import GPT2LMHeadModel, GPT2Tokenizer, pipeline

def main():
    # Model ve tokenizer'ı yükleyin
    model = GPT2LMHeadModel.from_pretrained('./models/code_model')
    tokenizer = GPT2Tokenizer.from_pretrained('./models/code_model')

    # Değerlendirme pipeline'ını oluşturun
    nlp = pipeline('text-generation', model=model, tokenizer=tokenizer)

    # Test metni üzerinde modeli değerlendirin
    test_text = "Python dilinde bir kod yazın: "
    result = nlp(test_text, max_length=50, num_return_sequences=1, truncation=True)
    print(result)

if __name__ == "__main__":
    main()
