# Arithmetic-Evaluator
CNN based Model to Evaluate Handwritten Arithmetic Expressions
The model is trained to detect singular images of digits 0-9 and arithmetic symbols, and predict the labels. The run notebook takes in an expression,uses image processing and contouring to extract individual digits and operators and send them to the model for prediction. Upon identification, basic python operations are used to get the answer

## All Data
Folder containing Training and Testing data used for the model. The Training data is a mix of images available online as well as self-written and augmented images, while the Test data is entirely self-built, with the help of various people to incorporate the factor of different handwritings

## Final Testing
Folder to place images to test the final model. The model correctly predicts the answers to the given expressions

## Train Model
Jupyter Notebook containing the architecture and the code to train the CNN model. The hyperparameters can be tweaked to get better performance. With the Dataset included in the Repo, I got around 95% accuracy on the testing data

## Run Model
Jupyter Notebbok that uses OpenCV and Python to preprocess and contour the input images into individual components to feed to the model, all implemented by self. After getting the labels, the script evaluates and prints the answer

## Better Model
Pointer to self to further improve the model. Also need to remove the dependency of OpenCV and introduce a DNN to predict the bounding boxes of each individual character, since contouring is unreliable
