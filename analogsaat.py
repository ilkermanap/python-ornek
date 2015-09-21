__author__ = 'ilker'

import math, time


def radian(ang):
    return ang * math.pi / 180.0


def analog_saat(r=100):
    t = time.localtime()
    h = t.tm_hour
    h = h % 12
    m = t.tm_min
    s = t.tm_sec

    print h, m, s
    secangle = radian(s * 6)
    sx = r * math.sin(secangle)
    sy = r * math.cos(secangle)

    print sx, sy

    minangle = radian(m * 6)
    mx = r * math.sin(minangle)
    my = r * math.cos(minangle)
    print mx, my

    hangle = radian((h * 30) + ((m / 60) * 30))
    hx = r * math.sin(hangle)
    hy = r * math.cos(hangle)
    print hx, hy
    return ((hx, hy), (mx, my), (sx, sy))


analog_saat()
