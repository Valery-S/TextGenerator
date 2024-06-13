from transformers import AutoTokenizer, AutoModelForCausalLM
from database import DataBase

db = DataBase()


tokenizer = AutoTokenizer.from_pretrained("ai-forever/mGPT")
model = AutoModelForCausalLM.from_pretrained("ai-forever/mGPT")

# Функция для генерации текста
def generateText(prompt:str, max_length=100, min_length=20):
    # Токенизация входного текста
    input_ids = tokenizer.encode(prompt, return_tensors='pt')

    # Генерация текста
    output = model.generate(
        input_ids,
        max_length=max_length + len(prompt),
        min_length=min_length + len(prompt),
        num_return_sequences=1,
        no_repeat_ngram_size=2,
        early_stopping=True,
        do_sample=False, 
        temperature=0.25,
    )

    # Декодирование и возврат результата
    generatedText = tokenizer.decode(output[0], skip_special_tokens=True).replace('\n\n', '\n')
    # generatedText = generatedText[:generatedText.find('\n\n')]
    
    saveToDB(prompt, generatedText)

    return generatedText


def saveToDB(prompt,generatedText):
    db.save_message(prompt, generatedText)
