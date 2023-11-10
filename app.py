from flask import Flask, jsonify
app= Flask(__name__)

@app.route('/')
def home():
    return "Welcome to my Flask Rest Api"

@app.route('/api/items',methods=['GET'])
def get_items():
    items = ['Item 1','Item 2','Item 3','Item 4']
    return jsonify(items)

if __name__ == '__main__':
    app.run(debug=True)