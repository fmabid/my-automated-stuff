from xml.etree import ElementTree

import glob
import pandas

TRAINING_DATA_DIR = 'path to XML file'
test_file = TRAINING_DATA_DIR + '/img2.xml'


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


TRAIN_CSV_FILE = 'path to csv file' + 'train_labels.csv'


if __name__ == "__main__":
    train_csv_data = xml_to_csv(TRAINING_DATA_DIR)
    train_csv_data.to_csv(TRAIN_CSV_FILE, index=None)
