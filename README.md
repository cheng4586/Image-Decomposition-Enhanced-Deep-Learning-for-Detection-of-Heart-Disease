# Image-Decomposition-Enhanced-Deep-Learning-for-Detection-of-Heart-Disease
Python code for the paper: Shu, Y., Smith, T. G., Arunachalam, S. P., Tolkacheva, E. G., & Cheng, C. (2023). Image-Decomposition-Enhanced Deep Learning for Detection of Rotor Cores in Cardiac Fibrillation. IEEE Transactions on Biomedical Engineering. DOI: 10.1109/TBME.2023.3292383

Empirical Mode Decomposition algorithm (EEMD) to decompose the image data and characterize the underlying dynamics, and the most representative component is then fed into a You-Only-Look-Once (YOLO) image-recognition architecture for heart disease detection.


A novel low-rank and joint-sparse decomposition (LJSD) is developed for effective reconstruction of epicardial electrical potential.
Ensemble Empirical Mode Decomposition algorithm (EEMD) with a You-Only-Look-Once (YOLO) image-recognition architecture is applied for heart diseasr detection

This integrated EEMD-YOLO model achieves the highest rotor detection accuracy (96%) compared to other filtering-AI methods. 

## Methodology
- CNN model (You-Only-Look-Once (YOLO) image-recognition architecture)
![YoLo](https://user-images.githubusercontent.com/71365210/189995854-905bdf41-3173-4bd5-8f34-8a3149780f53.jpg)
- Image partition and bounding box design
![image preprocess](https://user-images.githubusercontent.com/71365210/189996344-17ff2bb7-9f82-44c0-bcbc-5bc6ce9a21b6.jpg)


## Heart detection on simulated data
![simulation](https://user-images.githubusercontent.com/71365210/189996445-5492b24f-0f3a-4dce-8645-38ae7e468824.jpg)


## Heart detection on animal experiment data
![animals](https://user-images.githubusercontent.com/71365210/189996617-c83972d9-e5df-4ffd-93d5-696967f8c61c.jpg)

