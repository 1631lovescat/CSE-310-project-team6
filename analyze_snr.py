import numpy as np

# --- SNR 계산 함수 ---
def calculate_snr(signal, noise):
    signal_power = np.mean(signal ** 2)
    noise_power = np.mean(noise ** 2)
    
    if noise_power == 0:
        return float('inf')
        
    snr_ratio = signal_power / noise_power
    snr_db = 10 * np.log10(snr_ratio)
    return snr_db

# --- 신호 로드 ---
try:
    wifi_signal = np.load('data/wifi_signal.npy')
    jammer_noise = np.load('data/jammer_noise.npy')
except FileNotFoundError:
    print("에러: 먼저 generate_signals.py를 실행하세요.")
    exit()

# --- 시나리오 A: Jammer 비활성화 (아주 약한 기본 잡음 시뮬레이션) ---
# (wifi_signal 표준편차의 약 1/8.5 수준으로 잡음 설정 -> 약 18.5dB SNR이 됨)
base_noise = np.random.normal(0, np.std(wifi_signal) / 8.5, len(wifi_signal))
snr_no_jammer = calculate_snr(wifi_signal, base_noise)

# --- 시나리오 B: Jammer 활성화 ---
snr_with_jammer = calculate_snr(wifi_signal, jammer_noise)

print("Project 1: SNR 분석 결과")
print("====================================")
print(f"시나리오 A (Jammer OFF): {snr_no_jammer:.2f} dB")
print(f"시나리오 B (Jammer ON) : {snr_with_jammer:.2f} dB")
print("====================================")
print(f"SNR 저하: {snr_no_jammer - snr_with_jammer:.2f} dB")