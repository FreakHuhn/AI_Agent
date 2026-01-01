import os


def write_file(working_directory, file_path, content):
    """
    Write content to a file within a permitted working directory.
    
    Args:
        working_directory: The base directory where files can be written
        file_path: The relative path to the file to write (relative to working_directory)
        content: The string content to write to the file
    
    Returns:
        A success message string or an error message string prefixed with 'Error:'
    """
    try:
        # Convert working_directory to an absolute path and normalize it
        working_dir_abs = os.path.abspath(working_directory)
        
        # Join the working directory with the target file path and normalize it
        # This handles relative paths like "../../../etc/passwd" safely
        target_file = os.path.normpath(os.path.join(working_dir_abs, file_path))

        # Validate that the target file is within the permitted working directory
        # If the common path between them is not the working directory, 
        # the target file is outside the permitted area (e.g., /tmp/file.txt)
        if os.path.commonpath([working_dir_abs, target_file]) != working_dir_abs:
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

        # Check if the target path points to an existing directory
        # We should not overwrite a directory with file content
        if os.path.isdir(target_file):
            return f'Error: Cannot write to "{file_path}" as it is a directory'

        # Create all necessary parent directories if they don't exist
        # exist_ok=True means it won't raise an error if the directory already exists
        parent_directory = os.path.dirname(target_file)
        if parent_directory:  # Only create if there's a parent directory
            os.makedirs(parent_directory, exist_ok=True)

        # Open the file in write mode ("w") and write the content to it
        # Using 'with' statement ensures the file is properly closed afterwards
        with open(target_file, "w") as f:
            f.write(content)

        # Return a success message with feedback about how many characters were written
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'

    except Exception as e:
        # Catch any unexpected errors from os or file operations
        # Return them as error messages prefixed with 'Error:'
        return f'Error: {str(e)}'
