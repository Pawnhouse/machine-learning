import os
import pickle
import random

import numpy as np
from PIL import Image


LARGE_DATA_SET_FOLDER = 'notMNIST_large'
SMALL_DATA_SET_FOLDER = 'notMNIST_small'
PICKLE_FOLDER = 'pickle'
CLASSES = 'ABCDEFGHIJ'
NUMBER_OF_CLASSES = 10


def get_images(folder_path, is_verbose=True):
    """Загружает изображения из набора данных и возвращает список массивов NumPy."""
    images = []    
    for file in os.listdir(folder_path):
        image_path = os.path.join(folder_path, file)
        try:
            img = np.asarray(Image.open(image_path))
            images.append(img)
        except (IOError, SyntaxError):
            print('Поврежденное изображение ' + image_path)
            
    if is_verbose:
        print('Готово для ' + folder_path)
    return images


def save_data_set():
    """Сохраняет изображения в формате pickle."""
    for data_set_folder in [LARGE_DATA_SET_FOLDER, SMALL_DATA_SET_FOLDER]:
        for class_folder in os.listdir(data_set_folder):     
            os.makedirs(os.path.join(PICKLE_FOLDER, data_set_folder), exist_ok=True)
            pickle_class_images_file = os.path.join(PICKLE_FOLDER, data_set_folder, class_folder + '.pkl')
            class_images = get_images(os.path.join(data_set_folder, class_folder))
            with open(pickle_class_images_file, 'wb') as f:
                pickle.dump(class_images, f, pickle.HIGHEST_PROTOCOL)
        print()


def load_data_set(data_set_folder):
    """Загружает все изображения из папки pickle."""
    data_set = {}
    for class_file in os.listdir(os.path.join(PICKLE_FOLDER, data_set_folder)):
        class_file_path = os.path.join(PICKLE_FOLDER, data_set_folder, class_file)
        class_name = os.path.splitext(os.path.basename(class_file_path))[0]
        with open(class_file_path, 'rb') as class_file:
            data_set[class_name] = pickle.load(class_file)
    return data_set


def get_subset(data_set, size):
    """Получает подможножество изображений заданного размера."""
    subset = {}
    for class_name, images in data_set.items():
        subset[class_name] = random.sample(images, size // NUMBER_OF_CLASSES)
    return subset


def get_subsets():
    """Получает обучающае, валидационное и контрольное подмножества."""
    random.seed(7)
    large_data_set = load_data_set(LARGE_DATA_SET_FOLDER)
    small_data_set = load_data_set(SMALL_DATA_SET_FOLDER)
    training_subset = get_subset(large_data_set, 200000)
    validation_subset = get_subset(large_data_set, 10000)
    control_subset = small_data_set
    for class_name, images in training_subset.items():
        taken_images = {tuple(image.flatten()) for image in validation_subset[class_name] + control_subset[class_name]}
        training_subset[class_name] = [image for image in images if tuple(image.flatten()) not in taken_images]
    return training_subset, validation_subset, control_subset