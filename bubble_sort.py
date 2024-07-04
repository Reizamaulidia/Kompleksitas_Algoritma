from flask import Flask, render_template, request

app = Flask(__name__)

def bubble_sort(n, data):
    for i in range(1, n):
        for j in range(n - 1, i - 1, -1):
            if data[j] < data[j - 1]:
                tampung = data[j]
                data[j], data[j - 1] = data[j - 1], tampung
    return data

@app.route('/')
def index():
    return render_template('mengurutkan_bs.html')

@app.route('/proses', methods=['POST'])
def proses():
    n = int(request.form['n'])
    data = [int(request.form[f'data{i}']) for i in range(1, n + 1)]
    before_diurutkan = data[:]
    after_diurutkan = bubble_sort(n, data)
    hasil = {'data': before_diurutkan, 'sesudah_diurutkan': after_diurutkan}
    return render_template('mengurutkan_bs.html', hasil=hasil)

if __name__ == '__main__':
    app.run()
