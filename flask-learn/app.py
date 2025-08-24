from flask import Flask, jsonify, request, redirect, url_for, render_template
import json
import os
from pymongo import MongoClient

app = Flask(__name__)

# ======= JSON file API =======
DATA_FILE = 'data.json'

@app.route('/api')
def api():
    if not os.path.exists(DATA_FILE):
        return jsonify([])  # Return empty list if file missing
    with open(DATA_FILE, 'r') as f:
        data = json.load(f)
    return jsonify(data)

# ======= MongoDB (Atlas) Setup =======
# Replace with your actual MongoDB Atlas cluster URI
MONGO_URI = 'mongodb+srv://ahardik1199:12345@hardik.idnrlqw.mongodb.net/?retryWrites=true&w=majority&appName=hardik'
client = MongoClient(MONGO_URI)
db = client['test']
collection = db['newcoll']

# ======= Form and Submission Handling =======
@app.route('/', methods=['GET'])
def form():
    return render_template('form.html', error=None)

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name')
    age = request.form.get('age')
    try:
        if not name or not age:
            raise ValueError("Name and age are required")
        collection.insert_one({'name': name, 'age': int(age)})
        return redirect(url_for('success'))
    except Exception as e:
        error_msg = str(e)
        return render_template('form.html', error=error_msg)

@app.route('/success')
def success():
    return render_template('success.html')

# ========= Run Server ===========
if __name__ == '__main__':
    app.run(debug=True)
