#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from config import CFG_UPLOAD_FOLDER
from config import CFG_SECRET_KEY
from config import CFG_UPLOAD_LIMIT
from flask import Flask
from flask import jsonify
import views

app = Flask(__name__)

# 不使用 ascii 编码来序列化JSON对象
# 显示中文
app.config['JSON_AS_ASCII'] = False
app.config['MAX_CONTENT_LENGTH'] = CFG_UPLOAD_LIMIT
app.config['SECRET_KEY'] = CFG_SECRET_KEY
app.config['SESSION_TYPE'] = 'filesystem'
app.config['UPLOAD_FOLDER'] = CFG_UPLOAD_FOLDER


@app.route("/api/recognize", methods=["POST"])
def recognize():
    return jsonify(views.recognize())


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
