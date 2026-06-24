from flask import Flask, jsonify
import pymysql

app = Flask(__name__)

def get_db():
    return pymysql.connect(
        host='mydb.cxokuyue0ohr.ap-south-1.rds.amazonaws.com',
        user='admin',
        password='Thesp#db1234',
        database='myapp'
    )

@app.route('/')
def home():
    return "✅ App connected to database successfully!"

@app.route('/users')
def users():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    data = cursor.fetchall()
    conn.close()
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
