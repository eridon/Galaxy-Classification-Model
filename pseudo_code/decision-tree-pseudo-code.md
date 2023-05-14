# Convert the training dataset to numpy arrays

X = []
y = []
for each image-label pair in the training dataset:
Convert the image to a numpy array and append it to X
Convert the label to a numpy array and append it to y

# Reshape the input data

Reshape X to have a 2D shape, where each row represents an image

# Split the data into training and testing sets

Split X and y into training and testing sets, with 80% for training and 20% for testing

# Create a decision tree classifier

Create an instance of the DecisionTreeClassifier

# Train the classifier

Train the decision tree classifier using the training data (X_train, y_train)

# Make predictions on the test set

Use the trained classifier to predict the labels for the test data (X_test), and store the predicted labels in y_pred

# Convert y_test and y_pred to their original label format

Convert the one-hot encoded labels (y_test) and predicted labels (y_pred) back to their original label format
