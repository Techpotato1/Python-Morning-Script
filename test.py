#!/usr/bin/python3

# Calculate PI number using this formula:
# x[n+1] = x[n] + sin(x[n])
#
# x[n+1] = x[n] + x[n] + x[n]**3/fact(3) - x[n]**5/fact(5) + x[n]**7/fact(7) - x[n]**9/fact(9) + ....

from decimal import getcontext, Decimal
import sys

if len(sys.argv) < 2:
    print('Not enough arguments')
    quit()

precision = int(sys.argv[1])
excess_prec = 2

prec_cur = 100 if precision > 100 else precision

getcontext().prec = prec_cur + excess_prec

second = Decimal(3)  # Current element for PI
queue_cur = [Decimal(0), Decimal(0), Decimal(0), second]

qq_append = queue_cur.append
qq_pop = queue_cur.pop

limit = Decimal(10) ** (-prec_cur - excess_prec)

while True:

    sec_sq = second * second
    term = second
    acc = second + term
    count = Decimal(1)

    while term > limit:

        term *= sec_sq / ((count + 1) * (count + 2))
        acc -= term
        # print ('term1: {}'.format(term))

        term *= sec_sq / ((count + 3) * (count + 4))
        acc += term

        count += 4
        # print ('term2: {}'.format(term))

    # print ('acc: {}'.format(second))
    if acc in queue_cur:
        if prec_cur < precision:
            prec_cur += prec_cur
            if prec_cur > precision:
                prec_cur = precision
            limit = Decimal(10) ** (-prec_cur - excess_prec)
            getcontext().prec = prec_cur + excess_prec

        else:
            second = acc
            break

    qq_append(acc)
    qq_pop(0)
    second = acc
    # print ('second: {}'.format(second))

getcontext().prec = precision
print("PI: ", +second)