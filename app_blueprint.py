from flask import Blueprint, render_template, request, jsonify
from contentgeneration import generate_content, get_cost

app_blueprint = Blueprint('app_blueprint', __name__)

@app_blueprint.route('/', methods=['POST', 'GET'])
def index():

    return render_template("index.html")

@app_blueprint.route('/get_input', methods=['POST', 'GET'])
def get_input():
    check = False
    if request.method == 'POST':
        print(request.form)
        input_prompt = request.form['content-text']
        input_tone = request.form['content-tone']
        input_for = request.form['content-for']

        if input_for == 'sms':
            prompt = input_prompt + ' in 40 words or less that is ' + input_tone
            tokens = 45

        if input_for == 'mms':
            prompt = input_prompt + ' in 120 words or less that is ' + input_tone 
            tokens = 175

        if input_for == 'email':
            prompt = input_prompt + ' in 500 words that is ' + input_tone
            tokens = 600

        generated_text, tokens_used = generate_content(prompt=prompt, tokens=tokens)
        cost = get_cost(tokens_used=tokens_used, model="davinci")
        check = True
        # print(f'Text: {generated_text}\n\nTokens:\n{tokens_used}')
        
    
    return render_template("index.html", check=check, ai_text=generated_text, cost=cost)