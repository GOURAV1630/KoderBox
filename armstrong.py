from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

@app.route('/check_armstrong', methods=['GET', 'POST'])
def check_armstrong():
    if request.method == 'GET':
        return render_template('armstrong_form.html')

    elif request.method == 'POST':
        try:
            number = int(request.form.get('number'))
            order = len(str(number))
            temp = number
            total = 0

            while temp > 0:
                r = temp % 10
                total += (r ** order)
                temp //= 10

            is_armstrong = number == total
            return render_template('armstrong_result.html', number=number, is_armstrong=is_armstrong)

        except ValueError:
            return jsonify({"error": "Invalid input. Please enter a valid number."}), 400

if __name__ == '__main__':
    app.run(debug=True)
