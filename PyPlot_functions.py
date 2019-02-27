import numpy as np
import pandas as pd
from bokeh.plotting import*
from bokeh.io import*
from bokeh.models import PrintfTickFormatter
from bokeh.palettes import Category20, Set1
from os.path import normpath, basename
import os
import math
import decimal


def extract_excel_data(path):
    """

    :param path: path window
    :return:
    """
    head, tail = os.path.split(path)


   # Open a CSV or XLSX file

    if tail.find('xlsx') != -1:
        df = pd.read_excel(path, sep=',')
        # change name of columns
        n_col = len(df.columns)
        n_columns = []

        if n_col == 2:

            df.columns = ['Mass', 'Current']

            # Rename the columns
        if n_col > 2:
            for i in range(n_col-1):

                if i == 0:
                    name = "Mass"
                    n_columns.append(name)
                if i == 1:
                    name = "Current"
                    n_columns.append(name)

                if i != 0 & i != 1:

                    name = str(i)
                    n_columns.append(name)

            df.columns = n_columns

        df["Mass"] = df[pd.to_numeric(df.Mass, errors='coerce').notnull()]
    else:

        df = pd.read_csv(path, sep=',', skiprows=22)
        df = df.drop(df.columns[[0, 1, 2, 5, 6, 7, 8, 9, 10]], axis=1)

        df.columns = ['Mass', 'Current']

        #for i in range(len(df.Mass)):

        #    if df.Mass[i] == np.max(df.Mass):
        #        index = i
        #        print(df.Mass[i])
        #        break
        #df.Mass = df.Mass[0:index+1]
        #print(df.Mass)

    return df


def plot_parameters():
    p = figure(y_axis_type="log", sizing_mode = "stretch_both", tools="pan,wheel_zoom,box_zoom,reset,save,box_select,hover")
    p.yaxis[0].formatter = PrintfTickFormatter(format="%4.1e")

    # define axes label
    p.xaxis.axis_label = 'Mass [amu]'
    p.yaxis.axis_label = 'Current [A]'
    # define font style of major and label + size

    # define distance separation between axes and label
    p.xaxis.axis_label_standoff = 15
    p.yaxis.axis_label_standoff = 15
    # add a minor grid + color + width
    p.ygrid.minor_grid_line_color = 'grey'
    p.ygrid.minor_grid_line_alpha = 0.2
    p.xgrid.minor_grid_line_color = 'grey'
    p.xgrid.minor_grid_line_alpha = 0.2
    p.xaxis.ticker = np.arange(0, 105, 5)

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


def max_peak(mass_target, current, mass):
    """
    The aims of this function is to get the max current of a mass peak
    :param mass_target: int, mass that you want to study
    :param df: data frame
    :param mass: list of the mass
    :param m0: first index of the data frame
    :return: current max of the wanted peak
    """

    #for index in range(len(mass)):
    #    if mass[index] == mass_target:
    #        mass_index = index

    #mass_sup = mass_index + 8
    #mass_inf = mass_index - 8

    for index in range(len(mass)):
        if mass[index] >= mass_target+0.4:
            mass_SUP = index

            break

    for index in range(len(mass)):
        if mass[index] >= mass_target-0.4:
            mass_INF = index

            break

    list_current = current[mass_INF:mass_SUP]

    list_current = [0 if math.isnan(x) else x for x in list_current]

    list_mass = mass[mass_INF:mass_SUP]

    current_max = np.max(list_current)

    index_max_mass = list_current.index(current_max)
    value_max_mass = list_mass[index_max_mass]

    return current_max, value_max_mass


def decimal_number(current_max):
    """

    :param current_max:
    :return:
    """

    current_max = decimal.Decimal(current_max)
    decimal.getcontext().prec = 3
    current_max = decimal.getcontext().create_decimal(current_max)

    return current_max


def plot(filename):
    fig_mass = []
    fig_current = []
    legend = []
    for i in range(len(filename)):

            # path_data = path_data.replace('"','')
            df = extract_excel_data(filename[i])
            legend_scan = basename(normpath(str(filename[i])))
            legend_scan = legend_scan.replace('.xlsx', '')
            legend_scan = legend_scan.replace('.csv', '')
            legend.append(legend_scan)

            # find the maximum mass in the excel file
            mass_max = np.max(df.Mass)
            mass_min = np.min(df.Mass) 
            # Select the right range from 0 amu to max amu

            for index, row in df.iterrows():

                if df.Mass[index] == mass_min:

                    m0 = index

                if df.Mass[index] == mass_max:
                    m100 = index

                    break

            # define a list of the data to plot
            mass = df.Mass[m0:m100]

            current = df.Current[m0:m100]

            # delete negative values

            current = pd.Series.tolist(current)
            for i in range(len(current)):
                if current[i] < 0:

                    current[i] = np.abs(current[i])
            mass = pd.Series.tolist(mass)

            fig_mass.append(mass)
            fig_current.append(current)

            max_2, index_max_mass_2 = max_peak(2, current, mass)
            max_12, index_max_mass_12 = max_peak(12, current, mass)
            max_14, index_max_mass_14 = max_peak(14, current, mass)
            max_15, index_max_mass_15 = max_peak(15, current, mass)
            max_16, index_max_mass_16 = max_peak(16, current, mass)
            max_18, index_max_mass_18 = max_peak(18, current, mass)
            max_28, index_max_mass_28 = max_peak(28, current, mass)
            max_32, index_max_mass_32 = max_peak(32, current, mass)
            max_40, index_max_mass_40 = max_peak(40, current, mass)
            max_44, index_max_mass_44 = max_peak(44, current, mass)

            print("Filename: " + legend_scan)
            print("")
            print("mass[amu] " + " " + "current[mA] " + " " + "real mass")
            print("2", "         ", decimal_number(max_2),  " ", index_max_mass_2)
            print("12", "        ", decimal_number(max_12), " ", index_max_mass_12)
            print("14", "        ", decimal_number(max_14), " ", index_max_mass_14)
            print("15", "        ", decimal_number(max_15), " ", index_max_mass_15)
            print("16", "        ", decimal_number(max_16), " ", index_max_mass_16)
            print("18", "        ", decimal_number(max_18), " ", index_max_mass_18)
            print("28", "        ", decimal_number(max_28), " ", index_max_mass_28)
            print("32", "        ", decimal_number(max_32), " ", index_max_mass_32)
            print("40", "        ", decimal_number(max_40), " ", index_max_mass_40)
            print("44", "        ", decimal_number(max_44), " ", index_max_mass_44)
            print("")

    p = plot_parameters()

    for i in range(len(fig_mass)):

        p.line(fig_mass[i], fig_current[i], legend=legend[i], color=Set1[9][i], line_width=1.5)
        legend_parameters(p)

    show(p)
    reset_output()


def plot_norm_water(filename):
    """

    :param filename: path window
    :return:
    """
    fig_mass = []
    fig_current = []
    legend = []
    for i in range(len(filename)):

            # path_data = path_data.replace('"','')
            df = extract_excel_data(filename[i])

            # find the maximum mass in the excel file
            mass_max = np.max(df.Mass)
            mass_min = np.min(df.Mass)
            # Select the right range from 0 amu to max amu

            for index, row in df.iterrows():

                if df.Mass[index] == mass_min:

                    m0 = index

                if df.Mass[index] == mass_max:
                    m100 = index

                    break



           # define a list of the data to plot
            mass = df.Mass[m0:m100]

            current = df.Current[m0:m100]
            # delete negative values
            current[current < 0] = np.abs(current)
            current = pd.Series.tolist(current)
            mass = pd.Series.tolist(mass)

            fig_mass.append(mass)

            max_18, index_max_mass_18 = max_peak(18, current, mass)
            current = current/max_18

            fig_current.append(current)
            legend_scan = basename(normpath(str(filename[i])))
            legend_scan = legend_scan.replace('.xlsx', '')
            legend_scan = legend_scan.replace('.csv', '')
            legend.append(legend_scan)

    # define figure with type of axes and tools for dynamic visualization

    p = plot_parameters()

    for i in range(len(fig_mass)):
        if i == 0:
            color = 0
        else:
            color = (1+i)*2
        p.line(fig_mass[i], fig_current[i], legend=legend[i], color=Set1[9][color], line_width=1.5)
        legend_parameters(p)

    show(p)

    reset_output()


def plot_norm_hydrogen(filename):

    fig_mass = []
    fig_current = []
    legend = []
    for i in range(len(filename)):

            # path_data = path_data.replace('"','')
            df = extract_excel_data(filename[i])

            # find the maximum mass in the excel file
            mass_max = np.max(df.Mass)
            mass_min = np.min(df.Mass)
            # Select the right range from 0 amu to max amu

            for index, row in df.iterrows():

                if df.Mass[index] == mass_min:

                    m0 = index

                if df.Mass[index] == mass_max:
                    m100 = index

                    break


           # define a list of the data to plot
            mass = df.Mass[m0:m100]

            current = df.Current[m0:m100]
            # delete negative values
            current[current < 0] = np.abs(current)
            current = pd.Series.tolist(current)
            mass = pd.Series.tolist(mass)

            fig_mass.append(mass)

            max_2, index_max_mass_18 = max_peak(2, current, mass)
            current = current/max_2

            fig_current.append(current)
            legend_scan = basename(normpath(str(filename[i])))
            legend_scan = legend_scan.replace('.xlsx', '')
            legend_scan = legend_scan.replace('.csv', '')
            legend.append(legend_scan)



    # define figure with type of axes and tools for dynamic visualization
    p = figure(y_axis_type="log",
               tools="pan,wheel_zoom,box_zoom,reset,save,box_select,hover")

    p = plot_parameters()

    for i in range(len(fig_mass)):
        if i == 0:
            color = 0
        else:
            color = (1+i)*2
        p.line(fig_mass[i], fig_current[i], legend=legend[i], color=Set1[9][color], line_width=1.5)

        legend_parameters(p)

    show(p)
    reset_output()


def plot_norm_before_bo(filename):
    fig_mass = []
    fig_current = []
    legend = []
    for i in range(len(filename)):

            # path_data = path_data.replace('"','')
            df = extract_excel_data(filename[i])

            # find the maximum mass in the excel file
            mass_max = np.max(df.Mass)
            mass_min = np.min(df.Mass)
            # Select the right range from 0 amu to max amu

            for index, row in df.iterrows():

                if df.Mass[index] == mass_min:

                    m0 = index

                if df.Mass[index] == mass_max:
                    m100 = index

                    break

           # define a list of the data to plot
            mass = df.Mass[m0:m100]

            current = df.Current[m0:m100]
            # delete negative values
            current[current < 0] = np.abs(current)
            current = pd.Series.tolist(current)
            mass = pd.Series.tolist(mass)

            fig_mass.append(mass)

            max_18, index_max_mass_18 = max_peak(18, current, mass)
            current = current/max_18

            fig_current.append(current)
            legend_scan = basename(normpath(str(filename[i])))
            legend_scan = legend_scan.replace('.xlsx', '')
            legend_scan = legend_scan.replace('.csv', '')
            legend.append(legend_scan)

    x_1 = [14, 19]
    y_1 = [1, 1]

    x_2 = [19, 44.5]
    y_2 = [0.01, 0.01]

    x_3 = [44.5, 100]
    y_3 = [0.001, 0.001]
    # define figure with type of axes and tools for dynamic visualization
    p = figure(y_axis_type="log", y_range=(1e-3, 1),
               tools="pan,wheel_zoom,box_zoom,reset,save,box_select,hover")

    p = plot_parameters()

    for i in range(len(fig_mass)):

        color = 1 + i
        p.line(x_1, y_1, legend="Acceptance Limit", color="red", line_width=1.5)
        p.line(x_2, y_2, legend="Acceptance Limit", color="red", line_width=1.5)
        p.line(x_3, y_3, legend="Acceptance Limit", color="red", line_width=1.5)

        p.line(fig_mass[i], fig_current[i], legend=legend[i], color=Set1[9][color], line_width=1.5)
        legend_parameters(p)
        
    show(p)

    reset_output()


def plot_norm_after_bo(filename):

    fig_mass = []
    fig_current = []
    legend = []
    for i in range(len(filename)):

            # path_data = path_data.replace('"','')
            df = extract_excel_data(filename[i])

            # find the maximum mass in the excel file
            mass_max = np.max(df.Mass)
            mass_min = np.min(df.Mass)
            # Select the right range from 0 amu to max amu

            for index, row in df.iterrows():

                if df.Mass[index] == mass_min:

                    m0 = index

                if df.Mass[index] == mass_max:
                    m100 = index

                    break
           # define a list of the data to plot
            mass = df.Mass[m0:m100]

            current = df.Current[m0:m100]
            # delete negative values
            current[current < 0] = np.abs(current)
            current = pd.Series.tolist(current)
            mass = pd.Series.tolist(mass)

            fig_mass.append(mass)

            max_2, index_max_mass_18 = max_peak(2, current, mass)

            current = current/max_2

            fig_current.append(current)
            legend_scan = basename(normpath(str(filename[i])))
            legend_scan = legend_scan.replace('.xlsx', '')
            legend_scan = legend_scan.replace('.csv', '')
            legend.append(legend_scan)

    y1 = 1e-4
    y2 = 1
    y3 = 1e-1
    y4 = 5e-3
    y5 = 2e-3
    y6 = 5e-2
    y7 = 1e-3
    # define figure with type of axes and tools for dynamic visualization


    p = plot_parameters()

    for i in range(len(fig_mass)):
        color = 1 + i
        p.line(fig_mass[i], fig_current[i], legend=legend[i], color=Set1[9][color], line_width=1.5)

        legend_parameters(p)

    p.step([0, 1.28, 2.78, 2.8, 11.5, 11.52, 19.5, 19.52, 22.16, 22.17, 27.5, 27.52, 28.5, 28.52, 32.5, 32.52, 34, 34.02, 43.5,
        43.52, 44.5, 44.52, 46.52, 46.53, 48.5, 48.52, 100], [y1, y1, y2, y1, y1, y3, y3, y1, y1, y4, y4, y3, y3, y4, y4, y1, y1, y5,
        y5, y6, y6, y5, y5, y1, y1, y7, y7], legend="Acceptance limit", color="red", line_width=1.5)
    show(p)

    reset_output()


