import sys
from pm4py.objects.log.importer.xes import importer as xes_importer
from pm4py.visualization.heuristics_net import visualizer as hn_visualizer
from pm4py.algo.discovery.heuristics import algorithm as heuristics_miner
from pm4py.visualization.petri_net import visualizer as pn_visualizer
from pm4py.objects.petri_net.exporter import exporter as pnml_exporter

file_name = sys.argv[1]

file_path = '/../heuristic_miner/input_data/' + file_name

print(file_path)

log = xes_importer.apply(file_path)

net, initial_marking, final_marking = heuristics_miner.apply(log, parameters={heuristics_miner.Variants.CLASSIC.value.Parameters.DEPENDENCY_THRESH: 0.99})

# gviz = pn_visualizer.apply(net, initial_marking, final_marking)
# pn_visualizer.view(gviz)


pnml_exporter.apply(net=net, initial_marking=initial_marking, output_filename="/../heuristic_miner/output_data/petri_final.pnml", final_marking=final_marking)
