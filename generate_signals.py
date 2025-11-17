import numpy as np
import os

# --- 파라미터 ---
fs = 20e6  # 샘플링 레이트 (예: 20MHz)
duration = 1  # 1초
n_samples = int(fs * duration)
t = np.arange(n_samples) / fs

# --- 디렉토리 생성 ---
os.makedirs('data', exist_ok=True)

# 1. 원본 Wi-Fi 신호 생성 (단순 사인파로 시뮬레이션)
# (2.412GHz 신호를 20MHz로 샘플링하면 12MHz의 aliased 신호가 됨)
freq_wifi = 2.412e9
wifi_signal = np.sin(2 * np.pi * (freq_wifi % fs) * t)

# 2. Jammer 신호 생성 (Abstract 기반)
# (Amplitude 50, Gaussian noise)
# np.random.normal의 scale(표준편차)이 가우시안 노이즈의 '세기'이며,
# 여기에 50을 곱해 진폭(Amplitude)을 맞추기
noise_power_scale = 1.0 
jammer_noise = 50 * np.random.normal(0, noise_power_scale, n_samples)

# 3. 파일로 저장 (NumPy 배열) 
np.save('data/wifi_signal.npy', wifi_signal)
np.save('data/jammer_noise.npy', jammer_noise)

print("Project 1: 신호 생성 완료!")
print(f"  - data/wifi_signal.npy (샘플: {n_samples}개)")
print(f"  - data/jammer_noise.npy (진폭: 50)")