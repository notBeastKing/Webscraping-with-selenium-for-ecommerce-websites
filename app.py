from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import time
import scrap_utils
import FINAL


app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    """Render the main page"""
    return render_template('index.html')


@app.route('/search', methods=["POST"])
def search():
    """Handle search requests"""
    search_query = request.form['search']
    
    info = FINAL.SCRAPE(search_query)
    products = FINAL.sort_list(info)    
    return jsonify(info)

if __name__ == '__main__':
    app.run(debug=True, port = 5000)
