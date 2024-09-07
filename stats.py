''''
Alex Solano
10/04/2022
CS 152 A
In this program, we created functions to calculate and return the sum, mean, max, min, variance of data. This program also includes a test() function to make sure the functions work properly. Also,
in this program, for extension, we created a function to calculate and return the standard deviation and mode of data. The test() function was also used to make sure the functions work properly.

Call it like this in the terminal:
python3 stats.py
'''

def sum(numbers):
    '''This function takes a list type paramater and returns the total sum of the elements in the list.'''
    list_sum = 0.0
    for num in numbers:
        list_sum += num
    return list_sum

def test():
    '''This function checks to see if the other functions in stats.py are working properly by using a simple list and printing out the sum, mean, max, min, and variance of the list.'''
    test_list = [1, 2, 3, 4]
    test_sum = sum(test_list)
    print(test_sum)
    test_mean = mean(test_list)
    test_max = max(test_list)
    test_min = min(test_list)
    test_variance = variance(test_list)
    print(test_mean, test_max, test_min, test_variance)
    # the lines below were for testing the extension functions
    #extension_test_list1 = [5, 7, 9, 7, 3, 5, 7, 9, 7, 7, 2, 7, 6, 1, 10, 4, 8, 7, 8, 5]
    #extension_test_list2 = [11, 23, 24, 19, 24, 10, 9, 1, 300, 300, 301, 200, 11, 23] 
    #test_mode1 = mode(extension_test_list1)
    #test_mode2 = mode(extension_test_list2)
    #print("Mode of extension test list 1: " + str(test_mode1))
    #print("Mode of extension test list 2: " + str(test_mode2))
    #test_standard_variance1 = standard_deviation(extension_test_list1)
    #test_standard_variance2 = standard_deviation(extension_test_list2)
    #print("Standard Variance of test list 1: " + str(test_standard_variance1))
    #ethprint("Standard Variance of test list 1: " + str(test_standard_variance2))


def mean(data):
    '''This function takes a list type parameter, calculates the mean of the list, and returns the mean. '''
    mean = sum(data) / len(data)
    return mean

def min(data):
    '''This function takes a list type parameter, finds the min value of the list, and returns the min value.'''
    min = data[0]
    for num in data:
        if num < min:
            min = num
    return min

def max(data):
    '''This function takes a list type parameter, finds the max value of the list, and returns the max value.'''
    max = data[0]
    for num in data:
        if num > max:
            max = num
    return max

def variance(data):
    '''This function takes a list type parameter, finds the variance of the list, and returns the variance.'''
    data_mean = mean(data)
    sum_square_diff = 0
    denom = (len(data) - 1)
    for num in data:
        sum_square_diff += (num - data_mean) ** 2
    return sum_square_diff / denom

#extension functions
def mode(data):
    '''This function takes a list type parameter, find the mode, or the most common value(s), of the list, and returns the mode.'''
    count_list = [] # This empty list will hold the number of times its corresponding value from the data appears in the data
    for i in range(0, len(data)): # This for indexed loop will go through all the values of data
        current_value = data[i] # We set the current_value to the element of the list the loop is currently on
        count = 0 # This variable will keep track of the number of times the element of the list the loop is currently on
        for num in data: # This for each loop will go through the data
            if num == current_value: # This checks to see if the element this for each loop is on is equal to the current_value the for indexed loop is on
                count += 1 # Add 1 to count if the if conditional is true
        count_list.append(count) # After the for each loop goes through checking to see how many times the current_value appears in the data, we append the value to the list count_list
    max_count = -1 # This variable will keep track of what is the maximum amount of times a value appears in the data. We set it to -1 since the value will be greater than -1
    for value in count_list: # This for each loop will go through each element in the list mode_list
        if value > max_count: # This checks to see if the current value the for each loop is on is greater than max_count
            max_count = value # This will make the current max_count equal to the value the for each loop is on if the if conditional is true
    mode_of_data = [] # This empty list will hold the numbers who appear the same of times as the max amount of times a value appears in the data
    for i in range(0,len(count_list)): # This for indexed loop will go through all the values in the list count_list
        if count_list[i] == max_count: # This will check to see if the current value the for indexed loop is equal to max_count
            if data[i] not in mode_of_data: # This will check to see if the corresponding data value of the current value is not in list mode_of_data. This is to ensure we don't have any data values repeating in list mode_of_data.
                mode_of_data.append(data[i]) # This will append the corresponding data value of the current value the for indexed loop if the if conditional is true.
    return mode_of_data

def standard_deviation(data):
    '''This function takes a list type parameter, calculates the standard deviation of the list, and returns the standard deviation'''
    data_mean = mean(data)
    denom = len(data)
    sum_square_diff = 0
    for num in data:
        sum_square_diff += (num - data_mean) ** 2
    return ((sum_square_diff) / (denom)) ** 0.5

if __name__ == "__main__":
    test()