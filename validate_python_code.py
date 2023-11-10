import os
import subprocess
import sys

def run_command(command):
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    return stdout.decode("utf-8"), stderr.decode("utf-8"), process.returncode

def validate_python_code(file_path):
    print(f"Validating Python code in {file_path}...")

    # Linting with Pylint
    print("Running Pylint...")
    stdout, stderr, returncode = run_command(["pylint", file_path])
    if returncode != 0:
        print("Pylint found issues:")
        print(stderr)
    else:
        print("No issues found by Pylint.")

    # Type checking with Mypy
    print("Running Mypy...")
    stdout, stderr, returncode = run_command(["mypy", file_path])
    if returncode != 0:
        print("Mypy found issues:")
        print(stderr)
    else:
        print("No issues found by Mypy.")

    # Unit testing with pytest
    print("Running pytest...")
    stdout, stderr, returncode = run_command(["pytest", file_path])
    if returncode != 0:
        print("pytest found issues:")
        print(stderr)
    else:
        print("No issues found by pytest.")

    # Code formatting check with Black
    print("Checking code formatting with Black...")
    stdout, stderr, returncode = run_command(["black", "--check", file_path])
    if returncode != 0:
        print("Black found formatting issues:")
        print(stderr)
    else:
        print("No formatting issues found by Black.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python validate_python_code.py <file_path>")
        sys.exit(1)

    file_path = sys.argv[1]
    if not os.path.isfile(file_path):
        print(f"No such file: {file_path}")
        sys.exit(1)

    validate_python_code(file_path)