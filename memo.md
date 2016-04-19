##各スクリプトとそれがダウンロードしてくるファイル

- download_comment_data.sh
  - nico_comment_feature_v1.hdf5
  - nico_comment_feature_v1_vocabulary.txt
  - nico_illust_tag_v2.hdf5
  - seiga_comment.tsv
- download_img_data.sh
  - dataset_003 - 055.zip
- download_img_ids.sh
  - 160131_ids.txt
- download_metadata.sh
  - meta_003 - 055.json
- download_tag_list.sh
  - tags.json
  
## seiga_comment.tsvの中身

im1474580       お借りします…！
im993341        なぜか泣きそうになった
im1636622       やぽ＾＠＾
im1812711       別にサラダ油でもいいんですけど、僕はオリーブオイル
im2520541       即ハボ
im2304057       暇人なんだなw
im2320788       すごい まだr-18タグ残ってるw
im2304057       シュー
im2304057       コレハコワシガイガ...口凸口
im1720347       おいしそう！（違

## dataset_003.zipを解凍した中身（のファイル）

- 355141.jpg
- 355210.jpg
- 368401.jpg
- 387391.jpg
- 391490.jpg
- 398951.jpg
- 399410.jpg

## 160131_ids.txtの中身（画像IDリストってこと？）

355141
355210
368401
387391
391490
398951
399410
403150
415710
426361

## meta_003.jsonの中身

※category_tag_idというのは、結局タグIDの一部ということか？  
  
  {  
     "category_tag_id":4196,
     "clip_count":4,
     "comment_summary":"im4685795 im4685792 im4686977 im355141 かわええｗｗｗ かわいい うぽつ ｗｗ マキバオーｗみえたｗ 足跡ﾍﾟﾀｯ いい感じですね マキバオーか、さかさ なんて純粋な瞳なん",
     "created":"2010-03-05T12:05:17",
     "description":"(w)",
     "genre":200,
     "illust_type":0,
     "image_id":355141,
     "tag_ids":[  
        4196,
        1348443
     ],
     "title":"初描き",
     "user_id":11096035,
     "view_count":617
  }{  
     "category_tag_id":50,
     "clip_count":11,
     "comment_summary":"本当に最古なんて！ 最古と聞いて エスカルゴン『私は、 最古のゲームタグの付 かわいい ドット描けるのはいい かっけええ うぽつ 良いメタナイトだ＾＾ わぁい！ ｗｗ 小",
     "created":"2010-03-05T13:50:11",
     "description":"どう森で使用できるドット絵パターン。\r\nカービィ系が描きやすくお気に入りですｗ\r\n\r\n色変えも楽ですもんね\r\nちなみにこれはDSではパレット１６（wiiならパレット１）",
     "genre":200,
     "illust_type":0,
     "image_id":355210,
     "tag_ids":[  
        6,
        50,
        356,
        444,
        19920,
        831915,
        1009259,
        1282089
     ],
     "title":"ドット絵というのもいいと思わない？",
     "user_id":7257504,
     "view_count":2222
  }...
  
## tag,jsonの中身

{"created": "2009-11-14T15:06:19", "name": "ニコニコ大百科", "normalized_name": "ニコニコ大百科", "normalized_tag_id": 1, "tag_id": 1}  
{"created": "2009-11-14T15:06:19", "name": "ニワンゴ", "normalized_name": "ニワ ンゴ", "normalized_tag_id": 2, "tag_id": 2}  
{"created": "2009-11-14T15:06:19", "name": "【運営】", "normalized_name": "【運 営】", "normalized_tag_id": 3, "tag_id": 3}  
{"created": "2009-11-14T15:08:07", "name": "ひろゆき", "normalized_name": "ヒロ ユキ", "normalized_tag_id": 4, "tag_id": 4}  
{"created": "2009-11-14T15:08:07", "name": "たらこ", "normalized_name": "タラコ", "normalized_tag_id": 5, "tag_id": 5}  
{"created": "2009-11-14T15:08:07", "name": "描いてみた", "normalized_name": "描 イテミタ", "normalized_tag_id": 6, "tag_id": 6}  
{"created": "2009-11-14T15:10:53", "name": "写真", "normalized_name": "写真", "normalized_tag_id": 7, "tag_id": 7}  
{"created": "2009-11-14T15:10:53", "name": "テストにご利用ください", "normalized_name": "テストニゴ利用クダサイ", "normalized_tag_id": 8, "tag_id": 8}  
{"created": "2009-11-14T15:17:33", "name": "ニコニコ動画", "normalized_name": " ニコニコ動画", "normalized_tag_id": 9, "tag_id": 9}  
{"created": "2009-11-14T15:17:33", "name": "ロゴ", "normalized_name": "ロゴ", "normalized_tag_id": 10, "tag_id": 10} 
 
 