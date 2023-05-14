import os
import sys
import shutil
import json

from annotate_images import *
from annotate_video import *


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

    res_root = os.path.join(os.getcwd(), res_folder)

    # Remove directory if exists
    if os.path.exists(res_root):
        shutil.rmtree(res_root)

    os.mkdir(res_root)
    print("Directory '%s' created" % res_root)

    testset = os.listdir(test_root)

    if '.DS_Store' in testset:
        testset.remove('.DS_Store')

    # Command
    # python3 src/annotations_test.py -i test/image_test_set test/image_res_set
    if flag == '-i':
        image_json_root = os.path.join(os.getcwd(), '../test/image_res_json')

        if os.path.exists(image_json_root):
            shutil.rmtree(image_json_root)

        os.mkdir(image_json_root)

        for imagename in testset:
            print('Annotating', imagename)
            image_path = os.path.join(test_root, imagename)
            img, res = get_image_info(image_path)

            annotate_img = annotate_still_image(img)
            cv.imwrite(os.path.join(res_root, imagename), annotate_img)

    # python3 annotations_test.py -v ../test/video_test_set ../test/video_res_set
    elif flag == '-v':
        video_json_root = os.path.join(os.getcwd(), '../test/video_res_json')

        if os.path.exists(video_json_root):
            shutil.rmtree(video_json_root)

        os.mkdir(video_json_root)

        for videoname in testset:
            print('Annotating', videoname)
            video_path = os.path.join(test_root, videoname)
            _ = annotate_video(video_path, outdir=os.path.join(res_root, videoname))

    else:
        print("ERROR: Invalid flag.\n")
        print("Flags: '-i' for images, '-v' for videos")
        exit()


if __name__ == '__main__':
    main()
