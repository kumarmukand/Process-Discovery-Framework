import os
import sys
from pm4py.objects.log.importer.xes import importer as xes_importer
from pm4py.algo.discovery.inductive import algorithm as inductive_miner
from pm4py.objects.petri_net.exporter import exporter as pnml_exporter
from pm4py.visualization.process_tree import visualizer as pt_visualizer

file_name = sys.argv[1]

file_path = '/../inductive_miner/input_data/' + file_name

print(file_path)

log = xes_importer.apply(file_path)
net, initial_marking, final_marking = inductive_miner.apply(log)



# tree = inductive_miner.apply_tree(log)

# gviz = pt_visualizer.apply(tree)
# pt_visualizer.view(gviz)


pnml_exporter.apply(net=net, initial_marking=initial_marking, output_filename="/../inductive_miner/output_data/petri_final.pnml", final_marking=final_marking)

