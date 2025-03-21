from flask import Flask, request, jsonify
import datetime

app = Flask(__name__)

# Route to return student number
@app.route('/')
def home():
    return jsonify({"student_number": "200615666"}) 

# Webhook route for fulfillment
@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)
    intent_name = req['queryResult']['intent']['displayName']

    # Handle Study Timer intent
    if intent_name == "Study Timer":
        duration = req['queryResult']['parameters'].get('Duration', None)

        # Check if duration was provided
        if duration:
            duration_seconds = int(duration['amount']) * 60  # Convert minutes to seconds
            response_text = f"Great! I’ve set a {duration['amount']} {duration['unit']} study timer. Stay focused!"
        else:
            response_text = "How long should I set the study timer for?"

    # Fallback if intent is not recognized
    else:
        response_text = "Hmm... I didn’t quite get that. Can you try again?"

    # Return the response
    return jsonify({"fulfillmentText": response_text})

if __name__ == '__main__':
    app.run(debug=True)
