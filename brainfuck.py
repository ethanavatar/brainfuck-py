def brainfuck(program : str):
    memory = [0]
    pointer = 0
    i = 0
    while i < len(program):
        if program[i] == '>':
            pointer += 1
            if pointer == len(memory):
                memory.append(0)
        elif program[i] == '<':
            pointer -= 1
            if pointer < 0:
                raise Exception('Pointer is out of bounds')
        elif program[i] == '+':
            memory[pointer] += 1
        elif program[i] == '-':
            memory[pointer] -= 1
        elif program[i] == '.':
            print(chr(memory[pointer]), end='')
        elif program[i] == ',':
            memory[pointer] = ord(input())
        elif program[i] == '[':
            if memory[pointer] == 0:
                brace = 1
                while brace != 0:
                    i += 1
                    if program[i] == '[':
                        brace += 1
                    elif program[i] == ']':
                        brace -= 1
                i += 1
                

        elif program[i] == ']':
            if memory[pointer] != 0:
                brace = 1
                while brace != 0:
                    i -= 1
                    if program[i] == ']':
                        brace += 1
                    elif program[i] == '[':
                        brace -= 1
                i -= 1
        i += 1



if __name__ == '__main__':
    import sys

    if sys.argv[1] == '-f' and len(sys.argv) == 3:
        program = open(sys.argv[2], 'r').read()

    elif sys.argv[1] == '-s' and len(sys.argv) == 3:
        program = sys.argv[2]

    else:
        print('Usage: python3 brainfuck.py [options] <input>')
        print('Options:')
        print('\t-f <file>\tRead program from file')
        print('\t-s <string>\tRead program from string')
        sys.exit(1)

    brainfuck(program)