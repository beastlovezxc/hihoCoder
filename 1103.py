while True:
    try:
        chs = raw_input()

        length = len(chs)

        stack = []
        i = 0
        rn = 0
        bn = 0
        yn = 0
        while i < length:
            if chs[i] == '<':
                if chs[i + 1] == 'r':
                    stack.append('r')
                    i += 5
                    continue
                elif chs[i + 1] == 'b':
                    stack.append('b')
                    i += 6
                    continue
                elif chs[i + 1] == 'y':
                    stack.append('y')
                    i += 8
                    continue
                elif chs[i + 1] == '/':
                    if chs[i + 2] == 'r':
                        stack.pop()
                        i += 6
                        continue
                    elif chs[i + 2] == 'b':
                        stack.pop()
                        i += 7
                        continue
                    elif chs[i + 2] == 'y':
                        stack.pop()
                        i += 9
                        continue
            else:
                if stack and chs[i].isalpha():
                    if stack[-1] == 'r':
                        rn += 1
                    elif stack[-1] == 'b':
                        bn += 1
                    elif stack[-1] == 'y':
                        yn += 1
            i += 1

        print rn, yn, bn
    except EOFError:
        break
