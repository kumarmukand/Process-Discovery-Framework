import pm4py
import sys
import os.path
from pm4py.objects.log.importer.xes import importer as xes_importer
from pm4py.algo.discovery.correlation_mining import algorithm as correlation_miner
from pm4py.visualization.petri_net import visualizer as pn_visualizer
from pm4py.objects.petri_net.exporter import exporter as pnml_exporter

file_name = sys.argv[1]

file_path = '/../correlation_miner/input_data/' + file_name

print(file_path)

log = xes_importer.apply(file_path)

net, initial_marking, final_marking = correlation_miner.apply(log)



pnml_exporter.apply(net=net, initial_marking=initial_marking, output_filename="/../correlation_miner/output_data/output.pnml", final_marking=final_marking)
