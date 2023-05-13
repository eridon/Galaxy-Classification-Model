# Galaxy Image Classification Model

This project aims to develop an accurate galaxy image classification model by leveraging a combination of convolutional neural networks (CNNs) and decision tree techniques. The model is designed to classify galaxies into three main categories; spiral, elliptical, and irregular. The performance of the model is then evaluated on a test dataset, and custom tuning options are provided to allow for further optimisation.

## Dataset

The galaxy image dataset is located in the "galaxy_images" directory. Additionally, a new dataset can be curated using the 'dataset_generator.py' file included in the repository.

## CNN Model

The CNN model used in this project is based on the ResNet50 architecture, which has been pre-trained on the ImageNet dataset. The pre-trained ResNet50 model is loaded with all its layers set as non-trainable. To adapt the model for galaxy image classification, additional layers, including a flatten layer, a dense layer, a dropout layer, and a final dense layer with softmax activation, were added. The model is then compiled with the Adam optimizer and categorical cross-entropy loss function.

## Decision Tree Model

In addition to the CNN model, a decision tree classifier is trained on the flattened dataset. The decision tree model is evaluated on the test set using metrics such as accuracy, precision, recall, and F1 score. A confusion matrix is also plotted to provide visual performance insights.

## Combined Model

The decision tree model and the neural network are combined to make predictions on the test set. If the predictions from both models differ, a random choice is made between them. This approach aims to improve the overall classification accuracy and robustness of the model. The combined predictions are evaluated, and the accuracies of the CNN model, decision tree model, and combined model are plotted for comparison.

## Custom Tuning (GUI)

This program provides a graphical user interface (GUI) to adjust parameters such as the number of epochs. This allows users to fine-tune the model according to their specific requirements. After modifying the hyperparameters, the model is retrained using the updated settings, and accuracy curves are plotted to visualise the performance. The accuracy of the tuned model is compared to that of the default CNN model.

## How to Use

1. Clone the repository to your local machine.
2. If using MacOS, open a terminal at the repository location and type 'jupyter notebook' and navigate to 'galaxy_classification_model.ipynb'.
3. If using Windows, use the Windows search feature to find Anaconda. Open the Anaconda Prompt and enter 'jupyter notebook'. Then navigate to 'galaxy_classification_model.ipynb'.
4. Run the Python notebook step-by-step to execute the code.

## Sources

- [Tutorial Basics](https://datagen.tech/guides/computer-vision/resnet-50/)
- [ResNet50](https://keras.io/api/applications/resnet/#resnet50-function)
