from flask import Flask, render_template, request

app = Flask(__name__)

def menghitung_rerata(n, data):
    jmlh = sum(data)
    rerata = jmlh / n
    return jmlh, rerata

@app.route('/')
def index():
    return render_template('menghitung-rerata.html')

@app.route('/proses', methods=['POST'])
def proses():
    n = int(request.form['n'])
    data = [float(request.form[f'data{i}']) for i in range(1, n + 1)]
    jmlh, rerata = menghitung_rerata(n, data)
    hasil = {'data': data, 'jumlah': jmlh, 'rerata': rerata}
    return render_template('menghitung-rerata.html', hasil=hasil, n=n, data=data)

if __name__ == '__main__':
    app.run()