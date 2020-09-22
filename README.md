# caffe-onnx
This tool converts caffe model convert to onnx model.  
Only use for inference.

## Introduction  
This is the second version of converting caffe model to onnx model. In this version, all the parameters will be transformed to tensor and tensor value info when reading `.caffemodel` file and each operator node is constructed directly into the type of NodeProto in onnx.


## Dependencies  
- protobuf  
- onnx==1.4.0    

```bash
$ pip install -r requirements.txt
```

( caffe environment is not required! )

## How to Use  
```
usage: convert.py [-h] --prototxt PROTOTXT --caffemodel CAFFEMODEL --onnx ONNX
                  [--frozen FROZEN]

positional arguments:
  prototxt          caffe's prototxt file path
  caffemodel        caffe's caffemodel file path
  onnx              onnx model name
  frozen            frozen graph or not
```

## Example usage
Download pretrained model for face gender prediction from the [link](https://data.vision.ee.ethz.ch/cvl/rrothe/imdb-wiki/) and convert caffe model to onnx using
```
python convert.py --prototxt gender.prototxt --caffemodel gender.caffemodel --onnx gender.onnx --frozen true
```

## Proto
If you have custom layers in caffe which makes your `caffe.proto` is different than the one in the origin caffe code. The things you should do before convertion is:  
- First of all, compile your proto file with `protoc`
```bash
# for example
protoc /your/path/to/caffe_ssd.proto --python_out ./proto
```
- Then specify the caffe proto file by replacing the line `from proto import caffe_upsample_pb2 as caffe_pb2` with your module.
   

## Supported operators  
BatchNorm  
Convolution  
Deconvolution  
Concat  
Dropout  
InnerProduct(Reshape+Gemm)  
LRN  
Pooling  
Unpooling  
ReLU  
Softmax  
Eltwise  
Upsample  
Scale  


## Caffe models  
- Resnet50  
- AlexNet  
- Agenet  
- Yolo V3  
- vgg16  
- GoogLeNet  
- Sphereface  


## Development Guide
See [Develop Guide](./DEVELOP_GUIDE.md)
