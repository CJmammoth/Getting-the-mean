#create an array with data type and value list
import array as arr
#dislay text for mean
def display_mean():
    print("The mean of this is ")
#function in getting the mean
def get_mean():
    n = len(dataset)
    get_sum = sum(dataset)
    mean = get_sum / n
    m = str(mean)
    print(m)
#data
friends_usage = [9,10,5,7,5,7,5,4,3,5]
#values and variables for the function
sample_data = arr.array('i', friends_usage)
dataset = sample_data[0:10]
sample_data_list = dataset.tolist()
#output
display_mean()
get_mean()