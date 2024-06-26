from transformers import GPT2Tokenizer, GPT2LMHeadModel, Trainer, TrainingArguments
from datasets import load_dataset

def main():
    # Veriyi yükleyin ve ön işleyin
    dataset = load_dataset('text', data_files={'train': 'data_utils.py/train_data.txt', 'validation': 'data_utils.py/eval_data.txt'})

    # Veriyi kontrol et
    print("Dataset loaded successfully:")
    print(dataset)

    # Model ve tokenizer'ı yükleyin
    tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
    model = GPT2LMHeadModel.from_pretrained('gpt2')

    # Tokenizer'a padding token ekleyin
    if tokenizer.pad_token is None:
        tokenizer.add_special_tokens({'pad_token': '[PAD]'})
        model.resize_token_embeddings(len(tokenizer))

    # Veriyi tokenleştirin ve labels ekleyin
    def tokenize_function(examples):
        tokens = tokenizer(examples['text'], truncation=True, padding='max_length', max_length=512)
        tokens['labels'] = tokens['input_ids'].copy()
        return tokens

    tokenized_datasets = dataset.map(tokenize_function, batched=True)

    # Tokenize edilmiş veriyi kontrol et
    print("Tokenized dataset:")
    print(tokenized_datasets)

    # Eğitim argümanlarını ayarlayın
    training_args = TrainingArguments(
        output_dir='./models/my_model',
        num_train_epochs=10,  # Eğitim dönemini artırdık
        per_device_train_batch_size=4,
        per_device_eval_batch_size=4,
        warmup_steps=500,
        weight_decay=0.01,
        logging_dir='./logs',
        logging_steps=10,                # Daha sık günlük kaydı
        save_steps=50,                   # Modeli daha sık kaydet
        evaluation_strategy="steps",     # Adım bazında değerlendirme
        eval_steps=50                    # Değerlendirme sıklığını ayarlama
    )

    # Trainer'ı oluşturun ve eğitin
    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=tokenized_datasets['train'],
        eval_dataset=tokenized_datasets['validation'],
        tokenizer=tokenizer
    )

    trainer.train()

    # Modeli ve tokenizer'ı kaydedin
    model.save_pretrained('./models/my_model')
    tokenizer.save_pretrained('./models/my_model')

if __name__ == "__main__":
    main()
