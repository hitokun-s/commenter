#!/usr/bin/env python
# -*- coding: utf-8 -*-

import six
import os
import sklearn.neighbors
import itertools
import numpy

import chainer.serializers

import illust2comment
import illust2comment.model
import illust2comment.utility

GPU = 0
IMAGE_MODEL_PATH = "data/nico_illust_tag_v2.hdf5"
COMMENT_DATA = "data/seiga_comment_random.tsv"

COMMENT_MODEL_PATH = "data/nico_comment_feature_v1.hdf5"
VOCABULARY_PATH = "data/nico_comment_feature_v1_vocabulary.txt"

# QUERY_IMAGE_URL = "http://3d.nicovideo.jp/alicia/img/profile_character.png"
QUERY_IMAGE_URL = "data/test.png"

TARGET_COMMENTS_NUM = 1000
HIDDEN_UNIT = 1024

CHARACTER_START = "\n"
CHARACTER_END = ""

vocabulary = [line.rstrip().decode("utf-8") for line in open(VOCABULARY_PATH)]
character_embedder = illust2comment.model.WordEmbedder(vocabulary)
comment_model = illust2comment.model.FeatureWordModel(vocab_size=character_embedder.vecsize, midsize=HIDDEN_UNIT, output_feature_size=4096)
chainer.serializers.load_hdf5(COMMENT_MODEL_PATH, comment_model)
image_model = illust2comment.model.ImageModel(406)
chainer.serializers.load_hdf5(IMAGE_MODEL_PATH, image_model.functions)
if GPU >= 0:
    chainer.cuda.check_cuda_available()
    chainer.cuda.get_device(GPU).use()
    xp = chainer.cuda.cupy
    image_model.functions.to_gpu()
    comment_model.to_gpu()
else:
    xp = numpy

class ImageFeatureExtractor(object):
    def __init__(self, image_model, xp):
        self.xp = xp
        self.image_model = image_model

    def get_image_feature_from_url(self, image_url):
        return self.get_image_feature(six.moves.urllib.request.urlopen(image_url))

    def get_image_feature(self, image_path):
        # 学習時のバグにより二重に平均画像(128)を引いていることに注意してください。ごめんなさい。
        img_array = self.xp.array(illust2comment.utility.img2array(illust2comment.utility.load_image(image_path)) - 128)
        return chainer.cuda.to_cpu(image_model.feature(img_array).data)[0]

class CommentFeatureExtractor(object):
    def __init__(self, comment_model, character_embedder, xp):
        self.xp = xp
        self.comment_model = comment_model
        self.character_embedder = character_embedder

    def get_comment_feature(self, comment):
        comment_model.reset_state()
        character_list = ([CHARACTER_START] + list(comment) + [CHARACTER_END]*30)[:30]

        ### comment features
        predicted = None
        for character in character_list:
            char_id = self.character_embedder.embed_id(character)
            each_predicted = comment_model.feature(
                    chainer.Variable(self.xp.array([char_id], dtype=self.xp.int32), volatile=True),
            )
        predicted = each_predicted
        return chainer.cuda.to_cpu(predicted.data)[0]

comment_feature_extractor = CommentFeatureExtractor(comment_model, character_embedder, xp=xp)
image_feature_extractor = ImageFeatureExtractor(image_model, xp=xp)

features = []
comments = []
n = 0
import time
print(time.time())
for content_id, comment in illust2comment.utility.load_id_comments(COMMENT_DATA):
    if comment in comments:
        continue

    n += 1
    feature = comment_feature_extractor.get_comment_feature(comment)
    features.append(feature)
    comments.append(comment)
    if n % 100 == 0:
        print(n)
    if n > TARGET_COMMENTS_NUM:
        break
print(time.time())

engine = sklearn.neighbors.NearestNeighbors(n_neighbors=10, algorithm='auto', metric='euclidean')
engine.fit(features)

image_url = QUERY_IMAGE_URL
# IPython.display.display(IPython.display.Image(url=image_url))
feature = image_feature_extractor.get_image_feature_from_url(image_url)
distances_batch, target_indices_batch = engine.kneighbors([feature])
for distance, target_index in itertools.izip(distances_batch[0], target_indices_batch[0]):
    print(distance)
    print(comments[target_index])