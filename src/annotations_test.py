import os
import sys
import shutil

from annotate_images import *
from annotate_videos import *


def main():

    if len(sys.argv) != 4:
        print("ERROR: Incorrect number of arguments")
        print("Make sure your command follows the following format:")
        print("\npython3 src/annotations_test.py [flag] [test folder] [results folder]\n")
        print("Flags: '-i' for images, '-v' for videos")
        exit()

    # args: flag ('-i': still images, '-v': video), testset-folder, resset-folder
    flag = sys.argv[1]
    test_folder = sys.argv[2]
    res_folder = sys.argv[3]

    test_root = os.path.join(os.getcwd(), test_folder)

    # Create resset directory
    res_root = os.path.join(os.getcwd(), res_folder)

    # Remove directory if exists
    if os.path.exists(res_root):
        shutil.rmtree(res_root)

    os.mkdir(res_root)
    print("Directory '%s' created" % res_root)

    testset = os.listdir(test_root)
    testset.remove('.DS_Store')

    if flag == '-i':
        for imagename in testset:
            print('Annotating', imagename)
            image_path = os.path.join(test_root, imagename)
            img = annotate_still_image(image_path)

            cv.imwrite(os.path.join(res_root, imagename), img)

    elif flag == '-v':
        for videoname in testset:
            print('Annotating', videoname)
            video_path = os.path.join(test_root, videoname)
            video = annotate_video(video_path)

            cv.imwrite(os.path.join(res_root, videoname), video)

    else:
        print("ERROR: Invalid flag.\n")
        print("Flags: '-i' for images, '-v' for videos")
        exit()

    # annotate_still_image(image_path)
    # annotate_webcam()


if __name__ == '__main__':
    main()
