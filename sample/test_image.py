#!/usr/bin/env python
# -*- coding: utf-8 -*-

import six
import os
import sklearn.neighbors
import itertools
import numpy
import urllib2

import chainer.serializers

import illust2comment
import illust2comment.model
import illust2comment.utility

GPU = 0
IMAGE_MODEL_PATH = "data/nico_illust_tag_v2.hdf5"
COMMENT_DATA = "data/seiga_comment_random.tsv"

IMAGES_DIRECTORY = "image-data/"

TARGET_IMAGES_NUM = 1000

# QUERY_IMAGE_URL = "http://3d.nicovideo.jp/alicia/img/profile_character.png"
QUERY_IMAGE_URL = "data/test.png"

image_model = illust2comment.model.ImageModel(406)
chainer.serializers.load_hdf5(IMAGE_MODEL_PATH, image_model.functions)
if GPU >= 0:
    chainer.cuda.check_cuda_available()
    chainer.cuda.get_device(GPU).use()
    xp = chainer.cuda.cupy
    image_model.functions.to_gpu()
else:
    xp = numpy

class ImageFeatureExtractor(object):
    def __init__(self, image_model, xp):
        self.xp = xp
        self.image_model = image_model

    def get_image_feature_from_url(self, image_path):
        # return self.get_image_feature(urllib2.urlopen(image_url))
        return self.get_image_feature(image_path)

    def get_image_feature(self, image_path):
        img_array = self.xp.array(illust2comment.utility.img2array(illust2comment.utility.load_image(image_path)))
        return chainer.cuda.to_cpu(image_model.feature(img_array).data)[0]

features = []
image_pathes = []
image_feature_extractor = ImageFeatureExtractor(image_model, xp)
n = 0
import time
print(time.time())
for content_id, comment in illust2comment.utility.load_id_comments(COMMENT_DATA):
    image_path = os.path.join(IMAGES_DIRECTORY, "{}.jpg".format(content_id[2:]))
    if not os.path.exists(image_path):
        continue
    if image_path in image_pathes:
        continue

    n += 1
    feature = image_feature_extractor.get_image_feature(image_path)
    features.append(feature)
    image_pathes.append(image_path)
    if n % 100 == 0:
        print(n)
    if n > TARGET_IMAGES_NUM:
        break
print(time.time())

engine = sklearn.neighbors.NearestNeighbors(n_neighbors=10, algorithm='auto', metric='euclidean')
engine.fit(features)

image_url = QUERY_IMAGE_URL
# IPython.display.display(IPython.display.Image(url=image_url))
feature = image_feature_extractor.get_image_feature_from_url(image_url)
distances_batch, target_indices_batch = engine.kneighbors([feature])
for distance, target_index in itertools.izip(distances_batch[0], target_indices_batch[0]):
    print("filename:%s" % image_pathes[target_index])

