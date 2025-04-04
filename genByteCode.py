import dis
import py_compile
import importlib.util
import os
import sys

def compile_and_disassemble(source_file):
    """Compiles a Python source file and disassembles its bytecode without marshal."""

    try:
        # Generate the .pyc file
        py_compile.compile(source_file, doraise=True)

        # Get the .pyc file path
        bytecode_file = importlib.util.cache_from_source(source_file)

        # Read the code object from the .pyc file
        with open(bytecode_file, "rb") as f, open(str(f"{source_file}.byteCode"), "w") as out_f:
            f.read(4)  # Skip magic number
            f.read(4)  # Skip timestamp
            code_object = compile(open(source_file).read(), source_file, 'exec') #recompile the source code.
            dis.dis(code_object, file=out_f)
        print(f"\nDisassembly of {source_file}:\n")

    except py_compile.PyCompileError as e:
        print(f"Compilation error: {e}")
        sys.exit(1)
    except FileNotFoundError:
        print(f"Bytecode file not found after compilation.")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python compile_disassemble.py <source_file>")
        sys.exit(1)

    source_file = sys.argv[1]

    if not os.path.exists(source_file):
        print(f"Error: Source file '{source_file}' not found.")
        sys.exit(1)

    compile_and_disassemble(source_file)  