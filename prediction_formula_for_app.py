
import pandas as pd
import sklearn.linear_model as lin
import pandas as pd





def f(speed, p):
    return p[0] + speed * p[1]

def predict_power_output_zero_to_five(speed):
    return f(speed, p)

def greater_than_five_to_ten(speed):
    return f(speed, p)

def greater_than_ten_to_fifteen(speed):
    return f(speed, p)


def greater_than_fifteen_to_twenty(speed):
    return f(speed, p)

def greater_than_twenty_to_twenty_five(speed):
    return f(speed, p)


# Load a dataset.
df = pd.read_csv('powerproduction.csv')

# We are removing the non zero values
cleansed_data_2 = df.loc[df['power'] > 0 ]

# filtering between values https://stackoverflow.com/questions/29370057/select-dataframe-rows-between-two-dates

zero_to_five = cleansed_data_2.loc[(cleansed_data_2['speed'] > 0) & (cleansed_data_2['speed']< 5)]
greater_than_five_to_ten = cleansed_data_2.loc[(cleansed_data_2['speed'] > 5) & (cleansed_data_2['speed']< 10)]
greater_than_ten_to_fifteen = cleansed_data_2.loc[(cleansed_data_2['speed'] > 10) & (cleansed_data_2['speed']< 15)]
greater_than_fifteen_to_twenty = cleansed_data_2.loc[(cleansed_data_2['speed'] > 15) & (cleansed_data_2['speed']< 20)]
greater_than_twenty_to_twenty_five = cleansed_data_2.loc[(cleansed_data_2['speed'] > 20) & (cleansed_data_2['speed']< 25)]


powerproduction = zero_to_five

speed = powerproduction["speed"].to_numpy()
y = powerproduction["power"].to_numpy()

speed = speed.reshape(-1, 1)

model = lin.LinearRegression()
model.fit(speed, y)
r = model.score(speed, y)
p = [model.intercept_, model.coef_[0]]


def send_zero():
    return 0
    
def predict_power_output_c(a):
    # If a user types wind speeds lower than 0.275 or equal higher than 24.499, it will be handled with an if statement and return 0

    if a <= 0.275:
        send_zero()
        

    if a >= 24.499:
        send_zero()


    #if a user inputs a wind speed between 0 - 5 mph, they will get a linear prediction from wind speed data betwween 0 and 5 mph.

    if a > 0 and a < 5:
        #Load a dataset.
        powerproduction = zero_to_five
        speed = powerproduction["speed"].to_numpy()
        y = powerproduction["power"].to_numpy()

        speed = speed.reshape(-1, 1)

        model = lin.LinearRegression()
        model.fit(speed, y)
        r = model.score(speed, y)
        p = [model.intercept_, model.coef_[0]]

        print(speed)
        predict_power_output_zero_to_five(speed)

    #if a user inputs a wind speed between 5 - 10 mph, they will get a linear prediction from wind speed data betwween 5 and 10 mph.

    if a > 5 and a < 10:
        #Load a dataset.
        powerproduction =  greater_than_five_to_ten
        speed = powerproduction["speed"].to_numpy()
        y = powerproduction["power"].to_numpy()

        speed = speed.reshape(-1, 1)

        model = lin.LinearRegression()
        model.fit(speed, y)
        r = model.score(speed, y)
        p = [model.intercept_, model.coef_[0]]

        greater_than_five_to_ten(speed)
        

    #if a user inputs a wind speed between 10 - 15 mph, they will get a linear prediction from wind speed data betwween 10 and 15 mph.
      
    if a > 10 and a < 15:
        #Load a dataset.
        powerproduction =  greater_than_ten_to_fifteen
        speed = powerproduction["speed"].to_numpy()
        y = powerproduction["power"].to_numpy()

        speed = speed.reshape(-1, 1)

        model = lin.LinearRegression()
        model.fit(speed, y)
        r = model.score(speed, y)
        p = [model.intercept_, model.coef_[0]]

        
        
        greater_than_ten_to_fifteen(speed)
        

    #if a user inputs a wind speed between 15 - 20 mph, they will get a linear prediction from wind speed data betwween 15 and 20 mph.

    if a > 15 and a < 20:
        #Load a dataset.
        powerproduction =  greater_than_fifteen_to_twenty
        
        speed = powerproduction["speed"].to_numpy()
        y = powerproduction["power"].to_numpy()

        speed = speed.reshape(-1, 1)

        model = lin.LinearRegression()
        model.fit(speed, y)
        r = model.score(speed, y)
        p = [model.intercept_, model.coef_[0]]

        greater_than_fifteen_to_twenty(speed)


    #if a user inputs a wind speed between 20 - 25 mph, they will get a linear prediction from wind speed data betwween 20 and 25 mph.

    if a > 20 and a < 25:
        #Load a dataset.
        powerproduction =  greater_than_twenty_to_twenty_five
        
        speed = powerproduction["speed"].to_numpy()
        y = powerproduction["power"].to_numpy()

        speed = speed.reshape(-1, 1)

        model = lin.LinearRegression()
        model.fit(speed, y)
        r = model.score(speed, y)
        p = [model.intercept_, model.coef_[0]]

        greater_than_twenty_to_twenty_five(speed)

print(predict_power_output_c(2))
