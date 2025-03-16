## Определение номера дома

Мобильное приложение определяет номер дома на фотографии.
Для распознавания цифр используется нейронная сеть, разработанная в 4 лабораторной работе.
Модель YOLOv5 определяет положение цифр на фотографии.

### Пример работы приложения

<div style="display: flex; flex-wrap: wrap; gap: 5px;">
    <img src="screenshots/Screenshot_2025_03_16_14_14_00_173_com_example_ml_android_app.jpg" alt="Screenshot 1" style="width: 300px; border: 1px solid black; border-radius: 5px;"/>
    <img src="screenshots/Screenshot_2025_03_16_14_14_22_472_com_example_ml_android_app.jpg" alt="Screenshot 2" style="width: 300px; border: 1px solid black; border-radius: 5px;"/>
    <img src="screenshots/Screenshot_2025_03_16_14_14_32_586_com_example_ml_android_app.jpg" alt="Screenshot 3" style="width: 300px; border: 1px solid black; border-radius: 5px;"/>
    <img src="screenshots/Screenshot_2025_03_16_14_14_50_748_com_example_ml_android_app.jpg" alt="Screenshot 4" style="width: 300px; border: 1px solid black; border-radius: 5px;"/>
</div>

### Разработка

Приложение разработано на языке программирования Kotlin в Android Studio 2024.
Для установки на Android можно воспользоваться файлом [ml-android-app.apk](ml-android-app.apk).
Модель YOLOv5 была взята из репозитория 
[yolov5-svhn-detection](https://github.com/joycenerd/yolov5-svhn-detection).