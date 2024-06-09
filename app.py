from flask import Flask, request, jsonify
import chat

app = Flask(__name__)

@app.route('/chat', methods=['POST'])
def chatbot():
    userInput = request.get_json()['input']
    if not userInput:
        return jsonify({'response': 'No input provided'}), 400
    try:
        response = chat.getResponse(userInput)
        return jsonify({'response': response})
    except Exception as e:
        return jsonify({'response': 'Error processing input'}), 500

if __name__ == '__main__':
    app.run(debug=True)