SPDX-FileCopyrightText: Copyright Amazon.com Inc. or its affiliates.

SPDX-License-Identifier: MIT

# Custom Labels Dog Classifier

## In todays lab we will be created an Amazon Rekognition Custom Labels model to identify different dog breeds!
### Prerequisites
You'll need access to a Terminal (Mac/Linux etc) with git and python3 installed.

To prepare the dataset:
* First, clone this github repository (if you haven't already)!!!NEED TO CHANGE ONCE FINAL REPO IS PUBLISHED!!!
    git clone https://github.com/aws-samples/custom_labels_lab
    
* Next you'll want to download the dataset from Stanford University (If you are on a PC or have issues with curl, you can also paste the link into a browser to download)
    curl http://vision.stanford.edu/aditya86/ImageNetDogs/images.tar --output images.tar

* Then we want to unpack our .tar file
    tar -xvf images.tar
    
* The original dataset contains 120 classes and 20,000+ images. This is possible to train with custom labels, but it will take many hours. In order to reduce the training time we will trim the classes to 20 and give them easier to read names. To trim the dataset run the following command:
    python3 trimDataset.py
    
### Now let's get started training our model

1) Open to the Rekognition service page in the AWS Console
2) Then Navigate to the Custom Labels page by clicking the link on the left hand side. (If you don't see any left hand links, press the "hamburger" icon in the top left of the page)


![](screenshots/1.png)

3) When you first navigate to the custom labels page, it will prompt you to create an S3 bucket. Go ahead and select "Create S3 bucket"

![](screenshots/2.png)

4) You'll want to select "Getting Started." Or, if you don't see the "Getting Started" option, Select "Projects" from the left hand menu, and then select "Create Project"

![](screenshots/3.png)

5) Name your project a valid name, the select "Create Project"

![](screenshots/4.png)

6) Once your project has been created, you'll need to create a dataset. 

![](screenshots/5.png)

There are several different ways to create datasets, including uploading and labeling directly in the console.
However, in this case we will upload our images to S3. You'll want to select the option for "Import images from S3 bucket" and then hit the link for "S3 bucket" at the bottom of the page.
This will take you to the S3 folder where you can upload your images.

**If your machine only has command line access (no UI) then click this follow [these instructions](https://docs.aws.amazon.com/cli/latest/userguide/cli-services-s3-commands.html#using-s3-commands-managing-objects-copy) to see how to upload your images from the AWS Command Line Interface (CLI). Your command should look something like "aws s3 cp Images/ s3://custom-labels-console-us-east-1-dae32e64e4/assets/stanford-dogs/"**

![](screenshots/6.png)

7) You'll want to create a folder to store you dataset in. Click the link to create folder.

![](screenshots/7.png)

8) Name your folder whatever you would like. In this case we name it dogClassifier.

![](screenshots/8.png)

9) You can select the folders containing the images, and then drag and drop them into your S3 bucket. There's a lot of images, so it might take several minutes.

![](screenshots/9.png)

10) Once the upload has completed, you can click the button in the top right to copy the file path. Ensure you can see the class folders from this directory, as this is important for labelling later.

![](screenshots/10.png)

11) Then you'll want to click back to the other tab, titled "Create Dataset". Here we will paste the filepath from your clipboard. You'll also want to check the checkbox for "Automatically attach a label to my images based on the folder they're stored in."

![](screenshots/11.png)
![](screenshots/12.png)

12) Now your images are loaded into your dataset. You'll notice the labels were already created based on the folder structure of your data.
Now you'll want to train your model based on this data.

![](screenshots/13.png)

13) When on the train model screen, your model should already be pre-populated. You'll need to choose the dataset you just created, and then click the option for "Split Data Set."
This will automatically reserve 20% of your dataset to the side, and use it to evaulate the performance of you model.

14) Then you'll want to select "Train." The training process will take at least an hour.

![](screenshots/14.png)

14) Once your model has been trained, you can click the name to view more information.

![](screenshots/15.png)

15) From the model detail screen, you can see information about the overall performance of the model, as well as performance on each individual class of images.
You can click the botton for "View Test Result" to see more detaied info.

![](screenshots/16.png)

16) Here you can see each image from the test set, and whether or not it was correctly labeled.

![](screenshots/17.png)

17) You can also select specific outcomes. Here you can see the example of the false positives.

![](screenshots/18.png)

18) If you wish to start your model, you can go back to the model detail page and find the CLI commands. Be aware that starting your model will cause it to start occuring costs.

![](screenshots/19.png)
