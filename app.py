from flask import Flask, render_template, request, jsonify
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start_cpu_stress', methods=['GET', 'POST'])
def start_cpu_stress():
    if request.method == 'POST':
        try:
            subprocess.Popen(["stress", "--cpu", "1", "--timeout", "300"])
            message = 'CPU stress started for 300 seconds.'
        except Exception as e:
            message = str(e)
        return render_template('cpu_stress.html', message=message)
    else:
        return render_template('cpu_stress.html')

@app.route('/start_ram_stress', methods=['GET', 'POST'])
def start_ram_stress():
    if request.method == 'POST':
        try:
            subprocess.Popen(["stress", "--vm", "1", "--vm-bytes", "4G", "--timeout", "300"])
            message = 'RAM stress started with 4GB for 300 seconds.'
        except Exception as e:
            message = str(e)
        return render_template('ram_stress.html', message=message)
    else:
        return render_template('ram_stress.html')

@app.route('/start_disk_io_stress', methods=['GET', 'POST'])
def start_disk_io_stress():
    if request.method == 'POST':
        try:
            subprocess.Popen(["stress", "--io", "2", "--timeout", "300"])
            message = 'Disk I/O stress started for 300 seconds.'
        except Exception as e:
            message = str(e)
        return render_template('disk_io_stress.html', message=message)
    else:
        return render_template('disk_io_stress.html')

@app.route('/start_disk_write_stress', methods=['GET', 'POST'])
def start_disk_write_stress():
    if request.method == 'POST':
        try:
            subprocess.Popen(["stress", "--hdd", "2", "--hdd-bytes", "3G", "--timeout", "480"])
            message = 'Disk write stress started with 3GB for 7 Minutes.'
        except Exception as e:
            message = str(e)
        return render_template('disk_write_stress.html', message=message)
    else:
        return render_template('disk_write_stress.html')

@app.route('/start_full_stress', methods=['GET', 'POST'])
def start_full_stress():
    if request.method == 'POST':
        try:
            subprocess.Popen(["stress", "--cpu", "1", "--vm", "1", "--vm-bytes", "3G", "--timeout", "300"])
            message = 'CPU and RAM stress started for 300 seconds.'
        except Exception as e:
            message = str(e)
        return render_template('full_stress.html', message=message)
    else:
        return render_template('full_stress.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)