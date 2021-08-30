from flask import Flask, render_template
from data import Articles
app = Flask(__name__)

@app.route('/hello')
def hello_world():
    return 'Hello World!'
# @ : 함수를 처리해줌
# .route : 중개역할

@app.route('/', methods=['Get', 'POST']) # get방식이던 post방식이던 여기로 들어오면 다음 함수를 처리해라
def index():
    name="KIM"
    return render_template('index.html', data=name) # 가져오고자 하는 html 파일 가져오기

@app.route('/articles', methods=['Get','Post']) # articles로 요청을 날림
def articles():
    list_data = Articles()
    return render_template('articles.html', data=list_data)

@app.route('/detail/<ids>') # <ids> : 파라미터 처리. 변하는 값이 들어오면 자동으로 바꿔서 들어가도록 함 
def detail(ids): 
    return int(ids)

if __name__ == '__main__':
    app.run(debug=True)
