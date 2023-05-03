import pm4py
import os
import sys
from pm4py.objects.log.importer.xes import importer as xes_importer
from pm4py.visualization.dfg import visualizer as dfg_visualization
from pm4py.algo.discovery.dfg import algorithm as dfg_discovery
from pm4py.objects.petri_net.exporter import exporter as pnml_exporter
import pickle



file_name = sys.argv[1]
file_path = '/../dfg/input_data/' + file_name
print(file_path)

log = xes_importer.apply(file_path)




dfg = dfg_discovery.apply(log, variant=dfg_discovery.Variants.PERFORMANCE)
parameters = {dfg_visualization.Variants.PERFORMANCE.value.Parameters.FORMAT: "png"}
gviz = dfg_visualization.apply(dfg, log=log, variant=dfg_visualization.Variants.PERFORMANCE, parameters=parameters)


with open('/../dfg/output_data/output_dfg.pickle', 'wb') as outputfile:
    pickle.dump(dfg, outputfile)


# with open('output.pickle', 'rb') as inputfile:
#     output = pickle.load(inputfile)

  
# parameters = {dfg_visualization.Variants.PERFORMANCE.value.Parameters.FORMAT: "svg"}
# gviz = dfg_visualization.apply(output, log=log, variant=dfg_visualization.Variants.PERFORMANCE, parameters=parameters)

# dfg_visualization.view(gviz)










