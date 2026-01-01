import os
import sys

# Add the project root to the path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from functions.write_file import write_file


def test_write_file():
    """Test the write_file function with various scenarios."""
    print("Testing write_file function...\n")
    
    # Test 1: Write to a file within the working directory (with nested directory creation)
    print("Test 1: write_file('calculator', 'lorem.txt', 'wait, this isn\\'t lorem ipsum')")
    result = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
    print(f"Result: {result}\n")
    
    # Test 2: Write to a nested file path (creates directories if needed)
    print("Test 2: write_file('calculator', 'pkg/morelorem.txt', 'lorem ipsum dolor sit amet')")
    result = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
    print(f"Result: {result}\n")
    
    # Test 3: Try to write outside the permitted working directory (should fail)
    print("Test 3: write_file('calculator', '/tmp/temp.txt', 'this should not be allowed')")
    result = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
    print(f"Result: {result}\n")


if __name__ == "__main__":
    test_write_file()
