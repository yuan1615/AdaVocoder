# import os
# from shutil import copyfile
# import librosa
# from scipy.io import wavfile
# import numpy as np
# from tqdm import tqdm
#
# save_path = '/home/admin/yuanxin/2.TTSData/AISHELL-3/wavs'
#
# train_path = '/home/admin/yuanxin/2.TTSData/AISHELL-3/train/wav'
# train_file = '/home/admin/yuanxin/2.TTSData/AISHELL-3/train/content.txt'
# test_path = '/home/admin/yuanxin/2.TTSData/AISHELL-3/test/wav'
# test_file = '/home/admin/yuanxin/2.TTSData/AISHELL-3/test/content.txt'
#
#
# file_list = os.listdir(train_path)
# for speaker_name in file_list:
#     wave_list = os.listdir(os.path.join(train_path, speaker_name))
#     for wavname in wave_list:
#         copyfile(os.path.join(train_path, speaker_name, wavname), os.path.join(save_path, wavname))
#
# file_list = os.listdir(test_path)
# for speaker_name in file_list:
#     wave_list = os.listdir(os.path.join(test_path, speaker_name))
#     for wavname in wave_list:
#         copyfile(os.path.join(test_path, speaker_name, wavname), os.path.join(save_path, wavname))
#

# with open(train_file, 'r', encoding='utf-8') as f:
#     lines = f.readlines()
#     with open('AISHELL-3/train.txt', 'w', encoding='utf-8') as f1:
#         for l in lines:
#             l = l.split('.')[0] + '|'
#             f1.write(l + '\n')
#
# with open(test_file, 'r', encoding='utf-8') as f:
#     lines = f.readlines()
#     with open('AISHELL-3/val.txt', 'w', encoding='utf-8') as f1:
#         for l in lines:
#             l = l.split('.')[0] + '|'
#             f1.write(l + '\n')
#

# file_list = os.listdir(save_path)
# for file in tqdm(file_list):
#     wav, _ = librosa.load(os.path.join(save_path, file), 22050)
#     wav = wav / max(abs(wav)) * 32767.0
#     wavfile.write(
#         os.path.join(save_path, file),
#         22050,
#         wav.astype(np.int16),
#     )
