from flask import Flask, render_template_string
import socket

app = Flask(__name__)

@app.route('/')
def home():
    hostname = socket.gethostname()

    try:
        ip_address = socket.gethostbyname(hostname)
    except socket.gaierror:
        # 오류 발생 시 localhost로 대체
        ip_address = '127.0.0.1'

    html = '''
    <h1>서버 정보</h1>
    <p><strong>호스트 이름:</strong> {{ hostname }}</p>
    <p><strong>IP 주소:</strong> {{ ip }}</p>
    '''
    return render_template_string(html, hostname=hostname, ip=ip_address)


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=5000)
