import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.keras import utils

from mypackage import notmnist


def get_samples(subset, size=None):
    """Формирует матрицу признаков X и метки y для модели TensorFlow."""
    X = []
    y = []

    for class_name, images in subset.items():
        if size is not None:
            images = images[:size // notmnist.NUMBER_OF_CLASSES]
        X = X + images
        y.extend([ord(class_name) - ord('A')] * len(images)) 
        
    X = tf.constant(X)  
    y = utils.to_categorical(tf.constant(y))
    return X, y


def plot_history(history):
    """Отображает результаты функции потерь и точности."""
    plt.plot(history.history['accuracy'], label='Обучающая подвыборка')
    plt.plot(history.history['val_accuracy'], label='Валидационная подвыборка')
    plt.title('Точность модели')
    plt.ylabel('Точность')
    plt.xlabel('Эпоха')
    plt.legend(loc='upper left')
    plt.show()


def print_result(history, control_loss, control_accuracy):
    """Выводит результаты для трех подвыборок."""
    training_loss = history.history['loss'][-1]
    training_accuracy = history.history['accuracy'][-1]
    validation_loss = history.history['val_loss'][-1]
    validation_accuracy = history.history['val_accuracy'][-1]
    
    print(f"обучающая подвыборка\t – потери: {training_loss:.4f} – точность: {training_accuracy:.4f}")
    print()
    print(f"валидационная подвыборка – потери: {validation_loss:.4f} – точность: {validation_accuracy:.4f}")
    print()
    print(f"контрольная подвыборка\t – потери: {control_loss:.4f} – точность: {control_accuracy:.4f}")