### RQ2: How effective are the model-structure mutation operators in detecting defects?

The current folder stores the results of 11 mutation models calculating scenario task metrics during 50 rounds of mutation, as well as the distance between the middle layers of the model on different frameworks. The results of different experimental subjects (E1, E2, E3) are divided and stored according to the model type. Each model folder contains two files: "RQ2 eval. csv" and "RQ2 middlelayer_distance_new. csv". Among them, the first column "output_dis" in the "RQ2 eval. csv" file stores the distance of the last layer output of the current round of mutation model on the MindSpot and PyTorch frameworks. The following columns show the evaluation index values of the mutation model on both frameworks.

The current folder stores the results of 11 mutation models calculating scenario task metrics during 50 rounds of mutation, as well as the distance between the middle layers of the model on different frameworks. The results of different experimental subjects (E1, E2, E3) are divided and stored according to the model type. Each model folder contains two files: "RQ2 eval. csv" and "RQ2 middlelayer_distance_new. csv". Among them, the first column "output_dis" in the "RQ2 eval. csv" file stores the distance of the last layer output of the current round of mutation model on the MindSpot and PyTorch frameworks. The following columns show the evaluation index values of the mutation model on both frameworks. The content of each model evaluation indicator file "RQ2 eval. csv" can be found in the following table.

| Modelname        | Evaluation Metric | Description                                                  |
| ---------------- | ----------------- | ------------------------------------------------------------ |
| ResNet50         | Accuracy          | Since the test set CIFAR-10 was a 10 class dataset, we not only recorded the overall accuracy of the mutation model on the CIFAR-10 test set, but also separately recorded the accuracy of the mutation model on a single class. Therefore, the VGG16 and Resnet50 models each included 11 columns of results in the experimental results of the MindSpore and PyTorch frameworks. |
| VGG16            | Accuracy          | Since the test set CIFAR-10 was a 10 class dataset, we not only recorded the overall accuracy of the mutation model on the CIFAR-10 test set, but also separately recorded the accuracy of the mutation model on a single class. Therefore, the VGG16 and Resnet50 models each included 11 columns of results in the experimental results of the MindSpore and PyTorch frameworks. |
| SSD-mobilenetv2  | Map               | Both yolov3 and SSDmobilenetv2 are calculated using the map function provided by the PyCOCOTools toolkit. The results include the IOU values of the target object detected using anchor boxes of different sizes. Therefore, the results of the mutation model on the MindSpore and Python frameworks each contain 12 columns. Specific information can be found in the introduction of the PyCOCOTools toolkit. |
| YoLoV3-Darknet53 | Map               | Both yolov3 and SSDmobilenetv2 are calculated using the map function provided by the PyCOCOTools toolkit. The results include the IOU values of the target object detected using anchor boxes of different sizes. Therefore, the results of the mutation model on the MindSpore and Python frameworks each contain 12 columns. Specific information can be found in the introduction of the PyCOCOTools toolkit. |
| DeeplabV3        | IOU               | The deeplabv3 model calculates the average IOU on all category data and the IOU on each category, so the results on the MindSpore and PyTorch frameworks each contain twenty-one columns. |
| Unet             | Dice              | The unet model calculates the average Dice and IOU on all categories of data, so the results on the MindSpore and PyTorch frameworks each contain two columns. |
| TextCNN          | Accuracy          | The TextCNN model performs a binary classification task, so the results of the mutation model on MindSpore and PyTorch frameworks only include one column of accuracy on all data in the test set |
| PatchCore        | AUC               | The patchcore model calculates the AUC values of the data at the image level and pixel level, respectively. Therefore, the results on the MindSpore and PyTorch frameworks each have two columns |



Please note that due to the long running time of the SSIM-AE, OpenPose, and SSD-resnet50 models in calculating evaluation metrics, we did not report the results of these three models.



The first column in the file "RQ2-middlelayer_distance_new.csv" stores the name of the middle layer of the model, and the following 10 columns record the differences in the middle layer output of the 5th, 10th, 15th, 20th,... and 50th generation mutation models executed on the Python and Mindshare frameworks.



