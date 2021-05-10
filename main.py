import pandas as pd
import numpy as np
import csv

def main():

    df = load_data_frame()
    df = translate_data(df)

def load_data_frame():

    with open("transport.csv", "r", newline="") as fp:
        reader = csv.reader(fp, delimiter=";")
        df = pd.DataFrame(reader)
        df = df.drop(labels=[0,1], axis=0)
        new_header = df.iloc[0]
        df = df[1:]
        df.columns = new_header
        df = df.drop(labels=["_Svar-ID", "Resume-Code", "Start", "Dato og tid", "Deltagerstatus"], axis=1)

        return df

def translate_data(df):

    old_column_names = ["1. Hvor gammel er du?", "2. Er du mand eller kvinde?", "3. Hvilken form for by bor du i?", "4. Hvad er din civil status?",
                        "5. Har du hjemmeboende børn?", "6. Har du bil?", "7. Har du en cykel?", "8. Hvilken form for transport bruger du mest når du skal rundt i egen by?",
                        "9. Hvilken form for transport bruger du mest når du skal ud for egen by?", "10. Hvor langt har du til arbejde?",
                        "11. Hvilken form for transport bruger du mest til og fra arbejde?", "12. Hvor langt har du til skole?",
                        "13. Hvilken form for transport bruger du mest til og fra skole?", "14. Har parkerings muligheder indflydelse på dit valg af transport?",
                        "15. Hvis det er en solskinsdag - vælg det udsagn der passer bedst", "16. Hvis det er en regnvejrsdag - vælg det udsagn der passer bedst"]

    new_column_names = ["Age", "Gender", "City", "Civil status", "Kids living at home", "Owns a car", "Owns a bike", "Kind of transport within own city",
                        "Kind of transport outside own city", "Distance to work", "Transport to and from work", "Distance to school", "Transport to and from school",
                        "Does parkings have an influence", "Statement on a shiny day", "Statement on a rainy day"]

    for i in range(len(new_column_names)):
        df = df.rename(columns={old_column_names[i]:new_column_names[i]})

    df['Gender'] = df['Gender'].map({'Mand': 'Male', 'Kvinde': 'Female'})
    df['City'] = df['City'].map({'Forstad': 'Suburb', 'Storby': 'Big city', 'Landet': 'Country'})
    df['Civil status'] = df['Civil status'].map({'Single': 'Single', 'I forhold': 'In relationship', 'Ved ikke': 'Dont know'})
    df['Kids living at home'] = df['Kids living at home'].map({'ja': 'yes', 'nej': 'no'})
    df['Owns a car'] = df['Owns a car'].map({'ja': 'yes', 'nej': 'no'})
    df['Owns a bike'] = df['Owns a bike'].map({'ja': 'yes', 'nej': 'no'})
    df['Kind of transport within own city'] = df['Kind of transport within own city'].map({'Bil': 'Car', 'Knallert': 'Moped', 'Cykel': 'Bike', 'Tog': 'Train',
                                                                                           'Bus': 'Bus', 'Jeg går/løber': 'I walk/run', 'Andet': 'Other'})
    df['Kind of transport outside own city'] = df['Kind of transport outside own city'].map({'Bil': 'Car', 'Knallert': 'Moped', 'Cykel': 'Bike', 'Tog': 'Train',
                                                                                           'Bus': 'Bus', 'Jeg går/løber': 'I walk/run', 'Andet': 'Other'})
    df['Distance to work'] = df['Distance to work'].map({'Under 1 km': 'Under 1 km', 'Mellem 1-5 km': 'Between 1-5 km', 'Mellem 5-15 km': 'Between 5-15 km',
                                                         'Mellem 15-25 km': 'Between 15-25 km', 'Mellem 25-40 km': 'Between 25-40 km', 'Over 40 km': 'Over 40 km',
                                                         'Jeg arbejdeder kun hjemmefra': 'I only work from home', 'Jeg har ikke noget arbejde': 'I dont have a job'})
    df['Transport to and from work'] = df['Transport to and from work'].map({'Bil': 'Car', 'Knallert': 'Moped', 'Cykel': 'Bike', 'Tog': 'Train',
                                                                                           'Bus': 'Bus', 'Jeg går/løber': 'I walk/run', 'Jeg har ikke noget arbejde':
                                                                                 'I dont have a job', 'Andet': 'Other'})
    df['Distance to school'] = df['Distance to school'].map({'Under 1 km': 'Under 1 km', 'Mellem 1-5 km': 'Between 1-5 km', 'Mellem 5-15 km': 'Between 5-15 km',
                                                         'Mellem 15-25 km': 'Between 15-25 km', 'Mellem 25-40 km': 'Between 25-40 km', 'Over 40 km': 'Over 40 km',
                                                        'Jeg går ikke i skole': 'I dont go to school'})
    df['Transport to and from school'] = df['Transport to and from school'].map({'Bil': 'Car', 'Knallert': 'Moped', 'Cykel': 'Bike', 'Tog': 'Train',
                                                                                           'Bus': 'Bus', 'Jeg går/løber': 'I walk/run', 'Jeg går ikke i skole':
                                                                                 'I dont go to school', 'Andet': 'Other'})
    df['Does parkings have an influence'] = df['Does parkings have an influence'].map({'Ja': 'yes', 'Nej': 'no', 'Ved ikke': 'Dont know'})

    df['Statement on a shiny day'] = df['Statement on a shiny day'].map({'Jeg går eller cykler altid hvis afstanden passer til det': 'Walk/bike alwas if the weather fits',
                                                                         'Jeg går eller cykler en gang imellem hvis afstanden passer til det': 'Walk/bike sometimes if the weather fits',
                                                                         'Jeg går eller cykler sjældent også selvom afstanden passer til det': 'Walk/bike rarely even if the weather fits',
                                                                         'Jeg tager stort set altid tog, bus eller bil': 'Always train, bus or car',
                                                                         'Ved ikke': 'Dont know'})
    df['Statement on a rainy day'] = df['Statement on a rainy day'].map({'Jeg går eller cykler altid hvis afstanden passer til det': 'Walk/bike alwas if the weather fits',
                                                                         'Jeg går eller cykler en gang imellem hvis afstanden passer til det': 'Walk/bike sometimes if the weather fits',
                                                                         'Jeg går eller cykler sjældent også selvom afstanden passer til det': 'Walk/bike rarely even if the weather fits',
                                                                         'Jeg tager stort set altid tog, bus eller bil': 'Always train, bus or car',
                                                                         'Ved ikke': 'Dont know'})
    print()


if __name__ == '__main__':
    main()
