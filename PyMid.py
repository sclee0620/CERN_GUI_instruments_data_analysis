import pandas as pd
from bokeh.plotting import*
from bokeh.io import*
from bokeh.models import PrintfTickFormatter
from bokeh.palettes import Category20, Colorblind, Set1
from PyPlot_functions import legend_parameters


def plot_parameters_mid():

    p = figure(y_axis_type="log", sizing_mode = "stretch_both", tools="pan,wheel_zoom,box_zoom,reset,save,box_select,hover")
    p.yaxis[0].formatter = PrintfTickFormatter(format="%4.1e")

    # define axes label
    p.xaxis.axis_label = 'Time [seconds]'
    p.yaxis.axis_label = 'Current [mA]'
    # define font style of major and label + size

    # define distance separation between axes and label
    p.xaxis.axis_label_standoff = 15
    p.yaxis.axis_label_standoff = 15
    # add a minor grid + color + width
    p.ygrid.minor_grid_line_color = 'grey'
    p.ygrid.minor_grid_line_alpha = 0.2
    p.xgrid.minor_grid_line_color = 'grey'
    p.xgrid.minor_grid_line_alpha = 0.2


    return p


def legend_parameters(p):
    p.xaxis.axis_label_text_font_size = "22pt"
    p.yaxis.axis_label_text_font_size = "22pt"
    p.xaxis.major_label_text_font_size = "22pt"
    p.yaxis.major_label_text_font_size = "22pt"
    p.xaxis.axis_label_text_font_style = "normal"
    p.yaxis.axis_label_text_font_style = "normal"
    p.xaxis.major_label_text_font = 'Times New Roman'
    p.yaxis.major_label_text_font = 'Times New Roman'
    p.yaxis.axis_label_text_font = 'Times New Roman'
    p.xaxis.axis_label_text_font = 'Times New Roman'
    p.legend.label_text_font_size = "14pt"
    p.legend.label_text_font = "Times New Roman"
    p.legend.click_policy = "hide"
    p.legend.label_standoff = 5
    p.legend.glyph_width = 20
    p.legend.spacing = 10
    p.legend.padding = 5
    p.legend.margin = 5


def plot_mid_quadera(filename):

    df = pd.read_excel(filename[0], sep=',', skiprows=6)
    mass_list = list(df.columns.values)


    list_index = []
    current_list = []
    relative_time_list = []
##
    for i in range(len(mass_list)):

        # give a list of index of the mass value

        if type(mass_list[i]) == int:

            index = mass_list.index(mass_list[i])
            current_list.append(df.iloc[1:, index])
            relative_time_list.append(df.iloc[1:, index-1])
            list_index.append(index)

    p = plot_parameters_mid()

    for i in range(len(list_index)):

        p.line(relative_time_list[i], current_list[i], legend=str(list_index[i]), color=Category20[20][i], line_width=1.5)
        legend_parameters(p)

    show(p)
    reset_output()


def plot_mid_massoft(filename):

    df = pd.read_csv(filename[0], sep=',')

    for i in range(len(df)):
        if df.iloc[i, 0] == "Time":

            index = i

    df = pd.read_csv(filename[0], sep=',', skiprows=index + 1)
    mass_list = list(df.columns.values)
    time = df[mass_list[1]] / 1000
    mass_list = mass_list[2:]
    print(mass_list)


    p = plot_parameters_mid()

    for i in range(len(mass_list)):
        p.line(time, df[mass_list[i]], legend=str(mass_list[i]), color=Category20[20][i], line_width=1.5)
        legend_parameters(p)

    show(p)
    reset_output()

def plot_mid_antoine(filename):
     df = pd.read_excel(filename[0], sep=',')

     for i in range(len(df)):
         if df.iloc[i, 0] == "mass 2_time":
             index = i
             print(index)

     df = pd.read_excel(filename[0], sep=',', skiprows=index + 1)

     current_list = []
     relative_time_list =[]
     columns_list = list(df.columns.values)
     print(len(columns_list))
     print(columns_list)

     p = plot_parameters_mid()



     time = df.iloc[:, 0] - df.iloc[0, 0]
     print(time)
     for i in range(len(time)):
         time[i] =time[i].total_seconds()











