from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/')  # default URL
def student():
    return render_template('input_info.html')


@app.route('/result', methods=['POST', 'GET'])
def result():
    if request.method == 'POST':
        result = dict()
        result['Name'] = request.form.get('Name')
        result['Univ'] = request.form.get('Univ')
        result['Student Number'] = request.form.get('Student Number')
        result['Gender'] = request.form.get('Gender')
        result['Major'] = request.form.get('Major')
        if request.form.getlist('Programming Language'):
            result['Programming Language'] = ', '.join(request.form.getlist('Programming Language'))
        else:
            result['Programming Language'] = 'None'

        # 학번
        # 성별
        # 학과
        # 프로그래밍 언어 -> hint) ','.join(list명)을 사용하면 list 안에 있는 항목들이 ','로 나누어져 출력됨.

        return render_template("result.html", result=result)


if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host='0.0.0.0', port=80)
    # docker 안의 80번 포트를 docker 밖에 있는 80번 포트로 연결하는 것. 
    # -> ' -p ' 왼쪽 80 : 도커 안의 포트, 오른쪽 80 : 도커 밖의 포트