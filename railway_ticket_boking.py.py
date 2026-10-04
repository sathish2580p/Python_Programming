# # create a class with the name railway dept and should contains list of trains details 
# # and each train details should be in the form of dictionary it should contains methods
# # like get train get_train_name(),get_day_of_run(),get_train_by_the_day(),total_revenue()
# # consider train details as false


# class Railway_Dept:
#     global alltrains
#     def get_train_name(self,train_NO):
#         for train in  alltrains:
#             if train_NO == train['trainno']:
#                 print(train['trainname'])
#                 break
#         else:
#             print("train no doesn't exists")


#     def get_train_b_day(self, day):
#         trains = []
#         for train in  alltrains:
#             if day.upper() in train['days_of_run']:
#                 trains.append(train['trainname'])
#             if len(trains) != 0:
#                 return trains
#             else:
#                 return "no trains for the day"
            
#     def total_revenue(self,train_NO,**seats):
#         for train in alltrains:
#             if train_NO == train['trainno']:
#                 print('Revenue breakup for :', train['trainname'])
#                 print('General :',seats['general'],'*',train['prices']['general'],'=',
#                 seats['general']*train['prices']['general'])
#                 print('sleeper :',seats['sleeper'],'*',train['prices']['sleeper'],'=',
#                 seats['sleeper']*train['prices']['sleeper'])
#                 print('ac :',seats['ac'],'*',train['prices']['ac'],'=',
#                 seats['ac']*train['prices']['ac'])
#                 break
#         else:
#             print('no train exists')

            


# alltrains = [
#     {
#         'trainno' : 342134,
#         'trainname' : 'mysore express',
#         'starting' : 'banglore',
#         'days_of_run' : ['MON','TUE','WED','THU','FRI','SAT'],
#         'prices' : {
#             'general' : 70,
#             'sleeper' : 150,
#             'ac' : 300
#         } 
#     },
#     {
#     'trainno' : 123456,
#     'trainname' : 'tirupati express',
#     'starting' : 'smvt',
#     'days_of_run' : ['MON','TUE','THU','FRI','SAT'],
#     'prices' : {
#         'general' : 150,
#         'sleeper' : 350,
#         'ac' : 600
#         } 
#     },
#     {
#     'trainno' : 987654,
#     'trainname' : 'kanyakumari  express',
#     'starting' : 'madurai',
#     'days_of_run' : ['MON','TUE','THU'],
#     'prices' : {
#          'general' : 250,
#          'sleeper' : 550,
#          'ac' : 700
#         } 
#     },
#     {
#     'trainno' : 257642,
#     'trainname' : 'howra express',
#     'starting' : 'renigunta',
#     'days_of_run' : ['MON','TUE','THU'],
#     'prices' : {
#         'general' : 350,
#         'sleeper' : 650,
#         'ac' : 1000
#         } 
#     }
# ]

# rd.get_train 
    



class Railway_Dept:

    def get_train_name(self, train_NO):
        for train in alltrains:
            if train_NO == train['trainno']:
                print("Train Name:", train['trainname'])
                break
        else:
            print("Train no doesn't exist")


    def get_day_of_run(self, train_NO):
        for train in alltrains:
            if train_NO == train['trainno']:
                print("Days of Run:", train['days_of_run'])
                break
        else:
            print("Train no doesn't exist")


    def get_train_by_the_day(self, day):

        trains = []

        for train in alltrains:
            if day.upper() in train['days_of_run']:
                trains.append(train['trainname'])

        if len(trains) != 0:
            return trains
        else:
            return "No trains for the day"


    def total_revenue(self, train_NO, **seats):

        for train in alltrains:

            if train_NO == train['trainno']:

                print("Revenue breakup for:", train['trainname'])

                general = seats.get('general', 0)
                sleeper = seats.get('sleeper', 0)
                ac = seats.get('ac', 0)

                general_revenue = general * train['prices']['general']
                sleeper_revenue = sleeper * train['prices']['sleeper']
                ac_revenue = ac * train['prices']['ac']

                print(
                    "General:",
                    general, "*",
                    train['prices']['general'],
                    "=",
                    general_revenue
                )

                print(
                    "Sleeper:",
                    sleeper, "*",
                    train['prices']['sleeper'],
                    "=",
                    sleeper_revenue
                )

                print(
                    "AC:",
                    ac, "*",
                    train['prices']['ac'],
                    "=",
                    ac_revenue
                )

                total = general_revenue + sleeper_revenue + ac_revenue

                print("Total Revenue:", total)

                break

        else:
            print("No train exists")


alltrains = [
    {
        'trainno': 342134,
        'trainname': 'mysore express',
        'starting': 'banglore',
        'days_of_run': ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT'],
        'prices': {
            'general': 70,
            'sleeper': 150,
            'ac': 300
        }
    },

    {
        'trainno': 123456,
        'trainname': 'tirupati express',
        'starting': 'smvt',
        'days_of_run': ['MON', 'TUE', 'THU', 'FRI', 'SAT'],
        'prices': {
            'general': 150,
            'sleeper': 350,
            'ac': 600
        }
    },

    {
        'trainno': 987654,
        'trainname': 'kanyakumari express',
        'starting': 'madurai',
        'days_of_run': ['MON', 'TUE', 'THU'],
        'prices': {
            'general': 250,
            'sleeper': 550,
            'ac': 700
        }
    },

    {
        'trainno': 257642,
        'trainname': 'howra express',
        'starting': 'renigunta',
        'days_of_run': ['MON', 'TUE', 'THU'],
        'prices': {
            'general': 350,
            'sleeper': 650,
            'ac': 1000
        }
    }
]


# Create object
rd = Railway_Dept()


# 1. Get train name
rd.get_train_name(342134)


# 2. Get days of run
rd.get_day_of_run(342134)


# 3. Get trains running on a particular day
print("\nTrains running on MON:")
print(rd.get_train_by_the_day("MON"))


# 4. Calculate total revenue
print()
rd.total_revenue(
    342134,
    general=10,
    sleeper=5,
    ac=2
)

