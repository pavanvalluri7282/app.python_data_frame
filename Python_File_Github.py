# Import the required libraries

import pandas as pd
import matplotlib.pyplot as plt
from sqlalchemy import create_engine
import pymysql

df = pd.read_csv("youtube_dataset.csv")

# Verify if the dataset is loaded properly
df.head()
df.tail()

# Verify the no. of rows and columns of the dateset
df.shape


# Verify the characteristics of the columns/variables
df.dtypes


# Define the function

def dist_channel_1000records(dataset):
    
    # Take the top 1000 records i.e, the top 1000 channels
    df_top_1000_records = dataset[:1000]
    
    # 'NaN' values in the column 'channeltype' are replaced with string 'N.A'    
    df_top_1000_records.channeltype = df_top_1000_records.channeltype.fillna('N.A')
    
    # Calculate the distribution of channel type from the top 1000 records and store it in a dictionary
    channel_type_dist = df_top_1000_records['channeltype'].value_counts().to_dict()
    
    # Return the values of the distribution
    return channel_type_dist


# Call the function and print the result
df_top1000_records = dist_channel_1000records(df)
print(df_top1000_records)

# Plot the Distribution of the 1000 channels
def plot_distribution(df_top1000_records):
    # Extract the values from the dictionary into two lists
    channel_types = list(df_top1000_records.keys())
    frequency = list(df_top1000_records.values())

    # Set the graph size
    plt.figure(figsize=(10, 6))  

    # Create the barplot
    plt.bar(channel_types, frequency, color='springgreen')

    # Set labels and title
    plt.xlabel('Channel Type')
    plt.ylabel('Frequency')
    plt.title('Distribution of Channel Types of top 1000 youtube channels')

    # Rotate x-axis labels for better visibility
    plt.xticks(rotation=45, ha='right')

    # Show the plot
    plt.show()


# Call the function and plot the graph
plot_distribution(df_top1000_records)


# Create engine
# REPLACE THE FOLLOWING
# User_name:password WITH YOUR USER NAME AND PASSWORD
# youtube WITH YOUR DATABASE NAME

engine = create_engine('mysql+pymysql://User_name:password@localhost/youtube')


# Specify the connection string
conn = engine.connect()


# Take the top 1000 records i.e, the top 1000 channels
df_top_1000_records = df[:1000]

# Create a CSV file from the DataFrame
df_top_1000_records.to_csv('csv_top1000_records')

# Load CSV file into MySQL table
df_csv = pd.read_csv("csv_top1000_records")
df_csv.to_sql('csv_top1000_records', conn, if_exists='replace', index=False)

