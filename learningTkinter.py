'''
Alex Solano
CS 152
12/9/22
This practice program contains code that I was testing. Most of it is me learning more widgets and methods.'''

from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog
import re
import Rubik_Statisitcs as rs
import stats
import matplotlib.pyplot as plt

class RubiksAnalysisGUI(object):

    def __init__(self, window): # Add more buttons for the data analysis part
        self.window = window
        # Some cool stuff I could use
        window.title('Rubik\'s Cube Analyzer')
        # window.geometry('300x300')
        self.import_button = Button(window, text='Import a .csv file containg the times', command=self.open_file)
        self.import_button.grid(row=0, column=0)
        self.average_option = Button(window, text='Averages', command=self.average_options)
        self.average_option.grid(row=1, column=0)
        self.average_plot_label = Label(window, image='')
        self.average_plot_label.grid(row=6, column=0)
        self.time_trend_option = Button(window, text='Time Trend', command=self.time_trend)
        self.time_trend_option.grid(row=1, column=3)
        self.time_plot_label = Label(window, image='')
        self.time_plot_label.grid(row=6, column=3)
        self.data = []

    def open_file(self):
        filename = filedialog.askopenfilename()
        time_file = open(filename, 'r')
        source_str = time_file.readlines()
        # print(source_str)
        time_list = []
        for line in source_str:
            match_obj = re.search(r'(\d+);((\d+:)?\d+\.\d{2});', line)
            if match_obj != None:
                entry = [match_obj.group(1), match_obj.group(2)]
                time_list.append(entry)
        # print(time_list)
        # print(match_obj.group(3))
        data = rs.Rubik_Statistics(time_list)
        self.data = data.getData()

    def average_options(self):
        self.averages_options = StringVar(value=["Average of 5", "Average of 12", "Average of 100"])
        self.averages_button = Listbox(self.window, height=3, listvariable=self.averages_options)
        self.averages_button.grid(row=2, column=0)
        self.generate_avgs_button = Button(self.window, text="Generate Plot", command=self.show_average)
        self.generate_avgs_button.grid(row=3, column=0)
    
    def show_average(self):
        idx = self.averages_button.curselection()
        if len(idx) == 1:
            option = int(idx[0])
            if option == 0:
                self.plot_aof5()
                plot_image1 = PhotoImage(file='plot_aof5.png')
                self.average_plot_label['image'] = plot_image1
                # self.average_plot_label.grid(row=6, column=0)
            if option == 1:
                self.plot_aof12()
                plot_image2 = PhotoImage(file='plot_aof12.png')
                self.average_plot_label['image'] = plot_image2
                # self.average_plot_label.grid(row=6, column=0)
            if option == 2:
                self.plot_aof100()
                plot_image3 = PhotoImage(file='plot_aof100.png')
                self.average_plot_label['image'] = plot_image3
                # self.average_plot_label.grid(row=6, column=0)
    
    def plot_aof5(self):
        ''''''
        data = self.data
        aof5 = rs.Average(data)
        aof5.calculate_averages_of_5()
        rolling_aof5 = aof5.getAveragesOf5()
        x_axis = []
        y_axis = []
        for entry in rolling_aof5:
            x_axis.append(entry[0])
            y_axis.append(entry[1])
        plt.clf()
        plt.plot(x_axis, y_axis)
        plt.title("Rolling Averages of 5")
        plt.xlabel("Solve No.")
        plt.ylabel("Time (s)")
        plt.savefig('plot_aof5.png')
    
    def plot_aof12(self):
        ''''''
        data = self.data
        aof12 = rs.Average(data)
        aof12.calculate_averages_of_12()
        rolling_aof12 = aof12.getAveragesOf12()
        x_axis = []
        y_axis = []
        for entry in rolling_aof12:
            x_axis.append(entry[0])
            y_axis.append(entry[1])
        plt.clf()
        plt.plot(x_axis, y_axis)
        plt.title("Rolling Averages of 12")
        plt.xlabel("Solve No.")
        plt.ylabel("Time (s)")
        plt.savefig('plot_aof12.png')
    
    def plot_aof100(self):
        ''''''
        data = self.data
        aof100 = rs.Average(data)
        aof100.calculate_averages_of_100()
        rolling_aof100 = aof100.getAveragesOf100()
        x_axis = []
        y_axis = []
        for entry in rolling_aof100:
            x_axis.append(entry[0])
            y_axis.append(entry[1])
        plt.clf()
        plt.plot(x_axis, y_axis)
        plt.title("Rolling Averages of 100")
        plt.xlabel("Solve No.")
        plt.ylabel("Time (s)")
        plt.savefig('plot_aof100.png')

    def time_trend(self):
        ''''''
        times = rs.Rubik_Statistics(self.data)
        list_of_times = times.getData()
        x_axis = []
        y_axis = []
        for entry in list_of_times:
            x_axis.append(entry[0])
            y_axis.append(entry[1])
        plt.clf()
        plt.plot(x_axis, y_axis)
        plt.title("Time Trend")
        plt.xlabel('Solve No.')
        plt.ylabel('Time (s)')
        plt.savefig('time_trend.png')
        plot_image4 = PhotoImage(file='time_trend.png')
        self.time_plot_label['image'] = plot_image4

    def new_window(self):
        self.newwindow = Tk()
        self.close_button = Button(self.newwindow, text='Close', command=self.closewindow)
        self.close_button.grid(row=0, column=0)
        self.newwindow.mainloop()
    
    def closewindow(self):
        self.newwindow.destroy()


def main():
    window = Tk()
    # window2 = Tk()
    test_gui = RubiksAnalysisGUI(window)
    # test_plot = Data(window)
    window.mainloop()
    # window2.mainloop()

main()