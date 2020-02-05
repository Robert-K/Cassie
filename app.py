from flask import Flask, jsonify, request
from flask_cors import CORS
import json, atexit, time

DATA_PATH = 'data.json'
DEBUG = False

app = Flask(__name__)
app.config.from_object(__name__)

CORS(app, resources={r'/*': {'origins': '*'}})


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def get_data(path):
    if path == '':
        return jsonify(data)
    segments = path.split('/')
    result = data
    for segment in segments:
        if segment in result:
            result = result[segment]
        elif type(result) == list and segment.isdigit() and len(result) > int(segment):
            result = result[int(segment)]
        else:
            return 'Invalid path!'
    return jsonify(result)


@app.route('/transactions/add', methods=['POST'])
def post_transations_add():
    transaction = request.json
    transaction['date'] = time.strftime("%d.%m.%Y, %H:%M:%S")
    data['transactions'].append(transaction)
    data['users'][transaction['user']['id']]['balance'] -= transaction['amount']
    save_data(data)
    return 'Transaction received!'


def load_data():
    with open(DATA_PATH, 'r', encoding='utf-8') as json_file:
        return json.load(json_file)


def save_data(data_to_save):
    with open(DATA_PATH, 'w', encoding='utf-8') as f:
        json.dump(data_to_save, f, ensure_ascii=False, indent=4)


if __name__ == '__main__':
    data = load_data()

    atexit.register(save_data, data)

    app.run(host='0.0.0.0')
