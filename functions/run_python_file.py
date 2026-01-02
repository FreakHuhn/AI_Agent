import os
import subprocess
import sys
from google.genai import types


schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Executes a Python file within the working directory with optional arguments",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path to the Python file to run, relative to the working directory",
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                description="Optional list of arguments to pass to the Python file",
                items=types.Schema(type=types.Type.STRING),
            ),
        },
        required=["file_path"],
    ),
)


def run_python_file(working_directory, file_path, args=None):
    try:
        working_dir_abs = os.path.abspath(working_directory)
        target_file = os.path.normpath(os.path.join(working_dir_abs, file_path))

        # Ensure the target file stays within the permitted working directory
        if os.path.commonpath([working_dir_abs, target_file]) != working_dir_abs:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

        # Validate that the target exists and is a regular file
        if not os.path.isfile(target_file):
            return f'Error: "{file_path}" does not exist or is not a regular file'

        # Only allow Python files
        if not target_file.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file'

        python_exec = sys.executable or "python"
        command = [python_exec, target_file]
        if args:
            command.extend(args)

        result = subprocess.run(
            command,
            cwd=working_dir_abs,
            capture_output=True,
            text=True,
            timeout=30,
        )

        output_parts = []

        if result.returncode != 0:
            output_parts.append(f"Process exited with code {result.returncode}")

        has_stdout = bool(result.stdout)
        has_stderr = bool(result.stderr)

        if not has_stdout and not has_stderr:
            output_parts.append("No output produced")
        else:
            if has_stdout:
                output_parts.append(f"STDOUT:\n{result.stdout}")
            if has_stderr:
                output_parts.append(f"STDERR:\n{result.stderr}")

        return "\n".join(output_parts)

    except Exception as e:
        return f"Error: executing Python file: {e}"
