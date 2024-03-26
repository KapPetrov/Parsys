# Instruction table mapping
instruction_table = {
    'ADD': '0001',
    'SUB': '0010',
    'OUT': '1001',
    'LDA': '1100',
    'JMP': '0011',
    'HLT': '0000'
}

def process_instruction(instruction):
    # Split the instruction into opcode and operand if it contains a space
    if ' ' in instruction:
        opcode, operand = instruction.split()
        
        # Convert the opcode to binary according to the instruction table
        opcode_binary = instruction_table[opcode]
        
        # Convert the operand to binary (assuming it's an integer)
        operand_binary = bin(int(operand))[2:].zfill(8)
        
        # Concatenate opcode and operand and return the result
        return opcode_binary + operand_binary
    else:
        # If no operand is present, only convert the opcode
        opcode_binary = instruction_table[instruction]
        return opcode_binary + '00000000'

def main():
    # Read input from main.asm file
    with open('main.asm', 'r') as f:
        instructions = f.readlines()
    
    # Process each instruction
    processed_instructions = [process_instruction(instruction.strip()) for instruction in instructions]
    
    # Write the processed instructions to output.txt
    with open('output.txt', 'w') as f:
        f.write('\n'.join(processed_instructions))

if __name__ == "__main__":
    main()
