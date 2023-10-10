"""

3. Create a python file named ShippingAddress. Declare the following variables:
                    name
                    building_number
                    street_name
                    city
                    state
                    zip_code

    Use concatenation to print the full shipping address

        Ex:
            Given data:
                name = "Aaron Kissinger"
                building_number = 13621A
                street_name = "Legacy Circle"
                city = "Fairfax"
                state = "VA"
                zip_code = 22030

            Output:
                Your shipping address is:
                        Aaron Kissinger
                        13621A Legacy Circle
                        Fairfax, VA 22030

"""

name = 'New Life'
building_number = 32
neighborhood = 'Pasakonak'
street_name = 'Ataturk'
city = 'Balikesir'
district = 'Bandirma'
zip_code = 10200

print(f'Your shipping address is: \n{name}\n{neighborhood} Mh.\n{street_name} Bulvari No:{building_number}\n{zip_code}\n{district} / {city}')
