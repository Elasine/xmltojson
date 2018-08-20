# ! /usr/bin/python
# -*- coding:UTF-8 -*-
import os, sys
import glob
from PIL import Image
import codecs

# VEDAI 图像存储位置
vhr_img_dir = "JPEGImages"
# VEDAI 图像ground truth txt 文件存放位置
vhr_txt_dir = "ground-truth"
vhr_xml_dir = "annotations"

img_Lists = glob.glob(vhr_img_dir + '/*.jpg')

img_basenames = []  # e.g. 100.jpg
for item in img_Lists:
    img_basenames.append(os.path.basename(item))

img_names = []  # e.g. 100
for item in img_basenames:
    temp1, temp2 = os.path.splitext(item)
    img_names.append(temp1)

for img in img_names:
    im = Image.open((vhr_img_dir + '/' + img + '.jpg'))
    width, height = im.size



    # write in xml file
    # os.mknod(src_xml_dir + '/' + img + '.xml')
    with open((vhr_xml_dir + '/' + img + '.xml'), 'w') as xml_file:

        xml_file.write('<?xml version="1.0" encoding ="utf-8"?>\n')
        xml_file.write('<annotation>\n')
        xml_file.write('    <source>\n')
        xml_file.write('        <image>NWPU-VHR-10 image</image>\n')
        xml_file.write('        <annotation>NWPU 2016</annotation>\n')
        xml_file.write('        <flickrid>0</flickrid>\n')
        xml_file.write('        <database>{NWPU-VHR10}</database>\n')
        xml_file.write('        <author>{ Dr. Gong Cheng et al.}</author>\n')
        xml_file.write('    </source>\n')

        xml_file.write('    <folder>VOC2007</folder>\n')
        xml_file.write('    <filename>' + str(img) + '.jpg' + '</filename>\n')
        xml_file.write('    <segmented>0</segmented>\n')

       # xml_file.write('        <journal>{arxiv preprint:1804.07437}</journal>\n')
       # xml_file.write('        <year>2018</year>\n')

        xml_file.write('    <size>\n')
        xml_file.write('        <width>' + str(width) + '</width>\n')
        xml_file.write('        <height>' + str(height) + '</height>\n')
        xml_file.write('        <depth>3</depth>\n')
        xml_file.write('    </size>\n')

    # open the crospronding txt file
        with open(vhr_txt_dir + '/' + img + '.txt','r') as gt:
            # gt = open(src_txt_dir + '/gt_' + img + '.txt').read().splitlines()

            # write the region of image on xml file
            #uavinfo = gt.readlines()
            #for line in gt:

            lines = gt.readlines()
            for line in lines:
                if not line.strip():
                    continue
                line = (((line.replace('(', '')).replace(')', '')).replace('(', '')).replace(')', '')
                line = map(str, line)
                line = ''.join(line)
                spt = line.strip().split(',')  # 这里如果txt里面是以逗号‘，’隔开的，那么就改为spt = img_each_label.split(',')               if (spt[4] == str(0)):
                if spt[4] == str(0):
                    continue
                elif (spt[4] == str(1)):
                    spt[4] = "airplane"
                elif spt[4] == str(2):
                    spt[4] = "ship"
                elif spt[4] == str(3):
                    spt[4]= "storage tank"
                elif spt[4] == str(4):
                    spt[4] = "baseball diamond"
                elif spt[4] == str(5):
                    spt[4] = "tennis court"
                elif spt[4] == str(6):
                    spt[4]= "basketball court"
                elif spt[4] == str(7):
                    spt[4] = "ground track field"
                elif spt[4] == str(8):
                    spt[4] = "harbor"
                elif spt[4] == str(9):
                    spt[4]= "bridge"
                elif spt[4] == str(10):
                    spt[4] = "vehicle"



                xml_file.write('    <object>\n')
                xml_file.write('        <name>' + spt[4] + '</name>\n')
                xml_file.write('        <pose>unspecified</pose>\n')
                xml_file.write('        <truncated>0</truncated>\n')
                xml_file.write('        <difficult>0</difficult>\n')
                xml_file.write('        <bndbox>\n')
                xml_file.write('            <xmin>' + str(spt[0]) + '</xmin>\n')
                xml_file.write('            <ymin>' + str(spt[1]) + '</ymin>\n')
                xml_file.write('            <xmax>' + str(spt[2]) + '</xmax>\n')
                xml_file.write('            <ymax>' + str(spt[3]) + '</ymax>\n')
                xml_file.write('        </bndbox>\n')
                xml_file.write('    </object>\n')
        xml_file.write('</annotation>\n')
