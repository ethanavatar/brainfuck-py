# Brainfuck-py
A Brainfuck interpreter written in Python.

# Usage
```bash
Usage: python3 brainfuck.py [options] <input>
Options:
        -f <file>       Read program from file
        -s <string>     Read program from string
```

For example:
```bash
$ python3 brainfuck.py -f brainfuck.bf
Hello, world!

$ python3 brainfuck.py -s "++++++++[>++++[>++>+++>+++>+<<<<-]>+>+>->>+[<]<-]>>.>---.+++++++..+++.>>.<-.<.+++.------.--------.>>+.>++."
Hello, world!
```

It can also be used in-line by importing it as a module:
```python
>>> from brainfuck import brainfuck
>>> program = "++++++++[>++++[>++>+++>+++>+<<<<-]>+>+>->>+[<]<-]>>.>---.+++++++..+++.>>.<-.<.+++.------.--------.>>+.>++."
>>> brainfuck(program)
Hello, world!
```


# TODO
 - Debuging tools
 - Optimization
 - Rewrite in rust maybe
