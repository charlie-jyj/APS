def recur_reverse(string):
    if len(string) == 1:
        return string
    else:
        return recur_reverse(string[-1]) + recur_reverse(string[:len(string)-1:])


print(recur_reverse('apple'))