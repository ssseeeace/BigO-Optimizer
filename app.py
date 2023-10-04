from flask import Flask, render_template, request, jsonify
import openai

app = Flask(__name__)

# insert apikey
openai.api_key = ''


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/optimize', methods=['POST'])
def optimize_code():
    code = request.json['code']
    big_o = request.json['bigO']

    # Construct the prompt for ChatGPT
    prompt = f"Respond with only the code. Optimize the following code to achieve a time complexity of exactly {big_o}:\n\n{code}. If it is not possible simply respond 'Not Possible'"

    # Make the API call
    response = openai.Completion.create(
        engine="text-davinci-003", prompt=prompt, max_tokens=500)

    return jsonify({"optimized_code": response.choices[0].text.strip()})


if __name__ == '__main__':
    app.run(debug=True)
