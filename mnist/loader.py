import os
import struct
from array import array

class MNIST(object):
    def __init__(self, path='.'):
        self.path = path

        self.test_img_fname = 't10k-images-idx3-ubyte'
        self.test_lbl_fname = 't10k-labels-idx1-ubyte'

        self.train_img_fname = 'train-images-idx3-ubyte'
        self.train_lbl_fname = 'train-labels-idx1-ubyte'

        self.test_images = []
        self.test_labels = []

        self.train_images = []
        self.train_labels = []

    def load_testing(self):
        ims, labels = self.load(os.path.join(self.path, self.test_img_fname),
                         os.path.join(self.path, self.test_lbl_fname))

        self.test_images = ims
        self.test_labels = labels

        return ims, labels

    def load_training(self):
        ims, labels = self.load(os.path.join(self.path, self.train_img_fname),
                         os.path.join(self.path, self.train_lbl_fname))

        self.train_images = ims
        self.train_labels = labels

        return ims, labels

    @classmethod
    def load(cls, path_img, path_lbl):
        with open(path_lbl, 'rb') as file:
            magic, size = struct.unpack(">II", file.read(8))
            if magic != 2049:
                raise ValueError('Magic number mismatch, expected 2049,'
                    'got %d' % magic)

            labels = array("B", file.read())

        with open(path_img, 'rb') as file:
            magic, size, rows, cols = struct.unpack(">IIII", file.read(16))
            if magic != 2051:
                raise ValueError('Magic number mismatch, expected 2051,'
                    'got %d' % magic)

            image_data = array("B", file.read())

        images = []

        for i in range(size):
            images.append([0]*rows*cols)

        for i in range(size):

        for i in xrange(size):
            images.append([0]*rows*cols)

        for i in xrange(size):

            images[i][:] = image_data[i*rows*cols : (i+1)*rows*cols]

        return images, labels

    def test(self):
        test_img, test_label = self.load_testing()
        train_img, train_label = self.load_training()
        assert len(test_img) == len(test_label)
        assert len(test_img) == 10000
        assert len(train_img) == len(train_label)
        assert len(train_img) == 60000
        print('Showing num:%d' % train_label[0])
        #print(self.display(train_img[0]))
        # print(train_img[0])
        # print(len(train_img[0]))
        return train_img,train_label,test_img,test_label


    @classmethod
    def display(cls, img, width=28):
        render = ''
        for i in range(len(img)):
            if i % width == 0: render += '\n'
            if img[i] > 200:
                render += '1'
            else:
                render += '0'
        return render

if __name__ == "__main__":

    print('Testing')
    mn = MNIST('/home/lavish/Documents/EE322M-Project-master/Datasets/')
    train_img,train_label,test_img,test_label = mn.test()
    print(train_label[0])
    nwfile = open('data.arff','w')
    nwfile.write('@relation D'+str(len(train_img[0]))+'\n')
    for i in range(len(train_img[0])):
        nwfile.write('@attribute dim'+str(i)+' real'+'\n')
    nwfile.write('@attribute class {')
    for i in range(10):
        if(i!=9):
            nwfile.write(str(i)+',')
        else:
            nwfile.write(str(i)+'}')
    x=train_img[0]
    
    # print(a)
    for i in range(len(train_img)):
        a=','.join(str(float(x)) for x in train_img[i])
        a=a+','+str(train_label[i])
        nwfile.write(a+'\n')
    # a=','.join(str(float(x)) for x in train_img[1])
    # a=a+','+str(train_label[i])
    # nwfile.write(a+'\n')
    #     nwfile

