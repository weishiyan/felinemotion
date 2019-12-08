# Felinemotion to understand your cat!
This is the felinemotion repo for CSE583 project


## Background
The domestic cat (Feliscatus) is one of the most attractive pets in the world, and it generates mysterious kinds of sound according to its mood and situation.In this software, we deal with the automatic classification of cat emotions using machine learning.

The pet animals are close friends of the human from the time of human evolution, and they deliver their messages by producing some identical sounds. Most pets spend their whole time in human peripheries, thus sound analysis of pet animals is important. Domestic cat is one of the most widely loved pet animals in the world, and the whole population is around 88.3 million, according to the report of Live Science (2013).Understanding cat's emotion can be helpful for human beings in terms of security, prediction of behaviors, and intimate interactions if we are able to recognize them properly.

Description of data

Introduction of using SVM to learn cat emotion

## Project Structure

----
```
Felinemotion (master)  

|---Data
    |---vid
        |---trainingSet
            \---raw
    |---img
        |---trainingSet
            \---raw
|---Examples  
    |---example.ipynb  
|---Felinemotion 
    \---traningData
    \---userData
        \---frames
        \---audio_test.csv
        \---data_test.csv
        \---image_test.csv
        \userInput.wav
    |---video_input.py
    |---cat_detect.py
    |---image_output.py
    |---main.py  
    |---audio_create_model.py
    \---audio_input.py
    \---audio_training.py
    |---image_batch_csv.py
    |---svm.py
    |---tests/
        |---__init__.py
        |---unittests.py
|---doc
    \---technical_review.pdf
    |---Felinemotion_final.pdf
    |---functional_specifications.ipynb
    |---component_specifications.ipynb
|---DATA_DESCRIPTION.md  
|---LICENSE.txt  
|---README.md   

```
----

## Installation