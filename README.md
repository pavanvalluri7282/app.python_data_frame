# Introductory Python Data Manipulation Project

This Python project serves as an introduction to data manipulation in Python and the process of uploading data to MySQL Workbench. 
The project employs various libraries, including pandas, which is utilized for efficient data manipulation and analysis through data structures like DataFrames for 
tabular data handling. Additionally, it incorporates matplotlib.pyplot and sqlalchemy for creating static, animated, and interactive visualizations. 
The project also utilizes pymysql, a Python MySQL database adapter that facilitates communication between Python applications and MySQL databases.

## Getting Started

The subsequent guidelines will help you set up the project on your local machine to facilitate development and testing. 
Refer to the deployment section for information on how to launch the project on a live system.
### Prerequisites

Following softwares and sample dataset are used to develope and run this project:

1. Anaconda Navigator
2. MySQL Workbench
3. Dataset - Data of the top youtube channels from the website https://socialblade.com/youtube/

### Installing

Installing Anaconda Navigator and Starting Jupyter Notebooks

1. Go to the Anaconda website and download the suitable version for your operating system (Windows, macOS, or Linux).
2. Locate the installation file in your downloads folder and adhere to the installation instructions specific to your operating system. Anaconda Navigator is a component of the Anaconda distribution.
3. After the installation process is complete, initiate Anaconda Navigator, which can be found in your applications or programs menu.
4. Within Anaconda Navigator, locate and launch Jupyter Notebook from the home screen.
5. Once Jupyter Notebook opens in your web browser, click on the "New" button, and opt for "Python 3" to generate a new Python notebook.

### Installing MySQL workbench:

1. Go to the MySQL website and obtain the MySQL Workbench by downloading it from https://dev.mysql.com/downloads/windows/installer/8.0.html.
2. Find the installation file in your downloads folder and initiate the installation process by double-clicking on the executable (.exe) file.
3. Follow the prompts displayed on the screen to finalize the installation of MySQL Workbench.
4. For more comprehensive instructions, refer to https://www.mysqltutorial.org/install-mysql/.
5. Establish a password and generate a user profile to enable the connection and execution of MySQL Workbench queries from Python.

### Step by step details about the code: 

1. The DataFrame is populated by reading the 'youtube_dataset.csv' dataset.
2. Subsequent to loading the data, various validation steps are performed on the DataFrame. These involve employing methods and attributes such as .head(), .tail(), .shape, and .dtypes. The .head() method retrieves the initial rows of the DataFrame, while .tail() retrieves the concluding rows. The .shape attribute provides the dimensions (rows and columns) of the DataFrame, and .dtypes reveals the data types of each column.
3. The distribution of the top 1000 YouTube channels is computed and presented through the dist_channel_1000records function.
4. The distribution of the top 1000 YouTube channels is graphically represented using the plot_distribution function.
5. A CSV file is generated containing the records of the top 1000 YouTube channels. Subsequently, the data is loaded into a DataFrame, and employing the .to_sql() method, the contents of the Python DataFrame are transferred into MySQL Workbench.
6. A verification process is conducted in MySQL Workbench, wherein a select query confirms the successful loading of all 1000 records into the MySQL table.

### Built With

* [Anacoda Navigator 2.4.3 - Jupyter Notebook 6.5.4](https://www.anaconda.com/download) - Code in Python
* [MySQL Workbench 8.0.35](https://dev.mysql.com/downloads/windows/installer/8.0.html) - Database to store the results

### Authors

* Pavan Kumar V - [pavanvalluri7282](https://github.com/pavanvalluri7282)
* Narahara Karthik L - [Karthiklnk](https://github.com/Karthiklnk)

### License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details



### Thanks to Professor Omar Al-Trad, Ph.D.
