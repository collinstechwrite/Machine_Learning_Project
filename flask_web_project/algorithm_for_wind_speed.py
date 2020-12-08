import sklearn.linear_model as lin
import pandas as pd

def do_linear_regression(data,text):

    # Load a dataset.
    text = text
    powerproduction = data
    def f(speed, p):
        return p[0] + speed * p[1]

    def predict_power_output(speed):
        return round(f(speed, p),2)

    speed = powerproduction["speed"].to_numpy()
    y = powerproduction["power"].to_numpy()

    speed = speed.reshape(-1, 1)

    model = lin.LinearRegression()
    model.fit(speed, y)
    r = model.score(speed, y)
    p = [model.intercept_, model.coef_[0]]

    return(predict_power_output(float(text)))

# Load a dataset.
df = pd.read_csv('powerproduction.csv')

# We are removing the non zero values
cleansed_data_2 = df.loc[df['power'] > 0 ]

# filtering between values see https://stackoverflow.com/questions/29370057/select-dataframe-rows-between-two-dates



# If a user types wind speeds lower than 0.275 or equal higher than 24.499, it will be handled with an if statement and return 0

def receive_text_from_form(text):
    text = text
    if text <= 0.275:
        return 0

    if text >= 24.499:
        return 0


    #if a user inputs a wind speed between 0 - 5 mph, they will get a linear prediction from wind speed data betwween 0 and 5 mph.

    if text > 0 and text <= 5:
        zero_to_five = cleansed_data_2.loc[(cleansed_data_2['speed'] > 0) & (cleansed_data_2['speed']<= 5)]
        return do_linear_regression(zero_to_five,text)


    #if a user inputs a wind speed between 5 - 10 mph, they will get a linear prediction from wind speed data betwween 5 and 10 mph.

    if text > 5 and text <= 10:
        greater_than_five_to_ten = cleansed_data_2.loc[(cleansed_data_2['speed'] > 5) & (cleansed_data_2['speed']<= 10)]
        return do_linear_regression(greater_than_five_to_ten,text)


    #if a user inputs a wind speed between 10 - 15 mph, they will get a linear prediction from wind speed data betwween 10 and 15 mph.
        
    if text > 10 and text <= 15:
        greater_than_ten_to_fifteen = cleansed_data_2.loc[(cleansed_data_2['speed'] > 10) & (cleansed_data_2['speed']<= 15)]
        return do_linear_regression(greater_than_ten_to_fifteen,text)

    #if a user inputs a wind speed between 15 - 20 mph, they will get a linear prediction from wind speed data betwween 15 and 20 mph.

    if text > 15 and text <= 20:
        greater_than_fifteen_to_twenty = cleansed_data_2.loc[(cleansed_data_2['speed'] > 15) & (cleansed_data_2['speed']<= 20)]
        return do_linear_regression(greater_than_fifteen_to_twenty,text)

        #if a user inputs a wind speed between 20 - 25 mph, they will get a linear prediction from wind speed data betwween 20 and 25 mph.

    if text > 20 and text <= 25:
        greater_than_fifteen_to_twenty = cleansed_data_2.loc[(cleansed_data_2['speed'] > 20) & (cleansed_data_2['speed']<= 25)]
        do_linear_regression(greater_than_twenty_to_twenty_five,text)

