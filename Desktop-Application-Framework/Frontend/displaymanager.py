import docker
import requests
import time
from pm4py.objects.log.importer.xes import importer as xes_importer
import docker
import time
from pm4py.visualization.petri_net import visualizer as pn_visualizer
from pm4py.objects.petri_net.importer import importer as pnml_importer
from pm4py.visualization.dfg import visualizer as dfg_visualization
import pickle
import os

class DisplayManager:

    def func1(self, algo_name ):
        net, initial_marking, final_marking = pnml_importer.apply("/Users/jahnavijaiswal/WiSe21/Lab/Sprint_2/Backend/Desktop-Application-Framework/app-data/"+algo_name+"/output_data/petri_final.pnml")
        gviz = pn_visualizer.apply(net, initial_marking, final_marking)
        pn_visualizer.view(gviz)
    
    def func2(self , algo_name , log_direc ):
        with open("/Users/jahnavijaiswal/WiSe21/Lab/Sprint_2/Backend/Desktop-Application-Framework/app-data/"+algo_name+"/output_data/output_dfg.pickle", 'rb') as inputfile:
            print("input file",inputfile)
            output = pickle.load(inputfile)
            parameters = {dfg_visualization.Variants.PERFORMANCE.value.Parameters.FORMAT: "png"}
            gviz = dfg_visualization.apply(output, log=log_direc, variant=dfg_visualization.Variants.PERFORMANCE, parameters=parameters)
            dfg_visualization.view(gviz)
