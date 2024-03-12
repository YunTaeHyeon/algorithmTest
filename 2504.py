string = input()

stack = []

def cal(string):

    res = 0
    temp = 0

    for i in range(len(string)):

        if string[i]=="[":
            stack.append(string[i])

        elif string[i]=="(":
            stack.append(string[i])

        
        if len(stack) != 0:
            if string[i]=="]":
                item = stack.pop(-1)

                temp = 3

                if item != "[":
                    return 0
                
                if len(stack) != 0:
                    for j in stack:
                        if j == "(":
                            temp *= 2
                        else:
                            temp *= 3
                            print(temp)
                
            if string[i]==")":
                item = stack.pop(-1)

                temp = 2

                if item != "(":
                    return 0

                if len(stack) != 0:
                    for j in stack:
                        if j == "(":
                            temp *= 2
                        else:
                            temp *= 3

            
            
            res = res + temp

        else:
            return 0

    return res

result = cal(string)

print(result)

#낙곱새, 유타로, 등갈비