import os
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/generate-with-llama', methods=['POST'])
def generate():
    try:
        data = request.get_json() or {}
        prompt = data.get('prompt', 'Ingen prompt angiven')
        print(f"Mottog genereringsförfrågan med prompt: {prompt}")
        return jsonify({
            "status": "success", 
            "message": "Bildgenerering startad i bakgrunden",
            "prompt": prompt
        }), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
