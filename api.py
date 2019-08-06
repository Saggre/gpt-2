from flask import Flask, request, jsonify
import generate_samples as gpt2

app = Flask(__name__)


@app.route('/gpt2', methods=['POST'])
def gpt2_post():
    req_data = request.get_json(force=True)
    print(req_data)
    input_text = req_data['inputData']
    output_text = gpt2.interact_model(input_text=input_text)
    return {'error': '', 'text': output_text}  # Fetches first column that is Employee ID


if __name__ == '__main__':
    app.run(port='5002')
