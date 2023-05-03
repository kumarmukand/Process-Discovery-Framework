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
from displaymanager import DisplayManager

class DockerManager:
    def __init__(self, client = docker.from_env()):
        self.client = client
    
    
    def list_algorithms(self):
        url = "http://localhost:5000/v2/_catalog"
        algo_list_request = requests.get(url)
        print(algo_list_request.json())
        return algo_list_request.json()


    
    def run_algorithm(self, algo_name, log_name , direc_name):
        
        print("algo_name: ",algo_name)
        log_direc = xes_importer.apply(direc_name)
        #print("log_direc",log_direc)
        volumes= ['/Users/jahnavijaiswal/WiSe21/Lab/Sprint_2/Backend/Desktop-Application-Framework/app-data/'+algo_name]
        volume_bindings = {
                            '/Users/jahnavijaiswal/WiSe21/Lab/Sprint_2/Backend/Desktop-Application-Framework/app-data/'+algo_name: {
                                'bind': '/'+algo_name,
                                'mode': 'rw',
                            },
        }

        host_config = self.client.api.create_host_config(
                            binds=volume_bindings
        )

        container = self.client.api.create_container(
                            image= algo_name,
        #                   name="alpha_miner",
                            volumes=volumes,
                            host_config=host_config,
                            command= log_name
        ) 
        response = self.client.api.start(container=container.get('Id'))

        time.sleep(5)
        display_manager = DisplayManager()
        
        test_path =  "/Users/jahnavijaiswal/WiSe21/Lab/Sprint_2/Backend/Desktop-Application-Framework/app-data/"+algo_name+"/output_data/"
        files_test_path = os.listdir(test_path)
        for files in files_test_path:
            print("filess in o/p",files)
            if ".pickle" in files:
                #self.func2(algo_name, log_direc)
                display_manager.func2(algo_name, log_direc)
            elif ".pnml" in files:
                #self.func1(algo_name)
                display_manager.func1(algo_name)

        





        #print(log_name)
    
        # if ".xes" in log_name:
        #     print("is xes format!")
        #     self.func1(algo_name , log_name)


        #net, initial_marking, final_marking = pnml_importer.apply("/Users/jahnavijaiswal/WiSe21/Lab/Sprint_2/Backend/Desktop-Application-Framework/app-data/"+algo_name+"/output_data/petri_final.pnml")

        #gviz = pn_visualizer.apply(net, initial_marking, final_marking)
        #pn_visualizer.view(gviz)
        #pn_visualizer.view(gviz)
        

           

    
        
    # def func2(self):
    #     #log="running-example.xes"
    #     with open("/Users/jahnavijaiswal/WiSe21/Lab/Sprint_2/Backend/Desktop-Application-Framework/app-data/"+algo_name+"/output_data/output_dfg.pickle", 'rb') as inputfile:
    #         output = pickle.load(inputfile)
    #         parameters = {dfg_visualization.Variants.PERFORMANCE.value.Parameters.FORMAT: "svg"}
    #         gviz = dfg_visualization.apply(output, log=log_name, variant=dfg_visualization.Variants.PERFORMANCE, parameters=parameters)
    #         dfg_visualization.view(gviz)

    