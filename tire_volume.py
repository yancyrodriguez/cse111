#week 01 tire volume
#additional request has been added. The user is requested to enter a phone number
import math
from datetime import datetime
#input from user
tire_width = float(input('Enter the width of the tire in mm (ex 205):'))
aspect_ratio = float(input('Enter the aspect ratio of the tire (ex 60):'))
diameter_wheel = float(input('Enter the diameter of the wheel in inches (ex 15):'))

total = (((math.pi * (tire_width**2) * aspect_ratio)) * ((tire_width * aspect_ratio) + (2540 * diameter_wheel)) / 10000000000)
#compute the volume
print(f'The aproximate volume is: {total: .2f} liters')
#convert to integers 
tire_width = int(tire_width)
aspect_ratio = int(aspect_ratio)
diameter_wheel = int(diameter_wheel)

total = round(total, 2)
today = datetime.now()
today = f'{today: %Y-%m-%d}'

line_to_write = f'{today}, {tire_width}, {aspect_ratio}, {diameter_wheel}, {total}'

#write into a text
with open('volumes.txt', 'at') as volume_file:
    volume_file.write('\n' + line_to_write)

# If user wants to buy a tire
buy_tires = input('Do you want to buy tires with these dimensions? (yes/no): ').lower()

if buy_tires == 'yes':
    #ask for phone number
    phone_number = input('Enter your phone number: ')

    #phone number in the text file
    with open('volumes.txt', 'at') as volume_file:
        volume_file.write(f'\nPhone number: {phone_number}')

    print(f'Thank you! Your phone number {phone_number} has been saved.')
else:
    print('Thank you.')

  

