# Galaxy Image Classification Model

This project aims to develop an accurate galaxy image classification model by leveraging a combination of deep learning and decision tree techniques. The model is designed to classify images of galaxies based on their visual features. The performance of the model is evaluated on a test dataset, and custom tuning options are provided to allow for furthur optimisation. 

## Dataset

- The galaxy image dataset is located in the "galaxy_images" directory. 
- A new dataset can be curated using 'dataset_generator.py' file.

## CNN Model

- The CNN model used in this project is based on the ResNet50 architecture which is trained on the ImageNet dataset.
- The pre-trained ResNet50 model is loaded with all its layers set as non-trainable. 
- Additional layers, including a flatten layer, a dense layer, a dropout layer, and a final dense layer with softmax activation, are added to the model. 
- The model is then compiled with the Adam optimizer and categorical cross-entropy loss function. 
- The training history is recorded and the average accuracy is calculated.

## Decision Tree Model

- A decision tree classifier is trained on the flattened training dataset. 
- This model is evaluated on the test set using metrics such as accuracy, precision, recall, and F1 score.
- A confusion matrix is then plotted to visualise the model's performance.

## Combined Model

- The decision tree and the neural network are combined to make predictions on the test set. 
- The predictions from both models are compared, and if they differ, a random choice is made between the two predictions. 
- The combined predictions are evaluated, and the accuracies of the CNN model, decision tree model, and combined model are plotted.

## Custom Tuning (GUI)

- The program provides a GUI interface for customising the CNN model by adjusting parameters such as the number of epochs and learning rate. 
- The model is then retrained using the updated hyperparameters, and accuracy curves are plotted to visualise the performance. 
- The accuracy of the tuned model is compared to that of the default CNN model.

## How to Use

1. Clone the repository 
2. If on MacOS, open a terminal on the repository and type in 'jupyter notebook'. Then navigate to 'galaxy_classification_model.ipynb'.
3. If on Windows, use the windows search facility to search for Anaconda and type in 'jupyter notebook'. Then navigate to 'galaxy_classification_model.ipynb'.
2. Run the python notebook step-by-step.
