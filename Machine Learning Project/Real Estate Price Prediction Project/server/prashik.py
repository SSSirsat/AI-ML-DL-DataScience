from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/BC')
def hello():
    return "Prashik MadarChod hai dada, hooo Such meee!!!"


if __name__ == '__main__':
    print("Starting Python Flask Server  For Home Price Prediction...")
    app.run()
