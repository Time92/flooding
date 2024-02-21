from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/check_flood', methods=['POST'])
def check_flood():
    # Get location data from the request
    data = request.get_json()

    # Perform flood level check logic (replace with your actual logic)
    # For simplicity, let's assume the flood level is always moderate
    flood_level = 'moderate'

    return jsonify({'flood_level': flood_level})

if __name__ == '__main__':
    app.run(debug=True)
