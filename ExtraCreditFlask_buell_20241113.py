# %% [markdown]
# Extra Credit
# 
# Submissions must be a Python file and not a notebook file (i.e *.ipynb)
# Do not use global variables
# 
# http://flask.pocoo.org/docs/1.0/quickstart/
# 
# Using the flask web server, load the HTML form contained in the variable main_page. 
# The form should load at route '/'.
# The user should then be able to enter a number and click Calculate, at which time the browser will submit an HTTP POST to the web server. The web server will then capture the post, extract the number entered, and display the number multiplied by 5 on the browser.

# %%
from flask import Flask, request

main_page = '''
<html>
    <head>
    <title></title>
    <link rel="stylesheet" href="http://netdna.bootstrapcdn.com/bootstrap/3.3.2/css/bootstrap.min.css">
    <link rel="stylesheet" href="http://netdna.bootstrapcdn.com/font-awesome/3.2.1/css/font-awesome.min.css">
    </head>
<body>
<form class="form-horizontal" method="post" action="/calc">
<fieldset>
<!-- Form Name -->
<legend>Multiplier</legend>
<!-- Text input-->
<div class="form-group">
  <label class="col-md-4 control-label" for="textinput">Number</label>  
  <div class="col-md-4">
  <input id="textinput" type="number" name='number' placeholder="Enter a number" class="form-control input-md">
  </div>
</div>
<!-- Button -->
<div class="form-group">
  <label class="col-md-4 control-label" for="singlebutton"></label>
  <div class="col-md-4">
    <button id="singlebutton" name="singlebutton" class="btn btn-primary">Calculate</button>
  </div>
</div>
</fieldset>
</form>
<script src="http://netdna.bootstrapcdn.com/bootstrap/3.3.2/js/bootstrap.min.js"></script>
</body>
</html>
'''

# %%
# ------ Place code below here \/ \/ \/ ------

app = Flask(__name__)

# Load form at route '/'
@app.route('/', methods=['GET'])
def index():
    return main_page

# Let user enter a number and click calculate, then browser will submit HTTP POST to web server
@app.route('/calc', methods=['POST'])
def calculate():
    number = int(request.form['number']) # Capture the post and extract the number entered

    result = number * 5    # Multiply the number by 5

    return f"{result}"     # Return the result 

# Run the app
if __name__ == "__main__":
    app.run()
# ------ Place code above here /\ /\ /\ ------


