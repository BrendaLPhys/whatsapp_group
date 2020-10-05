messages_df['Time'].value_counts().head(10).plot.barh() 

plt.xlabel('Number of messages')

plt.ylabel('Time')