import matplotlib.pyplot as plt
import os

# (analyze_snr.py에서 계산된 값을 여기에 하드코딩하거나 파일로 저장해서 불러오기. 여기서는 간단히 하드코딩)
snr_values = {
    'Jammer OFF': 18.59,  # <-- analyze_snr.py 결과값으로 변경
    'Jammer ON': -36.99   # <-- analyze_snr.py 결과값으로 변경
}

# --- 디렉토리 생성 ---
os.makedirs('results', exist_ok=True)

# --- 막대 그래프 생성 ---
plt.figure(figsize=(8, 6))
bars = plt.bar(snr_values.keys(), snr_values.values(), color=['green', 'red'])
plt.ylabel('Signal-to-Noise Ratio (SNR) [dB]')
plt.title('SNR Comparison: Jammer Activated vs. Deactivated')

# 그래프에 값 표시
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2.0, yval, f'{yval:.2f} dB', va='bottom' if yval > 0 else 'top')

# --- 그래프 파일로 저장 ---
plt.savefig('results/snr_comparison.png')
print("Project 1: 'results/snr_comparison.png' 그래프 저장 완료!")