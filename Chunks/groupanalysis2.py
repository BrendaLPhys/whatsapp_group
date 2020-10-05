df = pd.DataFrame(parsedData, columns=['Date', 'Time', 'Author', 'Message']) # Initialising a pandas Dataframe.
df["Date"] = pd.to_datetime(df["Date"])

# Deleting cases of Author being None
df = df.dropna()

# if for some reason you need to keep the original names, remove the following code:

#--------------------------------------------------------------------------------------------------------------
# Changing names
# Getting random names from a Game of thrones list
got_dt = pd.read_csv("https://raw.githubusercontent.com/mathbeveridge/asoiaf/master/data/asoiaf-all-nodes.csv")

# Defining names and aliases
names = list(df.Author.unique())
aliases = list(got_dt.Label.sample(len(names)))

# Replacing for Author
df.Author.replace(names, aliases, inplace=True)

# Replacing within messages
for (name, alias) in zip(names, aliases):
    df.Message = df.Message.str.replace(name, alias)
#-----------------------------------------------------------------------------------------------------------------

df.head()
df.info()