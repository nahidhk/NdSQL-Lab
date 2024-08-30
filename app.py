from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file_name = request.form.get('file_name')
        data = request.form.get('data')

        if file_name and data:
            with open(file_name, 'w') as file:
                file.write(data)
            return f'File "{file_name}" created successfully!'
        else:
            return 'Please provide both file name and data.'

    return '''
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Create File</title>
        </head>
        <body>
            <form method="post">
                <label for="file_name">Input the file name*</label>
                <input type="text" name="file_name" required>
                <label for="data">Input the Data*</label>
                <textarea name="data" required></textarea>
                <button type="submit">Create File</button>
            </form>
        </body>
        </html>
    '''

if __name__ == '__main__':
    app.run(debug=True)
