# create a ride sharing app model like uber,ola,rapido etc  using inheritance and polymorphism for drivers, riders
# create a different types of rides like standard and premium, calculate the total fair based on the ride 


# class Types_of_rides:
#     def standard(self):
#         pass
#     def premium(self):
#         pass
# class Ride_Sharing_App(Types_of_rides):
#     def standard(self):
#         pass
#     def premium(self):
#         pass

# starting
# ending
# total km
# standard per km 9.5 + 1.5% comm
# premium per km 14 + 3.5% comm




# Ride Sharing App using Inheritance and Polymorphism

class Types_of_rides:
    def calculate_fare(self, total_km):
        pass


# Standard Ride
class StandardRide(Types_of_rides):

    def calculate_fare(self, total_km):
        per_km = 9.5
        commission = 1.5

        base_fare = total_km * per_km
        commission_amount = base_fare * commission / 100
        total_fare = base_fare + commission_amount

        return total_fare


# Premium Ride
class PremiumRide(Types_of_rides):

    def calculate_fare(self, total_km):
        per_km = 14
        commission = 3.5

        base_fare = total_km * per_km
        commission_amount = base_fare * commission / 100
        total_fare = base_fare + commission_amount

        return total_fare


# Driver Class
class Driver:

    def __init__(self, name, vehicle):
        self.name = name
        self.vehicle = vehicle

    def display_driver(self):
        print("Driver Name:", self.name)
        print("Vehicle:", self.vehicle)


# Rider Class
class Rider:

    def __init__(self, name):
        self.name = name

    def display_rider(self):
        print("Rider Name:", self.name)


# Ride Sharing App
class Ride_Sharing_App:

    def __init__(self, starting, ending, total_km, ride_type):
        self.starting = starting
        self.ending = ending
        self.total_km = total_km
        self.ride_type = ride_type

    def calculate_total_fare(self):
        # Polymorphism
        return self.ride_type.calculate_fare(self.total_km)

    def display_ride(self):
        print("\n----- Ride Details -----")
        print("Starting Point:", self.starting)
        print("Ending Point:", self.ending)
        print("Total Distance:", self.total_km, "KM")
        print("Total Fare: ₹", self.calculate_total_fare())


# Driver
driver = Driver("Sathish", "Honda City")

# Rider
rider = Rider("Rahul")

driver.display_driver()
rider.display_rider()


# Standard Ride
standard = StandardRide()

ride1 = Ride_Sharing_App(
    "Bangalore",
    "Electronic City",
    20,
    standard
)

ride1.display_ride()


# Premium Ride
premium = PremiumRide()

ride2 = Ride_Sharing_App(
    "Bangalore",
    "Whitefield",
    20,
    premium
)

ride2.display_ride()




