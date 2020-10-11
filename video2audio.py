import os
import moviepy.editor as ed


# 读取指定文件夹下的文件
file_path = '/Users/hyman/Desktop/videos'
# file_path/music001.mp4
parent_path = os.path.dirname(file_path)
target_path = os.path.join(parent_path,'audios')
files = os.listdir(file_path)
# 创建目录
if not os.path.exists(target_path):
    os.makedirs(target_path)

# 转换
for file in files:
    # file_name = os.path.join(file_path,file)
    video = ed.VideoFileClip(os.path.join(file_path,file))
    audio = video.audio
    new_filename = '%s.mp3' % file[0:-4]
    audio.write_audiofile(os.path.join(target_path,new_filename))
