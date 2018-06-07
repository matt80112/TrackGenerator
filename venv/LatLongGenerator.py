import csv
import numpy as np
import folium
from tkinter import *


class LatLongGenerator:

    def __init__(self, master):
        frame = Frame(master)
        frame.pack()
        self.output_file = "Lat_Long.csv"

        self.lat_long_label = Label(frame, text = "Starting Lat/Long")
        self.lat_long_label.grid(row = 0, sticky=E)
        self.lat_entry = Entry(frame)
        self.lat_entry.grid(row = 0, column = 1)
        self.long_entry = Entry(frame)
        self.long_entry.grid(row=0, column=2)
        self.course_label = Label(frame, text = "Course")
        self.course_label.grid(row = 1, sticky = E)
        self.course_entry = Entry(frame)
        self.course_entry.grid(row=1, column=1)
        self.speed_label = Label(frame, text = "Speed (NM)")
        self.speed_label.grid(row = 2, sticky = E)
        self.speed_entry = Entry(frame)
        self.speed_entry.grid(row=2, column=1)
        self.sample_rate_label = Label(frame, text="Sample Rate")
        self.sample_rate_label.grid(row=3, sticky=E)
        self.sample_rate_entry = Entry(frame)
        self.sample_rate_entry.grid(row=3, column=1)
        self.hits_label = Label(frame, text="# of Hits")
        self.hits_label.grid(row=4, sticky=E)
        self.hits_entry = Entry(frame)
        self.hits_entry.grid(row=4, column=1)
        self.enter_button = Button(frame, text="Enter", command = self.calculate_values)
        self.enter_button.grid(row = 5, column = 1)
        self.quit_button = Button(frame, text="Quit", command = frame.quit)
        self.quit_button.grid(row=5, column=2)

    def calculate_values(self):
        lat = float(self.lat_entry.get())
        long = float(self.long_entry.get())
        course = int(self.course_entry.get())
        speed = float(self.speed_entry.get())
        sample_rate = float(self.sample_rate_entry.get())
        hits = int(self.hits_entry.get())
        a = np.array([long, lat])

        with open(self.output_file, 'w') as fout:
            wrtr = csv.writer(fout)
            for row in range(hits):

                d = (speed * sample_rate) / 216000
                x = d * (np.sin(np.degrees(course)))
                y = d * (np.cos(np.degrees(course)))

                if (0 < course < 90):
                    lat += x
                    long = long + y
                    row = [lat, long, course, speed]
                    wrtr.writerow(row)
                elif (90 < course < 180):
                    lat = lat - x
                    long = long - y
                    row = [lat, long, course, speed]
                    wrtr.writerow(row)
                elif (180 < course < 270):
                    lat = lat - x
                    long = long + y
                    row = [lat, long, course, speed]
                    wrtr.writerow(row)
                else:
                    lat += x
                    long = long - y
                    row = [lat, long, course, speed]
                    wrtr.writerow(row)



if __name__ == '__main__':
    root = Tk()
    lat_long = LatLongGenerator(root)
    root.mainloop()
    maptit