from flask import Flask, request, jsonify
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    print(f"Received webhook data: {data}")
    
    # Simulate AI processing
    response = {
        "status": "success",
        "message": "Weather data received and processed",
        "data": data
    }
    
    return jsonify(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9999)
