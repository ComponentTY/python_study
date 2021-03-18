from flask import Flask, jsonify, request
from flask_cors import CORS
import random
app = Flask(__name__)
CORS(app, resources=r'/*')


@app.errorhandler(404)
def page_not_found(error):
    return 'This page does not exist', error


@app.route('/', methods=['GET'])
def hello_world():
    data = {
        'data': 'hello world',
        'request': 1231
    }
    return jsonify(data)


@app.route('/about')
def about():
    return '这是about页面'


@app.route('/robot', methods=['POST'])
def robot():
    meet = ['你好', 'hello', 'hi', '你好啊', 'nihao', 'nihaoa']
    zaima = ['在吗', '在干嘛', '在干嘛呀', '干啥呢', '干啥嘞', 'what are you 弄啥嘞', 'what are you doing']
    meetme = ['认识我吗?', '你认识我吗', '你记得我吗?', '我是谁?']
    username = request.json.get('message')
    if username in meet:
        retry = ['很高兴认识你!', 'nice to meet you', '哈喽', '你好啊', '你好']
        return retry[random.randint(0, len(retry) - 1)]
    elif username in zaima:
        retry = ['在呢', '我在', '等你呢', '在玩呢', '想我了?', '在忙呢']
        return retry[random.randint(0, len(retry) - 1)]
    elif username in meetme:
        retry = ['我认识你啊', '你是那个我心中最美的人', '我已在此恭候多时,只为等你出现']
        return retry[random.randint(0, len(meetme) - 1)]
    else:
        return '我不知道你在说什么'


@app.route('/upload', methods=['POST'])
def upload():
    if request.method == 'POST':
        upload_file = request.files['file']
        task = request.form.get('task_id')
        chunk = request.form.get('chunk')
        name = request.form.get('name')
        filename = '%s%s' %(name, chunk)
        upload_file.save('./upload/%s' % filename)
    return 'success'


@app.route('/upload/apk', methods=['POST'])
def loadapk():
    if request.method == 'POST':
        requestFile = request.file()
        requestToString = request.form.to_dict()
        # requestDict = eval(requestToString.keys()[0])
        # print(requestToString['apkfile'])
        return jsonify(requestToString)


if __name__ == '__main__':
    app.run('0.0.0.0', 80)
