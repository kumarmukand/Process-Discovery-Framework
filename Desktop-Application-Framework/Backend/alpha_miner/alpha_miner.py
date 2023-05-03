import pm4py
import sys
import os.path
from pm4py.objects.log.importer.xes import importer as xes_importer
from pm4py.algo.discovery.alpha import algorithm as alpha_miner
from pm4py.visualization.petri_net import visualizer as pn_visualizer
from pm4py.objects.petri_net.exporter import exporter as pnml_exporter

file_name = sys.argv[1]

file_path = '/../alpha_miner/input_data/' + file_name

print(file_path)

log = xes_importer.apply(file_path)

net, initial_marking, final_marking = alpha_miner.apply(log)

#gviz = pn_visualizer.apply(net, initial_marking, final_marking)
#pn_visualizer.view(gviz)

pnml_exporter.apply(net=net, initial_marking=initial_marking, output_filename="/../alpha_miner/output_data/petri_final.pnml", final_marking=final_marking)
