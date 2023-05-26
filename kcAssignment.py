import csv
from flask import Flask, request, jsonify

app = Flask(__name__)

# Endpoint to retrieve student details with pagination
@app.route('/students', methods=['GET'])
def get_students():
    page = int(request.args.get('page', 1))  # Default page is 1
    page_size = int(request.args.get('page_size', 10))  # Default page size is 10

    # Read the student details from the CSV file
    with open('students.csv', 'r') as file:
        reader = csv.DictReader(file)
        students = list(reader)

    # Calculate the start and end indices for pagination
    start_index = (page - 1) * page_size
    end_index = start_index + page_size

    # Get the students for the requested page
    paginated_students = students[start_index:end_index]

    return jsonify(paginated_students)

if __name__ == '__main__':
    app.run()
