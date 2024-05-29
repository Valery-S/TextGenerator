from transformers import GPT2LMHeadModel, GPT2Tokenizer

# Загрузите модель и токенизатор
model_name = "sberbank-ai/rugpt3small_based_on_gpt2"
tokenizer = GPT2Tokenizer.from_pretrained(model_name)
model = GPT2LMHeadModel.from_pretrained(model_name)

# Функция для генерации текста
def generateText(prompt:str, max_length=150):
    # Токенизация входного текста
    input_ids = tokenizer.encode(prompt, return_tensors='pt')

    # Генерация текста
    output = model.generate(
        input_ids,
        max_length=max_length,
        num_return_sequences=1,
        no_repeat_ngram_size=2,
        early_stopping=True,
        do_sample=False, 
        temperature=0.2
    )

    # Декодирование и возврат результата
    generatedText = tokenizer.decode(output[0], skip_special_tokens=True)
    
    saveToDB(prompt,generatedText)

    return generatedText


def saveToDB(prompt,generatedText):
    
    pass