from win10toast import ToastNotifier # This library should be installed in order to run this program (pip install win10toast)
import psutil # This library should be installed in order to run this program (pip install psutil)

battery_percentage = psutil.sensors_battery() # For getting the battery percentage

# battery percent will return the current battery prcentage
percentage = battery_percentage.percent
charging = battery_percentage.power_plugged

if charging:
    if percentage == 100:
        charging_message = "Unplug your Charger"
    else:
        charging_message = "Charging"
else:
    charging_message = "Not Charging"
message = str(percentage)+ "% Charged\n" + charging_message

notify = ToastNotifier()
notify.show_toast("Battery", message, icon_path=" ",duration=10,threaded=False)