from xml.etree import ElementTree

import glob
import pandas

# paste here the pathe to the directory of XML files
XML_DATA_DIR = ''

# create the csv writer object
def xml_to_csv(path):
    xml_list = []

    for xml_file in glob.glob(path + '/*.xml'):
        tree = ElementTree.parse(xml_file)
        root = tree.getroot()

        for elemnt in root.findall('object'):
            value = (root.find('filename').text, int(root.find('size')[0].text), int(root.find('size')[1].text),
                     elemnt[0].text, elemnt[4][0].text, elemnt[4][1].text, elemnt[4][2].text, elemnt[4][3   ].text)
            xml_list.append(value)
        # end for
    # end for

    column_name = ['filename', 'width', 'height', 'class_name', 'xmin', 'ymin', 'xmax', 'ymax']
    xml_df = pandas.DataFrame(xml_list, columns=column_name)
    return xml_df
# end function


PATH_CSV_FILE = '/home/abid/PycharmProjects/cropsModel/TestModes/data/train/' + 'train_labels.csv'


if __name__ == "__main__":

    if XML_DATA_DIR == '':
        print("Define the path to directory at 'TRAINING_DATA_DIR'")
        exit()
    else:
        train_csv_data = xml_to_csv(XML_DATA_DIR)
        train_csv_data.to_csv(PATH_CSV_FILE, index=None)
