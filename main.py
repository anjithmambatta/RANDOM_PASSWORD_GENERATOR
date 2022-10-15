from flask import Flask,render_template,request
app = Flask(__name__)

@app.route("/")
@app.route("/home")
def index():
    return render_template("index.html")
@app.route("/external/" , methods=['POsT','GET'])
def external():
    length_of_password= str(request.form.get("LENGTH OF THE PASSWORD"))
    length_of_digit= str(request.form.get("LENGTH OF DIGIT"))
    length_of_upcase= str(request.form.get("LENGTH OF UPCASE"))
    length_of_locase= str(request.form.get("LENGTH OF LOCASE"))
    length_of_symbol= str(request.form.get("LENGTH OF SYMBOL"))

    import random
    max_len=length_of_password
    digits= ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    locase_charaters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                         'u', 'v', 'w', 'x', 'y', 'z']
    upcase_charaters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                         'U', 'V', 'W', 'X', 'Y', 'Z']
    symbols = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>', '*', '(', ')', '<']
    rand_digit=random.choices(digits, k=int(length_of_digit))
    rand_upper=random.choices(upcase_charaters, k=int(length_of_upcase))
    rand_lower= random.choices(locase_charaters, k=int(length_of_locase))
    rand_symbol=random.choices(symbols, k=int(length_of_symbol))
    temp_pass =(rand_digit+rand_upper+rand_lower+rand_symbol)
    org_pass = "".join(random.sample(temp_pass,int(max_len)))
    pswd = "".join(random.sample(org_pass, len(org_pass)))
    password= "".join(pswd)
    "password"
    return render_template('index.html', password=password)


if __name__ == '__main__':
    app.run(debug=True)