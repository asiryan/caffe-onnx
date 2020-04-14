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
usage: convert.py [-h] [caffe_graph_path] [caffe_params_path] [onnx_name] [save_dir]

positional arguments:
  caffe_graph_path          caffe's prototxt file path
  caffe_params_path         caffe's caffemodel file path
  onnx_name                 onnx model name
  save_dir                  onnx model file saved path
```  

1. As an example convert test network to onnx model by command
```
python convert.py caffemodel/test.prototxt caffemodel/test.caffemodel test onnxmodel
```
or run `test.bat`.

2. Visualize onnx model by netron
    ```bash
    $ netron onnxmodel/resnet50.onnx --host 0.0.0.0 --port 8008
    ```

3. If you have custom layers in caffe which makes your `caffe.proto` is different than the one in the origin caffe code. The things you should do before convertion is:  
    - First of all, compile your proto file with `protoc`
        ```bash
        # for example
        $ protoc /your/path/to/caffe_ssd.proto --python_out ./proto
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


## Visualization  
[Netron](https://github.com/lutzroeder/netron)  
[Netron Browser](https://lutzroeder.github.io/netron/)  


## Development Guide
See [Develop Guide](./DEVELOP_GUIDE.md)
