from flask import Flask, jsonify
import subprocess

app = Flask(__name__)

@app.route('/start_cpu_stress', methods=['GET'])
def start_cpu_stress():
    try:
        # Stress 1 CPUs for 300 seconds
        subprocess.Popen(["stress", "--cpu", "1", "--timeout", "300"])
        return jsonify({'message': 'CPU stress started for 300 seconds'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/start_ram_stress', methods=['GET'])
def start_ram_stress():
    try:
        # Stress RAM by allocating 6GB for 300 seconds
        subprocess.Popen(["stress", "--vm", "1", "--vm-bytes", "4G", "--timeout", "300"])
        return jsonify({'message': 'RAM stress started with 4GB for 300 seconds'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/start_disk_io_stress', methods=['GET'])
def start_disk_io_stress():
    try:
        # Stress disk I/O for 300 seconds
        subprocess.Popen(["stress", "--io", "2", "--timeout", "300"])
        return jsonify({'message': 'Disk I/O stress started for 300 seconds'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/start_disk_write_stress', methods=['GET'])
def start_disk_write_stress():
    try:
        # Write 3GB to disk for 480 seconds
        subprocess.Popen(["stress", "--hdd", "2", "--hdd-bytes", "3G", "--timeout", "480"])
        return jsonify({'message': 'Disk write stress started with 3GB for 7 Minutes'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/start_full_stress', methods=['GET'])
def start_full_stress():
    try:
        # Stress both 2 CPUs and allocate 6GB RAM for 300 seconds
        subprocess.Popen(["stress", "--cpu", "1", "--vm", "1", "--vm-bytes", "3G", "--timeout", "300"])
        return jsonify({'message': 'CPU and RAM stress started for 300 seconds'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
