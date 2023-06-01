

import openai
from flask import Flask, request, jsonify

app = Flask(__name__)

# set OpenAI API key
openai.api_key = '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'

# set GPT model parameters
prompt = 'Hello, how can I help you today?'
temperature = 0.5
max_tokens = 50
no_filter = True

@app.route('/generate-response', methods=['POST'])
def generate_response():
    # get the input from the front-end application
    input_text = request.form['input']
    
    # generate response from GPT model
    response = openai.Completion.create(
        engine='davinci',
        prompt=prompt + input_text,
        temperature=temperature,
        max_tokens=max_tokens,
        no_filter=no_filter
    )
    
    # return the response to the front-end application
    return jsonify({'response': response.choices[0].text.strip()})

if __name__ == '__main__':
    app.run()
