import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)

dt = 0.1
v = 0.5
N = 200
sigma = 1.0

t = np.arange(N) * dt
x_true = v * t
z = x_true + np.random.normal(0, sigma, N)

Q = 1e-3        # process noise: how much we distrust the motion model
R = sigma**2    # measurement noise: how noisy the sensor is

x_est = 0.0     # state estimate: our best guess of the position
P = 1.0         # error covariance: how unsure we are about that guess

est = np.zeros(N)
for k in range(N):
    x_pred = x_est + v * dt
    P_pred = P + Q
    K = P_pred / (P_pred + R)          # kalman gain: how much to trust the measurement
    x_est = x_pred + K * (z[k] - x_pred)
    P = (1 - K) * P_pred
    est[k] = x_est

plt.figure(figsize=(10, 5))
plt.plot(t, z, color="0.7", linewidth=1, label="noisy measurements")
plt.plot(t, x_true, "g-", linewidth=2, label="true path")
plt.plot(t, est, "b-", linewidth=2, label="kalman estimate")
plt.xlabel("time (s)")
plt.ylabel("position (m)")
plt.title("1D Kalman filter")
plt.legend()
plt.grid(True, alpha=0.3)
plt.savefig("kalman_plot.png", dpi=150)
plt.show()
