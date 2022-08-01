def past(h, m, s):
    milliseconds = 0
    if 0 <= h <= 23:
        milliseconds += h * 60 * 60 * 1000
    if 0 <= m <= 59:
        milliseconds += m * 60 * 1000
    if 0 <= m <= 59:
        milliseconds += s * 1000
    return milliseconds


past(1,0,1)
past(1, 0, 0)
