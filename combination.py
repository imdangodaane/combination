#!/usr/bin/env python3


def combination(elems, size):
    if len(elems) <= 1:
        return [elems]
    else:
        lst = []
        for i in range(len(elems)):
            m = [elems[i]]
            remainElems = elems[i+1:]
            print('remainElems =', remainElems)
            for p in combination(remainElems, size):
                print('p = ', p)
                print('m + p =', m + p)
                if len(m + p) == size:
                    lst.append(m + p)
                else:
                    m = m + p
                print('list = ', lst)
    return lst


print(combination([1, 2, 3, 4, 5], 2))
