from flask import Flask, jsonify
import psycopg2
import os

app = Flask(__name__)

def get_db_connection():
    return psycopg2.connect(
        host=os.environ.get('DB_HOST', 'db'),
        database=os.environ.get('DB_NAME', 'devops'),
        user=os.environ.get('DB_USER', 'devops'),
        password=os.environ.get('DB_PASSWORD', 'password')
    )

@app.route('/')
def hello():
    return jsonify({
        'message': 'Hello from DevOps!',
        'status': 'running'
    })

@app.route('/health')
def health():
    try:
        conn = get_db_connection()
        conn.close()
        return jsonify({'database': 'connected', 'status': 'healthy'})
    except Exception as e:
        return jsonify({'database': 'error', 'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
