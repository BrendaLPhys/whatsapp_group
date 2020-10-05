#changed message count to Word_Count because messagecount did not exist in the dataframe date_df

date_df = messages_df.groupby("Date").sum()

date_df.reset_index(inplace=True)

fig = px.line(date_df, x="Date", y="Word_Count", title='Number of Messages as time moves on.')

fig.update_xaxes(nticks=20)

fig.show()