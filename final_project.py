import pandas as pd
import matplotlib.pyplot as plt
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
month_positions = range(len(months))
month_to_position = {month: position for month, position in zip(months, month_positions)}
def line_graph(df):
    # convert the 'Month' column to datetime format
    df['Month'] = pd.to_datetime(df['Month'], format='%b-%y')
    # plotting
    plt.figure(figsize=(10, 6))
    plt.plot(df['Month'], df['Rate'], marker='o', color='b', linestyle='-')

    # adding labels and title
    plt.title('Monthly unemployment rate of women in the United States from March 2022 to March 2024')
    plt.xlabel('Month')
    plt.ylabel('Rate')
    plt.xticks(df['Month'], df['Month'].dt.strftime('%b %y'), rotation=45, ha='right')
    plt.ylim(0, 4.5)  # Setting y-axis limits
    plt.grid(True)

    # display the plot
    plt.tight_layout()
    plt.show()
def bar_graph(df):
    months = df['Month']
    unemployment_rates = df['Rate']
    # create a column chart
    plt.figure(figsize=(10, 6))
    plt.bar(months, unemployment_rates, color='blue', width=0.5)
    plt.title('Monthly unemployment rate of women in the United States from March 2022 to March 2024')
    plt.xlabel('Month')
    plt.ylabel('Unemployment Rate (%)')
    plt.xticks(rotation=90, ha='right')
    # set y-axis limits labels
    plt.ylim(0, 4.5)
    # format y-axis labels to two decimal places
    plt.gca().yaxis.set_major_formatter('{:.2f}'.format)
    plt.tight_layout()
    # show the chart
    plt.show()
# function to get the position of a month
def get_month_position(month):
    # map the months to their positions
    month_to_position = {month: position for month, position in zip(months, month_positions)}
    return month_to_position[month[:3]]
def two_bar_graph(df,months,month_positions):
    # add a new column to the DataFrame with the position of each month
    df['Month_Position'] = df['Month'].apply(get_month_position)    
    # filter data for each year
    df_2022 = df[df['Month'].str.contains('22')]
    df_2023 = df[df['Month'].str.contains('23')]
    df_2024 = df[df['Month'].str.contains('24')]
    # plotting
    plt.figure(figsize=(10, 6))
    # plot 2022 data in blue
    plt.bar(df_2022['Month_Position'] - 0.2, df_2022['Rate'], color='blue', label='Unemployment rate in 2022', width=0.15, align='center')
    # plot 2023 data in red
    plt.bar(df_2023['Month_Position'], df_2023['Rate'], color='red', label='Unemployment rate in 2023', width=0.15, align='center')

    # plot 2024 data in green
    plt.bar(df_2024['Month_Position'] + 0.2, df_2024['Rate'], color='green', label='Unemployment rate in 2024', width=0.15, align='center')

    # set x-axis ticks and labels
    plt.xticks(month_positions, months)

    # add labels and title
    #plt.xlabel('Month')
    #plt.ylabel('Rate')
    plt.title('Monthly unemployment rate of women in the United States from March 2022 to March 2024')
    plt.legend()
    plt.tight_layout()  # Adjust layout to prevent clipping of labels
    plt.show()
def main():
    df = pd.read_csv('Monthly unemployment rate of women in the United States from March 2022 to March 2024.csv')
    bar_graph(df)   
    two_bar_graph(df,months,month_positions)
    line_graph(df)
if __name__ == '__main__':
    main()
