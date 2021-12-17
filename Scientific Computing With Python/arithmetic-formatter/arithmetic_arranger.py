import sys


def arithmetic_arranger(problems, results=False):
    t = ""
    b = ""
    hyphen = ""
    solution = ""
    if len(problems) > 5:
        return "Error: Too many problems."
        sys.exit(0)

    for e, r in enumerate(problems):
        r = r.split(' ')

        if r[0].isdigit() is False:
            return "Error: Numbers must only contain digits."
            sys.exit(0)
        if r[2].isdigit() is False:
            return "Error: Numbers must only contain digits."
            sys.exit(0)

        res = max(r, key=len)
        sol = (' '.join(r))
        solutions = eval(sol)

        if r[1] == "*":
            return "Error: Operator must be '+' or '-'."
        if r[1] == "/":
            return "Error: Operator must be '+' or '-'."
        if len(res) > 4:
            return "Error: Numbers cannot be more than four digits."
            sys.exit(0)

        if len(r[0]) < len(r[2]):  #3 + 855
            b4_spaces = len(r[2]) + 2  #5
            length = len(str(solutions))  #3
            rw1_space = b4_spaces - len(r[0])  #4
            w = " " * rw1_space  #"----"
            t += w + r[0] + "    "
            b += r[1] + " " + r[2] + "    "
            hyphen += b4_spaces * "-" + "    "
            solution += " " * (b4_spaces - length) + str(solutions) + "    "

        if len(r[0]) == len(r[2]):
            b4_spaces = len(r[0]) + 2
            rw1_space = b4_spaces - len(r[0])
            w = " " * rw1_space
            t += w + r[0] + "    "
            b += r[1] + " " + r[2] + "    "
            hyphen += b4_spaces * "-" + "    "
            solution += w + str(solutions) + "    "

        if len(r[0]) > len(r[2]):
            w = " " * ((len(r[0]) + 2) - (len(r[2]) + 1))
            length = len(str(solutions))  # 4
            t += "  " + r[0] + "    "
            b += r[1] + w + r[2] + "    "
            hyphen += (len(r[0]) + 2) * "-" + "    "
            solution += (
                (len(r[0]) + 2) - length) * " " + str(solutions) + "    "

    t = t.rstrip()
    t += t.join("\n")
    b = b.rstrip()
    b += b.join("\n")
    hyphen = hyphen.rstrip()
    solution = solution.rstrip()

    if results:
        hyphen += hyphen.join("\n")
        return t + b + hyphen + solution
    else:
        return t + b + hyphen
