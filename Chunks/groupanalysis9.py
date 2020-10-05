text = " ".join(review for review in messages_df.Message)
print ("There are {} words in all the messages.".format(len(text)))