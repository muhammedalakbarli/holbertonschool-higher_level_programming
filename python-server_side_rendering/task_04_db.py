import json
import csv
import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)

def read_json():
    with open('products.json', 'r') as f:
        return json.load(f)

def read_csv():
    products = []
    with open('products.csv', 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            row['id'] = int(row['id'])
            row['price'] = float(row['price'])
            products.append(row)
    return products

def read_sql(product_id=None):
    products = []
    try:
        conn = sqlite3.connect('products.db')
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        if product_id:
            cursor.execute('SELECT * FROM Products WHERE id = ?', (product_id,))
        else:
            cursor.execute('SELECT * FROM Products')
        rows = cursor.fetchall()
        products = [dict(row) for row in rows]
        conn.close()
    except sqlite3.Error:
        pass
    return products

@app.route('/products')
def display_products():
    source = request.args.get('source')
    product_id = request.args.get('id')

    if source == 'sql':
        data = read_sql(product_id)
        if product_id and not data:
            return render_template('product_display.html', error="Product not found")
        return render_template('product_display.html', products=data)

    elif source == 'json':
        data = read_json()
    elif source == 'csv':
        data = read_csv()
    else:
        return render_template('product_display.html', error="Wrong source")

    if product_id:
        product_id = int(product_id)
        data = [p for p in data if p['id'] == product_id]
        if not data:
            return render_template('product_display.html', error="Product not found")

    return render_template('product_display.html', products=data)

if __name__ == '__main__':
    # Standard Flask start - ensure indentation is exactly 4 spaces
    app.run(debug=True, port=5000)
