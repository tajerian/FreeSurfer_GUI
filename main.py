
# Python program to create a basic form
# GUI application using the customtkinter module
import customtkinter as ctk
import tkinter as tk
from subprocess import Popen, PIPE
import os
import pandas as pd
import numpy as np
import tkinter.messagebox as tkmb
import customtkinter
from PIL import ImageTk, Image
import sys
import subprocess
from ast import literal_eval

path = os.path.realpath(__file__).split('/')[:-1]
path = ''.join([i+'/' for i in path])[:-1]
os.environ['FREESURFER_GUI']= path
path = os.environ['FREESURFER_GUI']
try:
    ENV = pd.read_csv(path+'/temp/ENV.txt',sep='\t')
    for i in range(1,4):
        os.environ[list(ENV)[i]] = ENV.iloc[0,i]
        print(list(ENV)[i],ENV.iloc[0,i])
except:
    try:
        sd =  os.environ['SUBJECTS_DIR']
    except:
        sd = path+'/freesurfer/subjects'
    try:
        fsh =  os.environ["FREESURFER_HOME"]
    except:
        fsh = path+'/freesurfer'
    try:
        fash =  os.environ['FASTSURFER_HOME']
    except:
        fash = path+'/fastsurfer'
    ENV = pd.DataFrame(np.array([path, sd,fsh,fash]).reshape(1,-1),
                columns=['FREESURFER_GUI','SUBJECTS_DIR', "FREESURFER_HOME", 'FASTSURFER_HOME']
                )
    ENV.to_csv(path+'/temp/ENV.txt',sep='\t',index=False)
    for i in range(1,4):
        os.environ[list(ENV)[i]] = ENV.iloc[0,i]
        print(list(ENV)[i],ENV.iloc[0,i])
class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
    
        self.title("FreeSurfer")
        self.geometry("900x900")

        # set grid layout 1x2
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # load images with light and dark mode image
        FSGUI = os.environ['FREESURFER_GUI']
        self.logo_image = customtkinter.CTkImage(Image.open(FSGUI+'/graphics/logo.png'), size=(57, 43))
        # self.large_test_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "large_test_image.png")), size=(500, 150))
        # self.image_icon_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "image_icon_light.png")), size=(20, 20))
        self.home_image = customtkinter.CTkImage(light_image=Image.open(FSGUI+'/graphics/brain1.png'),
                                                 dark_image=Image.open(FSGUI+'/graphics/brain2.png'), size=(40, 40))
        self.chat_image = customtkinter.CTkImage(light_image=Image.open(FSGUI+'/graphics/gad.png'),
                                                 dark_image=Image.open(FSGUI+'/graphics/gal.png'), size=(40, 40))
        self.add_user_image = customtkinter.CTkImage(light_image=Image.open(FSGUI+"/graphics/ROID.png"),
                                                     dark_image=Image.open(FSGUI+"/graphics/ROIL.png"), size=(40, 40))
        self.logitudinal_image = customtkinter.CTkImage(light_image=Image.open(FSGUI+'/graphics/longd.png'),
                                                 dark_image=Image.open(FSGUI+'/graphics/longl.png'), size=(40, 40))
        self.FastSurfer_image = customtkinter.CTkImage(light_image=Image.open(FSGUI+'/graphics/Fastsurfer.png'),
                                                 dark_image=Image.open(FSGUI+'/graphics/Fastsurfer.png'), size=(40, 40))
        self.FreeView_image = customtkinter.CTkImage(light_image=Image.open(FSGUI+'/graphics/freeview.png'),
                                                 dark_image=Image.open(FSGUI+'/graphics/freeview.png'), size=(40, 40))
        self.GEAR_image = customtkinter.CTkImage(light_image=Image.open(FSGUI+'/graphics/gearl.png'),
                                                 dark_image=Image.open(FSGUI+'/graphics/geard.png'), size=(40, 40))
        
        # create navigation frame
        self.navigation_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(8, weight=1)

        self.navigation_frame_label = customtkinter.CTkLabel(self.navigation_frame, text="  FreeSurfer GUI", image=self.logo_image,
                                                             compound="left", font=customtkinter.CTkFont(size=15, weight="bold"))
        self.navigation_frame_label.grid(row=0, column=0, padx=20, pady=20)

        self.home_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Cortical Reconstruction",
                                                   fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                   image=self.home_image, anchor="w", command=self.home_button_event)
        self.home_button.grid(row=1, column=0, sticky="ew")

        self.frame_2_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Group Analysis",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.chat_image, anchor="w", command=self.frame_2_button_event)
        self.frame_2_button.grid(row=2, column=0, sticky="ew")

        self.frame_3_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="ROI Analysis",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.add_user_image, anchor="w", command=self.frame_3_button_event)
        self.frame_3_button.grid(row=3, column=0, sticky="ew")

        self.frame_4_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Longitudinal Analysis",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.logitudinal_image, anchor="w", command=self.frame_4_button_event)
        self.frame_4_button.grid(row=4, column=0, sticky="ew")
        
        self.frame_5_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="FastSurfer (GPU Supported)",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.FastSurfer_image, anchor="w", command=self.frame_5_button_event)
        self.frame_5_button.grid(row=5, column=0, sticky="ew")

        self.frame_6_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Freeview",
                                                      font=customtkinter.CTkFont(size=15),
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.FreeView_image, anchor="w", command=self.frame_6_button_event)
        self.frame_6_button.grid(row=6, column=0, sticky="ew")

        self.frame_7_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Setup and Installation",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.GEAR_image, anchor="w", command=self.frame_7_button_event)
        self.frame_7_button.grid(row=7, column=0, sticky="ew")

        self.appearance_mode_menu = customtkinter.CTkOptionMenu(self.navigation_frame, values=["Light", "Dark", "System"],
                                                                command=self.change_appearance_mode_event)
        self.appearance_mode_menu.grid(row=9, column=0, padx=20, pady=20, sticky="s")
        
        ###################### create home frame ######################

        self.home_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.home_frame.grid_columnconfigure((1,2,3,4), weight=1)
        self.home_frame.grid_columnconfigure(0, weight=0)
        self.home_frame.grid_rowconfigure((0,1,2,3,4,5,6,7), weight=0)
        self.home_frame.grid_rowconfigure((8), weight=1)
        
        self.InputPath =['']
        self.OutputPath = ['']
        self.SubjectLabel = ctk.CTkLabel(self.home_frame, text="Subject Name")
        self.SubjectLabel.grid(row=0, column=0, padx=20, pady=20, sticky="ew")
        # Subject Field
        self.SubjectEntry = ctk.CTkEntry(self.home_frame, 
        placeholder_text="The results are saved in a folder with this name; e.g. subject_01.")
        self.SubjectEntry.grid(row=0, column=1, columnspan=4, padx=20, pady=20, sticky="ew")
        # Input Label
        self.InputLabel = ctk.CTkLabel(self.home_frame, text="Input Image")
        self.InputLabel.grid(row=1, column=0, padx=20, pady=20, sticky="ew")
 
        # Input Entry Field
        self.displayInput = ctk.CTkTextbox(self.home_frame, height=10)
        self.displayInput.grid(row=1, column=2, padx=10,columnspan=3, pady=20, sticky="snew")
        self.displayInput.insert("0.0", 'press open to select a file')
        self.InputButton = ctk.CTkButton(self.home_frame,text="open",command=self.InputText)
        self.InputButton.grid(row=1, column=1, columnspan=1, padx=5, pady=20, sticky="ew")
        # Output Folder Label
        self.OutputLabel = ctk.CTkLabel(self.home_frame, text="Output Folder")
        self.OutputLabel.grid(row=2, column=0, padx=20, pady=20, sticky="ew")
        # Output Button
        self.displayOutput = ctk.CTkTextbox(self.home_frame, height=10)
        self.displayOutput.grid(row=2, column=2, padx=10,columnspan=3, pady=20, sticky="snew")
        self.displayOutput.insert("0.0", 'press open to select a folder')
        self.OutputButton = ctk.CTkButton(self.home_frame, text="open",command=self.outputText)
        self.OutputButton.grid(row=2, column=1, columnspan=1, padx=5, pady=20, sticky="ew")
        # Workflow Label
        self.Workflow = ctk.CTkLabel(self.home_frame, text="Workflow")
        self.Workflow.grid(row=3, column=0, padx=20, pady=10, sticky="ewns")
        # Workflow Radio Buttons
        self.reconall = tk.StringVar(value="Fully Automated")
        self.Automated = ctk.CTkRadioButton(
            self.home_frame, text="Fully Automated", variable=self.reconall,value="Fully Automated")
        self.Automated.grid(row=3, column=1, padx=20, pady=10, sticky="ews")
        self.Manual = ctk.CTkRadioButton(
            self.home_frame, text="Manual Intervention", variable=self.reconall,value="Manual Intervention")
        self.Manual.grid(row=3, column=2, padx=20, pady=10, sticky="ews")
        # Manual Intervention Steps
        self.StepsLabel = ctk.CTkLabel(self.home_frame,text="Steps")
        self.StepsLabel.grid(row=4, column=0, padx=20, pady=5, sticky="ew")
        
        self.Steps = tk.StringVar(value="None")
        self.autorecon1 = ctk.CTkRadioButton(
            self.home_frame, text="autorecon1", variable=self.Steps,value="-autorecon1")
        self.autorecon1.grid(row=4, column=1, padx=20, pady=0, sticky="ew")

        self.autorecon2 = ctk.CTkRadioButton(
            self.home_frame, text="autorecon2", variable=self.Steps,value="-autorecon2")
        self.autorecon2.grid(row=4, column=2, padx=20, pady=0, sticky="ew")

        self.autorecon2cp = ctk.CTkRadioButton(
            self.home_frame, text="autorecon2-cp", variable=self.Steps,value="-autorecon2-cp")
        self.autorecon2cp.grid(row=5, column=1, padx=20, pady=0, sticky="ew")

        self.autorecon2wm = ctk.CTkRadioButton(
            self.home_frame, text="autorecon2-wm", variable=self.Steps,value="-autorecon2-wm")
        self.autorecon2wm.grid(row=5, column=2, padx=20, pady=0, sticky="ew")

        self.autorecon2pial = ctk.CTkRadioButton(
            self.home_frame, text="autorecon2-pial", variable=self.Steps,value="-autorecon2-pial")
        self.autorecon2pial.grid(row=5, column=3, padx=20, pady=0, sticky="ew")

        self.autorecon3 = ctk.CTkRadioButton(
            self.home_frame, text="autorecon3", variable=self.Steps,value="-autorecon3")
        self.autorecon3.grid(row=4, column=3, padx=20, pady=0, sticky="ew")
        # Hemi
        self.HemiLabel = ctk.CTkLabel(self.home_frame,text="hemisphere")
        self.HemiLabel.grid(row=6, column=0, padx=20, pady=10, sticky="ew")
        # Gender Radio Buttons
        self.Hemi = tk.StringVar(value="Both")
 
        self.HemiBoth = ctk.CTkRadioButton(
            self.home_frame, text="Both", variable=self.Hemi,value="Both")
        self.HemiBoth.grid(row=6, column=1, padx=20, pady=10, sticky="ew")
        self.HemiRight = ctk.CTkRadioButton(
            self.home_frame, text="Right",variable=self.Hemi,value="rh")
        self.HemiRight.grid(row=6, column=2, padx=20, pady=10, sticky="ew")
        self.HemiLeft = ctk.CTkRadioButton(
            self.home_frame, text="Left",variable=self.Hemi,value="lh")
        self.HemiLeft.grid(row=6, column=3, padx=20, pady=10, sticky="ew")
 
        # Run Button
        self.RunButton = ctk.CTkButton(self.home_frame,text="Run", command=self.generateResults)
        self.RunButton.grid(row=7, column=0, columnspan=5, padx=20, pady=20, sticky="ew")
 
        # Text Box
        self.displayBox = ctk.CTkTextbox(self.home_frame)
        self.displayBox.grid(row=8, column=0,rowspan=1, columnspan=5, padx=20, pady=20, sticky="nsew")


        ######################## create second frame ######################
        
        self.second_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.second_frame.grid_columnconfigure((1,2,3,4), weight=1)
        self.second_frame.grid_columnconfigure(0, weight=0)
        self.second_frame.grid_rowconfigure((0,1,2,3,4), weight=0)
        self.second_frame.grid_rowconfigure((5), weight=1)
        self.FSGD = customtkinter.CTkFrame(self.second_frame, corner_radius=2)
        self.FSGD.grid(row=0, column=0, columnspan=5, padx=10, pady=10, sticky="snew")
        self.FSGD.grid_columnconfigure((0,1,2,3), weight=1)
        self.FSGD.grid_rowconfigure((0,1), weight=0)
        self.FSGDlabel = ctk.CTkLabel(self.FSGD,text="FSGD Tools")
        self.FSGDlabel.grid(row=0, column=0, columnspan=4, padx=5, pady=0, sticky="ew")
        self.FSGDboton = ctk.CTkButton(self.FSGD,text="FSGD Builder", command=self.fsgd)
        self.FSGDboton.grid(row=1, column=0, columnspan=1, padx=3, pady=5, sticky="ew")
        self.FSGDboton = ctk.CTkButton(self.FSGD,text="Excel to FSGD", command=self.ExceltoFSGD)
        self.FSGDboton.grid(row=1, column=1, columnspan=1, padx=3, pady=5, sticky="ew")
        self.FSGDboton = ctk.CTkButton(self.FSGD,text="Raw Data to FSGD", command=self.Raw2FSGD)
        self.FSGDboton.grid(row=1, column=2, columnspan=1, padx=3, pady=5, sticky="ew")
        self.FSGDboton = ctk.CTkButton(self.FSGD,text="FSGD Validation", command=self.ValFSGD)
        self.FSGDboton.grid(row=1, column=3, columnspan=1, padx=3, pady=5, sticky="ew")

        self.Contrast = customtkinter.CTkFrame(self.second_frame, corner_radius=2)
        self.Contrast.grid(row=1, column=0, columnspan=5, padx=10, pady=10, sticky="snew")
        # self.Contrast.grid_columnconfigure((), weight=0) 
        self.Contrast.grid_columnconfigure((0,1,2,3,4), weight=1)
        self.Contrast.grid_rowconfigure((0,1,2), weight=0)

        self.Contrastlabel = ctk.CTkLabel(self.Contrast,text="Contrast Builder")
        self.Contrastlabel.grid(row=0, column=0, columnspan=5, padx=5, pady=0, sticky="ew")

        
        self.ContrastGLM = customtkinter.CTkFrame(self.Contrast, corner_radius=0, fg_color="transparent")
        self.ContrastGLM.grid(row=1, column=0, columnspan=2, rowspan=2, padx=10, pady=0, sticky="snew")
        self.ContrastGLM.grid_columnconfigure(1, weight=1) 
        self.ContrastGLM.grid_columnconfigure(0, weight=0) 
        self.ContrastGLM.grid_rowconfigure((0,1), weight=1)
        self.ContrastModLabel = ctk.CTkLabel(self.ContrastGLM,text="GLM Mod:")
        self.ContrastModLabel.grid(row=0, column=0, columnspan=1, padx=3, pady=5, sticky="snew")
        self.ContrastMod = ctk.CTkOptionMenu(self.ContrastGLM, values=[ "DODS", "DOSS",],width=90) 
        self.ContrastMod.grid(row=0, column=1, padx=3, pady=5, sticky="snew")
        self.ContrastTestLabel = ctk.CTkLabel(self.ContrastGLM,text="Statistic:")
        self.ContrastTestLabel.grid(row=1, column=0, padx=3, pady=5, sticky="snew")
        self.ContrastTest = ctk.CTkOptionMenu(self.ContrastGLM, values=[ "T-Test", "F-Test",],width=90) 
        self.ContrastTest.grid(row=1, column=1, columnspan=1, padx=3, pady=5, sticky="snew")

        self.ContrastFLC = customtkinter.CTkFrame(self.Contrast, corner_radius=5, 
        border_width= 1, fg_color="transparent", border_color=("gray40", '#ffffff'),width=10)
        self.ContrastFLC.grid(row=1, column=2, columnspan=2, rowspan=2, padx=3, pady=3, sticky="snew")
        self.ContrastFLC.grid_columnconfigure((0,1,2), weight=1) 
        self.ContrastFLC.grid_rowconfigure((0,1), weight=1)
        self.ContrastFactorLabel = ctk.CTkLabel(self.ContrastFLC,text="Factor",width=60,height=1)
        self.ContrastFactorLabel.grid(row=0, column=0, padx=3, pady=0, sticky="s")
        self.ContrastLevelLabel = ctk.CTkLabel(self.ContrastFLC,text="Level",width=60,height=1)
        self.ContrastLevelLabel.grid(row=0, column=1, padx=3, pady=0, sticky="s")
        self.ContrastCOVLabel = ctk.CTkLabel(self.ContrastFLC,text="Covariate",width=60,height=1)
        self.ContrastCOVLabel.grid(row=0, column=2, padx=3, pady=0, sticky="s")
        self.ContrastFactor = ctk.CTkOptionMenu(self.ContrastFLC, values=[ '1', '2', '3'],width=60) 
        self.ContrastFactor.grid(row=1, column=0, padx=3, pady=0, sticky="n")
        self.ContrastLevel = ctk.CTkOptionMenu(self.ContrastFLC, values=[ '1', '2', '3', '4'],width=60) 
        self.ContrastLevel.grid(row=1, column=1, padx=3, pady=0, sticky="n")
        self.ContrastCOV = ctk.CTkOptionMenu(self.ContrastFLC, values=[ '0', '1', '2', '3', '4'],width=60) 
        self.ContrastCOV.grid(row=1, column=2, padx=3, pady=0, sticky="n")

        self.LoadManually = ctk.CTkButton(self.Contrast,text="Build Manually",
        command=self.contrastmanual,fg_color= '#d03b3b', hover_color='#9f3636')
        self.LoadManually.grid(row=1, column=4, columnspan=1, padx=10, pady=5, sticky="ew")
        self.LoadfromHYP = ctk.CTkButton(self.Contrast,text="Build from Hypothesis",
        command=self.contrasthypo,fg_color= '#d03b3b', hover_color='#9f3636')
        self.LoadfromHYP.grid(row=2, column=4, columnspan=1, padx=10, pady=5, sticky="ew")


        self.Assemble = customtkinter.CTkFrame(self.second_frame, corner_radius=2)
        self.Assemble.grid(row=2, column=0, columnspan=5, padx=10, pady=10, sticky="snew")
        self.Assemble.grid_columnconfigure((0,1,2,3,4), weight=1)
        self.Assemble.grid_rowconfigure((0,1,2,3,4), weight=0)

        self.Assemblelabel = ctk.CTkLabel(self.Assemble,text="Assemble Data (mris_preproc)")
        self.Assemblelabel.grid(row=0, column=0, columnspan=5, padx=5, pady=0, sticky="ew")

        self.AssembleFSGDPath = customtkinter.CTkFrame(self.Assemble, corner_radius=2, fg_color= "transparent")
        self.AssembleFSGDPath.grid(row=1, column=0, columnspan=5, padx=0, pady=5, sticky="snew")
        self.AssembleFSGDPath.grid_columnconfigure((0,1), weight=0)
        self.AssembleFSGDPath.grid_columnconfigure((2,3,4,5), weight=1)
        self.AssembleFSGDPath.grid_rowconfigure(0, weight=0)
        self.displayFSGDPath = ctk.CTkTextbox(self.AssembleFSGDPath, height=10)
        self.displayFSGDPath.grid(row=0, column=2, padx=10,columnspan=4, pady=0, sticky="snew")
        self.displayFSGDPath.insert("0.0", 'press open to select a FSGD file')
        self.FSGDPathButton = ctk.CTkButton(self.AssembleFSGDPath, text="open",command=self.InputFSGD)
        self.FSGDPathButton.grid(row=0, column=1, padx=5, pady=0, sticky="ew")
        self.FSGDPathLabel = ctk.CTkLabel(self.AssembleFSGDPath, text="Input FSGD")
        self.FSGDPathLabel.grid(row=0, column=0, padx=20, pady=0, sticky="ew")
        self.FSGDPathInput = ''

        self.AssembleENVPath = customtkinter.CTkFrame(self.Assemble, corner_radius=2, fg_color= "transparent")
        self.AssembleENVPath.grid(row=2, column=0, columnspan=5, padx=0, pady=5, sticky="snew")
        self.AssembleENVPath.grid_columnconfigure((0,1), weight=0)
        self.AssembleENVPath.grid_columnconfigure((2,3,4,5), weight=1)
        self.AssembleENVPath.grid_rowconfigure(0, weight=0)
        self.displayENVPath = ctk.CTkTextbox(self.AssembleENVPath, height=10)
        self.displayENVPath.grid(row=0, column=2, padx=10,columnspan=4, pady=0, sticky="snew")
        self.displayENVPath.insert("0.0", 'Current Path: '+os.environ['SUBJECTS_DIR'])
        self.ENVPathButton = ctk.CTkButton(self.AssembleENVPath, text="change",command=self.ChangeENV)
        self.ENVPathButton.grid(row=0, column=1, padx=5, pady=0, sticky="ew")
        self.ENVPathLabel = ctk.CTkLabel(self.AssembleENVPath, text="SUBJECTS_DIR")
        self.ENVPathLabel.grid(row=0, column=0, padx=8, pady=0, sticky="w")
        self.ENVPathInput = os.environ['SUBJECTS_DIR']

        self.AssembleOptions = customtkinter.CTkFrame(self.Assemble, corner_radius=2, fg_color= "transparent")
        self.AssembleOptions.grid(row=3, column=0, columnspan=5, padx=0, pady=5, sticky="snew")
        self.AssembleOptions.grid_columnconfigure((0,2,4), weight=0)
        self.AssembleOptions.grid_columnconfigure((1,3,5), weight=1)
        self.AssembleOptions.grid_rowconfigure(0, weight=0)
        self.AssembleHemiLabel = ctk.CTkLabel(self.AssembleOptions,text="Hemisphere:")
        self.AssembleHemiLabel.grid(row=0, column=0, columnspan=1, padx=3, pady=5, sticky="snew")
        self.AssembleHemi = ctk.CTkOptionMenu(self.AssembleOptions, values=[ "left", "right",]) 
        self.AssembleHemi.grid(row=0, column=1, padx=3, pady=5, sticky="snew")
        self.AssembleFWMHLabel = ctk.CTkLabel(self.AssembleOptions, text="Smoothing (FWMH):")
        self.AssembleFWMHLabel.grid(row=0, column=2, padx=3, pady=5, sticky="snew")
        self.AssembleFWMH = ctk.CTkOptionMenu(self.AssembleOptions, values=[ '10mm', '00mm', '05mm', '15mm', '20mm', '25mm']) 
        self.AssembleFWMH.grid(row=0, column=3, columnspan=1, padx=3, pady=5, sticky="snew")
        self.AssembleMeasLabel = ctk.CTkLabel(self.AssembleOptions, text="Meas:")
        self.AssembleMeasLabel.grid(row=0, column=4, padx=3, pady=5, sticky="snew")
        self.AssembleMeas = ctk.CTkOptionMenu(self.AssembleOptions, values=['Volume', 'Thickness']) 
        self.AssembleMeas.grid(row=0, column=5, columnspan=1, padx=3, pady=5, sticky="snew")

        self.AssembleRUN = customtkinter.CTkFrame(self.Assemble, corner_radius=2, fg_color= "transparent")
        self.AssembleRUN.grid(row=4, column=0, columnspan=5, padx=0, pady=5, sticky="snew")
        self.AssembleRUN.grid_columnconfigure((0,1), weight=1)
        self.AssembleRUN.grid_rowconfigure(0, weight=1)
        self.RUNcached = customtkinter.CTkFrame(self.AssembleRUN, corner_radius=2,width=90,
                            border_width= 1, fg_color="transparent", border_color=("gray40", '#ffffff'))
        self.RUNcached.grid(row=0, column=0, padx=10, pady=5, sticky="snew")
        self.RUNcached.grid_columnconfigure((0,1), weight=1)
        self.RUNcached.grid_rowconfigure((0,1), weight=0)
        self.RUNUncached = customtkinter.CTkFrame(self.AssembleRUN, corner_radius=2,
                            border_width= 1, fg_color="transparent", border_color=("gray40", '#ffffff'))
        self.RUNUncached.grid(row=0, column=1, padx=10, pady=5, sticky="snew")
        self.RUNUncached.grid_columnconfigure((0,1), weight=1)
        self.RUNUncached.grid_rowconfigure((0,1), weight=0)
        self.RUNcachedLabel = ctk.CTkLabel(self.RUNcached, text="If Previously Cached", text_color=['#3d62b8',"#5688fc"])
        self.RUNcachedLabel.grid(row=0, column=0, columnspan = 2, padx=20, pady=5, sticky="ew")        
        self.RUNUncachedLabel = ctk.CTkLabel(self.RUNUncached, text="If Uncached", text_color=['#3d62b8',"#5688fc"])
        self.RUNUncachedLabel.grid(row=0, column=0, columnspan = 2, padx=20, pady=5, sticky="ew")
        self.RUNcachedButton = ctk.CTkButton(self.RUNcached, text="RUN",
                                command=self.RunCached, fg_color= '#d03b3b', hover_color='#9f3636')
        self.RUNcachedButton.grid(row=1, column=0, columnspan = 2, padx=40, pady=5, sticky="snew")
        self.RUNUncachedButton = ctk.CTkButton(self.RUNUncached, text="RUN",
                                command=self.RunUncached, fg_color= '#d03b3b', hover_color='#9f3636')
        self.RUNUncachedButton.grid(row=1, column=0, columnspan = 2, padx=40, pady=5, sticky="snew")

        self.GLMAnalysis = customtkinter.CTkFrame(self.second_frame, corner_radius=2)
        self.GLMAnalysis.grid(row=3, column=0, columnspan=5, padx=10, pady=10, sticky="snew")
        self.GLMAnalysis.grid_columnconfigure((0,1,2,3,4), weight=1)
        self.GLMAnalysis.grid_rowconfigure((0,1,2,3,4,5,6), weight=0)

        self.GLMAnalysislabel = ctk.CTkLabel(self.GLMAnalysis,text="GLM Analysis (mri_glmfit)")
        self.GLMAnalysislabel.grid(row=0, column=0, columnspan=5, padx=5, pady=0, sticky="ew")

        self.GLMInputPath = customtkinter.CTkFrame(self.GLMAnalysis, corner_radius=2, fg_color= "transparent")
        self.GLMInputPath.grid(row=1, column=0, columnspan=5, padx=0, pady=5, sticky="snew")
        self.GLMInputPath.grid_columnconfigure((0,1), weight=0)
        self.GLMInputPath.grid_columnconfigure((2,3,4,5), weight=1)
        self.GLMInputPath.grid_rowconfigure(0, weight=0)

        self.displayGLMInputPath = ctk.CTkTextbox(self.GLMInputPath, height=10)
        self.displayGLMInputPath.grid(row=0, column=2, padx=10,columnspan=4, pady=0, sticky="snew")
        self.displayGLMInputPath.insert("0.0", 'press open to select the Assembled Data')
        self.GLMInputButton = ctk.CTkButton(self.GLMInputPath, text="open",command=self.GLMAssembledInput)
        self.GLMInputButton.grid(row=0, column=1, padx=5, pady=0, sticky="ew")
        self.GLMInputLabel = ctk.CTkLabel(self.GLMInputPath, text="Input Images")
        self.GLMInputLabel.grid(row=0, column=0, padx=15, pady=0, sticky="ew")
        self.GLMInput = ''
  
        self.GLMAnalysisFSGDPath = customtkinter.CTkFrame(self.GLMAnalysis, corner_radius=2, fg_color= "transparent")
        self.GLMAnalysisFSGDPath.grid(row=2, column=0, columnspan=5, padx=0, pady=5, sticky="snew")
        self.GLMAnalysisFSGDPath.grid_columnconfigure((0,1), weight=0)
        self.GLMAnalysisFSGDPath.grid_columnconfigure((2,3,4,5), weight=1)
        self.GLMAnalysisFSGDPath.grid_rowconfigure(0, weight=0)      

        self.displayglmFSGDPath = ctk.CTkTextbox(self.GLMAnalysisFSGDPath, height=10)
        self.displayglmFSGDPath.grid(row=0, column=2, padx=10,columnspan=4, pady=0, sticky="snew")
        self.displayglmFSGDPath.insert("0.0", 'press open to select a FSGD file')
        self.glmFSGDPathButton = ctk.CTkButton(self.GLMAnalysisFSGDPath, text="open",command=self.InputFSGD)
        self.glmFSGDPathButton.grid(row=0, column=1, padx=5, pady=0, sticky="ew")
        self.glmFSGDPathLabel = ctk.CTkLabel(self.GLMAnalysisFSGDPath, text="Input FSGD")
        self.glmFSGDPathLabel.grid(row=0, column=0, padx=20, pady=0, sticky="ew")

        self.GLMAnalContrastPath = customtkinter.CTkFrame(self.GLMAnalysis, corner_radius=2, fg_color= "transparent")
        self.GLMAnalContrastPath.grid(row=3, column=0, columnspan=5, padx=0, pady=5, sticky="snew")
        self.GLMAnalContrastPath.grid_columnconfigure((0,1), weight=0)
        self.GLMAnalContrastPath.grid_columnconfigure((2,3,4,5), weight=1)
        self.GLMAnalContrastPath.grid_rowconfigure(0, weight=0)

        self.displayContrastPath = ctk.CTkTextbox(self.GLMAnalContrastPath, height=10)
        self.displayContrastPath.grid(row=0, column=2, padx=10,columnspan=4, pady=0, sticky="snew")
        self.displayContrastPath.insert("0.0", 'press open to select a Contrast file')
        self.GLMAnalContrastButton = ctk.CTkButton(self.GLMAnalContrastPath, text="open",command=self.InputContrast)
        self.GLMAnalContrastButton.grid(row=0, column=1, padx=5, pady=0, sticky="ew")
        self.GLMAnalContrastLabel = ctk.CTkLabel(self.GLMAnalContrastPath, text="Input Contrast")
        self.GLMAnalContrastLabel.grid(row=0, column=0, padx=12, pady=0, sticky="ew")
        self.GLMContrastInput = ''

        self.GLMENVPath = customtkinter.CTkFrame(self.GLMAnalysis, corner_radius=2, fg_color= "transparent")
        self.GLMENVPath.grid(row=4, column=0, columnspan=5, padx=0, pady=5, sticky="snew")
        self.GLMENVPath.grid_columnconfigure((0,1), weight=0)
        self.GLMENVPath.grid_columnconfigure((2,3,4,5), weight=1)
        self.GLMENVPath.grid_rowconfigure(0, weight=0)
        self.displayglmENVPath = ctk.CTkTextbox(self.GLMENVPath, height=10)
        self.displayglmENVPath.grid(row=0, column=2, padx=10,columnspan=4, pady=0, sticky="snew")
        self.displayglmENVPath.insert("0.0", 'Current Path: '+os.environ['SUBJECTS_DIR'])
        self.GLMENVPathButton = ctk.CTkButton(self.GLMENVPath, text="change",command=self.ChangeENV)
        self.GLMENVPathButton.grid(row=0, column=1, padx=5, pady=0, sticky="ew")
        self.GLMENVPathLabel = ctk.CTkLabel(self.GLMENVPath, text="SUBJECTS_DIR")
        self.GLMENVPathLabel.grid(row=0, column=0, padx=8, pady=0, sticky="w")

        self.GLMAssembleOptions = customtkinter.CTkFrame(self.GLMAnalysis, corner_radius=2, fg_color= "transparent")
        self.GLMAssembleOptions.grid(row=5, column=0, columnspan=5, padx=0, pady=5, sticky="snew")
        self.GLMAssembleOptions.grid_columnconfigure((0,2), weight=0)
        self.GLMAssembleOptions.grid_columnconfigure((1,3), weight=1)
        self.GLMAssembleOptions.grid_rowconfigure(0, weight=0)
        self.GLMAssembleHemiLabel = ctk.CTkLabel(self.GLMAssembleOptions,text="Hemisphere:")
        self.GLMAssembleHemiLabel.grid(row=0, column=0, columnspan=1, padx=3, pady=5, sticky="snew")
        self.GLMAssembleHemi = ctk.CTkOptionMenu(self.GLMAssembleOptions, values=[ "left", "right",]) 
        self.GLMAssembleHemi.grid(row=0, column=1, padx=3, pady=5, sticky="snew")
        self.GLMAssembleModeLabel = ctk.CTkLabel(self.GLMAssembleOptions, text="Mode")
        self.GLMAssembleModeLabel.grid(row=0, column=2, padx=3, pady=5, sticky="snew")
        self.GLMAssembleMode = ctk.CTkOptionMenu(self.GLMAssembleOptions, values=[ 'DODS','DOSS']) 
        self.GLMAssembleMode.grid(row=0, column=3, columnspan=1, padx=3, pady=5, sticky="snew")

        self.RUNglmButton = ctk.CTkButton(self.GLMAnalysis, text="RUN",
                                command=self.MriGlmfit, fg_color= '#d03b3b', hover_color='#9f3636')
        self.RUNglmButton.grid(row=6, column=0, columnspan = 5, padx=200, pady=5, sticky="snew")

        self.Show = customtkinter.CTkFrame(self.second_frame, corner_radius=2)
        self.Show.grid(row=5, column=0, columnspan=5, padx=10, pady=10, sticky="snew")
        self.Show.grid_columnconfigure((0,1,2,3,4), weight=1)
        self.Show.grid_rowconfigure((0,1,2,3,4), weight=0)

        self.Showlabel = ctk.CTkLabel(self.Show,text="Ilustration")
        self.Showlabel.grid(row=0, column=0, columnspan=5, padx=5, pady=0, sticky="ew")

        ########################  create third frame  ######################## 
        
        self.third_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")

        self.third_frame.grid_columnconfigure((1,2,3,4), weight=1)
        self.third_frame.grid_columnconfigure(0, weight=0)
        self.third_frame.grid_rowconfigure((0,1,2,3,4), weight=0)
        self.third_frame.grid_rowconfigure((5), weight=1)
        self.Settings = customtkinter.CTkFrame(self.third_frame, corner_radius=2)
        self.Settings.grid(row=0, column=0, columnspan=5, padx=10, pady=10, sticky="snew")
        self.Settings.grid_columnconfigure((0,1,2,3), weight=1)
        self.Settings.grid_rowconfigure((0,1), weight=0)
        self.Settingslabel = ctk.CTkLabel(self.Settings,text="Settings")
        self.Settingslabel.grid(row=0, column=0, columnspan=4, padx=5, pady=0, sticky="ew")

        self.SegENVPath = customtkinter.CTkFrame(self.Settings, corner_radius=2, fg_color= "transparent")
        self.SegENVPath.grid(row=1, column=0, columnspan=5, padx=0, pady=5, sticky="snew")
        self.SegENVPath.grid_columnconfigure((0,1), weight=0)
        self.SegENVPath.grid_columnconfigure((2,3,4,5), weight=1)
        self.SegENVPath.grid_rowconfigure(0, weight=0)
        self.displaySegENVPath = ctk.CTkTextbox(self.SegENVPath, height=10)
        self.displaySegENVPath.grid(row=0, column=2, padx=10,columnspan=4, pady=0, sticky="snew")
        self.displaySegENVPath.insert("0.0", 'Current Path: '+os.environ['SUBJECTS_DIR'])
        self.SegENVPathButton = ctk.CTkButton(self.SegENVPath, text="change",command=self.ChangeENV)
        self.SegENVPathButton.grid(row=0, column=1, padx=5, pady=0, sticky="ew")
        self.SegENVPathLabel = ctk.CTkLabel(self.SegENVPath, text="SUBJECTS_DIR")
        self.SegENVPathLabel.grid(row=0, column=0, padx=8, pady=0, sticky="w")

        self.SegSubjectPath = customtkinter.CTkFrame(self.Settings, corner_radius=2, fg_color= "transparent")
        self.SegSubjectPath.grid(row=2, column=0, columnspan=5, padx=0, pady=5, sticky="snew")
        self.SegSubjectPath.grid_columnconfigure((0,1), weight=0)
        self.SegSubjectPath.grid_columnconfigure((2,3,4,5), weight=1)
        self.SegSubjectPath.grid_rowconfigure(0, weight=0)
        self.displaySegSubjectPath = ctk.CTkTextbox(self.SegSubjectPath, height=10)
        self.displaySegSubjectPath.grid(row=0, column=2, padx=10,columnspan=4, pady=0, sticky="snew")
        self.displaySegSubjectPath.insert("0.0", 'Select Subjects from SUBJECTS_DIR' )
        self.SegSubjectPathButton = ctk.CTkButton(self.SegSubjectPath, text="Select",command=self.SelectSubject)
        self.SegSubjectPathButton.grid(row=0, column=1, padx=5, pady=0, sticky="ew")
        self.SegSubjectPathLabel = ctk.CTkLabel(self.SegSubjectPath, text="Subjects ")
        self.SegSubjectPathLabel.grid(row=0, column=0, padx=26, pady=0, sticky="w")
        self.segsub = []
        
        self.outputFrame = customtkinter.CTkFrame(self.Settings, corner_radius=2, fg_color= "transparent")
        self.outputFrame.grid(row=3, column=0, columnspan=5, padx=0, pady=5, sticky="snew")
        self.outputFrame.grid_columnconfigure((0,1), weight=0)
        self.outputFrame.grid_columnconfigure((2,3,4,5), weight=1)
        self.outputFrame.grid_rowconfigure(0, weight=0)
        self.SettingOutputLabel = ctk.CTkLabel(self.outputFrame, text="Output Folder")
        self.SettingOutputLabel.grid(row=0, column=0, padx=14, pady=0, sticky="w")
        self.SettingdisplayOutput = ctk.CTkTextbox(self.outputFrame, height=8)
        self.SettingdisplayOutput.grid(row=0, column=2, padx=10,columnspan=4, pady=0, sticky="snew")
        self.SettingdisplayOutput.insert("0.0", 'press open to select a folder')
        self.SettingOutputButton = ctk.CTkButton(self.outputFrame, text="open",command=self.SegOutput)
        self.SettingOutputButton.grid(row=0, column=1, padx=5, pady=0, sticky="ew")
        self.SettingOutputPath = ''

        self.SettingOPTFrame = customtkinter.CTkFrame(self.Settings, corner_radius=2, fg_color= "transparent")
        self.SettingOPTFrame.grid(row=4, column=0, columnspan=5, padx=0, pady=5, sticky="snew")
        self.SettingOPTFrame.grid_columnconfigure((0,5), weight=0)
        self.SettingOPTFrame.grid_columnconfigure((1,2,3,4,6), weight=1)
        self.SettingOPTFrame.grid_rowconfigure(0, weight=0)
        self.SettingExperimentLabel = ctk.CTkLabel(self.SettingOPTFrame, text="Experiment:")
        self.SettingExperimentLabel.grid(row=0, column=0, padx=5, pady=5, sticky="snew")
        self.SettingExperimentEntry = ctk.CTkEntry(self.SettingOPTFrame,
        placeholder_text="A Tabular file will be created with this name; e.g. Table.xlsx")
        self.SettingExperimentEntry.grid(row=0, column=1, columnspan=4, padx=4, pady=5, sticky="snew")
        self.SettingModeLabel = ctk.CTkLabel(self.SettingOPTFrame, text="Format:")
        self.SettingModeLabel.grid(row=0, column=5, padx=3, pady=5, sticky="snew")
        self.SettingMode = ctk.CTkOptionMenu(self.SettingOPTFrame, values=[ 'Excel','CSV','Text'], width=20) 
        self.SettingMode.grid(row=0, column=6, columnspan=1, padx=3, pady=5, sticky="snew")

        self.Segmentaions = customtkinter.CTkFrame(self.third_frame, corner_radius=2)
        self.Segmentaions.grid(row=1, column=0, columnspan=5, padx=10, pady=10, sticky="snew")
        self.Segmentaions.grid_columnconfigure((0,1,2,3), weight=1)
        self.Segmentaions.grid_rowconfigure((0,1), weight=0)
        self.Segmentaionslabel = ctk.CTkLabel(self.Segmentaions,text="Segmentaions")
        self.Segmentaionslabel.grid(row=0, column=0, columnspan=4, padx=5, pady=0, sticky="ew")

        self.SegCommand = customtkinter.CTkFrame(self.Segmentaions, corner_radius=2, fg_color= "transparent")
        self.SegCommand.grid(row=1, column=0, columnspan=5, padx=0, pady=5, sticky="snew")
        self.SegCommand.grid_columnconfigure(0, weight=0)
        self.SegCommand.grid_columnconfigure((1,2), weight=1)
        self.SegCommand.grid_rowconfigure(0, weight=0)
        self.SegMeasLabel = ctk.CTkLabel(self.SegCommand, text="Meas:")
        self.SegMeasLabel.grid(row=0, column=0, padx=30, pady=5, sticky="snew")
        self.SegMeas = ctk.CTkOptionMenu(self.SegCommand, values=[ 'Volume', 'Intensity'],width=200) 
        self.SegMeas.grid(row=0, column=1, columnspan=1, padx=3, pady=5, sticky="snew")

        self.SegStatButton = ctk.CTkButton(self.SegCommand, text="Create Stats",
                            command=self.CreateSegStats,fg_color= '#d03b3b', hover_color='#9f3636')
        self.SegStatButton.grid(row=0, column=2, columnspan=1, padx=90, pady=0, sticky="snew")

        self.Parcellations = customtkinter.CTkFrame(self.third_frame, corner_radius=2)
        self.Parcellations.grid(row=2, column=0, columnspan=5, padx=10, pady=10, sticky="snew")
        self.Parcellations.grid_columnconfigure((0,1,2,3), weight=1)
        self.Parcellations.grid_rowconfigure((0,1), weight=0)
        self.Parcellationslabel = ctk.CTkLabel(self.Parcellations,text="Parcellations")
        self.Parcellationslabel.grid(row=0, column=0, columnspan=4, padx=5, pady=0, sticky="ew")

        self.ParsCommand = customtkinter.CTkFrame(self.Parcellations, corner_radius=2, fg_color= "transparent")
        self.ParsCommand.grid(row=1, column=0, columnspan=5, padx=0, pady=5, sticky="snew")
        self.ParsCommand.grid_columnconfigure((0,2), weight=0)
        self.ParsCommand.grid_columnconfigure((1,3,4), weight=1)
        self.ParsCommand.grid_rowconfigure(0, weight=0)
        self.ParsMeasLabel = ctk.CTkLabel(self.ParsCommand, text="Meas:")
        self.ParsMeasLabel.grid(row=0, column=0, padx=3, pady=5, sticky="snew")
        self.ParsMeas = ctk.CTkOptionMenu(self.ParsCommand, values=["Thickness", "Volume", "Area", "MeanCurv"]) 
        self.ParsMeas.grid(row=0, column=1, columnspan=1, padx=10, pady=5, sticky="snew")
        self.ParsHemiLabel = ctk.CTkLabel(self.ParsCommand,text="Hemisphere:")
        self.ParsHemiLabel.grid(row=0, column=2, columnspan=1, padx=10, pady=5, sticky="snew")
        self.ParsHemi = ctk.CTkOptionMenu(self.ParsCommand, values=[ "left", "right",]) 
        self.ParsHemi.grid(row=0, column=3, padx=3, pady=5, sticky="snew")

        self.ParsStatButton = ctk.CTkButton(self.ParsCommand, text="Create Stats",
                            command=self.CreateParsStats,fg_color= '#d03b3b', hover_color='#9f3636')
        self.ParsStatButton.grid(row=0, column=4, columnspan=1, padx=10, pady=0, sticky="snew")

        ########################  create forth frame  ########################

        self.forth_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")

        self.forth_frame.grid_columnconfigure((1,2,3,4), weight=1)
        self.forth_frame.grid_columnconfigure(0, weight=0)
        self.forth_frame.grid_rowconfigure((0,1,2,3,4), weight=0)
        self.forth_frame.grid_rowconfigure((5), weight=1)

        self.BASE = customtkinter.CTkFrame(self.forth_frame, corner_radius=2)
        self.BASE.grid(row=0, column=0, columnspan=5, padx=10, pady=10, sticky="snew")
        self.BASE.grid_columnconfigure((0,1,2,3), weight=1)
        self.BASE.grid_rowconfigure((0,1), weight=0)
        self.BASElabel = ctk.CTkLabel(self.BASE,text="Creating BASE from previously reconstructed CROSSes")
        self.BASElabel.grid(row=0, column=0, columnspan=4, padx=5, pady=0, sticky="ew")

        self.BASEENVPath = customtkinter.CTkFrame(self.BASE, corner_radius=2, fg_color= "transparent")
        self.BASEENVPath.grid(row=1, column=0, columnspan=5, padx=0, pady=5, sticky="snew")
        self.BASEENVPath.grid_columnconfigure((0,1), weight=0)
        self.BASEENVPath.grid_columnconfigure((2,3,4,5), weight=1)
        self.BASEENVPath.grid_rowconfigure(0, weight=0)
        self.displayBASEENVPath = ctk.CTkTextbox(self.BASEENVPath, height=10)
        self.displayBASEENVPath.grid(row=0, column=2, padx=10,columnspan=4, pady=0, sticky="snew")
        self.displayBASEENVPath.insert("0.0", 'Current Path: '+os.environ['SUBJECTS_DIR'])
        self.BASEENVPathButton = ctk.CTkButton(self.BASEENVPath, text="change",command=self.ChangeENV)
        self.BASEENVPathButton.grid(row=0, column=1, padx=5, pady=0, sticky="ew")
        self.BASEENVPathLabel = ctk.CTkLabel(self.BASEENVPath, text="SUBJECTS_DIR")
        self.BASEENVPathLabel.grid(row=0, column=0, padx=8, pady=0, sticky="w")

        self.BASESubjectPath = customtkinter.CTkFrame(self.BASE, corner_radius=2, fg_color= "transparent")
        self.BASESubjectPath.grid(row=2, column=0, columnspan=5, padx=0, pady=5, sticky="snew")
        self.BASESubjectPath.grid_columnconfigure((0,1), weight=0)
        self.BASESubjectPath.grid_columnconfigure((2,3,4,5), weight=1)
        self.BASESubjectPath.grid_rowconfigure(0, weight=0)
        self.displayBASESubjectPath = ctk.CTkTextbox(self.BASESubjectPath, height=10)
        self.displayBASESubjectPath.grid(row=0, column=2, padx=10,columnspan=4, pady=0, sticky="snew")
        self.displayBASESubjectPath.insert("0.0", 'Select Subjects from SUBJECTS_DIR' )
        self.BASESubjectPathButton = ctk.CTkButton(self.BASESubjectPath, text="Select",command=self.SelectBASESubject)
        self.BASESubjectPathButton.grid(row=0, column=1, padx=5, pady=0, sticky="ew")
        self.BASESubjectPathLabel = ctk.CTkLabel(self.BASESubjectPath, text="Subjects ")
        self.BASESubjectPathLabel.grid(row=0, column=0, padx=26, pady=0, sticky="w")
        self.BASEsub = []
        
        self.BASEOPTFrame = customtkinter.CTkFrame(self.BASE, corner_radius=2, fg_color= "transparent")
        self.BASEOPTFrame.grid(row=3, column=0, columnspan=5, padx=0, pady=5, sticky="snew")
        self.BASEOPTFrame.grid_columnconfigure((0,5), weight=0)
        self.BASEOPTFrame.grid_columnconfigure((1,2,3,4,6), weight=1)
        self.BASEOPTFrame.grid_rowconfigure(0, weight=0)
        self.BASEExperimentLabel = ctk.CTkLabel(self.BASEOPTFrame, text="BASE Name:")
        self.BASEExperimentLabel.grid(row=0, column=0, padx=5, pady=5, sticky="snew")
        self.BASEExperimentEntry = ctk.CTkEntry(self.BASEOPTFrame,
        placeholder_text="A BASE template will be created in SUBJECTS_DIR with this name")
        self.BASEExperimentEntry.grid(row=0, column=1, columnspan=6, padx=4, pady=5, sticky="snew")

        self.BASERUNButton = ctk.CTkButton(self.BASE, text="Run",
                            command=self.FSBASE,fg_color= '#d03b3b', hover_color='#9f3636')
        self.BASERUNButton.grid(row=4, column=0, columnspan=4, padx=200, pady=10, sticky="snew")

        self.LONG = customtkinter.CTkFrame(self.forth_frame, corner_radius=2)
        self.LONG.grid(row=1, column=0, columnspan=5, padx=10, pady=10, sticky="snew")
        self.LONG.grid_columnconfigure((0,1,2,3), weight=1)
        self.LONG.grid_rowconfigure((0,1), weight=0)
        self.LONGlabel = ctk.CTkLabel(self.LONG,text="Creating subject's LONG from BASE template")
        self.LONGlabel.grid(row=0, column=0, columnspan=4, padx=5, pady=0, sticky="ew")

        self.BASEPath = customtkinter.CTkFrame(self.LONG, corner_radius=2, fg_color= "transparent")
        self.BASEPath.grid(row=1, column=0, columnspan=5, padx=0, pady=5, sticky="snew")
        self.BASEPath.grid_columnconfigure((0,1), weight=0)
        self.BASEPath.grid_columnconfigure((2,3,4,5), weight=1)
        self.BASEPath.grid_rowconfigure(0, weight=0)
        self.displayBASEPath = ctk.CTkTextbox(self.BASEPath, height=10)
        self.displayBASEPath.grid(row=0, column=2, padx=10,columnspan=4, pady=0, sticky="snew")
        self.displayBASEPath.insert("0.0", 'Select BASE from SUBJECTS_DIR' )
        self.BASEPathButton = ctk.CTkButton(self.BASEPath, text="Select",command=self.SelectLONGBASESubject)
        self.BASEPathButton.grid(row=0, column=1, padx=5, pady=0, sticky="ew")
        self.BASEPathLabel = ctk.CTkLabel(self.BASEPath, text="BASE ")
        self.BASEPathLabel.grid(row=0, column=0, padx=26, pady=0, sticky="w")
        self.BASETemp = ''

        self.LONGSubjectPath = customtkinter.CTkFrame(self.LONG, corner_radius=2, fg_color= "transparent")
        self.LONGSubjectPath.grid(row=2, column=0, columnspan=5, padx=0, pady=5, sticky="snew")
        self.LONGSubjectPath.grid_columnconfigure((0,1), weight=0)
        self.LONGSubjectPath.grid_columnconfigure((2,3,4,5), weight=1)
        self.LONGSubjectPath.grid_rowconfigure(0, weight=0)
        self.displayLONGSubjectPath = ctk.CTkTextbox(self.LONGSubjectPath, height=10)
        self.displayLONGSubjectPath.grid(row=0, column=2, padx=10,columnspan=4, pady=0, sticky="snew")
        self.displayLONGSubjectPath.insert("0.0", 'Select a Subject from SUBJECTS_DIR to create LONG' )
        self.LONGSubjectPathButton = ctk.CTkButton(self.LONGSubjectPath, text="Select",command=self.SelectLONGSubject)
        self.LONGSubjectPathButton.grid(row=0, column=1, padx=5, pady=0, sticky="ew")
        self.LONGSubjectPathLabel = ctk.CTkLabel(self.LONGSubjectPath, text="Subject")
        self.LONGSubjectPathLabel.grid(row=0, column=0, padx=22, pady=0, sticky="w")
        self.LONGsub = ''
        
        self.LONGRUNButton = ctk.CTkButton(self.LONG, text="Run",
                            command=self.FSLONG,fg_color= '#d03b3b', hover_color='#9f3636')
        self.LONGRUNButton.grid(row=3, column=0, columnspan=4, padx=200, pady=10, sticky="snew")

        ########################  create fifth frame  ########################

        self.fifth_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")

        self.fifth_frame.grid_columnconfigure((1,2,3,4), weight=1)
        self.fifth_frame.grid_columnconfigure(0, weight=0)
        self.fifth_frame.grid_rowconfigure((0,1,2,3,4), weight=0)
        self.fifth_frame.grid_rowconfigure((5), weight=1)
        self.Fastinput = customtkinter.CTkFrame(self.fifth_frame, corner_radius=2)
        self.Fastinput.grid(row=0, column=0, columnspan=5, padx=10, pady=10, sticky="snew")
        self.Fastinput.grid_columnconfigure((0,1,2,3), weight=1)
        self.Fastinput.grid_rowconfigure((0,1,2,3), weight=0)
        self.Fastinputlabel = ctk.CTkLabel(self.Fastinput,text="FastSurfer recon-all")
        self.Fastinputlabel.grid(row=0, column=0, columnspan=4, padx=5, pady=0, sticky="ew")

        self.FastinputPath = customtkinter.CTkFrame(self.Fastinput, corner_radius=2, fg_color= "transparent")
        self.FastinputPath.grid(row=1, column=0, columnspan=5, padx=0, pady=5, sticky="snew")
        self.FastinputPath.grid_columnconfigure((0,1), weight=0)
        self.FastinputPath.grid_columnconfigure((2,3,4,5), weight=1)
        self.FastinputPath.grid_rowconfigure(0, weight=0)
        self.displayFastinputPath = ctk.CTkTextbox(self.FastinputPath, height=10)
        self.displayFastinputPath.grid(row=0, column=2, padx=10,columnspan=4, pady=0, sticky="snew")
        self.displayFastinputPath.insert("0.0", 'Press open to select an Image')
        self.FastinputPathButton = ctk.CTkButton(self.FastinputPath, text="change",command=self.FastInput)
        self.FastinputPathButton.grid(row=0, column=1, padx=5, pady=0, sticky="ew")
        self.FastinputPathLabel = ctk.CTkLabel(self.FastinputPath, text="Input Image")
        self.FastinputPathLabel.grid(row=0, column=0, padx=16, pady=0, sticky="w")
        self.FastinputImage = ''

        self.FastoutputPath = customtkinter.CTkFrame(self.Fastinput, corner_radius=2, fg_color= "transparent")
        self.FastoutputPath.grid(row=2, column=0, columnspan=5, padx=0, pady=5, sticky="snew")
        self.FastoutputPath.grid_columnconfigure((0,1), weight=0)
        self.FastoutputPath.grid_columnconfigure((2,3,4,5), weight=1)
        self.FastoutputPath.grid_rowconfigure(0, weight=0)
        self.displayFastoutputPath = ctk.CTkTextbox(self.FastoutputPath, height=10)
        self.displayFastoutputPath.grid(row=0, column=2, padx=10,columnspan=4, pady=0, sticky="snew")
        self.displayFastoutputPath.insert("0.0", 'press open to select a folder')
        self.FastoutputPathButton = ctk.CTkButton(self.FastoutputPath, text="change",command=self.FastOutput)
        self.FastoutputPathButton.grid(row=0, column=1, padx=5, pady=0, sticky="ew")
        self.FastinputPathLabel = ctk.CTkLabel(self.FastoutputPath, text="Output Folder")
        self.FastinputPathLabel.grid(row=0, column=0, padx=12, pady=0, sticky="w")
        self.FastoutputFolder = ''

        self.FastSubject = customtkinter.CTkFrame(self.Fastinput, corner_radius=2, fg_color= "transparent")
        self.FastSubject.grid(row=3, column=0, columnspan=5, padx=0, pady=5, sticky="snew")
        self.FastSubject.grid_columnconfigure((0,1), weight=0)
        self.FastSubject.grid_columnconfigure((2,3,4,5), weight=1)
        self.FastSubject.grid_rowconfigure(0, weight=0)
        self.FastSubjectLabel = ctk.CTkLabel(self.FastSubject, text="Subject Name")
        self.FastSubjectLabel.grid(row=0, column=0, padx=8, pady=0, sticky="w")
        self.FastSubjectEntry = ctk.CTkEntry(self.FastSubject, 
        placeholder_text="The results are saved in a folder with this name; e.g. subject_01")
        self.FastSubjectEntry.grid(row=0, column=1, padx=10,columnspan=5, pady=0, sticky="snew")
        
        self.FastSurferButton = ctk.CTkButton(self.Fastinput, text="Run recon-all Using FastSurfer",
                            command=self.FastSurfer,fg_color= '#d03b3b', hover_color='#9f3636')
        self.FastSurferButton.grid(row=4, column=0, columnspan=4, padx=200, pady=10, sticky="snew")

        ########################  create seventh frame  ########################

        self.seventh_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.seventh_frame.grid_columnconfigure((1,2,3,4), weight=1)
        self.seventh_frame.grid_columnconfigure(0, weight=0)
        self.seventh_frame.grid_rowconfigure((0,1,2,3,4), weight=0)
        self.seventh_frame.grid_rowconfigure((5), weight=1)

        self.FreeSinput = customtkinter.CTkFrame(self.seventh_frame, corner_radius=2)
        self.FreeSinput.grid(row=0, column=0, columnspan=5, padx=10, pady=10, sticky="snew")
        self.FreeSinput.grid_columnconfigure((0,1,2,3), weight=1)
        self.FreeSinput.grid_rowconfigure((0,1,2,3), weight=0)
        self.FreeSinputlabel = ctk.CTkLabel(self.FreeSinput,text="FreeSurfer Instalation")
        self.FreeSinputlabel.grid(row=0, column=0, columnspan=4, padx=5, pady=0, sticky="ew")

        with open('/etc/os-release', 'r') as f:
            x = []
            for i in f:
                x.append([i.split("=")[0],i.split("=")[1][1:-2]])
        x = dict(x)
        NAME = x['NAME']
        VERSION = x['VERSION']
        
        self.LINUX = customtkinter.CTkFrame(self.FreeSinput, corner_radius=2, fg_color= "transparent")
        self.LINUX.grid(row=1, column=0, columnspan=5, padx=0, pady=5, sticky="snew")
        self.LINUX.grid_columnconfigure((0,1), weight=0)
        self.LINUX.grid_columnconfigure((2,3,4,5), weight=1)
        self.LINUX.grid_rowconfigure(0, weight=0)
        self.LINUXLabel = ctk.CTkLabel(self.LINUX, text="Linux: ")
        self.LINUXLabel.grid(row=0, column=0, padx=16, pady=0, sticky="w")
        self.LINUXLabel = ctk.CTkLabel(self.LINUX, text=NAME+":  "+VERSION,
                                text_color= '#c41d1d', font=customtkinter.CTkFont(weight="bold"))
        self.LINUXLabel.grid(row=0, column=1,columnspan=3, padx=16, pady=0, sticky="w")

        if NAME.lower() == 'ubuntu':
            if int(x['VERSION'][:2]) == 18:
                self.self.link = 'https://surfer.nmr.mgh.harvard.edu/pub/dist/freesurfer/7.4.0/freesurfer-linux-ubuntu18_amd64-7.4.0.tar.gz'
                self.file = 'freesurfer-linux-ubuntu18_amd64-7.4.0.tar.gz'
            elif int(x['VERSION'][:2]) == 20:
                self.link ='https://surfer.nmr.mgh.harvard.edu/pub/dist/freesurfer/7.4.0/freesurfer-linux-ubuntu20_amd64-7.4.0.tar.gz'
                self. file = 'freesurfer-linux-ubuntu20_amd64-7.4.0.tar.gz'
            elif int(x['VERSION'][:2]) == 22:
                self.link = 'https://surfer.nmr.mgh.harvard.edu/pub/dist/freesurfer/7.4.0/freesurfer-linux-ubuntu22_amd64-7.4.0.tar.gz'
                self.file = 'freesurfer-linux-ubuntu22_amd64-7.4.0.tar.gz'
            else: 
                self.link = "Couldn't Find"
                self.file = "Couldn't Find"
        else:
            self.link = "Couldn't Find"
            self.file = "Couldn't Find"
        self.FSDOWN = customtkinter.CTkFrame(self.FreeSinput, corner_radius=2, fg_color= "transparent")
        self.FSDOWN.grid(row=2, column=0, columnspan=5, padx=0, pady=5, sticky="snew")
        self.FSDOWN.grid_columnconfigure((0,1), weight=0)
        self.FSDOWN.grid_columnconfigure((2,3,4,5), weight=1)
        self.FSDOWN.grid_rowconfigure(0, weight=0)
        self.FSDOWNLabel = ctk.CTkLabel(self.FSDOWN, text="Suitable FreeSurfer Version:")
        self.FSDOWNLabel.grid(row=0, column=0, padx=16, pady=0, sticky="w")
        self.FSDOWNLabel = ctk.CTkLabel(self.FSDOWN, text=self.file,
                                    text_color= '#c41d1d', font=customtkinter.CTkFont(weight="bold"))
        self.FSDOWNLabel.grid(row=0, column=1,columnspan=3, padx=16, pady=0, sticky="w")

        self.FreeInputIPath = customtkinter.CTkFrame(self.FreeSinput, corner_radius=2, fg_color= "transparent")
        self.FreeInputIPath.grid(row=3, column=0, columnspan=5, padx=0, pady=5, sticky="snew")
        self.FreeInputIPath.grid_columnconfigure((0,1), weight=0)
        self.FreeInputIPath.grid_columnconfigure((2,3,4,5), weight=1)
        self.FreeInputIPath.grid_rowconfigure(0, weight=0)
        self.displayFreeInputIPath = ctk.CTkTextbox(self.FreeInputIPath, height=10)
        self.displayFreeInputIPath.grid(row=0, column=2, padx=10,columnspan=4, pady=0, sticky="snew")
        self.displayFreeInputIPath.insert("0.0", 'Defult: '+ os.environ['FREESURFER_GUI']+'/freesurfer')
        self.FreeInputIPathButton = ctk.CTkButton(self.FreeInputIPath, text="change",command=self.FSINSTPATH)
        self.FreeInputIPathButton.grid(row=0, column=1, padx=5, pady=0, sticky="ew")
        self.FreeInputIPathLabel = ctk.CTkLabel(self.FreeInputIPath, text="Installation Path:")
        self.FreeInputIPathLabel.grid(row=0, column=0, padx=16, pady=0, sticky="w")
        self.FreeInputInst = os.environ['FREESURFER_GUI']

        self.FSLicensePath = customtkinter.CTkFrame(self.FreeSinput, corner_radius=2, fg_color= "transparent")
        self.FSLicensePath.grid(row=4, column=0, columnspan=5, padx=0, pady=5, sticky="snew")
        self.FSLicensePath.grid_columnconfigure((0,1), weight=0)
        self.FSLicensePath.grid_columnconfigure((2,3,4,5), weight=1)
        self.FSLicensePath.grid_rowconfigure(0, weight=0)
        self.displayFSLicensePath = ctk.CTkTextbox(self.FSLicensePath, height=10)
        self.displayFSLicensePath.grid(row=0, column=2, padx=10,columnspan=4, pady=0, sticky="snew")
        self.displayFSLicensePath.insert("0.0", 'Path to license.txt')
        self.FSLicensePathButton = ctk.CTkButton(self.FSLicensePath, text="open",command=self.FSLICENSE)
        self.FSLicensePathButton.grid(row=0, column=1, padx=5, pady=0, sticky="ew")
        self.FSLicensePathLabel = ctk.CTkLabel(self.FSLicensePath, text="License Path:      ")
        self.FSLicensePathLabel.grid(row=0, column=0, padx=16, pady=0, sticky="w")
        self.FSLicense = ''

        self.FreeSINSTButton = ctk.CTkButton(self.FreeSinput, text="Download & Install & Register & Setup Enviroment",
                            command=self.FSINSTALL,fg_color= '#d03b3b', hover_color='#9f3636')
        self.FreeSINSTButton.grid(row=5, column=0, columnspan=4, padx=100, pady=10, sticky="snew")

        self.FastSinput = customtkinter.CTkFrame(self.seventh_frame, corner_radius=2)
        self.FastSinput.grid(row=1, column=0, columnspan=5, padx=10, pady=10, sticky="snew")
        self.FastSinput.grid_columnconfigure((0,1,2,3), weight=1)
        self.FastSinput.grid_rowconfigure((0,1,2,3), weight=0)
        self.FastSinputlabel = ctk.CTkLabel(self.FastSinput,text="FastSurfer Instalation")
        self.FastSinputlabel.grid(row=0, column=0, columnspan=4, padx=5, pady=0, sticky="ew")

        self.FastInputIPath = customtkinter.CTkFrame(self.FastSinput, corner_radius=2, fg_color= "transparent")
        self.FastInputIPath.grid(row=1, column=0, columnspan=5, padx=0, pady=5, sticky="snew")
        self.FastInputIPath.grid_columnconfigure((0,1), weight=0)
        self.FastInputIPath.grid_columnconfigure((2,3,4,5), weight=1)
        self.FastInputIPath.grid_rowconfigure(0, weight=0)
        self.displayFastInputIPath = ctk.CTkTextbox(self.FastInputIPath, height=10)
        self.displayFastInputIPath.grid(row=0, column=2, padx=10,columnspan=4, pady=0, sticky="snew")
        self.displayFastInputIPath.insert("0.0", 'Defult: '+ os.environ['FREESURFER_GUI']+'/fastsurfer')
        self.FastInputIPathButton = ctk.CTkButton(self.FastInputIPath, text="change",command=self.FreeSINSTPATH)
        self.FastInputIPathButton.grid(row=0, column=1, padx=5, pady=0, sticky="ew")
        self.FastInputIPathLabel = ctk.CTkLabel(self.FastInputIPath, text="Installation Path:")
        self.FastInputIPathLabel.grid(row=0, column=0, padx=16, pady=0, sticky="w")
        self.FastInputInst = os.environ['FREESURFER_GUI']

        self.FastSINSTButton = ctk.CTkButton(self.FastSinput, text="Download & Install & Setup Enviroment",
                            command=self.FreeSINSTALL,fg_color= '#d03b3b', hover_color='#9f3636')
        self.FastSINSTButton.grid(row=2, column=0, columnspan=4, padx=100, pady=10, sticky="snew")

        ######################## select default frame ########################
        subdir = os.environ["SUBJECTS_DIR"]
        f'export SUBJECTS_DIR={subdir}\n'      
        
        self.select_frame_by_name("home")

    def SelectLONGBASESubject(self):
        self.displayBASEPath.delete("0.0", "200.0")
        self.BASETemp = ctk.filedialog.askdirectory(title='BASE template',initialdir = os.environ['SUBJECTS_DIR'])
        self.displayBASEPath.insert("0.0", self.BASETemp)
    def SelectLONGSubject(self):
        self.displayLONGSubjectPath.delete("0.0", "200.0")
        self.LONGsub = ctk.filedialog.askdirectory(title='LONG Subject',initialdir = os.environ['SUBJECTS_DIR'])
        self.displayLONGSubjectPath.insert("0.0", self.LONGsub)
    def FreeSINSTALL(self):
        SETUP_DIR = self.FastInputInst
        git_repo_url = 'https://github.com/deep-mi/fastsurfer.git'
        project_name = '/fastsurfer'
        FASTSURFER_HOME = SETUP_DIR + project_name + "/"
        down = f'cd {SETUP_DIR}\ngit clone --branch stable {git_repo_url}\n'
        package = f'pip install -r {FASTSURFER_HOME}/requirements.txt\n'
        command = down+package
        print(command)
        os.system(f"gnome-terminal -e 'bash -c \"{command}; exec bash\"'")
        with open('./.bashrc','a') as f:
            f.write(f'\nexport FASTSURFER_HOME={self.FastInputInst}/fastsurfer')
        df = pd.read_csv(os.environ["FREESURFER_GUI"]+'/temp/ENV.txt',sep='\t')
        df["FASTSURFER_HOME"][0] = f'{self.FastInputInst}/fastsurfer'
        df.to_csv(os.environ["FREESURFER_GUI"]+'/temp/ENV.txt',sep='\t',index=False)
    def FreeSINSTPATH(self):
        self.displayFastInputIPath.delete("0.0", "200.0")
        self.FastInputInst = ctk.filedialog.askdirectory(title='FREESURFER_HOME',initialdir = os.environ['FREESURFER_GUI'])
        self.displayFastInputIPath.insert("0.0", self.ENVPathInput+'/fastsurfer')

    def FSINSTPATH(self):
        self.displayFreeInputIPath.delete("0.0", "200.0")
        self.FastInputInst = ctk.filedialog.askdirectory(title='FREESURFER_HOME',initialdir = os.environ['FREESURFER_GUI'])
        self.displayFreeInputIPath.insert("0.0", self.ENVPathInput+'/freesurfer')
    def FSLICENSE(self):
        self.displayFSLicensePath.delete("0.0", "200.0")
        self.FSLicense = ctk.filedialog.askopenfilename(
                                filetypes = [('FreeSurfer License' ,"license.txt")],
                                title='Input License')
        self.displayFSLicensePath.insert("0.0", self.FSLicense)
    def FSINSTALL(self):
        if self.link == "Couldn't Find":
            tkmb.showerror('ERORR', 'Could not Figure Out The Right version')
        elif self.FSLicense == '':
            tkmb.showerror('ERORR', 'Select your license')
        else:
            down = f'cd {self.FreeInputInst}\nwget {self.link}\n'
            install = f'tar -xzvf {self.FreeInputInst}/{self.file}\n'
            register = f'cp {self.FSLicense} {self.FreeInputInst}/freesurfer/license.txt \n'
            package = 'sudo apt-get install tcsh \n'+\
                        'sudo apt-get install libglu1 \n'+\
                        'sudo apt-get install libxss1 \n'+\
                        'sudo apt-get install language-pack-en \n'+\
                        'sudo apt-get install gettext \n'+\
                        'sudo apt-get install xterm \n'+\
                        'sudo apt-get install x11-apps \n'+\
                        'sudo apt-get install csh \n'+\
                        'sudo apt-get install bc \n'+\
                        'sudo apt-get install libncurses5 \n'+\
                        'sudo apt-get install libjpeg62 \n'+\
                        'sudo apt-get install xorg-dev \n'+\
                        'pip install torchio==0.18.83 \n'+\
                        'pip install yacs==0.1.8 \n'+\
                        'pip -q install pydicom \n'+\
                        'pip -q install dicom2nifti \n'+\
                        'pip install lapy==0.4.1'
            command = down+install+register+package
            print(command)
            os.system(f"gnome-terminal -e 'bash -c \"{command}; exec bash\"'")
            with open('./.bashrc','a') as f:
                f.write(f'\nexport FREESURFER_HOME={self.FreeInputInst}/freesurfer \nsource $FREESURFER_HOME/SetUpFreeSurfer.sh')
            df = pd.read_csv(os.environ["FREESURFER_GUI"]+'/temp/ENV.txt',sep='\t')
            df["FREESURFER_HOME"][0] = f'{self.FreeInputInst}/freesurfer'
            df["SUBJECTS_DIR"][0] = f'{self.FreeInputInst}/freesurfer/subjects'
            df.to_csv(os.environ["FREESURFER_GUI"]+'/temp/ENV.txt',sep='\t',index=False)
    def FSBASE(self):
        if len(self.BASEsub)==0:
            tkmb.showerror('Error', 'Select your Subjects')
        elif self.BASEExperimentEntry.get() == '':
            tkmb.showerror('Error', 'Select BASE Template Name')
        else:
            subjects = ''.join(['-tp'+i+' ' for i in self.BASEsub])
            subdir = os.environ['SUBJECTS_DIR']
            command = f'export SUBJECTS_DIR={subdir}\n' +\
                  f'recon-all -base {self.BASEExperimentEntry.get()} {subjects} -all\n'
            os.system(f"gnome-terminal -e 'bash -c \"{command}; exec bash\"'")
    def FSLONG(self):
        if self.LONGsub == '':
            tkmb.showerror('Error', 'Select your Subject')
        elif self.BASETemp == '':
            tkmb.showerror('Error', 'Select The BASE Template')
        else:
            subject = self.LONGsub.split('/')[-1]
            base = self.BASETemp.split('/')[-1]
            subdir = os.environ['SUBJECTS_DIR']
            command = f'export SUBJECTS_DIR={subdir}\n' +\
                  f'recon-all -long {subject} {base} -all\n'
            os.system(f"gnome-terminal -e 'bash -c \"{command}; exec bash\"'")
    def CreateSegStats(self):
        if len(self.segsub)==0:
            tkmb.showerror('Error', 'Select your Subjects')
        elif self.SettingExperimentEntry.get() == '':
            tkmb.showerror('Error', 'Select Table Name')
        elif self.SettingOutputPath == '': 
            tkmb.showerror('Error', 'Select Output Path')
        else: 
            subdir = os.environ['SUBJECTS_DIR']
            subjects = ''.join([i+' ' for i in self.segsub])
            path = f'cd {self.SettingOutputPath}\n'+f'export SUBJECTS_DIR={subdir}\n'
            mea = self.SegMeas.get().lower() if self.SegMeas.get().lower() == 'volume' else 'mean'
            command = path + f'asegstats2table --subjects  {subjects} --common-segs --meas {mea} --stats aseg.stats --table segstats.txt'
            print(command)
            if 'segstats.txt' in os.listdir(self.SettingOutputPath):
                os.remove(self.SettingOutputPath+'/segstats.txt')
            else:
                pass
            os.system(command)
            if 'segstats.txt' in os.listdir(self.SettingOutputPath):
                try:
                    df = pd.read_csv(self.SettingOutputPath+'/segstats.txt', sep='\t')
                    if self.SettingMode.get() == 'Excel':
                        df.to_excel(self.SettingOutputPath+f'/{self.SettingExperimentEntry.get()}.xlsx', index=False) 
                        os.system(f'xdg-open '+self.SettingOutputPath+f'/{self.SettingExperimentEntry.get()}.xlsx')
                    if self.SettingMode.get() == 'CSV':
                        df.to_csv(self.SettingOutputPath+f'/{self.SettingExperimentEntry.get()}.csv', index=False)
                        os.system(f'xdg-open '+self.SettingOutputPath+f'/{self.SettingExperimentEntry.get()}.csv')
                    if self.SettingMode.get() == 'Text':
                        os.rename(self.SettingOutputPath+'/segstats.txt',
                              self.SettingOutputPath+f'/{self.SettingExperimentEntry.get()}.txt')
                        os.system(f'xdg-open '+self.SettingOutputPath+f'/{self.SettingExperimentEntry.get()}.txt')
                    tkmb.showinfo('Segmentation Extraction', 'Successful')
                    os.remove(self.SettingOutputPath+'/segstats.txt')
                except Exception as e:
                    tkmb.showerror('Error', 'Failed\n'+e)
            else:
                tkmb.showerror('Error', 'Failed')
    def CreateParsStats(self):
        if len(self.segsub)==0:
            tkmb.showerror('Error', 'Select your Subjects')
        elif self.SettingExperimentEntry.get() == '':
            tkmb.showerror('Error', 'Select Table Name')
        elif self.SettingOutputPath == '': 
            tkmb.showerror('Error', 'Select Output Path')
        else: 
            subdir = os.environ['SUBJECTS_DIR']
            subjects = ''.join([i+' ' for i in self.segsub])
            path = f'cd {self.SettingOutputPath}\n'f'export SUBJECTS_DIR={subdir}\n'
            hem = 'lh' if self.ParsHemi.get()=='Left' else 'rh'
            mea = self.ParsMeas.get().lower() 
            command = path + f'aparcstats2table --subjects {subjects} --hemi {hem} --meas {mea} --parc aparc --tablefile segstats.txt'
            print(command)
            if 'segstats.txt' in os.listdir(self.SettingOutputPath):
                os.remove(self.SettingOutputPath+'/segstats.txt')
            else:
                pass
            os.system(command)
            if 'segstats.txt' in os.listdir(self.SettingOutputPath):
                try:
                    df = pd.read_csv(self.SettingOutputPath+'/segstats.txt', sep='\t')
                    if self.SettingMode.get() == 'Excel':
                        df.to_excel(self.SettingOutputPath+f'/{self.SettingExperimentEntry.get()}.xlsx', index=False) 
                        os.system(f'xdg-open '+self.SettingOutputPath+f'/{self.SettingExperimentEntry.get()}.xlsx')
                    if self.SettingMode.get() == 'CSV':
                        df.to_csv(self.SettingOutputPath+f'/{self.SettingExperimentEntry.get()}.csv', index=False)
                        os.system(f'xdg-open '+self.SettingOutputPath+f'/{self.SettingExperimentEntry.get()}.csv')
                    if self.SettingMode.get() == 'Text':
                        os.rename(self.SettingOutputPath+'/segstats.txt',
                              self.SettingOutputPath+f'/{self.SettingExperimentEntry.get()}.txt')
                        os.system(f'xdg-open '+self.SettingOutputPath+f'/{self.SettingExperimentEntry.get()}.txt')
                    tkmb.showinfo('Segmentation Extraction', 'Successful')
                    os.remove(self.SettingOutputPath+'/segstats.txt')
                except Exception as e:
                    tkmb.showerror('Error', 'Failed\n'+e)
            else:
                tkmb.showerror('Error', 'Failed')
    def select_frame_by_name(self, name):
        # set button color for selected button
        self.home_button.configure(fg_color=("gray75", "gray25") if name == "home" else "transparent")
        self.frame_2_button.configure(fg_color=("gray75", "gray25") if name == "frame_2" else "transparent")
        self.frame_3_button.configure(fg_color=("gray75", "gray25") if name == "frame_3" else "transparent")
        self.frame_4_button.configure(fg_color=("gray75", "gray25") if name == "frame_4" else "transparent")
        self.frame_5_button.configure(fg_color=("gray75", "gray25") if name == "frame_5" else "transparent")
        self.frame_7_button.configure(fg_color=("gray75", "gray25") if name == "frame_7" else "transparent")

        # show selected frame
        if name == "home":
            self.home_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.home_frame.grid_forget()
        if name == "frame_2":
            self.second_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.second_frame.grid_forget()
        if name == "frame_3":
            self.third_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.third_frame.grid_forget()
        if name == "frame_4":
            self.forth_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.forth_frame.grid_forget()
        if name == "frame_5":
            self.fifth_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.fifth_frame.grid_forget()
        if name == "frame_7":
            self.seventh_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.seventh_frame.grid_forget()
    def InputText(self):
        self.displayInput.delete("0.0", "200.0")
        self.InputPath.pop()
        self.InputPath.append(ctk.filedialog.askopenfilename(title='Input Image',
                                            filetypes = [('MRI NIFTI Image' ,"*.nii"),
                                                        ('MRI ziped NIFTI Image' ,"*.nii.gz"),
                                                        ('MRI FS Image' ,"*.mgz"),
                                                        ('MRI DICOM Image' ,"*.dcm"),
                                                        ],))
        self.displayInput.insert("0.0", self.InputPath[-1])
    def outputText(self):
        self.displayOutput.delete("0.0", "200.0")
        self.OutputPath.pop()
        self.OutputPath.append(ctk.filedialog.askdirectory(title='Output Folder'))
        self.displayOutput.insert("0.0", self.OutputPath[-1])
    def SegOutput(self):
        self.SettingdisplayOutput.delete("0.0", "200.0")
        self.SettingOutputPath = ctk.filedialog.askdirectory(title='Output Folder')
        self.SettingdisplayOutput.insert("0.0", self.SettingOutputPath)
    def generateResults(self):
        self.displayBox.delete("0.0", "200.0")
        if self.reconall.get() == 'Manual Intervention' and self.Steps.get()=='None':
            self.displayBox.insert("0.0", 'Select step')
        if self.SubjectEntry.get()=='':
            self.displayBox.insert("0.0", 'Select a subject\n')
        if self.InputPath[-1]=='':
            self.displayBox.insert("0.0", 'Select the input file\n')
        if self.OutputPath[-1]=='':
            self.displayBox.insert("0.0", 'Select the output folder\n')
        else:
            command = self.createcommand()
            self.displayBox.insert("0.0", command +'\n')
            os.system(f"gnome-terminal -e 'bash -c \"{command}; exec bash\"'")
    def FastInput(self):
        self.displayFastinputPath.delete("0.0", "200.0")
        self.FastinputImage = ctk.filedialog.askopenfilename(title='Input Image',
                                            filetypes = [('MRI NIFTI Image' ,"*.nii"),
                                                        ('MRI ziped NIFTI Image' ,"*.nii.gz"),
                                                        ('MRI FS Image' ,"*.mgz"),
                                                        ],)
        self.displayFastinputPath.insert("0.0", self.FastinputImage)
    def FastOutput(self):
        self.displayFastoutputPath.delete("0.0", "200.0")
        self.FastoutputFolder = ctk.filedialog.askdirectory(title='Output Folder')
        self.displayFastoutputPath.insert("0.0", self.FastoutputFolder) 
    def FastSurfer(self):
        path = self.FastinputImage
        sid = self.FastSubjectEntry.get()
        out = self.FastoutputFolder
        if path =='':
            tkmb.showerror('Error', 'Select a T1 Image')
        elif sid == '':
            tkmb.showerror('Error', 'Select a Subject Name')
        elif out == '':
            tkmb.showerror('Error', 'Select an Output Folder')
        else:  
            command = '$FASTSURFER_HOME/run_fastsurfer.sh '+\
                        f'--t1 {path} --sd {out} --sid {sid} '+\
                        '--seg_only --py python3 --parallel --allow_root\n'+\
                        '$FASTSURFER_HOME/run_fastsurfer.sh '+\
                        f'--t1 {path} --sd /content/seg --sid {sid} '+\
                        '--surf_only --allow_root --parallel --threads 20 --py python3\n'
            print(command)
            os.system(f"gnome-terminal -e 'bash -c \"{command}; exec bash\"'")
    def createcommand(self): 
        # .get() is used to get the value of the checkboxes and entryfields
        if self.reconall.get() == 'Fully Automated':
            recon = '-all'
        if self.reconall.get() == 'Manual Intervention' and self.Steps.get()!='None':
            recon = self.Steps.get()
        if self.Hemi.get() == 'Both':
            hemi = ''
        if self.Hemi.get() != 'Both':
            hemi = ' -hemi '+self.Hemi.get()
        sd = self.OutputPath[-1]
        i = self.InputPath[-1]
        s = self.SubjectEntry.get()

        command = f"recon-all {recon} -i {i} -subject {s} -sd {sd}{hemi} -qcache -3T"
        return command
    
    def home_button_event(self):
        self.select_frame_by_name("home")

    def frame_2_button_event(self):
        self.select_frame_by_name("frame_2")

    def frame_3_button_event(self):
        self.select_frame_by_name("frame_3")

    def frame_4_button_event(self):
        self.select_frame_by_name("frame_4")
    
    def frame_5_button_event(self):
        self.select_frame_by_name("frame_5")

    def frame_6_button_event(self):
        subprocess.Popen('freeview')

    def frame_7_button_event(self):
        self.select_frame_by_name("frame_7")
    
    def change_appearance_mode_event(self, new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)
    def fsgd(self):
        FSGD1().mainloop()
    def ExceltoFSGD(self):
        FSGD3().mainloop()
    def Raw2FSGD(self):
        FSGD4().mainloop()
    def ValFSGD(self):
        FSGD5().mainloop()
    def contrastmanual(self):
        if int(self.ContrastFactor.get())*int(self.ContrastLevel.get()) < 3 and self.ContrastTest.get() == "F-Test":
            tkmb.showerror('Error','for F-test you should have at least 3 groups')
        elif int(self.ContrastFactor.get())*int(self.ContrastLevel.get())*int(self.ContrastCOV.get())==3*4*4:
            qa = tkmb.askyesno('Sanity check','seriously!!! are you nuts?')
            if qa:
                apc = Contrast1()
                apc.mainloop()
            else:
                pass
        else:
            apc = Contrast1()
            apc.mainloop()
    def SelectSubject(self):
        SegSubject().mainloop()
    def SelectBASESubject(self):
        BASESubject().mainloop()
    def contrasthypo(self):
        if int(self.ContrastFactor.get())*int(self.ContrastLevel.get())>3:
            tkmb.showerror('Error', 'too sophisticated model.\nyou can use this feature when you have a maximum of 3 groups')
        else:
            Contrast2().mainloop()
    def InputFSGD(self):
        self.displayFSGDPath.delete("0.0", "200.0")
        self.displayglmFSGDPath.delete("0.0", "200.0")
        self.FSGDPathInput = ctk.filedialog.askopenfilename(
                                filetypes = [('FSGD File' ,"*.fsgd")],
                                title='Input FSGD')
        self.displayFSGDPath.insert("0.0", self.FSGDPathInput)
        self.displayglmFSGDPath.insert("0.0", self.FSGDPathInput)
    def ChangeENV(self):
        self.displayENVPath.delete("0.0", "200.0")
        self.displayglmENVPath.delete("0.0", "200.0")
        self.displaySegENVPath.delete("0.0", "200.0")
        self.displayBASEENVPath.delete("0.0", "200.0")
        self.ENVPathInput = ctk.filedialog.askdirectory(title='SUBJECTS_DIR',initialdir = os.environ['SUBJECTS_DIR'])
        os.environ['SUBJECTS_DIR'] = self.ENVPathInput
        self.displayENVPath.insert("0.0", self.ENVPathInput)
        self.displayglmENVPath.insert("0.0", self.ENVPathInput)
        self.displaySegENVPath.insert("0.0", self.ENVPathInput)
        self.displayBASEENVPath.insert("0.0", self.ENVPathInput)
    def InputContrast(self):
        self.displayContrastPath.delete("0.0", "200.0")
        self.GLMContrastInput = ctk.filedialog.askopenfilename(
                                filetypes = [('Contrast File' ,"*.mtx")],
                                title='Input Contrast')
        self.displayContrastPath.insert("0.0", self.GLMContrastInput)
    def GLMAssembledInput(self):
        self.displayGLMInputPath.delete("0.0", "200.0")
        self.GLMInput = ctk.filedialog.askopenfilename(
                                filetypes = [('FS MGH File' ,"*.mgh")],
                                title='Input Image Data')
        self.displayGLMInputPath.insert("0.0", self.GLMInput)
    def RunUncached(self):
        if self.FSGDPathInput == '':
            tkmb.showerror('Error', 'Select a FSGD file')
        else:
            experiment = self.FSGDPathInput.split('/')[-1].split('.')[0]
            hem = 'lh' if self.AssembleHemi.get()=='Left' else 'rh'
            home = os.environ["FREESURFER_HOME"]
            subdir = os.environ["SUBJECTS_DIR"]
            if os.path.isdir(self.ENVPathInput+'/'+experiment):
                pass
            else:
                os.mkdir(self.ENVPathInput+'/'+experiment)
            with open(os.environ['FREESURFER_GUI']+'/temp/PreprocUncached.sh', 'w') as f:
                f.write(f'cd {self.ENVPathInput}/{experiment}\n')
                f.write(f'export SUBJECTS_DIR={subdir}\n')
                f.write(f'source {home}/SetUpFreeSurfer.sh\n')
                f.write(f'mris_preproc --fsgd {self.FSGDPathInput} '+\
                f'--meas {self.AssembleMeas.get().lower()} '+\
                f'--target fsaverage '+\
                f'--hemi {hem} '+\
                f'--out {hem}.{experiment}.{self.AssembleMeas.get().lower()}.00.mgh\n')      
                f.write(f'mri_surf2surf --hemi {hem} '+\
                f'--s fsaverage '+\
                f'--sval {hem}.{experiment}.{self.AssembleMeas.get().lower()}.00.mgh '+\
                f'--fwhm {self.AssembleFWMH.get()[:-2]} '+\
                f'--cortex '+\
                f'--tval {hem}.{experiment}.{self.AssembleMeas.get().lower()}.{self.AssembleFWMH.get()[:-2]}B.mgh')
            command = f"source {os.environ['FREESURFER_GUI']}/temp/PreprocUncached.sh"
            os.system(f"gnome-terminal -e 'bash -c \"{command}; exec bash\"'")
            self.displayGLMInputPath.delete("0.0", "200.0")
            self.GLMInput = f'{self.ENVPathInput}/{experiment}/'+\
                f'{hem}.{experiment}.{self.AssembleMeas.get().lower()}.{self.AssembleFWMH.get()[:-2]}B.mgh'
            self.displayGLMInputPath.insert("0.0", self.GLMInput)
    def RunCached(self):
        if self.FSGDPathInput == '':
            tkmb.showerror('Error', 'Select a FSGD file')
        else:
            experiment = self.FSGDPathInput.split('/')[-1].split('.')[0]
            hem = 'lh' if self.AssembleHemi.get()=='Left' else 'rh'
            home = os.environ["FREESURFER_HOME"]
            subdir = os.environ["SUBJECTS_DIR"]          
            if os.path.isdir(self.ENVPathInput+'/'+experiment):
                pass
            else:
                os.mkdir(self.ENVPathInput+'/'+experiment)
            with open(os.environ['FREESURFER_GUI']+'/temp/PreprocCached.sh', 'w') as f:
                f.write(f'cd {self.ENVPathInput}/{experiment}\n')
                f.write(f'export SUBJECTS_DIR={subdir}\n')
                f.write(f'source {home}/SetUpFreeSurfer.sh\n')
                f.write(f'mris_preproc --fsgd {self.FSGDPathInput} '+\
                f'--cache-in {self.AssembleMeas.get().lower()}.fwhm{self.AssembleFWMH.get()[:-2]}.fsaverage '+\
                f'--target fsaverage '+\
                f'--hemi {hem} '+\
                f'--out {hem}.{experiment}.{self.AssembleMeas.get().lower()}.{self.AssembleFWMH.get()[:-2]}.mgh')
            command = f"source {os.environ['FREESURFER_GUI']}/temp/PreprocUncached.sh"
            os.system(f"gnome-terminal -e 'bash -c \"{command}; exec bash\"'")
            self.displayGLMInputPath.delete("0.0", "200.0")
            self.GLMInput = f'{self.ENVPathInput}/{experiment}/'+\
                f'{hem}.{experiment}.{self.AssembleMeas.get().lower()}.{self.AssembleFWMH.get()[:-2]}.mgh'
            self.displayGLMInputPath.insert("0.0", self.GLMInput)
    def MriGlmfit(self):
        if self.FSGDPathInput == '':
            tkmb.showerror('Error', 'Select a FSGD file')
        elif self.GLMContrastInput == '':
            tkmb.showerror('Error', 'Select a Contrast file')
        elif self.GLMInput == '':
            tkmb.showerror('Error', 'Select the Assembled Image Data')
        else:
            experiment = self.FSGDPathInput.split('/')[-1].split('.')[0]
            hem = 'lh' if self.GLMAssembleHemi.get()=='Left' else 'rh'
            Mode = self.GLMAssembleMode.get().lower()
            home = os.environ["FREESURFER_HOME"]
            subdir = os.environ["SUBJECTS_DIR"]
            if os.path.isdir(self.ENVPathInput+'/'+experiment):
                pass
            else:
                os.mkdir(self.ENVPathInput+'/'+experiment)
            with open(os.environ['FREESURFER_GUI']+'/temp/MriGlmFit.sh', 'w') as f:
                f.write(f'cd {self.ENVPathInput}/{experiment}\n')
                f.write(f'export SUBJECTS_DIR={subdir}\n')
                f.write(f'source {home}/SetUpFreeSurfer.sh\n')
                f.write(f'mri_glmfit '+\
                f'--y {self.GLMInput} '+\
                f'--fsgd {self.FSGDPathInput} {Mode} '+\
                f'--C {self.GLMContrastInput} '+\
                f'--surf fsaverage {hem} '+\
                f'--cortex '+\
                f'--glmdir {hem}.{experiment}.glmdir')
            command = f"source {os.environ['FREESURFER_GUI']}/temp/MriGlmFit.sh"
            os.system(f"gnome-terminal -e 'bash -c \"{command}; exec bash\"'")

# Python program to create a basic form
# GUI application using the customtkinter module
import customtkinter as ctk
import tkinter as tk
from subprocess import Popen, PIPE
import os
import pandas as pd
import numpy as np
import tkinter.messagebox as tkmb
import customtkinter
from PIL import Image
import sys
import subprocess
from ast import literal_eval

# Sets the appearance of the window
# Supported modes : Light, Dark, System
# "System" sets the appearance mode to
# the appearance mode of the system
# Sets the color of the widgets in the window
# Supported themes : green, dark-blue, blue   
# ctk.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
# ctk.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"
 
# Dimensions of the window
appWidth, appHeight = 450, 190
subj = []
var = []
clas = []
exp = []
out = []

# App Class
class FSGD1(ctk.CTk):
    # The layout of the window will be written
    # in the init function itself
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Sets the title of the window to "App"
        self.title("FSGD Builder")  
        # Sets the dimensions of the window to 600x700
        self.geometry(f"{appWidth}x{appHeight}")   

        self.grid_columnconfigure((1,3), weight=1)
        self.grid_columnconfigure((0,2), weight=0)
        self.grid_rowconfigure((1,2,3,4), weight=1)
        self.grid_rowconfigure(0, weight=0)

        self.OutputLabel = ctk.CTkLabel(self, text="Output:")
        self.OutputLabel.grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.displayOutput = ctk.CTkTextbox(self, height=10)
        self.displayOutput.grid(row=0, column=2, padx=5,columnspan=3, pady=5, sticky="snew")
        self.displayOutput.insert("0.0", 'press open to select a folder')
        self.OutputButton = ctk.CTkButton(self, text="open",command=self.outputText)
        self.OutputButton.grid(row=0, column=1, columnspan=1, padx=10, pady=5, sticky="ew")
        self.OutputPath = ''

        self.ExperimentLabel = ctk.CTkLabel(self, text="Experiment:")
        self.ExperimentLabel.grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.ExperimentEntry = ctk.CTkEntry(self, 
        placeholder_text="A FSGD file will be created with this name; e.g. exp_01.fsgd")
        self.ExperimentEntry.grid(row=1, column=1, columnspan=3, padx=4, pady=5, sticky="ew")

        self.VarLabel = ctk.CTkLabel(self, text="# Variaable: ")
        self.VarLabel.grid(row=2, column=0, padx=0, pady=5, sticky="e")
        self.VarEntry = ctk.CTkEntry(self, 
        placeholder_text="Number of variables")
        self.VarEntry.grid(row=2, column=1, padx=4, pady=5, sticky="ew")

        self.ClassLabel = ctk.CTkLabel(self, text="    # Class: ")
        self.ClassLabel.grid(row=2, column=2, padx=0, pady=5, sticky="e")
        self.ClassEntry = ctk.CTkEntry(self, 
        placeholder_text="Number of Classes")
        self.ClassEntry.grid(row=2, column=3, padx=4, pady=5, sticky="ew")
        
        self.SubjectLabel = ctk.CTkLabel(self, text="# Subjects: ")
        self.SubjectLabel.grid(row=3, column=0, padx=0, pady=5, sticky="e")
        self.SubjectEntry = ctk.CTkEntry(self, 
        placeholder_text="Number of Subjects")
        self.SubjectEntry.grid(row=3, column=1, padx=4, pady=5, sticky="ew")


        
        self.RunButton = ctk.CTkButton(self,text="Insert data", command=self.exit)
        self.RunButton.grid(row=3, column=2, columnspan=2,padx=0, pady=10, sticky="ew")

    def exit(self):
        error = []
        error = error + ['select an experiment name!\n'] if self.ExperimentEntry.get() == '' else error
        try:
            if int(self.VarEntry.get()) >= 0:
                pass
            else:
                error = error + ['variables should be >0!\n']
        except:
            error = error + ['invalid number of variables!\n']
        try:
            if int(self.SubjectEntry.get()) >= 3:
                pass
            else:
                error = error+ ['subjects should be >3!\n']
        except:
            error = error + ['invalid number of subjects!\n']
        try:
            if int(self.ClassEntry.get()) >= 2:
                pass
            else:
                error = error+ ['classes should be >2!\n']
        except:
            error = error + ['invalid number of classes!\n']
        error = error + ['select an output folder!\n'] if self.OutputPath == '' else error
        if len(error)==0:
            subj.append(int(self.SubjectEntry.get()))
            var.append(int(self.VarEntry.get()))
            clas.append(int(self.ClassEntry.get()))
            exp.append(self.ExperimentEntry.get())
            out.append(self.OutputPath)
            FSGD1.destroy(self)
            FSGD2().mainloop()
        else:
            tkmb.showerror("Error", message=''.join(error))
    def outputText(self):
        self.displayOutput.delete("0.0", "200.0")
        self.OutputPath = ''
        self.OutputPath = (ctk.filedialog.askdirectory())
        self.displayOutput.insert("0.0", self.OutputPath)
 
# App Class
class FSGD2(ctk.CTk):
    # The layout of the window will be written
    # in the init function itself
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        v = 2+clas[-1] if var[-1] == 0 else 3+clas[-1]
        self.v = 2+clas[-1] if var[-1] == 0 else 3+clas[-1]
        self.grid_columnconfigure([i+1 for i in range(2+var[-1])], weight=4)
        self.grid_rowconfigure([i for i in range(v+subj[-1])], weight=4)
        self.grid_columnconfigure(0, weight=0)
        # Sets the title of the window to "App"
        self.title("FSGD Builder")  
        # Sets the dimensions of the window to 600x700
        self.geometry(f"{150*(2+var[-1])}x{40*(v+subj[-1])}")

        self.cell0x0 = ctk.CTkLabel(self, text="GroupDescriptorFile 1")
        self.cell0x0.grid(row=0, column=0,padx=5,pady=2, sticky="ew")
        self.cell1x0 = ctk.CTkLabel(self, text=f"Title {exp[-1]}")
        self.cell1x0.grid(row=1, column=0,padx=5,pady=2, sticky="ew")
        for i in range(clas[-1]):
            exec(f'self.cell{2+i}x0 = ctk.CTkFrame(self, corner_radius=0, fg_color="transparent")')
            exec(f'self.cell{2+i}x0.grid(row={2+i}, column=0, sticky="nsew")')
            exec(f'self.cell{2+i}x0.grid_columnconfigure((0,1), weight=1)')
            exec(f'self.cell{2+i}x0.grid_rowconfigure(0, weight=1)')
            exec(f'self.cell{2+i}x0x0 = ctk.CTkLabel(self.cell{2+i}x0, text="Class ")')
            exec(f'self.cell{2+i}x0x0.grid(row=0, column=0, sticky="ew")')
            exec(f'self.cell{2+i}x0x1 = ctk.CTkEntry(self.cell{2+i}x0,width=60)')
            exec(f"self.cell{2+i}x0x1.grid(row=0, column=1, padx=2, pady=2, sticky='snew')")
        if var[-1] != 0:
            exec(f'self.cell{2+clas[-1]}x0 = ctk.CTkLabel(self, text="Variables")')
            exec(f'self.cell{2+clas[-1]}x0.grid(row={2+clas[-1]}, column=0,padx=5,pady=2, sticky="ew")')
            for i in range(var[-1]):
                exec(f'self.cell{2+clas[-1]}x{3+i} = ctk.CTkEntry(self, placeholder_text="Var {i+1}")')
                exec(f'self.cell{2+clas[-1]}x{3+i}.grid(row={2+clas[-1]}, column={3+i},padx=2, pady=2, sticky="snew")')
        for i in range(subj[-1]):
            exec(f'self.cell{v+i}x0 = ctk.CTkLabel(self, text="Input")')
            exec(f'self.cell{v+i}x0.grid(row={v+i}, column=0,padx=2, pady=2, sticky="snew")')
        for i in range(subj[-1]):
            exec(f'self.cell{v+i}x1 = ctk.CTkEntry(self, placeholder_text="subject {i+1}")')
            exec(f'self.cell{v+i}x1.grid(row={v+i}, column=1,padx=2, pady=2,sticky="snew")')
        for i in range(subj[-1]):
            exec(f'self.cell{v+i}x2 = ctk.CTkEntry(self, placeholder_text="Class Name")')
            exec(f'self.cell{v+i}x2.grid(row={v+i}, column=2,padx=2, pady=2, sticky="snew")')
        for i in range(v,subj[-1]+v):
            for j in range(3,var[-1]+3):
                command = f"self.cell{i}x{j} = ctk.CTkEntry(self)\nself.cell{i}x{j}.grid(row={i}, column={j}, padx=2, pady=2, sticky='snew')"
                exec(command)
        self.fsgdresetButton = ctk.CTkButton(self,text="Reset sheet", command=self.fsgdreset)
        self.fsgdresetButton.grid(row=0, column=1+var[-1], columnspan=2,padx=2, pady=2, sticky="snew")
        self.fsgdnewButton = ctk.CTkButton(self,text="New sheet", command=self.fsgdnew)
        self.fsgdnewButton.grid(row=1, column=1+var[-1], columnspan=2,padx=2, pady=2, sticky="snew")
        self.fsgdsaveButton = ctk.CTkButton(self,text="Save Data to file", command=self.fsgdsave)
        self.fsgdsaveButton.grid(row=2, column=1+var[-1], columnspan=2,padx=2, pady=2, sticky="snew")
        self.fsgdsubmitButton = ctk.CTkButton(self,text="Save and Submit", command=self.fsgdsubmit)
        self.fsgdsubmitButton.grid(row=3, column=1+var[-1], columnspan=2,padx=2, pady=2, sticky="snew")
    def fsgdreset(self):
        FSGD2.destroy(self)
        FSGD2().mainloop()
    def fsgdnew(self):
        FSGD2.destroy(self)
        FSGD1().mainloop()
    def datamaker(self):
        subjects = []
        for i in range(subj[-1]):
            exec(f"subjects.append(self.cell{self.v+i}x1.get())")
        subjects = np.array(subjects).reshape(-1,1)
        classes = []
        for i in range(subj[-1]):
            exec(f"classes.append(self.cell{self.v+i}x2.get())")
        classes = np.array(classes).reshape(-1,1)
        data = np.concatenate((subjects, classes), axis = 1)
        vars = []
        for i in range(var[-1]):
            exec(f'var{i+1} = []')
            for j in range(subj[-1]):
                exec(f"var{i+1}.append(self.cell{self.v+j}x{3+i}.get())")
            exec(f'vars.append(np.array(var{i+1}))')
        for v in vars:
            v = np.array(v).reshape(-1,1)
            data = np.concatenate((data, v), axis = 1)
        return data
    def fsgdmaker(self):
        error = ''
        data = self.datamaker()
        empty = data[np.where(data == '')].ravel()
        if len(empty)!= 0:
            error = error+(f'there are {len(empty)} empty cells\n')
        for i in range(var[-1]):
            j=[]
            exec(f'j.append(self.cell{2+clas[-1]}x{3+i}.get())')
            if j[-1]=='':
                error = error+(f'var name {i+1} is empty\n')
        for i in range(clas[-1]):
            j=[]
            exec(f'j.append(self.cell{2+i}x0x1.get())')
            if j[-1]=='':
                error = error+(f'Class name {i+1} is empty\n')
        clasnames = []
        for i in range(clas[-1]):
            exec(f'clasnames.append(self.cell{2+i}x0x1.get())')
        varnames=[]
        for i in range(var[-1]):
            exec(f'varnames.append(self.cell{2+clas[-1]}x{3+i}.get())')
        data = pd.DataFrame(data,columns = ['subjects', 'group']+varnames)
        difclas1 = set(data['group'].value_counts().index) - set(clasnames)
        difclas2 = set(clasnames) - set(data['group'].value_counts().index)
        if len(difclas1)+len(difclas2) != 0:
            error = error+(f'Class inputs not compatible with Class names\n')
        if len(set(clasnames))!= len(clasnames):
            error = error+(f'Class names are repeated\n')
        difsub = len(set(data['subjects'].value_counts().index)) - len(data['subjects'])
        if difsub != 0:
            s = data['subjects'].value_counts().index[0]
            n = data['subjects'].value_counts()[0]
            error = error+(f'Subject {s} is repeated {n} times\n')
        if error == '':
            data['Variables']='Input'
            data= data.iloc[:,[-1]+[i for i in range(len(list(data))-1)]]
            experiment = exp[-1]
            c = clasnames
            v = list(data)
            n = len(c)+3 if varnames != [] else len(c)+2
            data.index=range(n,len(data)+n)
            data = data.reindex(index = range(len(data)+n))
            data.iloc[0,0]= 'GroupDescriptorFile 1'
            data.iloc[1,0]= 'Title '+ experiment
            for i, j  in enumerate(c):
                data.iloc[i+2,0]= 'Class ' + j
            if varnames != []:
                for i in range(len(v)):
                    if i == 1 or i == 2 : 
                        continue
                    else:
                        data.iloc[n-1,i] = v[i]
            return data, experiment
        else:
            tkmb.showerror("Error", message=error)
    def fsgdsave(self):
        data, experiment = self.fsgdmaker()
        fc = out[-1] + '/'+experiment+'.txt'
        fa = fc.split('.txt')[0]+'.fsgd'
        data.to_csv(fc, sep ='\t',index=False, header=False)
        os.system(f"tr '\r' '\n' < {fc} > {fa}")
        os.system(f"rm {fc}")
        tkmb.showinfo("Converting", message= 'Successful')



    def fsgdsubmit(self):
        data, experiment = self.fsgdmaker()
        fc = out[-1] + '/'+experiment+'.txt'
        fa = fc.split('.txt')[0]+'.fsgd'
        data.to_csv(fc, sep ='\t',index=False, header=False)
        os.system(f"tr '\r' '\n' < {fc} > {fa}")
        os.system(f"rm {fc}")
        FSGD2.destroy(self)
        tkmb.showinfo("Converting", message= 'Successful')
        app.FSGDPathInput = fa
        app.displayFSGDPath.delete("0.0", "200.0")
        app.displayFSGDPath.insert("0.0", app.FSGDPathInput)
        app.displayglmFSGDPath.delete("0.0", "200.0")
        app.displayglmFSGDPath.insert("0.0", app.FSGDPathInput)
        


class FSGD3(ctk.CTk):
    # The layout of the window will be written
    # in the init function itself
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Sets the title of the window to "App"
        self.title("Excel to FSGD")  
        # Sets the dimensions of the window to 600x700
        self.geometry(f"{appWidth}x{appHeight}")   

        self.grid_columnconfigure((1,3), weight=1)
        self.grid_columnconfigure((0,2), weight=0)
        self.grid_rowconfigure((2,3), weight=1)
        self.grid_rowconfigure((0,1), weight=0)

        self.OutputLabel = ctk.CTkLabel(self, text="Output Folder:")
        self.OutputLabel.grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.displayOutput = ctk.CTkTextbox(self, height=10)
        self.displayOutput.grid(row=0, column=2, padx=5,columnspan=3, pady=5, sticky="snew")
        self.displayOutput.insert("0.0", 'press open to select a folder')
        self.OutputButton = ctk.CTkButton(self, text="open",command=self.outputText)
        self.OutputButton.grid(row=0, column=1, columnspan=1, padx=10, pady=5, sticky="ew")
        self.OutputPath = ''

        self.InputLabel = ctk.CTkLabel(self, text="Input File:")
        self.InputLabel.grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.displayInput = ctk.CTkTextbox(self, height=10)
        self.displayInput.grid(row=1, column=2, padx=5,columnspan=3, pady=5, sticky="snew")
        self.displayInput.insert("0.0", 'press open to select a file')
        self.InputButton = ctk.CTkButton(self,text="open",command=self.InputText)
        self.InputButton.grid(row=1, column=1, columnspan=1, padx=10, pady=5, sticky="ew")
        self.InputPath = ''

        self.valconvertButton = ctk.CTkButton(self,text="Validate and Convert", command=self.ValidateFSGD)
        self.valconvertButton.grid(row=2, column=0, columnspan=4,padx=10, pady=5, sticky="snew")

        self.novalconvertButton = ctk.CTkButton(self,text="Convert without File Validation", command=self.Excel2FSGD)
        self.novalconvertButton.grid(row=3, column=0, columnspan=4,padx=10, pady=5, sticky="snew")

    def OpenExcel(self):
        error = ''
        fname = self.InputPath.split('/')[-1]
        if self.OutputPath == '':
            error = error + 'please open output folder\n'
        if self.InputPath == '':
            error = error + 'please open input file\n'
        if error != '':
            tkmb.showerror("Error", message= error)
        if error == '':
            try: 
                if self.InputPath.split('/')[-1].split('.')[0] == 'csv':
                    data = pd.read_csv(self.InputPath, dtype=str, header=None)
                else:
                    data = pd.read_excel(self.InputPath, dtype=str, header=None)
                return data, fname 
            except Exception as e:
                error = error + f'could not open {fname}\n{e}\n'
                tkmb.showerror("Error", message= error)
    def Excel2FSGD(self):
        data, experiment = self.OpenExcel()
        try:
            fc = out[-1] + '/'+experiment+'.txt'
            fa = fc.split('.txt')[0]+'.fsgd'
            data.to_csv(fc, sep ='\t',index=False, header=False)
            os.system(f"tr '\r' '\n' < {fc} > {fa}")
            os.system(f"rm {fc}")
            tkmb.showinfo("Converting", message= 'Successful')
        except:
            tkmb.showerror("Converting", message= 'Failed')
    def ValidateFSGD(self):
        data, experiment = self.OpenExcel()
        data = pd.DataFrame(d[data[0].dropna().index,:])
        d = data.to_numpy()
        error = ''
        if len(list(data)) < 3:
            error = error + 'File is corrupted or empty\n'
        else:   
            if 'GroupDescriptorFile ' not in ''.join(d[:,0]):
                error = error + 'could not find File Descriptor tag\n'
            if 'GroupDescriptorFile ' in ''.join(d[:,0]):
                if 'GroupDescriptorFile ' not in d[0,0]:
                    error = error + 'File Descriptor tag is not in the right place\n'
            if 'Title ' not in ''.join(d[:,0]):
                error = error + 'could not find Title tag\n'
            if 'Title ' in ''.join(d[:,0]):
                if 'Title ' in d[1,0]:
                    exp = d[1,0].split('Title ')[-1]
                else:
                    error = error + 'Title tag is not in the right place\n'
            if 'Class ' not in ''.join(d[:,0]):
                error = error + 'could not find Class tag\n'
            if 'Class ' in ''.join(d[:,0]):
                cind = []
                for i, j in enumerate(d[:,0]):
                    if 'Class ' in j:
                        cind.append(i)
                if len(cind) < 2:
                    error = error + 'there are less than 2 class tags\n'
                if cind != list(range(2,2+len(cind))):
                    error = error + 'Class tags are not in the right place\n'
                classes = [i.split('Class ')[-1] for i in d[cind,0]]
                if len(set(classes)) != len(classes):
                    error = error + 'Class tags are repeated\n'
                if set(classes) != set(data[2].dropna()):
                    error = error + 'Class tags are not compatible with Class inputs\n'
            if len(list(data)) == 3:
                vars = []
            if len(list(data)) > 3:
                if 'Variables' not in ''.join(d[:,0]):
                    error = error + 'could not find Variables tag\n'
                    vars = []
                if 'Variables' in ''.join(d[:,0]):
                    if 'Variables' != d[2+len(cind), 0]:
                        error = error + 'Variables tag is not in the right place\n'
                        vars = []
                else:
                    vars = d[2+len(cind), 3-len(d[0]):].tolist()
                    if len(set(vars)) != len(vars):
                        error = error + f'found repeated variable names: {set(vars)}\n'
            if 'Input' not in ''.join(d[:,0]):
                error = error + 'could not find Input tag\n'
            if 'Input' in ''.join(d[:,0]):
                inpind = []
                for i, j in enumerate(d[:,0]):
                    if 'Input' == j:
                        inpind.append(i)
                if len(inpind) < 3:
                    error = error + 'there are less than 3 Input tags\n'
                else:
                    inputs = data.iloc[inpind,:]
                    cl = data.iloc[cind,:]
                    discip = data.iloc[0:2,:]
        if error == '':
            if vars == []:
                fdata = pd.concat((discip,cl,inputs),axis = 0,ignore_index=True)
            else:
                v = data.loc[data[0]=='Variables']
                fdata = pd.concat((discip,cl,v,inputs),axis = 0,ignore_index=True)
            print(fdata)
            print(self.OutputPath)
            fc = self.OutputPath + '/'+experiment+'.txt'
            fa = fc.split('.txt')[0]+'.fsgd'
            fdata.to_csv(fc, sep ='\t',index=False, header=False)
            os.system(f"tr '\r' '\n' < {fc} > {fa}")
            os.system(f"rm {fc}")
            tkmb.showinfo("Converting", message= 'Successful')
        if error != '':
            tkmb.showerror("Converting", message= error)
    def outputText(self):
        self.displayOutput.delete("0.0", "200.0")
        self.OutputPath = ''
        self.OutputPath = (ctk.filedialog.askdirectory(title='Output Folder'))
        self.displayOutput.insert("0.0", self.OutputPath)
    def InputText(self):
        self.displayInput.delete("0.0", "200.0")
        self.InputPath = ''
        self.InputPath = (ctk.filedialog.askopenfilename(
                                filetypes = [("Excel file","*.xlsx"),("Excel file 97-2003","*.xls")
                                             ,("CSV Files","*.csv")],
                                title='Input Image'))
        self.displayInput.insert("0.0", self.InputPath)


class FSGD4(ctk.CTk):
    # The layout of the window will be written
    # in the init function itself
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Sets the title of the window to "App"
        self.title("Raw Data to FSGD")  
        # Sets the dimensions of the window to 600x700
        self.geometry(f"{450}x{240}")   

        self.grid_columnconfigure((1,3), weight=1)
        self.grid_columnconfigure((0,2), weight=0)
        self.grid_rowconfigure(3, weight=1)
        self.grid_rowconfigure((0,1,2,4,5), weight=0)

        self.OutputLabel = ctk.CTkLabel(self, text="Output Folder:")
        self.OutputLabel.grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.displayOutput = ctk.CTkTextbox(self, height=10)
        self.displayOutput.grid(row=0, column=2, padx=5,columnspan=3, pady=5, sticky="snew")
        self.displayOutput.insert("0.0", 'press open to select a folder')
        self.OutputButton = ctk.CTkButton(self, text="open",command=self.outputText)
        self.OutputButton.grid(row=0, column=1, columnspan=1, padx=10, pady=5, sticky="ew")
        self.OutputPath = ''

        self.InputLabel = ctk.CTkLabel(self, text="Input File:")
        self.InputLabel.grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.displayInput = ctk.CTkTextbox(self, height=10)
        self.displayInput.grid(row=1, column=2, padx=5,columnspan=3, pady=5, sticky="snew")
        self.displayInput.insert("0.0", 'press open to select a file')
        self.InputButton = ctk.CTkButton(self,text="open",command=self.InputText)
        self.InputButton.grid(row=1, column=1, columnspan=1, padx=10, pady=5, sticky="ew")
        self.InputPath = ''

        self.ExperimentLabel = ctk.CTkLabel(self, text="Experiment:")
        self.ExperimentLabel.grid(row=2, column=0, padx=5, pady=5, sticky="e")
        self.ExperimentEntry = ctk.CTkEntry(self, 
        placeholder_text="A FSGD file will be created with this name; e.g. exp_1.fsgd")
        self.ExperimentEntry.grid(row=2, column=1, columnspan=3, padx=4, pady=5, sticky="snew")

        self.VariableLabel = ctk.CTkLabel(self, text="Variables:")
        self.VariableLabel.grid(row=3, column=0, padx=5, pady=5, sticky="e")
        self.VariableEntry = ctk.CTkEntry(self, 
        placeholder_text="Variable columns' names; e.g. Var_01, Var_02, Var_03")
        self.VariableEntry.grid(row=3, column=1, columnspan=3, padx=4, pady=5, sticky="snew")


        self.SubjectLabel = ctk.CTkLabel(self, text="Subject:")
        self.SubjectLabel.grid(row=4, column=0, padx=5, pady=5, sticky="e")
        self.SubjectEntry = ctk.CTkEntry(self, 
        placeholder_text="Subject column's name")
        self.SubjectEntry.grid(row=4, column=1, columnspan=1, padx=4, pady=5, sticky="snew")

        self.ClassLabel = ctk.CTkLabel(self, text="Class:")
        self.ClassLabel.grid(row=4, column=2, padx=5, pady=5, sticky="e")
        self.ClassEntry = ctk.CTkEntry(self, 
        placeholder_text="Class column's name")
        self.ClassEntry.grid(row=4, column=3, columnspan=1, padx=4, pady=5, sticky="snew")

        self.novalconvertButton = ctk.CTkButton(self,text="Convert from raw data", command=self.Excel2FSGD)
        self.novalconvertButton.grid(row=5, column=0, columnspan=4,padx=10, pady=5, sticky="snew")

    def OpenExcel(self):
        error = ''
        fname = self.InputPath.split('/')[-1]
        if self.OutputPath == '':
            error = error + 'please open output folder\n'
        if self.InputPath == '':
            error = error + 'please open input file\n'
        if self.ExperimentEntry.get() == '':
            error = error + 'please select experiment name\n'
        if self.SubjectEntry.get() == '':
            error = error + 'please select Subject column\n'
        if self.ClassEntry.get() == '':
            error = error + 'please select class column\n'
        if error != '':
            tkmb.showerror("Error", message= error)
        if error == '':
            try: 
                if self.InputPath.split('/')[-1].split('.')[0] == 'csv':
                    data = pd.read_csv(self.InputPath, dtype=str)
                else:
                    data = pd.read_excel(self.InputPath, dtype=str)
                return data, self.ExperimentEntry.get()
            except Exception as e:
                error = error + f'could not open {fname}\n{e}\n'
                tkmb.showerror("Error", message= error)
    def Excel2FSGD(self):
        error = ''
        data, experiment = self.OpenExcel()
        labels = list(data)
        nvar = []
        if self.VariableEntry.get() != '':
            for i in self.VariableEntry.get().split(','):
                if i == '':
                    continue
                if i[0] == ' ':
                    i = i[1:]
                if i == '':
                    continue
                if i[-1] == ' ':
                    i = i[:-1]
                if i == '':
                    continue
                nvar.append(i)
        if nvar != []:
            if set(nvar+[
                self.SubjectEntry.get(), self.ClassEntry.get()
            ])-set(labels) != {}:
                for i in list(set(nvar)-set(labels)):
                    error = error + f'could not find {i} column'
        if data[self.SubjectEntry.get()].value_counts()[0] != 1:
            error = error + 'there are repeated subjects'
        if error == '':
            data['Variables']='Input'
            ndata = data[['Variables',self.SubjectEntry.get(),self.ClassEntry.get()]+nvar]
            data = ndata.dropna()
            message = ''
            if len(data) != len(ndata):
                message = 'rows with null values were droped\n'
            c = data.value_counts(self.ClassEntry.get()).index.tolist()[::-1]
            v = data.columns.tolist()
            n = len(c)+2 if nvar == [] else len(c)+3
            data.index = range(n,len(data)+n)
            data = data.reindex(index = range(len(data)+n))
            data.iloc[0,0]= 'GroupDescriptorFile 1'
            data.iloc[1,0]= 'Title '+ experiment
            for i, j  in enumerate(c):
                data.iloc[i+2,0]= 'Class ' + j
            if nvar != []:
                for i in range(len(v)):
                    if i == 1 or i == 2 : 
                        continue
                    else:
                        data.iloc[n-1,i] = v[i]
            try:
                fc =  self.OutputPath  + '/'+experiment+'.txt'
                fa = fc.split('.txt')[0]+'.fsgd'
                data.to_csv(fc, sep ='\t',index=False, header=False)
                os.system(f"tr '\r' '\n' < {fc} > {fa}")
                os.system(f"rm {fc}")
                tkmb.showinfo("Converting", message= message + 'Successful')
            except Exception as e:
                tkmb.showerror("Converting", message= e + '\nFailed')
        if error != '':
            tkmb.showerror("Error", message = error)
    def outputText(self):
        self.displayOutput.delete("0.0", "200.0")
        self.OutputPath = ''
        self.OutputPath = (ctk.filedialog.askdirectory(title='Output Folder'))
        self.displayOutput.insert("0.0", self.OutputPath)
    def InputText(self):
        self.displayInput.delete("0.0", "200.0")
        self.InputPath = ''
        self.InputPath = (ctk.filedialog.askopenfilename(
                                filetypes = [("Excel file","*.xlsx"),("Excel file 97-2003","*.xls")
                                             ,("CSV Files","*.csv")],
                                title='Input Image'))
        self.displayInput.insert("0.0", self.InputPath)

class FSGD5(ctk.CTk):
    # The layout of the window will be written
    # in the init function itself
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Sets the title of the window to "App"
        self.title("FSGD Validation")  
        # Sets the dimensions of the window to 600x700
        self.geometry(f"{450}x{120}")   

        self.grid_columnconfigure((1,3), weight=1)
        self.grid_columnconfigure((0,2), weight=0)
        self.grid_rowconfigure((0,1,2), weight=1)

        self.InputLabel = ctk.CTkLabel(self, text="Input File:")
        self.InputLabel.grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.displayInput = ctk.CTkTextbox(self, height=10)
        self.displayInput.grid(row=1, column=2, padx=5,columnspan=3, pady=5, sticky="snew")
        self.displayInput.insert("0.0", 'press open to select a FSGDfile')
        self.InputButton = ctk.CTkButton(self,text="open",command=self.InputText)
        self.InputButton.grid(row=1, column=1, columnspan=1, padx=10, pady=5, sticky="ew")
        self.InputPath = ''

        self.ExperimentLabel = ctk.CTkLabel(self, text="FSGD File Troubleshooter")
        self.ExperimentLabel.grid(row=0, column=0,columnspan=4, padx=5, pady=5, sticky="snew")

        self.novalconvertButton = ctk.CTkButton(self,text="Validate", command=self.FSGDval)
        self.novalconvertButton.grid(row=2, column=0, columnspan=4,padx=10, pady=5, sticky="snew")

    def OpenExcel(self):
        try:
            if self.InputPath.split('.')[-1] == 'fsgd':
                data = pd.read_csv(self.InputPath, dtype=str, sep = '\t', header=None)
                return data
            else:
                tkmb.showerror("Error", message= 'please select a *.fsgd file')
        except Exception as e:
            tkmb.showerror("Error", message= e)
    def FSGDval(self):
        error = ''
        data = self.OpenExcel()
        inputs = data.loc[data[0]=='Input']
        empty = inputs.to_numpy()[np.where(inputs.to_numpy() == np.nan)].ravel()
        if len(inputs[0]) < 3:
            error = error + 'File is corrupted or empty\n'
        else:
            if len(empty)!= 0:
                error = error+(f'there are {len(empty)} empty input cells\n')
            classes = []
            title = ''
            gd = ''
            invalid = []
            var=[]
            for i, j in enumerate(data[0]):
                if 'Input' == j:
                    pass
                elif 'Title ' in j:
                    title = (i,j.split('Title ')[-1])
                elif 'GroupDescriptorFile 1' in j:
                    gd = (i,j)
                elif 'Class ' in j:
                    classes.append((i,j.split('Class ')[-1]))
                elif 'Variables' == j:
                    var = data.iloc[i,:].to_numpy()
                    vari = i 
                else:
                    invalid.append((i,j))
            if title == '':
                error = error + 'could not find Title tag\n'
            else:
                if title[0] != 1:
                   error = error + 'Title tag is not in the right place\n'
                if title[1] == '' or title[1] == ' ':
                   error = error + 'Title tag is empty\n'
            if gd == '':
                error = error + 'could not find File Descriptor tag\n'
            else:
                if gd[0] != 0:
                    error = error + 'Title tag is not in the right place\n'
            if len(classes) == 0:
                error = error + 'could not find any Class tag\n'
            if len(classes) == 1:
                error = error + 'found less than 2 Class tags\n'
            else:
                if [i[0] for i in classes] != list(range(2,2+len(classes))):
                    error = error + 'Class tags are not in the right place\n'
                for i in [i[1] for i in classes]:
                    if i == '' or i == ' ':
                       error = error + 'Class tag is empty\n'
            if vari != 2+len(classes):
                error = error + 'Variables tag is not in the right place\n'
            if len(invalid) != 0:
                error = error + f'found {len(invalid)} invalid tags\n'
            svc = inputs[1].value_counts()
            for i, j in enumerate(svc):
                if j > 1:
                    error = error + f'subject {svc.index[i]} is repeated\n'
            if set([i[1] for i in classes]) != set(inputs[2]):
                error = error + f'Class tags are not compatible with class inputs\n'
            if len(inputs[0]) > 3:
                if len(var) != 0:
                    if np.nan in var[3:]:
                        error = error + 'there are missing variable names'
                    if not np.isnan(var[1]) and not np.isnan(var[2]):
                        error = error + 'variable names are in the wrong place\n'
                    var = var[3:]
                    if len(set(var))!= len(var):
                        error = error + 'there are repeated variable names\n'
                else:
                    error = error + 'could not find Variables tag\n'
        if error == '':
            tkmb.showinfo("Validation", message= 'could not find any problems')
        if error != '':
            tkmb.showerror("Validation", message= error)
    def InputText(self):
        self.displayInput.delete("0.0", "200.0")
        self.InputPath = ''
        self.InputPath = (ctk.filedialog.askopenfilename(
                                filetypes = [('FSGD File' ,"*.fsgd")],
                                title='Input FSGD'))
        self.displayInput.insert("0.0", self.InputPath)

class Contrast1(ctk.CTk):
    # The layout of the window will be written
    # in the init function itself
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        mod = app.ContrastMod.get() 
        test = app.ContrastTest.get() 
        factor = int(app.ContrastFactor.get()) # '1', '2', '3'  Category
        level = int(app.ContrastLevel.get()) # '1', '2', '3', '4'   CLASS
        cov = int(app.ContrastCOV.get()) # '0', '1', '2', '3', '4'
        group = level*factor

        self.mod = mod
        self.test = test
        self.factor = factor
        self.level = level
        self.cov = cov
        self.group = group 
        nregressor = group*(cov+1) if mod=="DODS" else (group + cov)

        self.outputFrame = customtkinter.CTkFrame(self, corner_radius=5)
        self.outputFrame.grid(row=3, column=0,columnspan = cov+1, padx=5, pady=20, sticky="snew")
        self.outputFrame.grid_columnconfigure([i for i in range(5)][2:], weight=1)
        self.outputFrame.grid_columnconfigure((0,1), weight=0)
        self.outputFrame.grid_rowconfigure((0,1,3), weight=1)

        self.OutputLabel = ctk.CTkLabel(self.outputFrame, text="Output:")
        self.OutputLabel.grid(row=1, column=0, padx=5, pady=5, sticky="snew")
        self.displayOutput = ctk.CTkTextbox(self.outputFrame, height=8)
        self.displayOutput.grid(row=1, column=2, padx=5,columnspan=3, pady=5, sticky="snew")
        self.displayOutput.insert("0.0", 'press open to select a folder')
        self.OutputButton = ctk.CTkButton(self.outputFrame, text="open",command=self.outputText)
        self.OutputButton.grid(row=1, column=1, columnspan=1, padx=10, pady=5, sticky="snew")
        self.OutputPath = ''

        self.ExperimentLabel = ctk.CTkLabel(self.outputFrame, text="Experiment:")
        self.ExperimentLabel.grid(row=0, column=0, padx=5, pady=5, sticky="snew")
        self.ExperimentEntry = ctk.CTkEntry(self.outputFrame, 
        placeholder_text="A Contrast file will be created with this name; e.g. exp_01.mtx")
        self.ExperimentEntry.grid(row=0, column=1, columnspan=4, padx=4, pady=5, sticky="snew")

        self.OutputButton = ctk.CTkButton(self.outputFrame, text="Create",\
        command=self.save,height=35,fg_color= '#d03b3b', hover_color='#9f3636')
        self.OutputButton.grid(row=2, column=0, columnspan=5, padx=10, pady=5, sticky="sn")

        self.grid_columnconfigure([i for i in range(cov+1)], weight=1)
        self.grid_rowconfigure((0,1,2,3), weight=0)

        # Sets the title of the window to "App"
        self.title("Contrast Builder")  
        # Sets the dimensions of the window to 600x700
        w = 500 if (nregressor * 68) < 500  else nregressor * 74
        h = group*25 if test == "F-Test" else 0
        self.geometry(f"{w}x{335 + h}")
        a= 0 if group ==1 or factor ==1 else 5
        b= 1 if group == 1 or factor ==1 else 5
        d= 10 if group == 1 or factor ==1 else 3
        if mod == "DODS":
            exec(f'self.GLMModeLabel = customtkinter.CTkLabel(self, corner_radius=5,text= "Different Offset, Different Slope"\
                 ,text_color=["#1a013b","#5688fc"],font=customtkinter.CTkFont(size=15, weight="bold"))')
            exec(f'self.GLMModeLabel.grid(row=0, column=0,columnspan = cov+1, padx=10, pady=5, sticky="snew")')
            for i in range(cov+1):
                if i == 0:
                    g = True
                    exec(f'self.groupFrameLabel = customtkinter.CTkLabel(self, corner_radius=5,text= "Classes",width=60,height=10\
                         ,text_color="#bf1d11",font=customtkinter.CTkFont(size=13, weight="bold"))')
                    exec(f'self.groupFrameLabel.grid(row=1, column=0, padx=10, pady=10, sticky="snew")')
                    exec('self.groupFrame = customtkinter.CTkFrame(self, corner_radius=5,\
                         border_width= 1, fg_color="transparent", border_color=("gray40", "#ffffff"),width=10)')
                    exec(f'self.groupFrame.grid(row=2, column=0, padx=5, pady=0, sticky="snew")')
                    exec('self.groupFrame.grid_columnconfigure([i for i in range(level)], weight=1)') 
                    exec('self.groupFrame.grid_rowconfigure([i for i in range(group+1)], weight=1)')
                else:
                    g = False
                    exec(f'self.var{i}FrameLabel = customtkinter.CTkLabel(self, corner_radius=5,text= "Variable{i}",width=60,height=10\
                         ,text_color="#1174bf",font=customtkinter.CTkFont(size=13, weight="bold"))')
                    exec(f'self.var{i}FrameLabel.grid(row=1, column={i}, padx=10, pady=0, sticky="snew")')
                    exec(f'self.var{i}Frame = customtkinter.CTkFrame(self, corner_radius=5,\
                         border_width= 1, fg_color="transparent", border_color=("gray40", "#ffffff"),width=10)')
                    exec(f'self.var{i}Frame.grid(row=2, column={i}, padx=10, pady=0, sticky="snew")')
                    exec(f'self.var{i}Frame.grid_columnconfigure([i for i in range(group)], weight=1)') 
                    exec(f'self.var{i}Frame.grid_rowconfigure([i for i in range(group)], weight=1)')
                if g:
                    if factor == 1 or level == 1:
                        for j in range(group):
                            exec(f"self.ContrastCellLabel{i}x{j}x0 = ctk.CTkLabel(self.groupFrame,text= 'Group{j+1}',width=60,height=1)")
                            exec(f"self.ContrastCellLabel{i}x{j}x0.grid(row=0, column={j}, padx=3, pady=3, sticky='snew')")
                            exec(f"self.ContrastCell{i}x{j}x0x0 =  ctk.CTkEntry(self.groupFrame, placeholder_text= 'offset', width=60)")
                            exec(f"self.ContrastCell{i}x{j}x0x0.grid(row=1, column={j},padx=3, pady=3, sticky='snew')")
                            if test =="F-Test":
                                for k in range((group-2)):
                                    exec(f"self.ContrastCell{i}x{j}x0x{k+1} =  ctk.CTkEntry(self.groupFrame, placeholder_text= 'offset', width=60)")
                                    exec(f"self.ContrastCell{i}x{j}x0x{k+1}.grid(row={k+2}, column={j},padx=3, pady=3, sticky='snew')") 
                    else:
                        for j in range(level):
                            exec(f'self.Level{i}x{j}FrameLabel = customtkinter.CTkLabel(self.groupFrame, corner_radius=5,text= "Level{j+1}",width=60,height=1)')
                            exec(f'self.Level{i}x{j}FrameLabel.grid(row=0, column={j}, padx=5, pady=5, sticky="snew")')
                            exec(f'self.Level{i}x{j}Frame = customtkinter.CTkFrame(self.groupFrame, corner_radius=5,\
                                border_width= 1, fg_color="transparent", border_color=("gray40", "#ffffff"),width=10)')
                            exec(f'self.Level{i}x{j}Frame.grid(row=1, column={j}, rowspan=2, padx=5, pady=5, sticky="snew")')
                            exec(f'self.Level{i}x{j}Frame.grid_columnconfigure([i for i in range(factor)], weight=1)') 
                            for f in range(factor):
                                exec(f"self.ContrastCellLabel{i}x{j}x{f} = ctk.CTkLabel(self.Level{i}x{j}Frame,text= 'Fac{f+1}',width=60,height=1)")
                                exec(f"self.ContrastCellLabel{i}x{j}x{f}.grid(row=0, column={f}, padx=3, pady=5, sticky='snew')")
                                exec(f"self.ContrastCell{i}x{j}x{f} =  ctk.CTkEntry(self.Level{i}x{j}Frame, placeholder_text= 'offset', width=60)")
                                exec(f"self.ContrastCell{i}x{j}x{f}.grid(row=1, column={f},padx=3, pady=3, sticky='snew')")
                                if test =="F-Test":
                                    for k in range((group-2)):
                                        exec(f"self.ContrastCell{i}x{j}x{f}x{k} =  ctk.CTkEntry(self.Level{i}x{j}Frame, placeholder_text= 'offset', width=60)")
                                        exec(f"self.ContrastCell{i}x{j}x{f}x{k}.grid(row={k+2}, column={f},padx=3, pady=3, sticky='snew')")
                else:
                    if factor == 1 or level == 1:
                        for j in range(group): 
                            exec(f"self.ContrastCellLabel{i}x{j}x0 = ctk.CTkLabel(self.var{i}Frame,text= 'Group{j+1}',width=60,height=1)")
                            exec(f"self.ContrastCellLabel{i}x{j}x0.grid(row=0, column={j}, padx=3, pady=3, sticky='snew')")
                            exec(f"self.ContrastCell{i}x{j}x0x0 =  ctk.CTkEntry(self.var{i}Frame, placeholder_text= 'slope', width=60)")
                            exec(f"self.ContrastCell{i}x{j}x0x0.grid(row=1, column={j},padx=3, pady=3, sticky='snew')")
                            if test =="F-Test":
                                for k in range((group-2)):
                                    exec(f"self.ContrastCell{i}x{j}x0x{k+1} =  ctk.CTkEntry(self.var{i}Frame, placeholder_text= 'slope', width=60)")
                                    exec(f"self.ContrastCell{i}x{j}x0x{k+1}.grid(row={k+2}, column={j},padx=3, pady=3, sticky='snew')")
                    else:
                        for j in range(level):
                            exec(f'self.Level{i}x{j}FrameLabel = customtkinter.CTkLabel(self.var{i}Frame, corner_radius=5,text= "Level{j+1}",width=60,height=1)')
                            exec(f'self.Level{i}x{j}FrameLabel.grid(row=0, column={j}, padx=5, pady=5, sticky="snew")')
                            exec(f'self.Level{i}x{j}Frame = customtkinter.CTkFrame(self.var{i}Frame, corner_radius=5,\
                                border_width= 1, fg_color="transparent", border_color=("gray40", "#ffffff"),width=10)')
                            exec(f'self.Level{i}x{j}Frame.grid(row=1, column={j}, rowspan=2, padx=5, pady=5, sticky="snew")')
                            exec(f'self.Level{i}x{j}Frame.grid_columnconfigure([i for i in range(factor)], weight=1)') 
                            for f in range(factor):
                                exec(f"self.ContrastCellLabel{i}x{j}x{f} = ctk.CTkLabel(self.Level{i}x{j}Frame,text= 'Fac{f+1}',width=60,height=1)")
                                exec(f"self.ContrastCellLabel{i}x{j}x{f}.grid(row=0, column={f}, padx=3, pady=5, sticky='snew')")
                                exec(f"self.ContrastCell{i}x{j}x{f} =  ctk.CTkEntry(self.Level{i}x{j}Frame, placeholder_text= 'slope', width=60)")
                                exec(f"self.ContrastCell{i}x{j}x{f}.grid(row=1, column={f},padx=3, pady=3, sticky='snew')")
                                if test =="F-Test":
                                    for k in range((group-2)):
                                        exec(f"self.ContrastCell{i}x{j}x{f}x{k} =  ctk.CTkEntry(self.Level{i}x{j}Frame, placeholder_text= 'slope', width=60)")
                                        exec(f"self.ContrastCell{i}x{j}x{f}x{k}.grid(row={k+2}, column={f},padx=3, pady=3, sticky='snew')")
        if mod == "DOSS":
            if cov!=0:
                self.grid_columnconfigure([i+1 for i in range(cov)], weight=1)
                self.grid_columnconfigure(0, weight=cov)
            exec(f'self.GLMModeLabel = customtkinter.CTkLabel(self, corner_radius=5,text= "Different Offset, Same Slope"\
                 ,text_color=["#1a013b","#5688fc"],font=customtkinter.CTkFont(size=15, weight="bold"))')
            exec(f'self.GLMModeLabel.grid(row=0, column=0,columnspan = cov+1, padx=10, pady=5, sticky="snew")')
            for i in range(cov+1):
                if i == 0:
                    g = True
                    exec(f'self.groupFrameLabel = customtkinter.CTkLabel(self, corner_radius=5,text= "Classes",width=60,height=10\
                         ,text_color="#bf1d11",font=customtkinter.CTkFont(size=13, weight="bold"))')
                    exec(f'self.groupFrameLabel.grid(row=1, column=0, padx=10, pady=10, sticky="snew")')
                    exec('self.groupFrame = customtkinter.CTkFrame(self, corner_radius=5,\
                         border_width= 1, fg_color="transparent", border_color=("gray40", "#ffffff"),width=10)')
                    exec(f'self.groupFrame.grid(row=2, column=0, padx=5, pady=0, sticky="snew")')
                    exec('self.groupFrame.grid_columnconfigure([i for i in range(level)], weight=1)') 
                    exec('self.groupFrame.grid_rowconfigure([i for i in range(group+1)], weight=1)')
                else:
                    g = False
                    exec(f'self.var{i}FrameLabel = customtkinter.CTkLabel(self, corner_radius=5,text= "Variable{i}",width=60,height=10\
                         ,text_color="#1174bf",font=customtkinter.CTkFont(size=13, weight="bold"))')
                    exec(f'self.var{i}FrameLabel.grid(row=1, column={i}, padx=5, pady=0, sticky="snew")')
                    exec(f'self.var{i}Frame = customtkinter.CTkFrame(self, corner_radius=5,\
                         border_width= 1, fg_color="transparent", border_color=("gray40", "#ffffff"),width=10)')
                    exec(f'self.var{i}Frame.grid(row=2, column={i}, padx=3, pady={a}, sticky="snew")')
                    exec(f'self.var{i}Frame.grid_columnconfigure((0), weight=1)') 
                    exec(f'self.var{i}Frame.grid_rowconfigure([i for i in range(group+2)], weight=1)')
                if g:
                    if factor == 1 or level == 1:
                        for j in range(group):
                            exec(f"self.ContrastCellLabel{i}x{j}x0 = ctk.CTkLabel(self.groupFrame,text= 'Group{j+1}',width=60,height=1)")
                            exec(f"self.ContrastCellLabel{i}x{j}x0.grid(row=0, column={j}, padx=3, pady={d}, sticky='snew')")
                            exec(f"self.ContrastCell{i}x{j}x0x0 =  ctk.CTkEntry(self.groupFrame, placeholder_text= 'offset', width=60)")
                            exec(f"self.ContrastCell{i}x{j}x0x0.grid(row=1, column={j},padx=3, pady=3, sticky='snew')")
                            if test =="F-Test":
                                for k in range((group-2)):
                                    exec(f"self.ContrastCell{i}x{j}x0x{k+1} =  ctk.CTkEntry(self.groupFrame, placeholder_text= 'offset', width=60)")
                                    exec(f"self.ContrastCell{i}x{j}x0x{k+1}.grid(row={k+2}, column={j},padx=3, pady=3, sticky='snew')") 
                    else:
                        for j in range(level):
                            exec(f'self.Level{i}x{j}FrameLabel = customtkinter.CTkLabel(self.groupFrame, corner_radius=5,text= "Level{j+1}",width=60,height=1)')
                            exec(f'self.Level{i}x{j}FrameLabel.grid(row=0, column={j}, padx=5, pady=5, sticky="snew")')
                            exec(f'self.Level{i}x{j}Frame = customtkinter.CTkFrame(self.groupFrame, corner_radius=5,\
                                border_width= 1, fg_color="transparent", border_color=("gray40", "#ffffff"),width=10)')
                            exec(f'self.Level{i}x{j}Frame.grid(row=1, column={j}, rowspan=2, padx=5, pady=5, sticky="snew")')
                            exec(f'self.Level{i}x{j}Frame.grid_columnconfigure([i for i in range(factor)], weight=1)') 
                            for f in range(factor):
                                exec(f"self.ContrastCellLabel{i}x{j}x{f} = ctk.CTkLabel(self.Level{i}x{j}Frame,text= 'Fac{f+1}',width=60,height=1)")
                                exec(f"self.ContrastCellLabel{i}x{j}x{f}.grid(row=0, column={f}, padx=3, pady=5, sticky='snew')")
                                exec(f"self.ContrastCell{i}x{j}x{f}x0 =  ctk.CTkEntry(self.Level{i}x{j}Frame, placeholder_text= 'offset', width=60)")
                                exec(f"self.ContrastCell{i}x{j}x{f}x0.grid(row=1, column={f},padx=3, pady=3, sticky='snew')")
                                if test =="F-Test":
                                    for k in range((group-2)):
                                        exec(f"self.ContrastCell{i}x{j}x{f}x{k+1} =  ctk.CTkEntry(self.Level{i}x{j}Frame, placeholder_text= 'offset', width=60)")
                                        exec(f"self.ContrastCell{i}x{j}x{f}x{k+1}.grid(row={k+2}, column={f},padx=3, pady=3, sticky='snew')")
                else:
                    exec(f"self.ContrastCellLabel1{i}x0 = ctk.CTkLabel(self.var{i}Frame,text= 'Average',width=60,height=1)")
                    exec(f"self.ContrastCellLabel1{i}x0.grid(row=0, column=0, padx=3, pady={b}, sticky='snew')")
                    exec(f"self.ContrastCellLabel2{i}x0 = ctk.CTkLabel(self.var{i}Frame,text= 'Effect',width=60,height=1)")
                    exec(f"self.ContrastCellLabel2{i}x0.grid(row=1, column=0, padx=3, pady={a}, sticky='snew')")

                    exec(f"self.ContrastCell{i}x0 =  ctk.CTkEntry(self.var{i}Frame, placeholder_text= 'slope', width=60)")
                    exec(f"self.ContrastCell{i}x0.grid(row=2, column=0,padx=3, pady=3, sticky='snew')")
                    if test =="F-Test":
                        for k in range((group-2)):
                            exec(f"self.ContrastCell{i}x0x{k} =  ctk.CTkEntry(self.var{i}Frame, placeholder_text= 'slope', width=60)")
                            exec(f"self.ContrastCell{i}x0x{k}.grid(row={k+3}, column=0,padx=3, pady=3, sticky='snew')")
    def  concatenate(self):
        if self.mod == "DODS":
            cov=[]
            e=0
            if self.factor!= 1 and self.level!= 1:
                for i in range(self.cov+1):
                    for j in range(self.level):
                        for f in range(self.factor):
                            try:
                                exec(f"cov.append(self.ContrastCell{i}x{j}x{f}.get())")
                                if cov[-1] == '':
                                    cov[-1] = 0
                                elif float(cov[-1]).is_integer():
                                    cov[-1] = int(cov[-1])
                                else:
                                    cov[-1] = float(cov[-1])
                            except:
                                e+=1
                            if self.test == "F-Test":
                                for k in range((self.group-2)):
                                    try:
                                        exec(f"cov.append(self.ContrastCell{i}x{j}x{f}x{k}.get())")
                                        if cov[-1] == '':
                                            cov[-1] = 0
                                        elif float(cov[-1]).is_integer():
                                            cov[-1] = int(cov[-1])
                                        else:
                                            cov[-1] = float(cov[-1])
                                    except:
                                        e+=1
                data = np.array(cov).ravel() if self.test != "F-Test" else np.array(cov).reshape(-1,self.group-1).T
            else:
                if self.test == "T-Test":
                    for i in range(self.cov+1):
                        for j in range(self.group):
                            try:
                                exec(f"cov.append(self.ContrastCell{i}x{j}x0x0.get())")
                                if cov[-1] == '':
                                    cov[-1] = 0
                                elif float(cov[-1]).is_integer():
                                    cov[-1] = int(cov[-1])
                                else:
                                    cov[-1] = float(cov[-1])
                            except Exception as ee:
                                e+=1
                else:
                    for i in range(self.cov+1):
                        for j in range(self.group):
                            for k in range(self.group-1):
                                try:
                                    exec(f"cov.append(self.ContrastCell{i}x{j}x0x{k}.get())")
                                    if cov[-1] == '':
                                        cov[-1] = 0
                                    elif float(cov[-1]).is_integer():
                                        cov[-1] = int(cov[-1])
                                    else:
                                        cov[-1] = float(cov[-1])
                                except Exception as ee:
                                    e+=1
            data = np.array(cov).ravel() if self.test == "T-Test" else np.array(cov).reshape(-1,self.group-1).T
            if e != 0:
                tkmb.showerror('Error', f'found {e} invalid entries')
        else:
            group = []
            cov=[]
            e=0
            if self.factor == 1 or self.level == 1:
                if self.test == "T-Test":
                    for j in range(self.group):
                        try:
                            exec(f"group.append(self.ContrastCell0x{j}x0x0.get())")
                            if group[-1] == '':
                                group[-1] = 0
                            elif float(group[-1]).is_integer():
                                group[-1] = int(group[-1])
                            else:
                                group[-1] = float(group[-1])
                        except:
                            e+=1
                else:
                    for j in range(self.group):
                        for k in range(self.group-1):
                            try:
                                exec(f"group.append(self.ContrastCell0x{j}x0x{k}.get())")
                                if group[-1] == '':
                                    group[-1] = 0
                                elif float(group[-1]).is_integer():
                                    group[-1] = int(group[-1])
                                else:
                                    group[-1] = float(group[-1])
                            except:
                                e+=1
            else:
                if self.test == "T-Test":
                    for j in range(self.level):
                        for f in range(self.factor):
                            try:
                                exec(f"group.append(self.ContrastCell0x{j}x{f}x0.get())")
                                if group[-1] == '':
                                    group[-1] = 0
                                elif float(group[-1]).is_integer():
                                    group[-1] = int(group[-1])
                                else:
                                    group[-1] = float(group[-1])
                            except:
                                e+=1
                else:
                    for j in range(self.level):
                            for f in range(self.factor):
                                for k in range((self.group-1)):
                                    try:
                                        exec(f"group.append(self.ContrastCell0x{j}x{f}x{k}.get())")
                                        if group[-1] == '':
                                            group[-1] = 0
                                        elif float(group[-1]).is_integer():
                                            group[-1] = int(group[-1])
                                        else:
                                            group[-1] = float(group[-1])
                                    except:
                                        e+=1
            for i in range(1,self.cov+1):
                try:
                    exec(f"cov.append(self.ContrastCell{i}x0.get())")
                    if cov[-1] == '':
                        cov[-1] = 0
                    elif float(cov[-1]).is_integer():
                        cov[-1] = int(cov[-1])
                    else:
                        cov[-1] = float(cov[-1])
                except:
                    e+=1
                if self.test != "T-Test":
                    for k in range(self.group-2):
                        try:
                            exec(f"cov.append(self.ContrastCell{i}x0x{k}.get())")
                            if cov[-1] == '':
                                cov[-1] = 0
                            elif float(cov[-1]).is_integer():
                                cov[-1] = int(cov[-1])
                            else:
                                cov[-1] = float(cov[-1])
                        except:
                            e+=1
            data = np.array(cov),np.array(group)
            if len(cov) !=0:
                data = np.concatenate((data[1].reshape(-1,self.group-1
                    ).T,data[0].reshape(self.cov,-1).T),axis = 1
                    ) if self.test != "T-Test" else np.concatenate((
                    data[1], data[0]), axis = 0)
            else:
                data = np.array(group)
        return data, e
    def save(self):
        data, error = self.concatenate()
        if error != 0:
            tkmb.showerror('Error', f'found {error} invalid entries')
        else:
            if data.ndim == 1:
                data = data.reshape(1,-1)
            data = pd.DataFrame(data)
            if self.OutputPath != '':
                if self.ExperimentEntry.get()!= '':
                    path = self.OutputPath +'/'+self.ExperimentEntry.get()+'.mtx'
                    data.to_csv(path,sep='\t',index=False, header=False)
                    app.displayContrastPath.delete("0.0", "200.0")
                    app.GLMContrastInput = path
                    app.displayContrastPath.insert("0.0", path)
                else:
                    tkmb.showerror('Error', f'insert a name')
            else:
                tkmb.showerror('Error', f'choose a folder')
    def outputText(self):
        self.displayOutput.delete("0.0", "200.0")
        self.OutputPath = ''
        self.OutputPath = (ctk.filedialog.askdirectory())
        self.displayOutput.insert("0.0", self.OutputPath)

class Contrast2(ctk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        mod = app.ContrastMod.get() 
        test = app.ContrastTest.get() 
        factor = int(app.ContrastFactor.get()) # '1', '2', '3'  Category
        level = int(app.ContrastLevel.get()) # '1', '2', '3', '4'   CLASS
        cov = int(app.ContrastCOV.get()) # '0', '1', '2', '3', '4'
        group = level*factor

        self.mod = mod
        self.test = test
        self.factor = factor
        self.level = level
        self.cov = cov
        self.group = group 
        nregressor = group*(cov+1) if mod=="DODS" else (group + cov)
        hypothesis=[]
        if group == 1:
            if cov == 0:
                hypothesis.append(('is the intercept/mean equal to 0?',[1]))
            else: 
                v = [f'variable{i+1}' for i in range(cov)]
                v = [v[0]]+[' and '+i for i in v[1:]]
                hypothesis.append(("is the intercept equal "+\
                "to 0 after regressing out the effect/s of "+''.join(v)+'?',[1]+[0]*cov))
                for i, j in enumerate([f'variable{i+1}' for i in range(cov)]):
                    temp = ([0]*(cov+1))
                    temp[i+1] = 1
                    hypothesis.append((f'is the slope of {j} equals to 0?', temp))
        if group == 2:
            hypothesis.append(('is there a difference between the group intercepts?',[1,-1]))
            hypothesis.append(('is there a main effect of Group1?',[1,0]))
            hypothesis.append(('is there a main effect of Group2?',[0,1]))
            hypothesis.append(('does mean of the group means differ from 0?',[0.5,0.5]))
            if cov != 0:
                v = [f'variable{i+1}' for i in range(cov)]
                v2 = [v[0]]+[' and '+i for i in v[1:]]
                if mod == "DODS":
                    hypothesis =[
                        (i[:-1]+' after regressing out the effect/s of '+''.join(v2)+'?'
                        ,j+[0,0]*cov) for i,j in hypothesis]
                    for i, j in enumerate(v):
                        temp = ([0,0]*(cov+1))
                        temp[(i+1)*2] = 1
                        temp[(i+1)*2+1] = -1
                        hypothesis.append((f'is there a difference between the group slopes for {j} after regressing out other variables?',temp))
                        temp = ([0,0]*(cov+1))
                        temp[(i+1)*2] = 1
                        hypothesis.append((f'is the {j} slope weight for Group1 equals to 0 after regressing out other variables?', temp))
                        temp = ([0,0]*(cov+1))
                        temp[(i+1)*2+1] = 1
                        hypothesis.append((f'is the {j} slope weight for Group2 equals to 0 after regressing out other variables?', temp))
                        temp = ([0,0]*(cov+1))
                        temp[(i+1)*2] = 0.5
                        temp[(i+1)*2+1] = 0.5
                        hypothesis.append((f'is there an average affect of {j} after regressing out other variables?', temp))
                else:
                    hypothesis =[
                        (i[:-1]+' after regressing out the effect/s of '+''.join(v2)+'?'
                        ,j+[0]*cov) for i,j in hypothesis]
                    for i, j in enumerate(v):
                        temp = [0,0]+([0]*(cov))
                        temp[2+i] = 1
                        hypothesis.append((f'is there a main effect of {j} after regressing out other variables?', temp))
                    for i, j in enumerate(v[:-1]):
                        for m, n in enumerate(v[i+1:]):
                            temp = [0,0]+([0]*(cov))
                            l = int(j.split('ble')[-1])
                            p = int(n.split('ble')[-1])
                            temp[1+l] = 1 
                            temp[1+p] = -1 
                            hypothesis.append((f'is there a diffrence between the slope of Variable{l} and Variable{p}', temp))
        if group == 3:
            hypothesis.append(('is there a difference between the group intercepts?',[[1,-1,0],[1,0,-1]]))
            hypothesis.append(('is there a main effect of Group1?',[1,0,0]))
            hypothesis.append(('is there a main effect of Group2?',[0,1,0]))
            hypothesis.append(('is there a main effect of Group3?',[0,0,1]))
            hypothesis.append(('does mean of the group means differ from 0?',[.333,.333,.333]))
            if cov != 0:
                v = [f'variable{i+1}' for i in range(cov)]
                v2 = [v[0]]+[' and '+i for i in v[1:]]
                if mod == "DODS":
                    hypothesis =[
                        [i[:-1]+' after regressing out the effect/s of '+''.join(v2)+'?'
                        ,j+[0,0,0]*cov] for i,j in hypothesis]
                    hypothesis[0][1][0] =  hypothesis[0][1][0]+[0,0,0]*cov
                    hypothesis[0][1][1] =  hypothesis[0][1][1]+[0,0,0]*cov
                    hypothesis[0][1] = hypothesis[0][1][:2] 
                    for i, j in enumerate(v):
                        temp = ([0,0,0]*(cov+1))
                        temp[(i+1)*3] = 1
                        temp[(i+1)*3+1] = -1
                        t=[temp]
                        temp = ([0,0,0]*(cov+1))
                        temp[(i+1)*3] = 1
                        temp[(i+1)*3+2] = -1
                        t = t+[temp]
                        hypothesis.append((f'is there a difference between the group slope weights of {j} after regressing out other variables?',t))
                        temp = ([0,0,0]*(cov+1))
                        temp[(i+1)*3] = 1
                        hypothesis.append((f'is the {j} slope weight for Group1 equals to 0 after regressing out other variables?', temp))
                        temp = ([0,0,0]*(cov+1))
                        temp[(i+1)*3+1] = 1
                        hypothesis.append((f'is the {j} slope weight for Group2 equals to 0 after regressing out other variables?', temp))
                        temp = ([0,0,0]*(cov+1))
                        temp[(i+1)*3+2] = 1
                        hypothesis.append((f'is the {j} slope weight for Group3 equals to 0 after regressing out other variables?', temp))
                        temp = ([0,0,0]*(cov+1))
                        temp[(i+1)*2] = 0.5
                        temp[(i+1)*2+1] = 0.5
                        temp[(i+1)*2+2] = -1
                        hypothesis.append((f'is there a difference between average slope of Group1 and 2  and slope weight of Group3 in {j}?', temp))
                        temp = ([0,0,0]*(cov+1))
                        temp[(i+1)*2] = 0.5
                        temp[(i+1)*2+1] = -1
                        temp[(i+1)*2+2] = 0.5
                        hypothesis.append((f'is there a difference between average slope of Group1 and 3  and slope weight of Group2 in {j}?', temp))
                        temp = ([0,0,0]*(cov+1))
                        temp[(i+1)*2] = -1
                        temp[(i+1)*2+1] = 0.5
                        temp[(i+1)*2+2] = 0.5
                        hypothesis.append((f'is there a difference between average slope of Group2 and 3  and slope weight of Group1 in {j}?', temp))
                else:
                    hypothesis =[
                        (i[:-1]+' after regressing out the effect/s of '+''.join(v2)+'?'
                        ,j+[0]*cov) for i,j in hypothesis]
                    hypothesis =[
                        [i[:-1]+' after regressing out the effect/s of '+''.join(v2)+'?'
                        ,j+[0]*cov] for i,j in hypothesis]
                    hypothesis[0][1][0] =  hypothesis[0][1][0]+[0]*cov
                    hypothesis[0][1][1] =  hypothesis[0][1][1]+[0]*cov
                    hypothesis[0][1] = hypothesis[0][1][:2] 
                    for i, j in enumerate(v):
                        temp = [0,0,0]+([0]*(cov))
                        temp[3+i] = 1
                        hypothesis.append((f'is there a main effect of {j} after regressing out other variables?', temp))
                    for i, j in enumerate(v[:-1]):
                        for m, n in enumerate(v[i+1:]):
                            temp = [0,0,0]+([0]*(cov))
                            l = int(j.split('ble')[-1])
                            p = int(n.split('ble')[-1])
                            temp[2+l] = 1 
                            temp[2+p] = -1 
                            hypothesis.append((f'is there a diffrence between the slope of Variable{l} and Variable{p}', temp))
        self.hypothesis = hypothesis
        self.hyporadio = tk.StringVar(value="None")
        for i, j in enumerate(hypothesis):
            exec(f'self.hypo{i} = ctk.CTkRadioButton(self,text="{j[0]}", variable=self.hyporadio,value="{j[1]}")')
            exec(f'self.hypo{i}.grid(row={i}, column=0, columnspan = 2, padx=20, pady=10, sticky="snew")')
        start = len(hypothesis)
        self.grid_columnconfigure((0,1), weight=1)
        self.grid_rowconfigure([i for i in range(start)], weight=1)
        self.outputFrame = customtkinter.CTkFrame(self, corner_radius=5)
        self.outputFrame.grid(row=start, column=0,columnspan = 2, padx=5, pady=20, sticky="snew")
        self.outputFrame.grid_columnconfigure([i for i in range(5)][2:], weight=1)
        self.outputFrame.grid_columnconfigure((0,1), weight=0)
        self.outputFrame.grid_rowconfigure((0,1,3), weight=1)
        self.OutputLabel = ctk.CTkLabel(self.outputFrame, text="Output:")
        self.OutputLabel.grid(row=1, column=0, padx=5, pady=5, sticky="snew")
        self.displayOutput = ctk.CTkTextbox(self.outputFrame, height=8)
        self.displayOutput.grid(row=1, column=2, padx=5,columnspan=3, pady=5, sticky="snew")
        self.displayOutput.insert("0.0", 'press open to select a folder')
        self.OutputButton = ctk.CTkButton(self.outputFrame, text="open",command=self.outputText)
        self.OutputButton.grid(row=1, column=1, columnspan=1, padx=10, pady=5, sticky="snew")
        self.OutputPath = ''
        self.ExperimentLabel = ctk.CTkLabel(self.outputFrame, text="Experiment:")
        self.ExperimentLabel.grid(row=0, column=0, padx=5, pady=5, sticky="snew")
        self.ExperimentEntry = ctk.CTkEntry(self.outputFrame, 
        placeholder_text="A Contrast file will be created with this name; e.g. exp_01.mtx")
        self.ExperimentEntry.grid(row=0, column=1, columnspan=4, padx=4, pady=5, sticky="snew")
        self.OutputButton = ctk.CTkButton(self.outputFrame, text="Create",command=self.hypogen,\
        height=35,fg_color= '#d03b3b', hover_color='#9f3636')
        self.OutputButton.grid(row=2, column=0, columnspan=5, padx=10, pady=5, sticky="sn")
        # Sets the title of the window to "App"
        self.title("Contrast Builder")  
        self.geometry(f"{1200}x{200+start*45}")
    def hypogen(self):
        if int(self.group)<4:
            data = self.hyporadio.get()
            print(data)
            if self.hyporadio.get() == "None":
                tkmb.showerror("Error", "select a hypothesis")
            else:
                data = pd.DataFrame(literal_eval(data))
                if data.shape[-1]== 1:
                    data = data.T
                data.to_csv()
                if self.OutputPath != '':
                    if self.ExperimentEntry.get()!= '':
                        path = self.OutputPath +'/'+self.ExperimentEntry.get()+'.mtx'
                        data.to_csv(path,sep='\t',index=False, header=False)
                        app.displayContrastPath.delete("0.0", "200.0")
                        app.GLMContrastInput = path
                        app.displayContrastPath.insert("0.0", path)
                    else:
                        tkmb.showerror('Error', f'insert a name')
                else:
                    tkmb.showerror('Error', f'choose a folder')
        else:
            tkmb.showerror('Error', 'too sophisticated model.\nyou can use this feature when you have a maximum of 3 groups')


    def outputText(self):
        self.displayOutput.delete("0.0", "200.0")
        self.OutputPath = ''
        self.OutputPath = (ctk.filedialog.askdirectory())
        self.displayOutput.insert("0.0", self.OutputPath)
        
class SegSubject(customtkinter.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Sets the title of the window to "App"
        self.title("Select Subjects For Segmentation")  
        self.subjects = []
        root = os.environ['SUBJECTS_DIR']
        for i in sorted(os.listdir(root)):
            d = os.path.join(root, i)
            if os.path.isdir(d):
                self.subjects.append(i)
        self.subnum = len(self.subjects)
        colnum = 5 if self.subnum<60 else 10
        rows, residual = divmod(self.subnum,colnum)
        geo = []
        for i in range(rows):
            for j in range(colnum):
                geo.append([i,j])
        for i in range(residual):
            geo.append([rows,i])
        width = int(len(''.join(self.subjects))/rows*colnum*3)
        height = 100 + (rows+1)*50
        # Sets the dimensions of the window to 600x700
        self.geometry(f"{width}x{height}")   

        for i, j in geo:
            exec(f'self.Subject{i*colnum+j} = ctk.CTkCheckBox(self,text="{self.subjects[i*colnum+j]}", offvalue="",onvalue="{self.subjects[i*colnum+j]}")')
            exec(f'self.Subject{i*colnum+j}.grid(row={i}, column={j}, padx=5, pady=5, sticky="snew")')
        self.SelectButton = ctk.CTkButton(self, text="Select Subjects",
                                command=self.select, fg_color= '#d03b3b', hover_color='#9f3636')
        self.SelectButton.grid(row=rows+1, column=0, columnspan = colnum, padx=150, pady=20, sticky="snew")
        self.grid_columnconfigure(list(range(colnum)), weight=1)
        self.grid_rowconfigure([i for i in range(rows+2)], weight=1)
    def select(self):
        sub = []
        for i in range(self.subnum):
            exec(f'sub.append(self.Subject{i}.get())')
        sub = sorted(list(set(sub)-{'',}))
        app.segsub.clear()
        for i in sub:
            app.segsub.append(i)
        out = [i+', ' for i in sub]
        out = ''.join(out)[:-2]
        app.displaySegSubjectPath.delete("0.0", "200.0")
        app.displaySegSubjectPath.insert("0.0", out)
        SegSubject.destroy(self)

class BASESubject(customtkinter.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Sets the title of the window to "App"
        self.title("Select Subjects For Segmentation")  
        self.subjects = []
        root = os.environ['SUBJECTS_DIR']
        for i in sorted(os.listdir(root)):
            d = os.path.join(root, i)
            if os.path.isdir(d):
                self.subjects.append(i)
        self.subnum = len(self.subjects)
        colnum = 5 if self.subnum<60 else 10
        rows, residual = divmod(self.subnum,colnum)
        geo = []
        for i in range(rows):
            for j in range(colnum):
                geo.append([i,j])
        for i in range(residual):
            geo.append([rows,i])
        width = int(len(''.join(self.subjects))/rows*colnum*3)
        height = 100 + (rows+1)*50
        # Sets the dimensions of the window to 600x700
        self.geometry(f"{width}x{height}")   

        for i, j in geo:
            exec(f'self.Subject{i*colnum+j} = ctk.CTkCheckBox(self,text="{self.subjects[i*colnum+j]}", offvalue="",onvalue="{self.subjects[i*colnum+j]}")')
            exec(f'self.Subject{i*colnum+j}.grid(row={i}, column={j}, padx=5, pady=5, sticky="snew")')
        self.SelectButton = ctk.CTkButton(self, text="Select Subjects",
                                command=self.select, fg_color= '#d03b3b', hover_color='#9f3636')
        self.SelectButton.grid(row=rows+1, column=0, columnspan = colnum, padx=150, pady=20, sticky="snew")
        self.grid_columnconfigure(list(range(colnum)), weight=1)
        self.grid_rowconfigure([i for i in range(rows+2)], weight=1)
    def select(self):
        sub = []
        for i in range(self.subnum):
            exec(f'sub.append(self.Subject{i}.get())')
        sub = sorted(list(set(sub)-{'',}))
        app.BASEsub.clear()
        for i in sub:
            app.BASEsub.append(i)
        out = [i+', ' for i in sub]
        out = ''.join(out)[:-2]
        app.displayBASESubjectPath.delete("0.0", "200.0")
        app.displayBASESubjectPath.insert("0.0", out)
        SegSubject.destroy(self)

if __name__ == "__main__":
    app = App()
    app.call('wm', 'iconphoto', app._w, ImageTk.PhotoImage(Image.open(os.environ['FREESURFER_GUI']+'/graphics/freeview.png')))
    app.mainloop()
