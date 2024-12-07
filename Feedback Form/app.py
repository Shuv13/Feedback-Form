from flask import Flask, render_template, request, jsonify
import json
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit-feedback', methods=['POST'])
def submit_feedback():
    try:
        feedback_data = request.json
        feedback_data['timestamp'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        with open('feedback_data.json', 'a') as f:
            json.dump(feedback_data, f)
            f.write('\n')
        
        return jsonify({'success': True}), 200
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True) 