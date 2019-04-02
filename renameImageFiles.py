import os
import logging

dir_path = '/home/cropsModel/OriginalImage/trainData/'  # paste the absolute path of your folder/Directory.
extension = '.jpg'
new_prefix = 'img'


def main():
    counter = 1

    for filename in os.listdir(dir_path):
        if filename.endswith(extension):
            src = filename
            # set as img1.jpg format
            dest = new_prefix + str(counter) + extension

            # logger; filemode= 'append'
            logging.basicConfig(filename='testModel_image.log', filemode='a',
                                format='%(asctime)s - %(levelname)s - %(message)s',
                                level=logging.INFO)
            logging.info(src + ' renamed as ---> ' + dest)

            src = dir_path + src
            dest = dir_path + dest
            os.rename(src, dest)

            counter += 1
    logging.info('end\n')


if __name__ == '__main__':
    main()
