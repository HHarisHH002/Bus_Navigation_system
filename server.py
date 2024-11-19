from flask import Flask,render_template,request
import os
import time
app = Flask(__name__)
from main import run
@app.route('/',methods=['GET','POST'])
def initial_map():
      return render_template('initial_map.html')
   
@app.route('/route', methods=['GET', 'POST'])
def next_page():
    if request.method == 'GET':
        # Run the function that generates 'my_map.html'
        run()
        # Wait until the file is created
        file_path = os.path.join(app.root_path, 'templates', 'my_map.html')
        while not os.path.exists(file_path):
            time.sleep(0.1)  # Check every 100ms

        # Render the generated file
        return render_template('my_map.html', title='Map')


if __name__ == '__main__':
   app.run(debug=True)