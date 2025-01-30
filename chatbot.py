from flask import Flask, render_template, request, jsonify
import openai

openai.api_key = "your-openai-api-key"

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get", methods=["POST"])
def chatbot():
    user_input = request.json["message"]
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": user_input}],
    )
    return jsonify({"response": response["choices"][0]["message"]["content"]})

if __name__ == "__main__":
    app.run(debug=True)
