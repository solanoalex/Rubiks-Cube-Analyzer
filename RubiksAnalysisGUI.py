'''
Alex Solano
CS 152
12/10/22
This program we created a class, RubiksAnalysisGUI, that creates a GUI using the Tkinter module. The purpose of this GUI is to analyze someone's
solve times for solving a 3x3 Rubiks Cube. The GUI has a couple of buttons the user can click. There is the 'Import' button where the user can import
a .csv file containing the solve times. There are two buttons that are used to analyze the solve times. The first one is the 'Averages' button. This
button gives 3 options when the user clicks on it: Averages of 5, 12, and 100. The user can select one of the option and press the 'Generate Plot'
button, which will generate a plot of the average specified on the window. The best average specified and the standard deviation of the averages will
also be on the plot. The second one is the 'Generate Time Trend'. This button generates a plot of the solve times on the window. The best time, standard
deviation, and overall average of the solve times will also be on the plot. Lastly, there is a 'Close' button that will terminate the application.

I have also included some .csv files you can use for the program.

Call it like this in the terminal:
python3 RubiksAnalysisGUI.py
'''
from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog
import re
import Rubik_Statisitcs as rs
import stats
import matplotlib.pyplot as plt


class RubiksAnalysisGUI(object):
    '''This is the class to create a object that represents the GUI for the rubiks analysis.'''

    def __init__(self, window):
        '''Initializes a RubiksAnalysisGUI object. Creates a GUI with an importing button to import a .csv file, 
        average and time trend options that will generate a plot of the option clicked. The GUI also has two labels,
        one for the averages plots and one for the time trend plot,that are "invisible" since they have no text, but 
        when an plot is generated, the plot will be shown where the corresponding label is located.'''
        self.window = window
        window.title('Rubik\'s Times Analyzer')
        window.geometry('1200x2000')
        self.import_label = Label(window, text='Import a .csv file that contains the times')
        self.import_label.grid(row=0, column=0)
        self.import_button = Button(window, text='Import', command=self.open_file)
        self.import_button.grid(row=0, column=1)
        self.average_option = Button(window, text='Averages', command=self.average_options)
        self.average_option.grid(row=2, column=0)
        self.average_plot_label = Label(window, image='')
        self.average_plot_label.grid(row=7, column=0)
        self.time_trend_option = Button(window, text='Generate Time Trend', command=self.time_trend)
        self.time_trend_option.grid(row=2, column=5)
        self.time_plot_label = Label(window, image='')
        self.time_plot_label.grid(row=7, column=5)
        self.close_button = Button(window, text='Close', command=self.close_window)
        self.close_button.grid(row=0, column=2)
        self.data = []
    

    def open_file(self):
        '''This is the command for the import button. When clicked it will open a open file dialog window. The user 
        (hopefully) will select a .csv file containing at least two columns, with one column containing the solve no.
        and the other column containing the time. These two columns are extracted and used to set the data field.'''
        filename = filedialog.askopenfilename()
        time_file = open(filename, 'r')
        source_str = time_file.readlines()
        # print(source_str) # Testing to see if the lines in the .csv file were extracted properly
        time_list = []
        for line in source_str:
            match_obj = re.search(r'(\d+);((\d+:)?\d+\.\d{2});', line)
            if match_obj != None:
                entry = [match_obj.group(1), match_obj.group(2)]
                time_list.append(entry)
                # print(match_obj.group(1)) # Testing to see if the solve no. was extracted properly
                #print(match_obj.group(2))  # Testing to see if the time was extracted properly
        # print(time_list) # Testing to see if the data was extracted properly
        data = rs.Rubik_Statistics(time_list)
        self.data = data.getData()
    

    def average_options(self):
        '''This is the command for the average option. When clicked, it presents a list of options you can choose
        and a button below that says "Generate Plot".'''
        self.averages_options = StringVar(value=["Average of 5", "Average of 12", "Average of 100"])
        self.averages_button = Listbox(self.window, height=3, listvariable=self.averages_options)
        self.averages_button.grid(row=3, column=0)
        self.generate_avgs_button = Button(self.window, text="Generate Plot", command=self.show_average)
        self.generate_avgs_button.grid(row=6, column=0)
    

    def show_average(self):
        '''This is the command for the generate_avgs_button. When clicked, it will check to see which option was selected
        and generate a plot of the option selected. The plot generated is then displayed on the window.'''
        idx = self.averages_button.curselection()
        if len(idx) == 1:
            option = int(idx[0])
            if option == 0:
                self.plot_aof5()
                plot_image1 = PhotoImage(file='plot_aof5.png')
                self.average_plot_label['image'] = plot_image1
            if option == 1:
                self.plot_aof12()
                plot_image2 = PhotoImage(file='plot_aof12.png')
                self.average_plot_label['image'] = plot_image2
            if option == 2:
                self.plot_aof100()
                plot_image3 = PhotoImage(file='plot_aof100.png')
                self.average_plot_label['image'] = plot_image3
    

    def plot_aof5(self):
        '''Grabs the data, gets all the averages of 5, and creates a line graph of the rolling averags of 5. The STD of the 
        rolling averages of 5 and the best average of 5 is shown as well. The plot is then saved into the directory so that 
        it can be displayed on the window.'''
        data = self.data
        aof5 = rs.STD(data)
        aof5.calculateAof5STD()
        rolling_aof5 = aof5.getAveragesOf5()
        aof5_STD = aof5.getAof5STD()
        best_aof5 = aof5.getBestAof5()
        overall_avg = aof5.getMeanAof5()
        x_axis = []
        y_axis = []
        for entry in rolling_aof5:
            x_axis.append(entry[0])
            y_axis.append(entry[1])
        plt.clf()
        plt.plot(x_axis, y_axis, '-o', label='STD = ' + str(aof5_STD) + '\n' + 'Best Aof5: ' + str(best_aof5) + '\n' + 'Overall Average: ' + str(overall_avg))
        plt.title("Rolling Averages of 5")
        plt.xlabel("Solve No.")
        plt.ylabel("Time (s)")
        plt.legend(loc='upper right')
        plt.savefig('plot_aof5.png')
    

    def plot_aof12(self):
        '''Grabs the data, gets all the averages of 12, and creates a line graph of the rolling averags of 12. The STD of the 
        rolling averages of 12 and the best average of 12 is shown as well. The plot is then saved into the directory so that 
        it can be displayed on the window.'''
        data = self.data
        aof12 = rs.STD(data)
        aof12.calculateAof12STD()
        rolling_aof12 = aof12.getAveragesOf12()
        aof12_STD = aof12.getAof12STD()
        best_aof12 = aof12.getBestAof12()
        overall_avg = aof12.getMeanAof12()
        x_axis = []
        y_axis = []
        for entry in rolling_aof12:
            x_axis.append(entry[0])
            y_axis.append(entry[1])
        plt.clf()
        plt.plot(x_axis, y_axis, '-o', label='STD = ' + str(aof12_STD) + "\n" + "Best Aof12: " + str(best_aof12) + '\n' + "Overall Average: " + str(overall_avg))
        plt.title("Rolling Averages of 12")
        plt.xlabel("Solve No.")
        plt.ylabel("Time (s)")
        plt.legend(loc='upper right')
        plt.savefig('plot_aof12.png')


    def plot_aof100(self):
        '''Grabs the data, gets all the averages of 100, and creates a line graph of the rolling averags of 100. The STD of the 
        rolling averages of 100 and the best average of 100 is shown as well. The plot is then saved into the directory so that 
        it can be displayed on the window.'''
        data = self.data
        aof100 = rs.STD(data)
        aof100.calculateAof100STD()
        rolling_aof100 = aof100.getAveragesOf100()
        aof100_STD = aof100.getAof100STD()
        best_aof100 = aof100.getBestAof100()
        overall_avg = aof100.getMeanAof100()
        x_axis = []
        y_axis = []
        for entry in rolling_aof100:
            x_axis.append(entry[0])
            y_axis.append(entry[1])
        plt.clf()
        plt.plot(x_axis, y_axis, '-o', label='STD = ' + str(aof100_STD) + "\n" + "Best Aof100: " + str(best_aof100) + '\n' + "Overall Average: " + str(overall_avg))
        plt.title("Rolling Averages of 100")
        plt.xlabel("Solve No.")
        plt.ylabel("Time (s)")
        plt.legend(loc='upper right')
        plt.savefig('plot_aof100.png')


    def time_trend(self):
        '''This is the command for the time trend option. When the option is clicked, it generates a line graph of the time trend 
        of the data set. The STD of all the times and the best time is shown as well. The plot is then saved into the directory so 
        that it can be displayed on the window.'''
        data = self.data
        times = rs.STD(data)
        times.calculateOverallSTD()
        list_of_times = times.getData()
        overall_std = times.getOverallSTD()
        best_time = times.getBestTime()
        overall_avg = times.getTotalMean()
        x_axis = []
        y_axis = []
        for entry in list_of_times:
            x_axis.append(entry[0])
            y_axis.append(entry[1])
        plt.clf()
        plt.plot(x_axis, y_axis, '-o',label='STD = ' + str(overall_std) + "\n" + "Best Time: " + str(best_time) + "\n" + "Overall Average: " + str(overall_avg))
        plt.title("Time Trend")
        plt.xlabel('Solve No.')
        plt.ylabel('Time (s)')
        plt.legend(loc='upper right')
        plt.savefig('time_trend.png')
        plot_image4 = PhotoImage(file='time_trend.png')
        self.time_plot_label['image'] = plot_image4
    

    def close_window(self):
        '''Closes the window, which closes the application.'''
        self.window.destroy()
    

def main():
    window = Tk()
    rubiksGUI = RubiksAnalysisGUI(window)
    window.mainloop()


if __name__ == "__main__":
    main()