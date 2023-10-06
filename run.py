import subprocess


def run_python_script():
    script_path = "app.py"

    subprocess.Popen(["python3", script_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE)


run_python_script()
