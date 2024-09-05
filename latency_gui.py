import tkinter as tk
from tkinter import messagebox
import subprocess
import random

class LatencyChanger:
	def __init__(self, master): 		
		self.master = master
		master.title("Latency Changer")
		
		self.latency_label = tk.Label(master, text="Current latency: N/A")
		self.latency_label.pack(pady=10)

		self.latency_counter = 0
		self.latency_counter_label = tk.Label(master, text=f"Order: {self.latency_counter}")
		self.latency_counter_label.pack()
		
		self.init_latency_values()
		random.shuffle(self.latency_values)
		self.random_latency_button = tk.Button(master, text="Random", command=self.random_latency, width = 10, height = 2, pady = 10, padx = 5)
		self.random_latency_button.pack(side =tk.LEFT, padx=5, pady=5)
		
		self.remove_latency_button = tk.Button(master, text="Reset", command=self.reset_latency, width=10, height=2, pady=10, padx=5)
		self.remove_latency_button.pack(pady=5, padx = 5, side = tk.LEFT)
		
		self.quit_button = tk.Button(master, text="Quit", command=master.quit,  width = 10, height = 2, pady = 10, padx = 5)
		self.quit_button.pack(pady = 5, padx = 5, side = tk.RIGHT)
		
		self.input_label = tk.Label(master, text="(0-10000ms):")
		self.input_label.pack(pady=10)
		
		self.input_entry = tk.Entry(master, width=10)
		self.input_entry.pack()
		
		self.submit_button=tk.Button(master, text="Submit", command=self.submit_latency, width=10, height = 1, pady=3, padx = 5)
		self.submit_button.pack(pady=10)

	def init_latency_values(self):
		self.latency_values = [0, 50, 100]
		random.shuffle(self.latency_values)
		
	def random_latency(self):
		if not hasattr(self, 'latency_values') or not self.latency_values:
			self.init_latency_values()
			self.latency_counter = 0
		latency = self.latency_values.pop()
		self.change_latency(latency)
		self.latency_counter += 1
		self.latency_counter_label.config(text=f"Order: {self.latency_counter}")

	def reset_latency(self):
		self.change_latency(0)
		self.init_latency_values()
		self.latency_counter = 0
		self.latency_counter_label.config(text=f"Order: {self.latency_counter}")
			
	def change_latency(self, latency):
		subprocess.call(["bash", "-c", f"source .bashrc && setlat {latency}"])
		self.latency_label.config(text=f"Current latency: {latency}ms")
	
	def submit_latency(self):
		try:
			latency =int(self.input_entry.get())
			if latency < 0 or latency > 10000:
				raise ValueError
			self.change_latency(latency)
			self.input_entry.delete(0, tk.END)
		except ValueError:
			messagebox.showerror("Invalid Input", "Please enter a valid latency value (0-10000ms)")
			self.input_entry.delete(0, tk.END)
			
root = tk.Tk()
my_gui = LatencyChanger(root)
root.mainloop()
		
