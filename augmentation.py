import albumentations as A
import cv2
import os
from pascal_voc_writer import Writer
from xml.dom import minidom
import random
import copy

############ Buslaev, A., Iglovikov, V. I., Khvedchenya, E., Parinov, A., Druzhinin, M., & Kalinin, A. A. (2020). Albumentations: Fast and Flexible Image Augmentations. Information, 11(2), 125. MDPI AG. Retrieved from http://dx.doi.org/10.3390/info11020125#######

imagespath = 'C:/Users/emportent/Desktop/handgest/images/'
random.seed(7)


def readImage(filename):
    # OpenCV uses BGR channels
    img = cv2.imread(imagespath+filename)
    return img


def getCoordinates(filename):
    allbb = []
    xmldoc = minidom.parse(imagespath+filename)
    itemlist = xmldoc.getElementsByTagName('object')

    size = xmldoc.getElementsByTagName('size')[0]
    width = int((size.getElementsByTagName('width')[0]).firstChild.data)
    height = int((size.getElementsByTagName('height')[0]).firstChild.data)

    for item in itemlist:
        classid = (item.getElementsByTagName('name')[0]).firstChild.data
        xmin = ((item.getElementsByTagName('bndbox')[
            0]).getElementsByTagName('xmin')[0]).firstChild.data
        ymin = ((item.getElementsByTagName('bndbox')[
            0]).getElementsByTagName('ymin')[0]).firstChild.data
        xmax = ((item.getElementsByTagName('bndbox')[
            0]).getElementsByTagName('xmax')[0]).firstChild.data
        ymax = ((item.getElementsByTagName('bndbox')[
            0]).getElementsByTagName('ymax')[0]).firstChild.data

        xmin = int(xmin)
        ymin = int(ymin)
        xmax = int(xmax)
        ymax = int(ymax)

        b = [xmin, ymin, xmax, ymax, classid]
        allbb.append(b)
    return allbb


def start():
    count = 3000
    for filename in os.listdir(imagespath):

        if filename.endswith(".jpg") or filename.endswith(".JPG"):
            title, ext = os.path.splitext(os.path.basename(filename))
            image = readImage(filename)
        if filename.endswith(".txt"):
            xmlTitle, txtExt = os.path.splitext(os.path.basename(filename))
            if xmlTitle == title:
                # bboxes = getCoordinates(filename)
                bboxes = readYolo(imagespath+xmlTitle+'.txt')
                for i in range(0, 9):
                    img = copy.deepcopy(image)
                    transform = getTransform(i)
                    try:
                        transformed = transform(image=img, bboxes=bboxes)
                        transformed_image = transformed['image']
                        transformed_bboxes = transformed['bboxes']
                        name = title+str(count)+'.jpg'
                        cv2.imwrite(name, transformed_image)
                        # print(transformed_bboxes)
                        # writeVoc(transformed_bboxes, count, transformed_image)
                        writeYolo(transformed_bboxes, count, title)
                        count = count+1
                    except:
                        print("bounding box issues")
                        pass

                # bboxes = [[int(float(j)) for j in i] for i in bb]


def writeVoc(bboxes, count, image):
    height, width, channels = image.shape
    imagepath = r'C:/Users/enes-/Desktop/handgest/images/'+str(count)+'.jpg'
    xmlpath = (r'C:\Users\enes-\Desktop\handgest\images')+str(count)+'.xml'
    writer = Writer(imagepath, width, height)

    for i in bboxes:
        writer.addObject(i[4], int(i[0]), int(i[1]), int(i[2]), int(i[3]))
    writer.save(xmlpath)


def readYolo(filename):
    coords = []
    with open(filename, 'r') as fname:
        for file1 in fname:
            x = file1.strip().split(' ')
            x.append(x[0])
            x.pop(0)
            x[0] = float(x[0])
            x[1] = float(x[1])
            x[2] = float(x[2])
            x[3] = float(x[3])
            coords.append(x)
    return coords


def writeYolo(coords, count, name):

    with open(name+str(count)+'.txt', "w") as f:
        for x in coords:
            f.write("%s %s %s %s %s \n" % (x[-1], x[0], x[1], x[2], x[3]))


def getTransform(loop):
    if loop == 0:
        transform = A.Compose([
            A.HorizontalFlip(p=1),
        ], bbox_params=A.BboxParams(format='yolo'))
    elif loop == 1:
        transform = A.Compose([
            A.RandomBrightnessContrast(p=1),
        ], bbox_params=A.BboxParams(format='yolo'))
    elif loop == 2:
        transform = A.Compose([
            A.MultiplicativeNoise(multiplier=0.5, p=0),
        ], bbox_params=A.BboxParams(format='yolo'))
    elif loop == 3:
        transform = A.Compose([
            A.VerticalFlip(p=1)
        ], bbox_params=A.BboxParams(format='yolo'))
    elif loop == 4:
        transform = A.Compose([
            A.Blur(blur_limit=(50, 50), p=0)
        ], bbox_params=A.BboxParams(format='pascal_voc'))
    elif loop == 5:
        transform = A.Compose([
            A.Transpose(1)
        ], bbox_params=A.BboxParams(format='yolo'))
    elif loop == 6:
        transform = A.Compose([
            A.RandomRotate90(p=1)
        ], bbox_params=A.BboxParams(format='yolo'))
    elif loop == 7:
        transform = A.Compose([
            A.JpegCompression(quality_lower=0, quality_upper=1, p=0.2)
        ], bbox_params=A.BboxParams(format='yolo'))
    elif loop == 8:
        transform = A.Compose([
            A.Cutout(num_holes=50, max_h_size=40,
                     max_w_size=40, fill_value=128, p=0)
        ], bbox_params=A.BboxParams(format='pascal_voc'))

    return transform

start()