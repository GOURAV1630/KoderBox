from flask import Flask, request, jsonify

app = Flask(__name__)

students = {}

@app.route('/add_student', methods=['POST'])
def add_student():
    data = request.get_json()
    stud_id = data.get('stud_id')
    name = data.get('name')
    age = data.get('age')
    grades = data.get('grades')

    if stud_id is None or name is None or age is None or grades is None:
        return jsonify({"error": "Missing required data"}), 400

    gradelist = [int(grade) for grade in grades]
    students[stud_id] = {'Name': name, 'Age': age, 'Grades': gradelist}

    return jsonify({"message": "Student added successfully"}), 201

@app.route('/display_student/<int:stud_id>', methods=['GET'])
def display_student(stud_id):
    if stud_id in students:
        student = students[stud_id]
        return jsonify(student), 200
    else:
        return jsonify({"error": "Student not found"}), 404

@app.route('/students_marks_analyze', methods=['POST'])
def students_marks_analyze():
    data = request.get_json()
    stud_id = data.get('stud_id')

    if stud_id not in students:
        return jsonify({"error": "Student not found"}), 404

    marks_list = students[stud_id]['Grades']
    max_marks = max(marks_list)
    min_marks = min(marks_list)
    average_marks = sum(marks_list) / len(marks_list)

    highest_index = marks_list.index(max_marks) + 1
    lowest_index = marks_list.index(min_marks) + 1

    result = {
        "MarksList": marks_list,
        "MaximumMarks": max_marks,
        "MinimumMarks": min_marks,
        "AverageMarks": average_marks,
        "StudentWithHighestMarks": f"Student {highest_index}",
        "StudentWithLowestMarks": f"Student {lowest_index}",
    }

    return jsonify(result), 200

if __name__ == '__main__':
    app.run(debug=True)
