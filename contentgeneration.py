import openai
import secrets


openai.api_key = secrets.API_KEY


def generate_content(prompt, tokens):
    try:
        response = openai.Completion.create(engine="text-davinci-001", prompt=prompt, max_tokens=tokens)
    
    except APIConnectionError:
        response["choices"][0]["text"] = "Max retries! Try again in an hour!"
    
    return response["choices"][0]["text"]


def get_tokens_from_characters(chars):
    avg_char_per_word = 5
    total_words = chars // avg_char_per_word
    
    return total_words
    
def get_cost(ai_content, model):
    model_price = {
        "ada": 0.0004,
        "babbage": 0.0005,
        "curie": 0.0020,
        "davinci": 0.0200
    }
    num_words = len(ai_content.split())
    
    return (model_price[model] / 75) * num_words, num_words


if __name__ == "__main__":
    prompt = input("Prompt: ")
    model = "davinci"
    chars = 140
    # tokens = get_tokens_from_characters(chars)
    ai_content = generate_content(prompt, 40)
    cost, num_words = get_cost(ai_content, model)
    print(f'\nContent: {ai_content}\n=========\n\nCost: ${round(cost,5)}\n=========\n\nTotal words: {num_words}')