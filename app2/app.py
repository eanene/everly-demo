from flask import Flask

app = Flask(__name__)

@app.route('/app-2')
def everly_app_2():
    return 'This is the Python Microservice, the everlywell experience!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1717)
