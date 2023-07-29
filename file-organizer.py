import os
import shutil


path = input("path: ")
backup = input("enter the path for the backup (if you dont want to backup just press enter): ")

audio = (".3ga", ".aac", ".ac3", ".aif", ".aiff",
         ".alac", ".amr", ".ape", ".au", ".dss",
         ".flac", ".flv", ".m4a", ".m4b", ".m4p",
         ".mp3", ".mpga", ".ogg", ".oga", ".mogg",
         ".opus", ".qcp", ".tta", ".voc", ".wav",
         ".wma", ".wv")

video = (".webm", ".MTS", ".M2TS", ".TS", ".mov",
         ".mp4", ".m4p", ".m4v", ".mxf")

img = (".jpg", ".jpeg", ".jfif", ".pjpeg", ".pjp", ".png",
       ".gif", ".webp", ".svg", ".apng", ".avif")

program = (".exe", ".msi")

zip = (".zip", ".7z", ".tar", ".rar", ".iso", ".gzip")

def is_audio(file):
    return os.path.splitext(file)[1] in audio

def is_video(file):
    return os.path.splitext(file)[1] in video

def is_image(file):
    return os.path.splitext(file)[1] in img

def is_program(file):
    return os.path.splitext(file)[1] in program

def is_zip(file):
    return os.path.splitext(file)[1] in zip

def is_screenshot(file):
    name, ext = os.path.splitext(file)
    return (ext in img) and "screenshot" in name.lower()

os.chdir(path)


if not backup == "":
    shutil.copytree(path + "/", backup + '/backup')
    print('backing up files to ' + backup)
else:
    print('not backing up')


if not os.path.exists("audio"):
    os.mkdir("audio")
if not os.path.exists("video"):
    os.mkdir("video")
if not os.path.exists("screenshots"):
    os.mkdir("screenshots")
if not os.path.exists("images"):
    os.mkdir("images")
if not os.path.exists("programs"):
    os.mkdir("programs")
if not os.path.exists("zips"):
    os.mkdir("zips")



for file in os.listdir():
    if is_audio(file):
        shutil.move(file, path + "/audio")
    elif is_video(file):
        shutil.move(file, path + "/video")
    elif is_program(file):
        shutil.move(file, path + "/programs")
    elif is_zip(file):
        shutil.move(file, path + "/zips")
    elif is_image(file):
        if is_screenshot(file):
            shutil.move(file, path + "/screenshots")
        else:
            shutil.move(file, path + "/images")
