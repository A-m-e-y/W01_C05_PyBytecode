import collections
import sys

def count_instructions(disassembly_file):
    """Counts the occurrences of each instruction in a disassembly file."""

    instructions = []
    try:
        with open(disassembly_file, "r") as f:
            for line in f:
                parts = line.split()
                if len(parts) >= 2 and parts[1].isupper(): #check if second part is an instruction
                    instructions.append(parts[1])

        instruction_counts = collections.Counter(instructions)
        return instruction_counts

    except FileNotFoundError:
        print(f"Error: Disassembly file '{disassembly_file}' not found.")
        return None
    
counts = count_instructions(sys.argv[1])
with open(str(f"{sys.argv[1]}.cntInstr"), "w") as f:
    if counts:
            print("\nInstruction Counts (Highest to Lowest):")
            sorted_counts = sorted(counts.items(), key=lambda item: item[1], reverse=True) #sort from highest to lowest.
            for instruction, count in sorted_counts:
                print(f"{instruction}: {count}")
                f.write(f"{instruction}: {count}\n")
