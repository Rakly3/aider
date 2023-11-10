import os
import subprocess
import venv

def main():
    # Create a virtual environment
    venv_dir = "/tmp/venv"
    venv.create(venv_dir, with_pip=True)

    # Install packages in the virtual environment
    requirements_file = "/requirements.txt"
    subprocess.run([os.path.join(venv_dir, "bin", "pip"), "install", "-r", requirements_file], check=True)

    # Check for broken dependencies
    result = subprocess.run([os.path.join(venv_dir, "bin", "pip"), "check"], capture_output=True, text=True)

    # Output the result
    print(result.stdout)

if __name__ == "__main__":
    main()