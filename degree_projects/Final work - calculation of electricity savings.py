import tkinter as tk
import tkinter.messagebox


#За даними Міненерго, загальне споживання електроенергії в Україні у 2021 році становило 154 826 млн кВт•год.
#С 1 июня 2023 года украинцы платят за электроэнергию по единому тарифу – 2,64 гривны за киловатт-час.
#За цими даними, в Україні (окрім окупованих територій) проживало 14,7 млн домогосподарств, із них 40% у великих містах, 28% у малих містах та 32% у селах. Середній розмір домогосподарства у великих та малих містах майже однаковий (2,54 та 2,53 особи відповідно), а в селах трохи більший – 2,67 особи.


# Dictionary of bulb types and their corresponding savings coefficients
savings_coefficients = {
    "Incandescent bulb": 0,
    "Halogen bulb": 0.133333333,
    "Fluorescent Compact bulb": 0.2,
    "LED": 0.733333333,
}

# Dictionary of bulb characteristics
bulbs = {
    "Incandescent bulb": {
        "Electrical power (W)": 75,
        "Luminous power (lm)": 840,
        "Luminous efficiency (lm/W)": 11.2,
        "Operating time per day (h)": 1,
        "Consumption/year (kWh)": 27.375,
        "Electricity cost/year (₴)": 3.5888625
    },
    "Halogen bulb": {
        "Electrical power (W)": 55,
        "Luminous power (lm)": 820,
        "Luminous efficiency (lm/W)": 14.9090909090909,
        "Operating time per day (h)": 1,
        "Consumption/year (kWh)": 20.075,
        "Electricity cost/year (₴)": 2.6318325
    },
    "Fluorescent Compact bulb": {
        "Electrical power (W)": 15,
        "Luminous power (lm)": 850,
        "Luminous efficiency (lm/W)": 56.6666666666667,
        "Operating time per day (h)": 1,
        "Consumption/year (kWh)": 5.475,
        "Electricity cost/year (₴)": 0.7177725
    },
    "LED": {
        "Electrical power (W)": 10,
        "Luminous power (lm)": 910,
        "Luminous efficiency (lm/W)": 91,
        "Operating time per day (h)": 1,
        "Consumption/year (kWh)": 3.65,
        "Electricity cost/year (₴)": 0.478515
    }
}

# Energy cost in UAH per kWh for Kiev
energy_cost_kiev = 2.64

# Room size in square meters
room_size = 15
lighting_power_per_sqm = 18

# Number of light bulbs in the apartment
num_light_bulbs = 5

# Total number of families in Ukraine
total_families_in_ukraine = 14900000

# Function to calculate annual savings for one family
def calculate_annual_savings():
    new_bulb_type = bulb_type_var.get()
    power_old_bulb = bulbs["Incandescent bulb"]["Electrical power (W)"]
    power_new_bulb = bulbs[new_bulb_type]["Electrical power (W)"]
    hours_per_day = bulbs[new_bulb_type]["Operating time per day (h)"]
    days_per_year = 365

    num_light_bulbs = int(num_bulbs_entry.get())

    consumption_per_year_old = (power_old_bulb * hours_per_day * days_per_year * num_light_bulbs) / 1000
    consumption_per_year_new = (power_new_bulb * hours_per_day * days_per_year * num_light_bulbs) / 1000

    cost_per_year_old = consumption_per_year_old * energy_cost_kiev
    cost_per_year_new = consumption_per_year_new * energy_cost_kiev

    room_consumption = room_size * lighting_power_per_sqm * hours_per_day * days_per_year * num_light_bulbs / 1000
    room_cost_per_year = room_consumption * energy_cost_kiev

    total_cost_per_year_old = cost_per_year_old + room_cost_per_year
    total_cost_per_year_new = cost_per_year_new + room_cost_per_year

    savings_per_year = total_cost_per_year_old - total_cost_per_year_new

    result_label.config(text=f"Annual savings for one family: {int(savings_per_year)} ₴")

# Create the graphical interface
root = tk.Tk()
root.title("Annual energy savings calculator")

# Dropdown menu for selecting new bulb type
bulb_type_label = tk.Label(root, text="New bulb type:")
bulb_type_label.pack()

bulb_type_var = tk.StringVar()
bulb_type_var.set("Halogen bulb")

bulb_type_menu = tk.OptionMenu(root, bulb_type_var, "Incandescent bulb", "Halogen bulb", "Fluorescent Compact bulb", "LED")
bulb_type_menu.pack()

# Label to display the result
result_label = tk.Label(root, text="")
result_label.pack()

# Entry field for the number of light bulbs
num_bulbs_label = tk.Label(root, text="Number of light bulbs:")
num_bulbs_label.pack()

num_bulbs_entry = tk.Entry(root)
num_bulbs_entry.pack()

# Button to calculate annual savings for one family
calculate_button = tk.Button(root, text="Annual savings for one family", command=calculate_annual_savings)
calculate_button.pack()

# Function to calculate total savings for all families in Ukraine
def calculate_total_savings():
    # Savings for one apartment per year
    annual_savings_per_apartment = 437.22

    # Get the selected bulb type from the dropdown menu
    selected_bulb_type = bulb_type_var.get()

    # Get the savings coefficient based on the selected bulb type
    savings_coefficient = savings_coefficients.get(selected_bulb_type, 1.0)

    # Calculate the total savings for one family in kWh
    savings_kwh_per_family = annual_savings_per_apartment * savings_coefficient

    # Calculate the total savings for all families in Ukraine in kWh
    total_savings_kwh = savings_kwh_per_family * total_families_in_ukraine

    # Convert total savings from kWh to MWh
    total_savings_mwh = total_savings_kwh / 1000

    # Calculate the total savings in days based on Ukraine's daily electricity consumption
    total_savings_days = total_savings_kwh / 424180822

    # Display the result in a message box
    result_message = f"Annual electricity savings for Ukraine: {int(total_savings_mwh)} MWh\n"
    result_message += f"Total savings in Days: {int(total_savings_days)} days"
    result_label.config(text=result_message)
    tk.messagebox.showinfo("Total Savings", result_message)

# Button to calculate savings for all families in Ukraine
calculate_total_button = tk.Button(root, text="Annual electricity savings for Ukraine", command=calculate_total_savings)
calculate_total_button.pack()

root.mainloop()



