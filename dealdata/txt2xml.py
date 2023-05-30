'''
功能：实现YOLO格式的标注txt文件转化为voc格式
Faster R-CNN格式
'''

import os
from xml.dom.minidom import Document


def write_xml(Jfilename, imageWidth, imageHeight, Jpath, obj):
    doc = Document()
    annotation = doc.createElement("annotation")
    doc.appendChild(annotation)

    folder = doc.createElement("folder")
    foldertext = doc.createTextNode("JPEGImages")
    folder.appendChild(foldertext)
    annotation.appendChild(folder)

    filename = doc.createElement("filename")
    filenametext = doc.createTextNode(Jfilename)
    filename.appendChild(filenametext)
    annotation.appendChild(filename)

    path = doc.createElement("path")
    pathtext = doc.createTextNode(Jpath)
    path.appendChild(pathtext)
    annotation.appendChild(path)

    sourcename = "source"
    sourceE = doc.createElement(sourcename)

    database = doc.createElement("database")
    databasetext = doc.createTextNode("Unknown")
    database.appendChild(databasetext)
    sourceE.appendChild(database)
    annotation.appendChild(sourceE)

    sizename = "size"
    sizeE = doc.createElement(sizename)

    width = doc.createElement("width")
    widthtext = doc.createTextNode(str(imageWidth))
    width.appendChild(widthtext)
    sizeE.appendChild(width)

    height = doc.createElement("height")
    heighttext = doc.createTextNode(str(imageHeight))
    height.appendChild(heighttext)
    sizeE.appendChild(height)

    depth = doc.createElement("depth")
    depthtext = doc.createTextNode("1")
    depth.appendChild(depthtext)
    sizeE.appendChild(depth)

    annotation.appendChild(sizeE)

    segmented = doc.createElement("segmented")
    segmentedtext = doc.createTextNode("0")
    segmented.appendChild(segmentedtext)
    annotation.appendChild(segmented)
    for i in range(len(obj)):
        obj_list = obj[i].split(" ")

        Jname = obj_list[0]
        x = float(obj_list[1]) * 256
        y = float(obj_list[2]) * 256
        w = float(obj_list[3]) * 256
        h = float(obj_list[4]) * 256
        Jxmin = str(x - w / 2)
        Jxmax = str(x + w / 2)
        Jymin = str(y - h / 2)
        Jymax = str(y + h / 2)

        objectname = "object"
        objectE = doc.createElement(objectname)

        name = doc.createElement("name")
        nametext = doc.createTextNode(Jname)
        name.appendChild(nametext)
        objectE.appendChild(name)

        pose = doc.createElement("pose")
        posetext = doc.createTextNode("Unspecifiel")
        pose.appendChild(posetext)
        objectE.appendChild(pose)

        truncated = doc.createElement("truncated")
        truncatedtext = doc.createTextNode("0")
        truncated.appendChild(truncatedtext)
        objectE.appendChild(truncated)

        difficult = doc.createElement("difficult")
        difficulttext = doc.createTextNode("0")
        difficult.appendChild(difficulttext)
        objectE.appendChild(difficult)

        bndboxname = "bndbox"
        bndboxE = doc.createElement(bndboxname)

        xmin = doc.createElement("xmin")
        xmintext = doc.createTextNode(Jxmin)
        xmin.appendChild(xmintext)
        bndboxE.appendChild(xmin)

        ymin = doc.createElement("ymin")
        ymintext = doc.createTextNode(Jymin)
        ymin.appendChild(ymintext)
        bndboxE.appendChild(ymin)

        xmax = doc.createElement("xmax")
        xmaxtext = doc.createTextNode(Jxmax)
        xmax.appendChild(xmaxtext)
        bndboxE.appendChild(xmax)

        ymax = doc.createElement("ymax")
        ymaxtext = doc.createTextNode(Jymax)
        ymax.appendChild(ymaxtext)
        bndboxE.appendChild(ymax)
        objectE.appendChild(bndboxE)

        annotation.appendChild(objectE)

    f = open(os.path.join(xml_path, xml_name), "w")
    doc.writexml(f, indent='\t', newl='\n', addindent='\t', encoding=None)
    f.close()


if __name__ == "__main__":
    txt_path = r"./test_anno/"    # 存放txt地址
    xml_path = r"./annotation"    # xml保存地址
    img_path = r"./test_img/"     # 图像存放地址

    txt_files = os.listdir(txt_path)
    image_files = os.listdir(img_path)
    obj_num = 0
    for file in txt_files:
        txt_list = file.split(".")

        with open(os.path.join(txt_path, file), 'r') as load_f:
            lines = load_f.read().split("\n")
            print(lines)
            obj = lines[:len(lines) - 1]
            Jpath = os.path.join(img_path, txt_list[0] + '.jpg')
            xml_name = txt_list[0] + '.xml'
            Jfilename = txt_list[0]
            imageWidth = '256'
            imageHeight = '256'
            write_xml(Jfilename, imageWidth, imageHeight, Jpath, obj)

