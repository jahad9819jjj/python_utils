import sys
import cv2
import os


def target_file(inp):
    path = inp[1]
    seg = inp[1].split("/")
    output_file = seg[5] + "_" + seg[6] + "_" + seg[7] + ".avi"
    files = os.listdir(path)
    files = [file for file in files if 'png' in file]

    tmp = cv2.imread(path + '/0.png')
    print(tmp.shape)

    return [path, files, tmp, output_file]


def generate_video(path, files, img_info, output):
    codecs = 'H264'
    encoder = cv2.VideoWriter_fourcc(*codecs)
    video = cv2.VideoWriter(output, encoder, 20.0, (img_info.shape[1], img_info.shape[0]))

    if not video.isOpened():
        print("cannot be opened")
        sys.exit()

    for i in range(0, len(files)):
        new_path = path + '/%d.png' % i
        print(new_path)
        img = cv2.imread(new_path)
        # img = cv2.resize(img, (640, 480))
        if img is None:
            print("cannot read images")
            break
        video.write(img)

    video.release()
    print("written")


if __name__ == '__main__':
    info = target_file(sys.argv)
    generate_video(info[0], info[1], info[2], info[3])
