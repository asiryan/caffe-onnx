from google.protobuf import text_format
import onnx
from proto import caffe_upsample_pb2 as caffe_pb2

def loadcaffemodel(net_path,model_path):
    # read prototxt
    net = caffe_pb2.NetParameter()
    text_format.Merge(open(net_path).read(), net)
    # read caffemodel
    model = caffe_pb2.NetParameter()
    f = open(model_path, 'rb')
    model.ParseFromString(f.read())
    f.close()
    print("caffemodel was successfully loaded")
    return net,model

def loadonnxmodel(onnx_path):
    onnxmodel = onnx.load(onnx_path)
    return onnxmodel

def saveonnxmodel(onnxmodel,onnx_save_path):
    try:
        onnx.checker.check_model(onnxmodel)
        onnx.save_model(onnxmodel, onnx_save_path)
        print("the model has been successfully saved and has been saved to " + onnx_save_path)
    except Exception as e:
        print("the model was not saved successfully:\n", e)
