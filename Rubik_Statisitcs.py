'''
Alex Solano
CS 152
12/10/22
This program contains one parent class, Rubik_Statistics, and two child classes, Average and STD. This program is used to calculate
rolling averages of 5, 12, 100, best averages of 5, 12, 100, best times, and standard deviations of the rolling averages of 5, 12, 100,
and overall. There are also getters and calculate (setters) functions for each of the specific statisitcs. In order to create a Rubik_Statistics,
Average, or STD object, you only need to pass one argument, a list whose elements are lists containing the entry no. and solve time. This program
is specifically designed for the RubiksAnalysisGUI.py, but could also be used for similar data. The program also does its calculations by using the
stats module, a module I created earlier in this semester. There is also some test code at the bottom.

Call it like this in the terminal:
python3 Rubik_Statistics.py
'''
import stats


class Rubik_Statistics(object):
    '''This is the parent class.'''


    def __init__(self, data):
        '''Initiializes a Statistics object by taking a list.'''
        converted_data = []
        for entry in data:
            converted_data.append([int(entry[0]), float(entry[1])])
        self.data = converted_data
        self.best_time = 0
    

    def getData(self):
        '''Returns a tuple containing all the data.'''
        return tuple(self.data[:])
    

    def getBestTime(self):
        '''Returns the fastest time in the whole data set as a scalar value.'''
        data = self.getData()
        list_of_times = []
        for entry in data:
            list_of_times.append(entry[1])
        fastest_time = min(list_of_times)
        return fastest_time


class Average(Rubik_Statistics):
    '''This is a child class of Statistics, which is the parent class.'''


    def __init__(self, data):
        '''Initializes an Average object by using the parent class's init method. An Average object has 4 additional fields with default values.'''
        Rubik_Statistics.__init__(self, data)
        self.averagesof5 = []
        self.averagesof12 = []
        self.averagesof100 = []
        self.total_mean = 0
        self.mean_aof5 = 0
        self.mean_aof12 = 0
        self.mean_aof100 = 0
    

    def calculate_total_mean(self):
        '''This calculates the mean of the data set'''
        list_of_times = []
        data_set = self.getData()
        for entry in data_set:
            list_of_times.append(entry[1])
        total_mean = round(stats.mean(list_of_times), 2)
        self.total_mean = total_mean
    

    def getTotalMean(self):
        '''Returns the total mean of the data set as a scalar value'''
        return float(self.total_mean)
    

    def calculate_mean_aof5(self):
        '''This calculates the mean of the averages of 5.'''
        list_of_aof5 = []
        data_set = self.getAveragesOf5()
        for entry in data_set:
            list_of_aof5.append(entry[1])
        mean_aof5 = round(stats.mean(list_of_aof5), 2)
        self.mean_aof5 = mean_aof5
    

    def getMeanAof5(self):
        '''Returns the mean of the rolling averages of 5 as a scalar value'''
        return float(self.mean_aof5)
    

    def calculate_mean_aof12(self):
        '''This calculates the mean of the averages of 12.'''
        list_of_aof12 = []
        data_set = self.getAveragesOf12()
        for entry in data_set:
            list_of_aof12.append(entry[1])
        mean_aof12 = round(stats.mean(list_of_aof12), 2)
        self.mean_aof12 = mean_aof12


    def getMeanAof12(self):
        '''Returns the mean of the rolling averages of 12 as a scalar value'''
        return float(self.mean_aof12)


    def calculate_mean_aof100(self):
        '''This calculates the mean of the averages of 100.'''
        list_of_aof100 = []
        data_set = self.getAveragesOf100()
        for entry in data_set:
            list_of_aof100.append(entry[1])
        mean_aof100 = round(stats.mean(list_of_aof100), 2)
        self.mean_aof100 = mean_aof100
    

    def getMeanAof100(self):
        '''Returns the mean of the rolling averages of 100 as a scalar value'''
        return float(self.mean_aof100)
    

    def calculate_averages_of_5(self):
        '''This calculates all the average of 5's of the data set. To calculate it takes 5 data points in sequential order, drops the slowest 
        and fastest time and calculate the average of the other 3.'''
        aof_5 = []
        data_set = self.getData()
        data_size = len(data_set)
        # Need to check if there is enough data to calculate the averages
        if data_size < 5:
            pass
        else:
            # Starting the entry at 5 because you can only start calculating the average of 5 when you have at least 5 solves
            aof_5_entry = 5
            for i in range(data_size-4):
                set_of_5 = data_set[i:i+4]
                list_of_times = []
                for entry in set_of_5:
                    list_of_times.append(entry[1])
                # Need to remove the slowest and fastest time
                max_time = max(list_of_times)
                min_time = min(list_of_times)
                list_of_times.remove(max_time)
                list_of_times.remove(min_time)
                average = round(stats.mean(list_of_times), 2)
                aof_5.append([aof_5_entry, average])
                aof_5_entry += 1
        self.averagesof5 = aof_5
    

    def getAveragesOf5(self):
        '''Returns a tuple containing all the averages of 5'''
        return tuple(self.averagesof5[:])


    def calculate_averages_of_12(self):
        '''This calculates all the average of 12's of the data set. To calculate it takes 12 data points in sequential order, drops the slowest 
        and fastest times and calculate the average of the other 10.'''
        aof_12 = []
        data_set = self.getData()
        data_size = len(data_set)
        # Need to check if there is enough data to calculate the averages
        if data_size < 12:
            pass
        else:
            # Starting the entry at 12 because you can only start calculating the average of 12 when you have at least 12 solves
            aof_12_entry = 12
            for i in range(data_size-11):
                set_of_12 = data_set[i:i+11]
                list_of_times = []
                for entry in set_of_12:
                    list_of_times.append(entry[1])
                # Need to remove the slowest and fastest time
                max_time = max(list_of_times)
                min_time = min(list_of_times)
                list_of_times.remove(max_time)
                list_of_times.remove(min_time)
                average = round(stats.mean(list_of_times), 2)
                aof_12.append([aof_12_entry, average])
                aof_12_entry += 1
        self.averagesof12 = aof_12


    def getAveragesOf12(self):
        '''Returns a tuple containing all the averages of 12'''
        return tuple(self.averagesof12[:])


    def calculate_averages_of_100(self):
        '''This calculates all the average of 100's of the data set. To calculate it takes 100 data points in sequential order, drops the 5 
        slowest and fastest times and calculates the average of the other 90.'''
        aof_100 = []
        data_set = self.getData()
        data_size = len(data_set)
        # Need to check if there is enough data to calculate the averages
        if data_size < 100:
            pass
        else:
            # Starting the entry at 100 because you can only start calculating the average of 100 when you have at least 100 solves
            aof_100_entry = 100
            for i in range(data_size-99):
                set_of_100 = data_set[i:i+99]
                list_of_times = []
                for entry in set_of_100:
                    list_of_times.append(entry[1])
                # Need to remove the 5 slowest and fastest times from the data set
                for i in range(5):
                    max_time = max(list_of_times)
                    min_time = min(list_of_times)
                    list_of_times.remove(max_time)
                    list_of_times.remove(min_time)
                average = round(stats.mean(list_of_times), 2)
                aof_100.append([aof_100_entry, average])
                aof_100_entry += 1
        self.averagesof100 = aof_100
    

    def getAveragesOf100(self):
        '''Returns a tuple containing all the averages of 100'''
        return tuple(self.averagesof100[:])


    def getBestAof5(self):
        '''Returns the best average of 5 as a scalar'''
        averagesof5 = self.getAveragesOf5()
        list_of_averages = []
        for entry in averagesof5:
            list_of_averages.append(entry[1])
        best_time = min(list_of_averages)
        return float(best_time)
    

    def getBestAof12(self):
        '''Returns the best average of 12 as a scalar'''
        averagesof12 = self.getAveragesOf12()
        list_of_averages = []
        for entry in averagesof12:
            list_of_averages.append(entry[1])
        best_time = min(list_of_averages)
        return float(best_time)
    
    
    def getBestAof100(self):
        '''Returns the best average of 100 as a scalar'''
        averagesof100 = self.getAveragesOf100()
        list_of_averages = []
        for entry in averagesof100:
            list_of_averages.append(entry[1])
        best_time = min(list_of_averages)
        return float(best_time)


class STD(Average):
    '''This is a child class of Average, which is a child class of Statistics, which is the parent class.'''
    

    def __init__(self, data):
        '''Initializes a STD object by using Average's init method. A STD object has an additional 4 fields that have a default value'''
        Average.__init__(self, data)
        self.calculate_averages_of_5()
        self.calculate_mean_aof5()
        self.calculate_averages_of_12()
        self.calculate_mean_aof12()
        self.calculate_averages_of_100()
        self.calculate_mean_aof100()
        self.calculate_total_mean()
        self.aof5STD = 0
        self.aof12STD = 0
        self.aof100STD = 0
        self.overallSTD = 0
    

    def calculateAof5STD(self):
        '''This calculates the standard deviation of the averages of 5.'''
        aof5 = self.getAveragesOf5()
        list_of_times = []
        for entry in aof5:
            list_of_times.append(entry[1])
        aof5_std = round(stats.standard_deviation(list_of_times), 2)
        self.aof5STD = aof5_std


    def getAof5STD(self):
        '''Returns the standard deviation of the averages of 5 as a scalar value.'''
        return float(self.aof5STD)
    

    def calculateAof12STD(self):
        '''This calculates the standard deviation of the averages of 12.'''
        aof12 = self.getAveragesOf12()
        list_of_times = []
        for entry in aof12:
            list_of_times.append(entry[1])
        aof12_std = round(stats.standard_deviation(list_of_times), 2)
        self.aof12STD = aof12_std


    def getAof12STD(self):
        '''Returns the standard deviation of the averages of 12 as a scalar value.'''
        return float(self.aof12STD)
    

    def calculateAof100STD(self):
        '''This calculates the standard deviation of the averages of 100.'''
        aof100 = self.getAveragesOf100()
        list_of_times = []
        for entry in aof100:
            list_of_times.append(entry[1])
        aof100_std = round(stats.standard_deviation(list_of_times), 2)
        self.aof100STD = aof100_std


    def getAof100STD(self):
        '''Returns the standard deviation of the averages of 100 as a scalar value.'''
        return float(self.aof100STD)


    def calculateOverallSTD(self):
        '''This calculates the standard deviation of the whole data set.'''
        data = self.getData()
        list_of_times = []
        for entry in data:
            list_of_times.append(entry[1])
        overall_std = round(stats.standard_deviation(list_of_times), 2)
        self.overallSTD = overall_std
    

    def getOverallSTD(self):
        '''Returns the overall standard deviation of the whole data set as a scalar value'''
        return float(self.overallSTD)


# The  code below is testcode

def test_averages():
    '''This function is to test the methods of the Average class'''
    test_data = [['1058', '22.25'], ['1059', '28.94'], ['1060', '19.29'], ['1061', '21.74'], ['1062', '22.95'], ['1063', '20.01'], ['1064', '18.08'], ['1065', '27.75'], ['1066', '23.62'], ['1067', '20.53'], ['1068', '23.82'], ['1069', '21.60'], ['1070', '20.40'], ['1071', '20.35'], ['1072', '24.59'], ['1073', '24.24'], ['1074', '28.85'], ['1075', '23.22'], ['1076', '24.42'], ['1077', '19.93'], ['1078', '23.00'], ['1079', '17.77'], ['1080', '20.21'], ['1081', '19.15'], 
    ['1082', '47.34'], ['1083', '44.06'], ['1084', '23.05'], ['1085', '20.97'], ['1086', '21.18'], ['1087', '19.94'], ['1088', '20.28'], ['1089', '20.22'], ['1090', '21.16'], ['1091', '21.18'], ['1092', '20.89'], ['1093', '26.53'], ['1094', '19.25'], ['1095', '19.47'], ['1096', '27.91'], ['1097', '22.64'], ['1098', '25.59'], ['1099', '22.08'], ['1100', '22.50'], ['1101', '24.52'], ['1102', '22.83'], ['1103', '24.04'], ['1104', '22.06'], ['1105', '22.14'], ['1106', '23.50'], 
    ['1107', '21.79'], ['1108', '25.62'], ['1109', '19.72'], ['1110', '23.73'], ['1111', '20.71'], ['1112', '24.44'], ['1113', '23.19'], ['1114', '21.62'], ['1115', '21.06'], ['1116', '26.57'], ['1117', '27.06'], ['1118', '20.35'], ['1119', '21.15'], ['1120', '22.49'], ['1121', '18.11'], ['1122', '21.29'], ['1123', '23.68'], ['1124', '24.02'], ['1125', '21.13'], ['1126', '17.70'], ['1127', '21.23'], ['1128', '21.79'], ['1129', '20.71'], ['1130', '20.42'], ['1131', '21.70'], 
    ['1132', '19.18'], ['1133', '20.91'], ['1134', '21.87'], ['1135', '21.93'], ['1136', '19.74'], ['1137', '20.57'], ['1138', '20.68'], ['1139', '18.81'], ['1140', '30.73'], ['1141', '19.44'], ['1142', '19.71'], ['1143', '19.32'], ['1144', '24.47'], ['1145', '22.71'], ['1146', '20.02'], ['1147', '21.89'], ['1148', '19.82'], ['1149', '19.07'], ['1150', '20.55'], ['8924', '25.07'], ['8925', '21.39'], ['8926', '33.22'], ['8927', '33.62'], ['8928', '21.28'], ['8929', '26.65'], 
    ['8954', '20.99'], ['8955', '19.16'], ['8956', '21.04'], ['8957', '19.41'], ['8958', '17.51'], ['8959', '20.08'], ['8960', '15.25'], ['8961', '18.15'], ['8962', '19.08']]
    test_average = Average(test_data)
    test_average.calculate_averages_of_5()
    test_average.calculate_averages_of_12()
    test_average.calculate_averages_of_100()
    test_average.calculate_total_mean()
    list_aof5 = test_average.getAveragesOf5()
    best_aof5 = test_average.getBestAof5()
    list_aof12 = test_average.getAveragesOf12()
    best_aof12 = test_average.getBestAof12()
    list_aof100 = test_average.getAveragesOf100()
    best_aof100 = test_average.getBestAof100()
    total_mean = test_average.getTotalMean()
    # print(len(test_data))
    # print(len(test_data) - len(list_aof5)) # Should be 4
    print(list_aof5)
    print(best_aof5)
    # print(len(test_data) - len(list_aof12)) # Should be 11
    print(list_aof12)
    print(best_aof12)
    # print(len(test_data) - len(list_aof100)) # Should be 99
    print(list_aof100)
    print(best_aof100)
    print(total_mean)


def test_stand_dev():
    '''This function is to test the methods of the STD class'''
    test_data = [['1058', '22.25'], ['1059', '28.94'], ['1060', '19.29'], ['1061', '21.74'], ['1062', '22.95'], ['1063', '20.01'], ['1064', '18.08'], ['1065', '27.75'], ['1066', '23.62'], ['1067', '20.53'], ['1068', '23.82'], ['1069', '21.60'], ['1070', '20.40'], ['1071', '20.35'], ['1072', '24.59'], ['1073', '24.24'], ['1074', '28.85'], ['1075', '23.22'], ['1076', '24.42'], ['1077', '19.93'], ['1078', '23.00'], ['1079', '17.77'], ['1080', '20.21'], ['1081', '19.15'], 
    ['1082', '47.34'], ['1083', '44.06'], ['1084', '23.05'], ['1085', '20.97'], ['1086', '21.18'], ['1087', '19.94'], ['1088', '20.28'], ['1089', '20.22'], ['1090', '21.16'], ['1091', '21.18'], ['1092', '20.89'], ['1093', '26.53'], ['1094', '19.25'], ['1095', '19.47'], ['1096', '27.91'], ['1097', '22.64'], ['1098', '25.59'], ['1099', '22.08'], ['1100', '22.50'], ['1101', '24.52'], ['1102', '22.83'], ['1103', '24.04'], ['1104', '22.06'], ['1105', '22.14'], ['1106', '23.50'], 
    ['1107', '21.79'], ['1108', '25.62'], ['1109', '19.72'], ['1110', '23.73'], ['1111', '20.71'], ['1112', '24.44'], ['1113', '23.19'], ['1114', '21.62'], ['1115', '21.06'], ['1116', '26.57'], ['1117', '27.06'], ['1118', '20.35'], ['1119', '21.15'], ['1120', '22.49'], ['1121', '18.11'], ['1122', '21.29'], ['1123', '23.68'], ['1124', '24.02'], ['1125', '21.13'], ['1126', '17.70'], ['1127', '21.23'], ['1128', '21.79'], ['1129', '20.71'], ['1130', '20.42'], ['1131', '21.70'], 
    ['1132', '19.18'], ['1133', '20.91'], ['1134', '21.87'], ['1135', '21.93'], ['1136', '19.74'], ['1137', '20.57'], ['1138', '20.68'], ['1139', '18.81'], ['1140', '30.73'], ['1141', '19.44'], ['1142', '19.71'], ['1143', '19.32'], ['1144', '24.47'], ['1145', '22.71'], ['1146', '20.02'], ['1147', '21.89'], ['1148', '19.82'], ['1149', '19.07'], ['1150', '20.55'], ['8924', '25.07'], ['8925', '21.39'], ['8926', '33.22'], ['8927', '33.62'], ['8928', '21.28'], ['8929', '26.65'], 
    ['8954', '20.99'], ['8955', '19.16'], ['8956', '21.04'], ['8957', '19.41'], ['8958', '17.51'], ['8959', '20.08'], ['8960', '15.25'], ['8961', '18.15'], ['8962', '19.08']]
    test_std = STD(test_data)
    test_std.calculateAof5STD()
    test_std.calculateAof12STD()
    test_std.calculateAof100STD()
    test_std.calculateOverallSTD()
    std_aof5 = test_std.getAof5STD()
    std_aof12 = test_std.getAof12STD()
    std_aof100 = test_std.getAof100STD()
    std_overall = test_std.getOverallSTD()
    print(std_aof5)
    print(std_aof12)
    print(std_aof100)
    print(std_overall)

if __name__ == "__main__":
    test_averages()
    test_stand_dev()