import numpy as np
from scipy.io.wavfile import write
import os

# --- 파라미터 ---
fs_audio = 48000  # 오디오 샘플링 레이트 (48kHz)
duration = 10  # 10초
frequency = 1000  # 1kHz
amplitude = 0.5

# --- 디렉토리 생성 ---
os.makedirs('data', exist_ok=True)

# --- 1kHz 톤 생성 ---
t = np.linspace(0., duration, int(fs_audio * duration), endpoint=False)
audio_signal = amplitude * np.sin(2 * np.pi * frequency * t)

# --- .wav 파일로 저장 ---
# (scipy.io.write는 -1과 1 사이의 float를 받아 처리)
write('data/audio_source.wav', fs_audio, audio_signal.astype(np.float32))
print(f"Project 2: 'data/audio_source.wav' (48kHz, 1kHz 톤) 생성 완료!")