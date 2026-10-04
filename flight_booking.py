# WAP for ticket resevation system for flights it should contains the flight details as follows 
# create two methods like generate tickets and book tickets


import random

allflights = [
    {
        'flightname': 'Indigo',
        'flightid': 'IND123',
        'starting': 'banglore',
        'endpoint': 'pune',
        'flighttype': 'domestic',
        'price': 4550,
        'food': 'yes',
        'total_seats_avail': 15
    },
    {
        'flightname': 'airindia',
        'flightid': 'air456',
        'starting': 'banglore',
        'endpoint': 'delhi',
        'flighttype': 'domestic',
        'price': 3500,
        'food': 'no',
        'total_seats_avail': 20
    },
    {
        'flightname': 'visa',
        'flightid': 'vis987',
        'starting': 'banglore',
        'endpoint': 'kuwait',
        'flighttype': 'international',
        'price': 50000,
        'food': 'yes',
        'total_seats_avail': 10
    }
]


class Flights:

    def generate_ticket(self, flightid, seats):

        for flight in allflights:

            if flightid == flight['flightid']:

                if seats <= flight['total_seats_avail']:

                    # Generate random ticket number
                    ticket_no = (
                        flight['flightname'][:3].upper()
                        + str(random.randint(1000, 9999))
                    )

                    return ticket_no

                else:
                    return "Not enough seats available"

        return "Flight not found"


    def book_ticket(self, flightid, seats):

        for flight in allflights:

            if flightid == flight['flightid']:

                # Check seat availability
                if seats <= flight['total_seats_avail']:

                    # Reduce available seats
                    flight['total_seats_avail'] -= seats

                    # Calculate total price
                    total_price = flight['price'] * seats

                    # Generate ticket
                    ticket = self.generate_ticket(flightid, seats)

                    print("\n----- TICKET DETAILS -----")
                    print("Ticket Number :", ticket)
                    print("Flight Name   :", flight['flightname'])
                    print("Flight ID     :", flight['flightid'])
                    print("Starting      :", flight['starting'])
                    print("Destination   :", flight['endpoint'])
                    print("Flight Type   :", flight['flighttype'])
                    print("Seats Booked  :", seats)
                    print("Food          :", flight['food'])
                    print("Price/Seat    :", flight['price'])
                    print("Total Price   :", total_price)
                    print("Seats Left    :", flight['total_seats_avail'])

                    return

                else:
                    print("Not enough seats available")
                    return

        print("Flight not found")


# Object creation
f = Flights()

# Book ticket
f.book_ticket('IND123', 2)          




