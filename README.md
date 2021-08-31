[![CodeFactor](https://www.codefactor.io/repository/github/emportent/handface/badge)](https://www.codefactor.io/repository/github/emportent/handface)

# HandFace
Deep learning model for detection hand-face interactions

Note: This is a pilot model for a future research project, so it's not finished yet. 
The model has been trained in google-collab with 1796 unique images. For now, the total number of classes is 3: Cheek, forehead, and chin. In the labeling process sometimes it was very overwhelming since the human hands were big enough to cover the whole face. So in this scenario, I made my decision based on the place where the hand exerts the most pressure on the face (this paradigm is also consistent with my research )

Update: The train set has been increased to 12.752 after the augmentation process. The model is still in training.



![117hand](https://user-images.githubusercontent.com/54986652/128066029-b4114fb4-9da5-4cf6-a87e-0170f8988a5b.png)
![avoRMoX_700b](https://user-images.githubusercontent.com/54986652/128066080-040a076c-5102-4371-ae28-064a5dc10066.png)
![131hand](https://user-images.githubusercontent.com/54986652/128067708-fa65dba8-c1e8-456d-b59b-1ab2031d3870.png)





```
=================================================================
Layer (type:depth-idx)                   Param #
=================================================================
├─Model: 1-1                             --
|    └─Sequential: 2-1                   --
|    |    └─Focus: 3-1                   (5,232)
|    |    └─Conv: 3-2                    (41,568)
|    |    └─C3: 3-3                      (64,896)
|    |    └─Conv: 3-4                    (166,080)
|    |    └─C3: 3-5                      (628,224)
|    |    └─Conv: 3-6                    (663,936)
|    |    └─C3: 3-7                      (2,509,824)
|    |    └─Conv: 3-8                    (2,654,976)
|    |    └─SPP: 3-9                     (1,475,712)
|    |    └─C3: 3-10                     (4,131,840)
|    |    └─Conv: 3-11                   (295,296)
|    |    └─Upsample: 3-12               --
|    |    └─Concat: 3-13                 --
|    |    └─C3: 3-14                     (1,181,184)
|    |    └─Conv: 3-15                   (73,920)
|    |    └─Upsample: 3-16               --
|    |    └─Concat: 3-17                 --
|    |    └─C3: 3-18                     (295,680)
|    |    └─Conv: 3-19                   (331,968)
|    |    └─Concat: 3-20                 --
|    |    └─C3: 3-21                     (1,033,728)
|    |    └─Conv: 3-22                   (1,327,488)
|    |    └─Concat: 3-23                 --
|    |    └─C3: 3-24                     (4,131,840)
|    |    └─Detect: 3-25                 (92,943)
=================================================================
Total params: 21,106,335
Trainable params: 0
Non-trainable params: 21,106,335
=================================================================
=================================================================
Layer (type:depth-idx)                   Param #
=================================================================
├─Model: 1-1                             --
|    └─Sequential: 2-1                   --
|    |    └─Focus: 3-1                   (5,232)
|    |    └─Conv: 3-2                    (41,568)
|    |    └─C3: 3-3                      (64,896)
|    |    └─Conv: 3-4                    (166,080)
|    |    └─C3: 3-5                      (628,224)
|    |    └─Conv: 3-6                    (663,936)
|    |    └─C3: 3-7                      (2,509,824)
|    |    └─Conv: 3-8                    (2,654,976)
|    |    └─SPP: 3-9                     (1,475,712)
|    |    └─C3: 3-10                     (4,131,840)
|    |    └─Conv: 3-11                   (295,296)
|    |    └─Upsample: 3-12               --
|    |    └─Concat: 3-13                 --
|    |    └─C3: 3-14                     (1,181,184)
|    |    └─Conv: 3-15                   (73,920)
|    |    └─Upsample: 3-16               --
|    |    └─Concat: 3-17                 --
|    |    └─C3: 3-18                     (295,680)
|    |    └─Conv: 3-19                   (331,968)
|    |    └─Concat: 3-20                 --
|    |    └─C3: 3-21                     (1,033,728)
|    |    └─Conv: 3-22                   (1,327,488)
|    |    └─Concat: 3-23                 --
|    |    └─C3: 3-24                     (4,131,840)
|    |    └─Detect: 3-25                 (92,943)
=================================================================
Total params: 21,106,335
Trainable params: 0
Non-trainable params: 21,106,335
=================================================================

```
