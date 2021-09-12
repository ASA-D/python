import moviepy.editor as mp
from six import b

a = input("使用する動画ファイルの名前を書いてください")
b = input("使用する音楽ファイルの名前を書いてください。")

clip = mp.VideoFileClip(a).subclip()
clip.write_videofile('synthesis.mp4', audio= b)