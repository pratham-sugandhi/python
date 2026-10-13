from flask import Flask, render_template, request, jsonify
import os
from dotenv import load_dotenv
from google import genai

# Load environment variables
load_dotenv()

app = Flask(__name__)
api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)
MODEL = "gemini-3.8-flash"


@app.route("/")
def hello_world():
    return render_template("index.html")


@app.route("/ask", methods=["POST"])
def ask():
    query = request.form.get("question", "").strip()

    if not query:
        return jsonify({"error": "Question is required"}), 400

    try:
        response = client.models.generate_content(
            model=MODEL,
            contents=query,
            config={
                "temperature": 0.3,
                "max_output_tokens": 512,
            },
        )

        answer = response.text
        return jsonify({"response": answer}), 200

    except Exception as e:
        app.logger.exception("Error generating answer")
        return jsonify({"error": "Failed to generate answer"}), 500


@app.route("/summarize", methods=["POST"])
def summarize():
    email = request.form.get("email", "").strip()

    if not email:
        return jsonify({"error": "Email is required"}), 400

    prompt = (
        "Summarize the following email in 2-3 sentences:\n\n"
        f"{email}"
    )

    try:
        response = client.models.generate_content(
            model=MODEL,
            contents=prompt,
            config={
                "temperature": 0.3,
                "max_output_tokens": 512,
            },
        )

        summary = response.text
        return jsonify({"summary": summary}), 200

    except Exception:
        app.logger.exception("Error summarizing email")
        return jsonify({"error": "Failed to summarize email"}), 500


if __name__ == "__main__":
    app.run(debug=True)