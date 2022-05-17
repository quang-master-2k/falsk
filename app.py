from flask import Flask

app = Flask(__name__)

@app.route("/notify")
def notify():
    # thực hiện tính toán lại model

    return "<p>Hello, World!</p>"

@app.route('/getOrther',methods = ['POST'])
def getOrther():
    if request.method == 'POST':
        info = request.data
        # dùng data tính độ phù hợp
        return ''

if __name__ == '__main__':
    app.run()

