import os
import sys

# Add the project root to the path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from functions.get_file_content import get_file_content
from config import MAX_CHARS

def test_get_file_content():
    print("Testing get_file_content function...\n")
    
    # Test 1: Read lorem.txt with truncation
    print("Test 1: get_file_content('calculator', 'lorem.txt')")
    result = get_file_content("calculator", "lorem.txt")
    print(f"Content length: {len(result)}")
    print(f"Ends with truncation message: {result.endswith(']')}")
    print(f"Last 150 characters:\n{result[-150:]}\n")
    
    # Test 2: Read main.py
    print("Test 2: get_file_content('calculator', 'main.py')")
    result = get_file_content("calculator", "main.py")
    print(f"Content length: {len(result)}")
    print(f"Content preview:\n{result[:200]}...\n")
    
    # Test 3: Read pkg/calculator.py
    print("Test 3: get_file_content('calculator', 'pkg/calculator.py')")
    result = get_file_content("calculator", "pkg/calculator.py")
    print(f"Content length: {len(result)}")
    print(f"Content:\n{result}\n")
    
    # Test 4: Try to read /bin/cat (should error)
    print("Test 4: get_file_content('calculator', '/bin/cat')")
    result = get_file_content("calculator", "/bin/cat")
    print(f"Result: {result}\n")
    
    # Test 5: Try to read non-existent file
    print("Test 5: get_file_content('calculator', 'pkg/does_not_exist.py')")
    result = get_file_content("calculator", "pkg/does_not_exist.py")
    print(f"Result: {result}\n")

if __name__ == "__main__":
    test_get_file_content()
