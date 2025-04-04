# Python Bytecode Analysis and Profiling

## Overview

This project is designed to analyze Python scripts by generating their bytecode, counting the bytecode instructions, and profiling their execution. The goal is to identify the most commonly used bytecode instructions across a variety of Python scripts and gain insights into their performance characteristics.

The project consists of the following components:
1. **Bytecode Generation**: Converts a Python script into its bytecode and writes the disassembled bytecode to a file.
2. **Instruction Counting**: Counts the frequency of each bytecode instruction and writes the results to a file.
3. **Profiling**: Profiles the execution of the Python script using `cProfile` and generates a `.prof` file for further analysis.

---

## File Structure

### 1. `genByteCode_v2.py`
This script is the core of the project. It performs the following tasks:
- **Generate Bytecode**: Reads a Python script, compiles it into bytecode, and writes the disassembled bytecode to a file.
- **Count Instructions**: Counts the frequency of each bytecode instruction and writes the results to a file.
- **Run Profiler**: Profiles the execution of the Python script using `cProfile` and saves the profiling data to a `.prof` file.

#### Usage
```bash
python genByteCode_v2.py <path_to_python_file>
```

#### Outputs
- `<script_name>_bytecode.txt`: Contains the disassembled bytecode of the script.
- `<script_name>_instr_count.txt`: Contains the frequency of each bytecode instruction.
- `<script_name>.prof`: Contains profiling data for the script.

---

### 2. `matrixMul.py`
This script demonstrates matrix multiplication using the `numpy` library.

#### Usage
Run the script directly:
```bash
python matrixMul.py
```

#### Example Input
Matrix 1:
```
[[1, 2, 3],
 [4, 5, 6]]
```

Matrix 2:
```
[[7, 8],
 [9, 10],
 [11, 12]]
```

#### Example Output
Resultant Matrix:
```
[[58, 64],
 [139, 154]]
```

---

### 3. `matrixMulBuiltin.py`
This script demonstrates matrix multiplication using Python's built-in functionality (without `numpy`).

#### Usage
Run the script directly:
```bash
python matrixMulBuiltin.py
```

#### Example Input
Matrix 1:
```
[[1, 2, 3],
 [4, 5, 6]]
```

Matrix 2:
```
[[7, 8],
 [9, 10],
 [11, 12]]
```

#### Example Output
Resultant Matrix:
```
[[58, 64],
 [139, 154]]
```

---
## Workflow

1. **Analyze a Script**:
   - Run the `genByteCode_v2.py` script with the target Python file as an argument.
   - Example:
     ```bash
     python genByteCode_v2.py matrixMul.py
     ```
   - Outputs:
     - `matrixMul_bytecode.txt`: Disassembled bytecode.
     - `matrixMul_instr_count.txt`: Bytecode instruction counts.
     - `matrixMul.prof`: Profiling data.

2. **Profile a Script**:
   - Use the `run_profiler` function in `genByteCode_v2.py` to profile the script.
   - View the profiling results using `snakeviz`:
     ```bash
     snakeviz matrixMul.prof
     ```

3. **Matrix Multiplication**:
   - Compare the performance of matrix multiplication using `numpy` (`matrixMul.py`) and Python's built-in functionality (`matrixMulBuiltin.py`).

---

## Dependencies

- Python 3.x
- `numpy` (for `matrixMul.py`)
- `snakeviz` (for visualizing profiling data)

Install dependencies using `pip`:
```bash
pip install numpy snakeviz
```
