def max_cont_cnar(line,c):
    line_copy =line
    n = 0
    answer= []

    while n < 9:
        result =''
        while line_copy[n] ==c:
            result += c
            n += 1

            if n == len(line):
                break

        answer.append(len(result))
              
        fake_result =''
        while line_copy[n] !=c:
            fake_result += ' '
            answer.append(0)
            n += 1

            if n == len(line):
                break

        answer.append(0)
    
    return max(answer)
    
print(max_cont_cnar('おののひほののののかのかかお','の'))
