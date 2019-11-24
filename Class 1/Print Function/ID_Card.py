Name = "Syed Muhammad Moin Tirmizi"
Roll_No = "PIAIC52383"
Course = "AIC"
Distance_learning = "No"
City = "Islamabad"
Center = "Bahria University Auditorium"
Campus = "Main Campus"
Quarter = "Q1"
Day = "Sunday"
Time = "09:00 AM to 12:00 PM"
Batch = "3rd"

message = """
ID Card
Name: {}
Roll No: {}
Course: {}
Distance learning: {}
City: {}
Center: {}
Campus: {}
Quarter: {}
Day: {}
Time: {}
Batch: {}
"""

x = message.format(Name, Roll_No, Course, Distance_learning, City, Center, Campus, Quarter, Day, Time, Batch)
print (x)
