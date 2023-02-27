import openai
import secrets


openai.api_key = secrets.API_KEY


def generate_content(prompt, tokens):
    try:
        response = openai.Completion.create(engine="text-davinci-001", prompt=prompt, max_tokens=tokens)
        generated_text = response["choices"][0]["text"]
        tokens_used = response["usage"]["total_tokens"]
    
    except:
        response["choices"][0]["text"] = "Max retries! Try again in an hour!"
        generated_text = "API Connection error!"
        tokens_used = 0
    
    return generated_text, tokens_used


def get_tokens_from_characters(chars):
    avg_char_per_word = 5
    total_words = chars // avg_char_per_word
    
    return total_words
    
def get_cost(tokens_used, model):
    model_price = {
        "ada": 0.0004,
        "babbage": 0.0005,
        "curie": 0.0020,
        "davinci": 0.0200
    }
    cost = (model_price[model] * tokens_used) / 1000
   
    return cost


if __name__ == "__main__":
    prompt = input("Prompt: ")
    model = "davinci"
    chars = 140
    # tokens_to_use = get_tokens_from_characters(chars)
    ai_content, tokens_used = generate_content(prompt, 40)
    cost = get_cost(tokens_used, model)
    print(f'Content: {ai_content}\nCost: \n\n${round(cost,6)}\nCharacters used: \n\n{len(ai_content)}')