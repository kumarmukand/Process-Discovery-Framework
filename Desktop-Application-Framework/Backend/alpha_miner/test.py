from pm4py.visualization.petri_net import visualizer as pn_visualizer
from pm4py.objects.petri_net.importer import importer as pnml_importer

net, initial_marking, final_marking = pnml_importer.apply("petri_final.pnml")


gviz = pn_visualizer.apply(net, initial_marking, final_marking)
pn_visualizer.view(gviz)

