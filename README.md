# Selfie Segmentation Application

I developed this application to focus on important regions in webcam images selectively. It leverages OpenCV, Mediapipe, Matplotlib, and NumPy for image processing and employs Gradio for web deployment.

## About the project

In this project, the input is taken through the webcam using OpenCV, then all the pre-processing is done using Mediapipe and Matplotlib. Then by using NumPy we blur or darken the background which allows us to easily separate the background from users within a scene and focus on what matters. Finally, we wrap everything in Gradio for creating the web application.

## Dependencies

1. **OpenCV**: It helps capture the feed through the webcam.

2. **Mediapipe**: It helps in pre-processing the captured image.

3. **Matplolib**: It helps plot the image by setting up the axes.

4. **NumPy**: It helps blur or darken the image's less important regions.

5. **Gradio**: It is a simple application for creating web applications, especially for jupyter notebooks.

## Datasets

![tmp2jiq2h1_](https://github.com/Hansaraj09/Selfie_Segmentation/assets/93324559/b7bd8ed3-3fa7-43f9-8ed3-e869bde55a0f)

## Some Results

![tmp0nkxj4v3](https://github.com/Hansaraj09/Selfie_Segmentation/assets/93324559/fe8084f9-af6a-48e7-b0e3-32cbb0384b3e)

![image (2)](https://github.com/Hansaraj09/Selfie_Segmentation/assets/93324559/816146d4-0d4f-40cf-9f83-dc6ad905a67f)

## About Gradio

[Click Here](https://github.com/gradio-app/gradio)





