import math

BASE_H = 0.10
L1 = 0.10
L2 = 0.25
L3 = 0.30      # elbow to the point the fingers close on
SHOULDER_H = BASE_H + L1


def fk(theta1, theta2, theta3):
    reach = L2 * math.sin(theta2) + L3 * math.sin(theta2 + theta3)
    rise = L2 * math.cos(theta2) + L3 * math.cos(theta2 + theta3)
    return reach * math.cos(theta1), reach * math.sin(theta1), SHOULDER_H + rise


def ik(x, y, z):
    theta1 = math.atan2(y, x)
    r = math.hypot(x, y)
    s = z - SHOULDER_H
    D = (r * r + s * s - L2 * L2 - L3 * L3) / (2 * L2 * L3)   # law of cosines for the elbow
    if abs(D) > 1:
        return None
    theta3 = math.acos(D)
    k1 = L2 + L3 * math.cos(theta3)
    k2 = L3 * math.sin(theta3)
    theta2 = math.atan2(r, s) - math.atan2(k2, k1)
    return theta1, theta2, theta3


if __name__ == "__main__":
    import random
    random.seed(0)
    worst = 0.0
    for _ in range(20):
        p = fk(random.uniform(-math.pi, math.pi),
               random.uniform(-1.5, 1.5),
               random.uniform(0.2, 2.5))
        worst = max(worst, math.dist(p, fk(*ik(*p))))
    print("max round-trip error:", worst)
