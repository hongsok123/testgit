from math import sqrt

n = 112
xbar = 78_695
conf = 0.95
s = 14_530

mu = 74_914

z = (xbar - mu)/(s / sqrt(n))

if z > z_for_conf(conf) or z < -z_for_conf(conf):
    print("Rejected")
else:
    print("Not rejected")
