from typing import Dict
import matplotlib.pyplot as plt

def plot_loss_curves(history) -> None:
    """
    Shows separate loss curves for training and validation metrics.

    Args:
    history: TensorFlow model History object (see: https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/History)
    """

    loss = history.history['loss']
    val_loss = history.history['val_loss']
    accuracy = history.history['categorical_accuracy']
    val_accuracy = history.history['val_categorical_accuracy']
    epochs = range(len(history.history['loss']))
    # Plot loss
    plt.plot(epochs, loss, label='training_loss')
    plt.plot(epochs, val_loss, label='val_loss')
    plt.title('Loss')
    plt.xlabel('Epochs')
    plt.legend()
    # Plot accuracy
    plt.figure()
    plt.plot(epochs, accuracy, label='training_accuracy')
    plt.plot(epochs, val_accuracy, label='val_accuracy')
    plt.title('Accuracy')
    plt.xlabel('Epochs')
    plt.legend();

import zipfile

def unzip_data(filename,data_dir="data") -> None:
    """
    Unzips filename into the current working directory.
    Args:
        filename (str): a filepath to a target zip folder to be unzipped.
    """
    zip_ref = zipfile.ZipFile(filename, "r")
    zip_ref.extractall(data_dir)
    zip_ref.close()

import os
import tensorflow as tf

# Create a function to implement a ModelCheckpoint callback with a specific filename
def create_model_checkpoint(model_name: str, save_path: str="model_experiments"):
    """Used for making model checkpoint callback

    Args:
        model_name (str): Name of the model, functions creates a directory for the model of this name
        save_path (str, optional): Main directory to store all weights. Defaults to "model_experiments".

    Returns:
        _type_: Keras Callback object
    """
    return tf.keras.callbacks.ModelCheckpoint(filepath=os.path.join(save_path, model_name), verbose=1, save_best_only=True, save_weights_only=True)

def create_early_stopping(patience: int = 3, restore_best_weights: bool = True):
    """Generates a EarlyStopping callback

    Args:
        patience (int, optional): Number of iterations to look for improvement. Defaults to 3.
        restore_best_weights (bool, optional): Restore best weights. Defaults to True.

    Returns:
        _type_: Keras Callbacks object
    """
    return tf.keras.callbacks.EarlyStopping(patience = patience, restore_best_weights = restore_best_weights)


def get_metrics(loss, accuracy, precision, recall) -> Dict:
    """
    Calculates model accuracy, precision, recall and f1 score of a binary classification model.

    Args:
        y_true: true labels in the form of a 1D array
        y_pred: predicted labels in the form of a 1D array
    Returns:
        a dictionary of accuracy, precision, recall, f1-score.
    """
    # Calculate model accuracy


    model_results = {
        "Loss": loss,
        "Accuracy": accuracy*100,
        "Precision": precision,
        "Recall": recall,
        "F1-score": (precision+recall)/(2*precision*recall)
    }
    return model_results