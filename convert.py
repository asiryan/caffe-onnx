import os
import argparse
import onnx
from src.load_save_model import loadcaffemodel, saveonnxmodel
from src.caffe2onnx import Caffe2Onnx


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--prototxt",   type=str,  required=True,  help="input .prototxt")
    parser.add_argument("--caffemodel", type=str,  required=True,  help="input .caffemodel")
    parser.add_argument("--onnx",       type=str,  required=True,  help="output .onnx")
    parser.add_argument("--frozen",     type=bool, required=False, help="frozen graph or not")
    args = parser.parse_args()
    return args


def main(args):
    # parse data
    prototxt_path = args.prototxt
    caffemodel_path = args.caffemodel
    onnxmodel_path = args.onnx
    frozen = args.frozen
    if frozen is None: frozen = False

    # create model
    graph, params = loadcaffemodel(prototxt_path, caffemodel_path)
    c2o = Caffe2Onnx(graph, params, onnxmodel_path)
    onnxmodel = c2o.createOnnxModel()

    # frozen graph
    if frozen is True:
        print("removing not constant initializers from model")
        inputs = onnxmodel.graph.input
        name_to_input = {}
        for input in inputs:
            name_to_input[input.name] = input

        for initializer in onnxmodel.graph.initializer:
            if initializer.name in name_to_input:
                inputs.remove(name_to_input[initializer.name])

        print("frozen graph has been created")
    
    saveonnxmodel(onnxmodel, onnxmodel_path)


if __name__ == '__main__':
    args = parse_args()
    main(args)
