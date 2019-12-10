# Felinemotion to understand your cat!
This is the felinemotion repo for CSE583 project


## Background
The domestic cat (Feliscatus) is one of the most attractive pets in the world, and it generates mysterious kinds of sound according to its mood and situation.In this software, we deal with the automatic classification of cat emotions using machine learning.

The pet animals are close friends of the human from the time of human evolution, and they deliver their messages by producing some identical sounds. Most pets spend their whole time in human peripheries, thus sound analysis of pet animals is important. Domestic cat is one of the most widely loved pet animals in the world, and the whole population is around 88.3 million, according to the report of Live Science (2013).Understanding cat's emotion can be helpful for human beings in terms of security, prediction of behaviors, and intimate interactions if we are able to recognize them properly.

### Description of data
Due to the time limitation, training data were manually downloaded from youtubes. The video will first be divided into audio dataset and image data sets. After that, CNN and Haar Casade Algorithm are used to extract the required data. Audio datasets and image dataset will then be converted into pixel arrays. Lastly, both datasets will be merged into one csv file.

### Introduction of using SVM to learn cat emotion
Support vector machines (SVMs) are a set of supervised learning methods used for classification, regression and outliers detection. The advantages of support vector machines are: 1) Effective in high dimensional spaces; 2) Still effective in cases where number of dimensions is greater than the number of samples; 3) Uses a subset of training points in the decision function (called support vectors), so it is also memory efficient; and 4) Versatile: different Kernel functions can be specified for the decision function. Common kernels are provided, but it is also possible to specify custom kernels.

Linear Support Vector Classification (LinearSVC) is able to perform multi-class classification on a dataset. Similar to SVC with parameter kernel=’linear’, but implemented in terms of liblinear rather than libsvm, so it has more flexibility in the choice of penalties and loss functions and should scale better to large numbers of samples.


## Project Structure

----
```
Felinemotion (master)  

|---Data
    |---vid
        |---trainingSet
            |---raw
    |---img
        |---trainingSet
            |---raw
|---Examples  
    |---example.ipynb  
|---Felinemotion 
    |---trainingData
    |---userData
        |---frames
        |---audio_test.csv
        |---data_test.csv
        |---image_test.csv
        |userInput.wav
    |---video_input.py
    |---image_analysis.py
    |---random_pick_3.py
    |---image_output.py
    |---main.py  
    |---audio_create_model.py
    |---audio_input.py
    |---audio_training.py
    |---image_batch_csv.py
    |---svm.py
    |---tests
        |---__init__.py
        |---unittests.py
|---doc
    |---technical_review.pdf
    |---Felinemotion_final.pdf
    |---functional_specifications.ipynb
    |---component_specifications.ipynb
|---DATA_DESCRIPTION.md  
|---LICENSE.txt  
|---README.md   

```
----

### Installation
1. Clone the repo
2. Install environment $ conda env create -f felinemotion.yml

### User Guide
1. Run main.py
2. Open Felinemotion.html and upload the video

![](https://github.com/wyan1992/felinemotion/blob/master/videoInput.PNG)

3. After uploading the video, open image.html in templates directory

![](https://github.com/wyan1992/felinemotion/blob/master/inputReceived.PNG)

4. Select and confirm the best image expressing the emotion

![](https://github.com/wyan1992/felinemotion/blob/master/imageSelect.png)

5. The software will outout an emotion best fit from the data

![](https://github.com/wyan1992/felinemotion/blob/master/result.png)
