from functions.get_files_info import get_files_info


def main():
    # Test 1: Current directory
    result1 = get_files_info("calculator", ".")
    print("get_files_info(\"calculator\", \".\"):")
    print("Result for current directory:")
    for line in result1.split("\n"):
        print(f"  {line}")
    print()

    # Test 2: pkg subdirectory
    result2 = get_files_info("calculator", "pkg")
    print("get_files_info(\"calculator\", \"pkg\"):")
    print("Result for 'pkg' directory:")
    for line in result2.split("\n"):
        print(f"  {line}")
    print()

    # Test 3: Attempt to access /bin (outside working directory)
    result3 = get_files_info("calculator", "/bin")
    print("get_files_info(\"calculator\", \"/bin\"):")
    print("Result for '/bin' directory:")
    print(f"    {result3}")
    print()

    # Test 4: Attempt to access ../ (outside working directory)
    result4 = get_files_info("calculator", "../")
    print("get_files_info(\"calculator\", \"../\"):")
    print("Result for '../' directory:")
    print(f"    {result4}")


if __name__ == "__main__":
    main()
