---
layout: home

parent_id: 3-apps
id: 3.7-video
title: 🎥 Video

img_icon: 3.7-video.svg
---


### [A Comprehensive Study of Deep Video Action Recognition](https://arxiv.org/abs/2012.06567) (11 Dec 2020)



```
---------------             -----------------
|  Real time  |   ip:port   | Deep Learning |
| Videocamera |  ---------> |   inference   | 
---------------             -----------------

		  (RTSP or HTTP protocol)
```

# Ejemplos de URL (para VideoCapture de OpenCV)

HTTP               -----> http://192.168.18.37:8090/video
RSTP               -----> rtsp://192.168.1.64/1
RSTP con seguridad -----> rtsp://user:pass@192.168.1.64/1

Camara principal  del portatil ---> 0 (ó -1)
Camara secundaria del portatil ---> 1


# Código en OpenCV

- https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_gui/py_video_display/py_video_display.html

```python
import cv2

cap = cv2.VideoCapture('http://192.168.18.37:8090/video')

while(True):
    ret, frame = cap.read()   # Capture frame-by-frame. frame es nu nparray de 3 dims

    # Our operations on the frame come here...

    # Display the resulting frame
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break

cap.release() # When everything done, release the capture (apagar la camara)
cv2.destroyAllWindows()
```


### Mostrar el frame actual con Matplotlib

```python
cap = cv2.VideoCapture('http://192.168.18.37:8090/video')
cap.release()
plt.imshow(frame[:,:,::-1]) # OpenCV uses BGR, whereas matplotlib uses RGB
plt.show()
```

### Obtener ancho y alto

```python
cap = cv2.VideoCapture('http://192.168.18.37:8090/video')
width  = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))   # o también: cap.get(3)
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))  # o también: cap.get(4)
```

### Cambiar ancho y alto

```python
# Cambiar a 320x240
ret = cap.set(3,320)
ret = cap.set(4,240)
```

### Inferencia en Pytorch

- https://discuss.pytorch.org/t/pytorch-trained-model-on-webcam
- https://dida.do/blog/how-to-recognise-objects-in-videos-with-pytorch


```python
# First convert the image to a tensor, reverse the channels, unsqueeze and send to the right device.
frame_tensor = self.tfms(Image.fromarray(frame[:,:,::-1])).unsqueeze(0).to(self.device)
```


# Listado de propiedades de la captura

- https://docs.opencv.org/2.4/modules/highgui/doc/reading_and_writing_images_and_video.html#videocapture-get

| Id | Propiedad                   | Descripción                                                     |
|----|-----------------------------|-----------------------------------------------------------------|
|  0 | CV_CAP_PROP_POS_MSEC        | Current position of the video file in milliseconds (timestamp). |
|  1 | CV_CAP_PROP_POS_FRAMES      | 0-based index of the frame to be decoded/captured next.         | 
|  2 | CV_CAP_PROP_POS_AVI_RATIO   | Relative position of the video file (0: start, 1: end).         |
|  3 | CV_CAP_PROP_FRAME_WIDTH     | Width of the frames in the video stream.                        |
|  4 | CV_CAP_PROP_FRAME_HEIGHT    | Height of the frames in the video stream.                       |
|  5 | CV_CAP_PROP_FPS             | Frame rate.                                                     |
|  6 | CV_CAP_PROP_FOURCC          | 4-character code of codec.                                      |
|  7 | CV_CAP_PROP_FRAME_COUNT     | Number of frames in the video file.                             |
|  8 | CV_CAP_PROP_FORMAT          | Format of the Mat objects returned by retrieve() .              |
|  9 | CV_CAP_PROP_MODE            | Backend-specific value indicating the current capture mode.     |
| 10 | CV_CAP_PROP_BRIGHTNESS      | Brightness of the image (only for cameras).                     |
| 11 | CV_CAP_PROP_CONTRAST        | Contrast of the image (only for cameras).                       |
| 12 | CV_CAP_PROP_SATURATION      | Saturation of the image (only for cameras).                     |
| 13 | CV_CAP_PROP_HUE             | Hue of the image (only for cameras).                            |
| 14 | CV_CAP_PROP_GAIN            | Gain of the image (only for cameras).                           |
| 15 | CV_CAP_PROP_EXPOSURE        | Exposure (only for cameras).                                    |
| 16 | CV_CAP_PROP_CONVERT_RGB     | Boolean flags indicating whether images should be converted to RGB.
| 17 | CV_CAP_PROP_WHITE_BALANCE_U | The U value of the whitebalance setting                         |
| 18 | CV_CAP_PROP_WHITE_BALANCE_V | The V value of the whitebalance setting                         |
| 19 | CV_CAP_PROP_RECTIFICATION   | Rectification flag for stereo cameras (only in opencv 2.x)      |
| 20 | CV_CAP_PROP_ISO_SPEED       | The ISO speed of the camera (only in opencv 2.x)                |
| 21 | CV_CAP_PROP_BUFFERSIZE      | Amount of frames stored in internal buffer memory (only in opencv 2.x)         |
