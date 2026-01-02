import os
import sys

# Add the project root to the path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from functions.run_python_file import run_python_file


def test_run_python_file():
    print("Testing run_python_file function...\n")

    print("Test 1: run_python_file('calculator', 'main.py')")
    result = run_python_file("calculator", "main.py")
    print(f"Result:\n{result}\n")

    print("Test 2: run_python_file('calculator', 'main.py', ['3 + 5'])")
    result = run_python_file("calculator", "main.py", ["3 + 5"])
    print(f"Result:\n{result}\n")

    print("Test 3: run_python_file('calculator', 'tests.py')")
    result = run_python_file("calculator", "tests.py")
    print(f"Result:\n{result}\n")

    print("Test 4: run_python_file('calculator', '../main.py') (should error)")
    result = run_python_file("calculator", "../main.py")
    print(f"Result:\n{result}\n")

    print("Test 5: run_python_file('calculator', 'nonexistent.py') (should error)")
    result = run_python_file("calculator", "nonexistent.py")
    print(f"Result:\n{result}\n")

    print("Test 6: run_python_file('calculator', 'lorem.txt') (should error)")
    result = run_python_file("calculator", "lorem.txt")
    print(f"Result:\n{result}\n")


if __name__ == "__main__":
    test_run_python_file()
