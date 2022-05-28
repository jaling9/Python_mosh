def find_max(numbers):
    maximum = numbers[0] # 设置一个最大值，这个最大值也可能是错误的
                 # 所以我们需要遍历整个列表与max比较，如果它大于max，将其重置为该数字。
    for number in numbers:
        if number > maximum:
            maximum = number
        else:
            number <= maximum
        continue
    return(maximum)