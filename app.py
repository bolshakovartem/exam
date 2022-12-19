from flask import Flask
app = Flask(__name__)

@app.route('/')

def arifm_prog(a0, d, n):
    if n == 1:
        return a0
    else:
        return arifm_prog(a0, d, n - 1) + d

def sum_arifm_progr(a0, d, n):
    if n == 1:
        return a0
    else:
        return arifm_prog(a0, d, n) + sum_arifm_progr(a0, d, n - 1)

print(arifm_prog(2, 2, 6))
print(sum_arifm_progr(2, 2, 6))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')