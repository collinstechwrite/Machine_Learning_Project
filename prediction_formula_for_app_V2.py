def find_speed(a):
    def f(speed, p):
        return p[0] + speed * p[1]

    def predict_power_output_b(speed):
        return f(speed, p)


    import pandas as pd

    # Load a dataset.
    powerproduction = pd.read_csv('powerproduction.csv')

    # We are removing the non zero values
    cleansed_data_2 = powerproduction.loc[powerproduction['power'] > 0 ]

    # filtering between values https://stackoverflow.com/questions/29370057/select-dataframe-rows-between-two-dates
    zero_to_five = cleansed_data_2.loc[(cleansed_data_2['speed'] > 0) & (cleansed_data_2['speed']< 5)]


    import sklearn.linear_model as lin
    import pandas as pd

    # Load a dataset.
    powerproduction = zero_to_five # analysing power production from 0 - 5 mph wind speeds only




    speed = powerproduction["speed"].to_numpy()
    y = powerproduction["power"].to_numpy()

    speed = speed.reshape(-1, 1)

    model = lin.LinearRegression()
    model.fit(speed, y)
    r = model.score(speed, y)
    p = [model.intercept_, model.coef_[0]]

    return predict_power_output_b(a)

print(find_speed(2))

