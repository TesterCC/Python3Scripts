from moviepy.editor import VideoFileClip

# pip install moviepy -i https://pypi.tuna.tsinghua.edu.cn/simple
# 这个示例使用`moviepy`库打开视频文件，并检查是否存在音轨。如果`audio_tracks`不为空，则表示视频包含音轨。

video_path = r"E:\download_video\bilibili\redteam\xxxx.mp4"
video = VideoFileClip(video_path)
audio_tracks = video.audio
if audio_tracks:
    print("视频包含音轨")
else:
    print("视频不包含音轨")
