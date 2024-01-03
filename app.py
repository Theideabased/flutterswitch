from flask import Flask, render_template, request, jsonify 
import openai 
import os
from dotenv import load_dotenv
  
load_dotenv()
app = Flask(__name__) 
  
# OpenAI API Key 
openai.api_key = os.getenv("API_KEY")
  
def get_completion(prompt): 
    print(prompt) 
    query = openai.Completion.create( 
        engine="text-davinci-003", 
        prompt=prompt, 
        max_tokens=1024, 
        n=1, 
        stop=None, 
        temperature=0.5, 
    ) 
  
    response = query.choices[0].text 
    return response 
  
@app.route("/", methods=['POST', 'GET']) 
def query_view(): 
    if request.method == 'POST': 
        print('step1') 
        prompt = request.form['prompt'] 
        response = get_completion(prompt) 
        print(response) 
  
        return jsonify({'response': response}) 
    return render_template('index.html') 
  
  
if __name__ == "__main__": 
    app.run(host='0.0.0.0', port=5000, debug=True)