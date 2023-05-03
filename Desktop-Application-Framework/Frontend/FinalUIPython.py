from os import path
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow,QWidget, QFileDialog, QTextEdit, QPushButton, QLabel, QVBoxLayout, QDialog, QMessageBox
from FinalUI import*
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtCore import QCoreApplication
from pm4py.visualization.dfg import visualizer as dfg_visualization
import glob
import sys
import os
from Dialog_box import Ui_Error_Label 
import pandas as pd
from pm4py.objects.log.importer.xes import importer as xes_importer
import docker
import time
import os, shutil
from pm4py.visualization.petri_net import visualizer as pn_visualizer
from pm4py.objects.petri_net.importer import importer as pnml_importer
from dockermanager import DockerManager
import json
class FirstApp(Ui_MainWindow):
    def __init__(self,window):
        
        self.setupUi(window)
        
        self.direcname= " "
        self.tabWidget.setCurrentIndex(0)
        self.buttonSelectDocker.setEnabled(False)
        self.buttonApplyAlgorithm.setEnabled(False)
        self.buttonImportlog.clicked.connect(self.logload)
        self.buttonApplyAlgorithm.clicked.connect(self.run_algorithm)
        self.buttonSelectDocker.clicked.connect(self.selectLog)
        self.buttonExport.clicked.connect(self.exportFiles)
        self.buttonExit.clicked.connect(self.ExitApp)
        self.buttonDisplay.clicked.connect(self.displayOutput)

        self.tabWidget.setTabEnabled(2,False);
        dock_manager = DockerManager()
        
        algorithms_list = dock_manager.list_algorithms()["repositories"]
        for algo in algorithms_list:
            self.listAlgorithm.addItem(algo)

        self.listAlgorithm.clicked.connect(self.algo_item_clicked)   
        
    def logload(self):
        filename=QtWidgets.QFileDialog.getOpenFileName()
        self.direcname = filename[0]
        self.log_name = QFileInfo(self.direcname).fileName()
        print(self.log_name)
        #print(self.direcname)
        if os.stat(self.direcname).st_size == 0:
            print("empty file!")
            self.open_dialog_box()
        else:
            print("not empty")
            self.listImportedLog.addItem(self.log_name)
            self.buttonSelectDocker.setEnabled(True)
            self.input_path = "/Users/jahnavijaiswal/WiSe21/Lab/Sprint_2/Backend/Desktop-Application-Framework/app-data/INPUT/"
            shutil.copy(self.direcname,self.input_path)
        self.listImportedLog.clicked.connect(self.log_item_clicked)

    
    def ExitApp(self):

        filelist_INPUT = glob.glob(os.path.join(self.input_path, "*"))
        for f in filelist_INPUT:
            os.remove(f)
        
        filelist_output_data = glob.glob(os.path.join(self.output_path, "*"))
        for f in filelist_output_data:
            os.remove(f)
        
        filelist_input_data = glob.glob(os.path.join(self.algo_input_path, "*"))
        for f in filelist_input_data:
            os.remove(f)
        
        MainWindow.close()


    def exportFiles(self):
    
        self.completeName = self.output_path
        print("Complete name",self.completeName)
        fn= QFileDialog.getSaveFileName(caption='Export File')
        self.dest=fn[0]
        
        files_output = os.listdir(self.completeName)
        print(self.dest)

        for file in files_output:
            if fn != '':
                ab=shutil.copy(self.completeName+file,self.dest)

    def displayOutput(self):
        
        print("3)")
        print(self.log_name_selected)
        if ".pnml" in self.log_name_selected:
            print("4")
            print("input path",self.input_path+self.log_name_selected)
            net, initial_marking, final_marking = pnml_importer.apply(self.input_path+self.log_name_selected)
            gviz = pn_visualizer.apply(net, initial_marking, final_marking)
            pn_visualizer.view(gviz)
            print("5")
            
        else:
            msgBox = QMessageBox()
            msgBox.setText("Select a petrinet or a .pickle file!")
            msgBox.exec()
            

            
                
                
    def log_item_clicked(self):

        item1 =self.listImportedLog.currentItem()
        self.log_name_selected = str(item1.text())        
        print("selected current log is",self.log_name_selected)

    
    def algo_item_clicked(self):

        item =self.listAlgorithm.currentItem()
        self.algo_name_selected = str(item.text())
        print("The selected current item is",self.algo_name_selected)
        
        with open('config.json','r') as f:
            config = json.load(f)
       
        
        if self.algo_name_selected == "alpha_miner":
            self.label_showAlgoSummary.setText("".join(config['ALPHA_MINER']['DESCRIPTION'])+"".join(config['ALPHA_MINER']['INPUT'])+"".join(config['ALPHA_MINER']['OUTPUT']))
        elif self.algo_name_selected == "inductive_miner":
            self.label_showAlgoSummary.setText("".join(config['INDUCTIVE_MINER']['DESCRIPTION'])+"".join(config['INDUCTIVE_MINER']['INPUT'])+"".join(config['INDUCTIVE_MINER']['OUTPUT']))
        elif self.algo_name_selected == "heuristic_miner":
            self.label_showAlgoSummary.setText("".join(config['HEURISTIC_MINER']['DESCRIPTION'])+"".join(config['HEURISTIC_MINER']['INPUT'])+"".join(config['HEURISTIC_MINER']['OUTPUT']))
        #elif self.algo_name_selected == "CORRELATION_MINER":
            #self.label_showAlgoSummary.setText("".join(config['CORRELATION_MINER']['DESCRIPTION'])+"".join(config['CORRELATION_MINER']['INPUT'])+"".join(config['CORRELATION_MINER']['OUTPUT']))
        elif self.algo_name_selected == "dfg":
            self.label_showAlgoSummary.setText("".join(config['DFG']['DESCRIPTION'])+"".join(config['DFG']['INPUT'])+"".join(config['DFG']['OUTPUT']))
        
            
    def showLogSummary(self):
        log = xes_importer.apply(self.direcname)
        print(log[0])
        self.labelLogSummary.setText(str(log[0]))
        self.labelLogSummary.setWordWrap(True)

    def selectLog(self):
        self.tabWidget.setCurrentIndex(1)
        self.buttonApplyAlgorithm.setEnabled(True)
        
        print("INPUT_path",self.input_path)
        print("selected_log_name",self.log_name_selected)
        self.input_file_path = self.input_path+self.log_name_selected
        print("INPUT File Path",self.input_file_path)

    
    def run_algorithm(self):

        print("selected algorithm is",self.algo_name_selected) 
        self.algo_input_path = '/Users/jahnavijaiswal/WiSe21/Lab/Sprint_2/Backend/Desktop-Application-Framework/app-data/'+self.algo_name_selected+'/input_data'
        print("The log directory",self.input_file_path)
        #files_input_path = os.listdir(input_path)
        logfile_path = self.input_file_path
        print("log file path:",logfile_path)
        shutil.copy(logfile_path,self.algo_input_path)
        
        
        dock_manager = DockerManager()
       
        dock_manager.run_algorithm(self.algo_name_selected , self.log_name_selected, logfile_path)

        # adding o/p files to import log screen
        
        self.output_path = '/Users/jahnavijaiswal/WiSe21/Lab/Sprint_2/Backend/Desktop-Application-Framework/app-data/'+self.algo_name_selected+'/output_data/'
        self.path = '/Users/jahnavijaiswal/WiSe21/Lab/Sprint_2/Backend/Desktop-Application-Framework/app-data/INPUT/'
        
        files_output_path = os.listdir(self.output_path)
        
        # for files in files_input_path:
        #     print("filess",files)
        #     shutil.copy(files, path)

        print("output_path",self.output_path)
        print("input path",self.path)
        for file in files_output_path:
            print("o/p files",file)
            shutil.copy(self.output_path+file,self.path)
            self.listImportedLog.addItem(file)


    def open_dialog_box(self):
        self.window = QtWidgets.QDialog()
        self.ui = Ui_Error_Label()
        self.ui.setupUi(self.window)
        self.window.show()
  
app= QtWidgets.QApplication(sys.argv)
MainWindow= QtWidgets.QMainWindow()
ui=FirstApp(MainWindow)
MainWindow.show()
app.exec_()