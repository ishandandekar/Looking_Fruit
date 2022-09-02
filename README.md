# Looking-Fruit

<p align="center">
    <img width=300 height=170 src="assets/meme.jpeg">
</p>

:wave: Hello and welcome to the **Looking-Fruit :apple:** code repository. This is a short and simple computer vision project. In this project, I replicate and try to improve the models used to classify images of fruits. You can see the research paper [here](https://www.researchgate.net/publication/321475443_Fruit_recognition_from_images_using_deep_learning). The original code repository can be found [here](https://github.com/Horea94/Fruit-Images-Dataset). This is my first independant paper replication project :smile:.

## Introduction

Computer Vision domain has always been my curiosity. I thought paper replication was a great start to then replicate state-of-the-art models like ResNets.
The **objective** of the research paper was to classify images various fruits and vegetables correctly. The researchers made a total of 10 models based and documented there results. The main of this project is to beat and/or achieve the highest score on the test set when compared to their best model.

**Abstract of the paper:**  
In this paper we introduce a new, high-quality, dataset of images
containing fruits. We also present the results of some numerical experiment for training a neural network to detect fruits. We discuss the
reason why we chose to use fruits in this project by proposing a few
applications that could use such classifier.

## Data

The original data for the paper was published and created by the researchers themselves. The dataset contains a total of around **90,000** images of **131** fruits and vegetables. The data is then split into two sets: training and testing sets. This test set contains almost 25% of the total dataset.  
The training data has around **400+ images for each class** (except Ginger Root). Although, the model would get generalised more on more data, but due to unnecessarily huge size of the dataset, it was trimmed for training the models better. Further, data augmentation was performed to make the model make better predictions on new images.
The test data was kept separately untouched, and was used just to evaluate the models on unknown data. Each class had around **100+** images. This data was not augmented.

For my ease-of-use I uploaded the original dataset available on Github to Kaggle, and used this for the project. Check out the dataset [here](https://www.kaggle.com/datasets/ishandandekar/fruitimagedataset) and do try making models yourself!

> :bulb: Check out the original dataset via : [Github](https://github.com/Horea94/Fruit-Images-Dataset) [Kaggle](https://www.kaggle.com/datasets/moltean/fruits)

## Models

1. **Model 0** : A simple model with fully connected multiple Dense layers; this model acts as a baseline.
1. **Model 1** : 2 pairs of CNN and MaxPool layers with a Flatten layer and Dense layer in the end for classification.
1. **Model 2** : Multiple CNN layers, MaxPool layers with a Flatten layer and Dense layer in the end; _should get better results from this._
1. **Model 3** : Using transfer learning, exploit ResNet model for classification.
1. **Model 4** : Using transfer learning, exploit EfficientNetBx for classification.
1. **Model 5** : Use fine-tuned ResNet model for classification.
1. **Model 6** : Use fine-tuned EfficientNetBx for classification.

## Contents of the repository

```
Looking_Fruit/
├─ assets/
├─ .gitignore
├─ Looking_Fruit_nbk.ipynb
├─ README.md
├─ helper_functions.py
```

- _assets_ : various media materials which were helpful for the project.
- _.gitignore_ : this file was used to make `git` not track certain private files.
- _Looking_Fruit_nbk_ : jupyter/colab notebook used for this project. The notebook also describes the models and approach.
- _README.md_ : documentation of the project.
- _helper_functions.py_ : python script containing various utility functions which were used during the modelling experiments.

## Contribution

I appreciate reviews and criticism. Although this is not a conventional open-source project, if you find any errors (even a typo!) and/or want to improve something in the repository, and/or want to help document the project, feel free to create a pull request! :smile:.

#### TODO:

- [ ] Make notebook
- [ ] Beautify notebook
- [ ] Add 'Open in colab' button
- [x] Add dataset to Kaggle
- [x] Beautify Kaggle dataset (desc etc.)
- [ ] Update README
