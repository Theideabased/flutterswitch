from flask import Flask, request, jsonify
import requests
import json

app = Flask(__name__)

gpt_key = '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'

# Endpoint to receive code file and initiate conversion
@app.route('/convert_code', methods=['POST'])
def convert_code():
    uploaded_code = request.files['file']
    input1 = request.form.get('input1')
    input2 = request.form.get('input2')
    
    # Read the code file or extract code content
    code_content = uploaded_code.read().decode('utf-8')

    # Prepare the prompt based on user inputs 
    prompt = f"Translate this flutter code from the {input1} version to {input2} version: {code_content}"
    
    # # prepare the data for the request
    # data = {
    #     'prompt': prompt,
    #     'max_tokens': 400
    # }
    #
    # Send code content to ChatGPT API for intent understanding
    gpt_response = requests.post(
        'https://api.openai.com/v1/engines/davinci/completions',
        headers={f'Authorization': 'Bearer {gpt_key}'},
        json={'prompt': code_content, 'max_tokens': 100}
    )
    if gpt_response.status_code == 200:
        result = gpt_response.json()
        converted_code = result['choices'][0]['text']
        return jsonify({'converted_code' : converted_code})
    else:
        print(f"request failed with status code: {gpt_response.status_code}")
    
# except KeyError as e:
# return jsonify({'error': f'Missing required parameter: {str(e)}'}), 400
# except Exception as e:
# return jsonify({'error': f'An error occurred: {str(e)}'}), 500
    # Extract intent from GPT-3 response (not implemented here)
    # Perform code conversion based on identified intent (not implemented here)
    # Converted code will be in 'converted_code' variable
    
    # Return the converted code back to Flutter
    # return jsonify(converted_code)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
