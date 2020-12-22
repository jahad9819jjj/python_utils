import sys
import cv2
import os

if __name__ == '__main__':
    args = sys.argv
    # print(args[0], "******", args[1])
    path = args[1]
    seg = args[1].split("/")

    output_file = seg[5] + "_" + seg[6] + "_" + seg[7] + ".avi"
    files = os.listdir(path)
    files = [file for file in files if 'png' in file]
    print(files)
    print(len(files))

    codecs = 'H264'
    # encoder = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
    encoder = cv2.VideoWriter_fourcc(*codecs)
    video = cv2.VideoWriter(output_file, encoder, 20.0, (768, 966))

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
