import tkinter as tk

# Dictionary of bulb characteristics for different bulb types for bulb power 100W
bulbs_data = {
    "Incandescent bulb": {
        "Electrical power (W)": 100,
        "Luminous power (lm)": 1200,
        "Luminous efficiency (lm/W)": 12
    },
    "Halogen bulb": {
        "Electrical power (W)": 70,
        "Luminous power (lm)": 1200,
        "Luminous efficiency (lm/W)": 17.1428571428571
    },
    "Fluorescent Compact bulb": {
        "Electrical power (W)": 20,
        "Luminous power (lm)": 1350,
        "Luminous efficiency (lm/W)": 67.5
    },
    "LED": {
        "Electrical power (W)": 12,
        "Luminous power (lm)": 1300,
        "Luminous efficiency (lm/W)": 108.333333333333
    }
}

# Energy cost in UAH per kWh for Kiev
energy_cost_kiev = 2.64


# Calculate annual electricity consumption for one bulb
def calculate_annual_consumption():
    bulb_type = bulb_type_var.get()
    num_bulbs = int(num_bulbs_var.get())
    operating_time = int(operating_time_var.get())
    bulb_info = bulbs_data[bulb_type]
    electrical_power = bulb_info["Electrical power (W)"]
    annual_consumption = (electrical_power / 1000) * 365 * operating_time * num_bulbs
    annual_consumption_label.config(text=f"Annual consumption: {annual_consumption:.2f} kWh")


# Calculate annual savings for one bulb compared to Incandescent bulb
def calculate_annual_savings():
    bulb_type = bulb_type_var.get()
    num_bulbs = int(num_bulbs_var.get())
    operating_time = int(operating_time_var.get())
    bulb_info = bulbs_data[bulb_type]
    electrical_power = bulb_info["Electrical power (W)"]
    luminous_efficiency = bulb_info["Luminous efficiency (lm/W)"]

    # Calculate the luminous efficiency of an Incandescent bulb
    incandescent_bulb_info = bulbs_data["Incandescent bulb"]
    incandescent_luminous_efficiency = incandescent_bulb_info["Luminous efficiency (lm/W)"]

    annual_consumption = (electrical_power / 1000) * 365 * operating_time * num_bulbs
    incandescent_annual_consumption = (incandescent_bulb_info[
                                           "Electrical power (W)"] / 1000) * 365 * operating_time * num_bulbs
    annual_cost = annual_consumption * energy_cost_kiev
    incandescent_annual_cost = incandescent_annual_consumption * energy_cost_kiev
    annual_savings = incandescent_annual_cost - annual_cost

    # Convert annual_savings to an integer for whole UAH
    annual_savings_label.config(text=f"Annual savings: {int(annual_savings)} UAH")


# Create the main window
root = tk.Tk()
root.title("\U0001F4A1 Bulb calculator 100W")

# Label and entry for specifying the number of bulbs
num_bulbs_label = tk.Label(root, text="Number of bulbs:")
num_bulbs_var = tk.StringVar()
num_bulbs_entry = tk.Entry(root, textvariable=num_bulbs_var)
num_bulbs_var.set(1)  # Default value

# Label and entry for specifying operating time per day
operating_time_label = tk.Label(root, text="Operating time per day (h):")
operating_time_var = tk.StringVar()
operating_time_entry = tk.Entry(root, textvariable=operating_time_var)
operating_time_var.set(4)  # Default value

# Dropdown menu for selecting bulb type
bulb_type_label = tk.Label(root, text="Bulb Type:")
bulb_type_var = tk.StringVar()
bulb_type_var.set("Incandescent bulb")  # Default value
bulb_type_option_menu = tk.OptionMenu(root, bulb_type_var, *bulbs_data.keys())

# Button to calculate annual savings
calculate_savings_button = tk.Button(root, text="Calculate annual savings:", command=calculate_annual_savings)

# Labels to display the results
annual_consumption_label = tk.Label(root, text="")
annual_savings_label = tk.Label(root, text=" 0 UAH")

# Grid layout for widgets
num_bulbs_label.grid(row=0, column=0)
num_bulbs_entry.grid(row=0, column=1)
operating_time_label.grid(row=1, column=0)
operating_time_entry.grid(row=1, column=1)
bulb_type_label.grid(row=2, column=0)
bulb_type_option_menu.grid(row=2, column=1)
calculate_savings_button.grid(row=3, column=0)
annual_savings_label.grid(row=3, column=1, columnspan=2)

# Start the main loop
root.mainloop()