from flask import Flask, jsonify, request

app = Flask(__name__)

schedules = []

@app.route('/api/schedules', methods=['GET', 'POST'])
def manage_schedules():
    if request.method == 'POST':
        schedules.append(request.json)
        return jsonify({"message": "Scheduled"}), 201
    return jsonify(schedules)

if __name__ == '__main__':
    app.run(debug=True)