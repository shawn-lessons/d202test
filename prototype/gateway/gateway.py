from flask import Flask, request, jsonify, render_template_string
import sqlite3

dashboard_template = """
<!DOCTYPE html>
<html>
<head>
    <title>Readings Dashboard</title>
</head>
<body>
    <h1>Readings Dashboard</h1>
    <table border="1">
        <tr>
            <th>ID</th>
            <th>Name</th>
            <th>Temperature</th>
        </tr>
        {% for reading in readings %}
        <tr>
            <td>{{ reading[0] }}</td>
            <td>{{ reading[1] }}</td>
            <td>{{ reading[2] }}</td>
        </tr>
        {% endfor %}
    </table>
</body>
</html>
"""

app = Flask(__name__)
DATABASE = 'data.db'

@app.route('/add_reading', methods=['POST'])
def add_item():
    if request.is_json:
        try:
            data = request.get_json()
            number = data['number']
            name = data['name']

            conn = sqlite3.connect(DATABASE)
            cursor = conn.cursor()

            cursor.execute('INSERT INTO readings (number, name) VALUES (?, ?)', (number, name))
            conn.commit()
            conn.close()

            return jsonify({'message': 'Reading added successfully!'}), 201
        except Exception as e:
            return jsonify({'error': str(e)}), 400
    else:
        return jsonify({'error': 'Request body must be JSON'}), 400
    
@app.route('/dashboard', methods=['GET'])
def dashboard():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('SELECT id, name, number FROM readings')
    readings = cursor.fetchall()
    conn.close()
    
    # Render the readings in an HTML template
    return render_template_string(dashboard_template, readings=readings)
if __name__ == '__main__':
    app.run(debug=False, host="0.0.0.0")
