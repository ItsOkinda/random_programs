import pywifi
import webbrowser
import time

def scan_wifi_networks():
    wifi = pywifi.PyWiFi()
    iface = wifi.interfaces()[0]

    iface.scan()
    #30 seconds wifi scan
    time.sleep(30)
    scan_results = iface.scan_results()

    if not scan_results:
        print("No WiFi networks found.")
    else:
        print("Available WiFi networks:")
        for i, result in enumerate(scan_results):
            print(f"{i + 1}. SSID: {result.ssid}")
            print(f"   MAC Address: {result.bssid}")
            print(f"   Signal Strength: {result.signal}")

        while True:
            try:
                choice = int(input("Enter the number of the WiFi network to connect to (0 to exit): "))
                if choice == 0:
                    break
                elif choice < 1 or choice > len(scan_results):
                    print("Invalid choice. Please enter a valid number.")
                else:
                    selected_network = scan_results[choice - 1]
                    ssid = selected_network.ssid
                    password = input(f"Enter the password for '{ssid}' (or leave empty for open networks): ")

                    if selected_network.akm[0] == pywifi.const.AKM_TYPE_NONE:
                        
                        connect_to_wifi(iface, ssid, None)
                    else:
                        connect_to_wifi(iface, ssid, password)

                    break
            except ValueError:
                print("Invalid input. Please enter a number.")

def connect_to_wifi(iface, ssid, password):
    wifi_profile = pywifi.Profile()
    wifi_profile.ssid = ssid
    if password is None:
        wifi_profile.auth = pywifi.const.AUTH_ALG_OPEN
    else:
        wifi_profile.auth = pywifi.const.AUTH_ALG_SHARED
        wifi_profile.akm.append(pywifi.const.AKM_TYPE_WPA2PSK)
        wifi_profile.cipher = pywifi.const.CIPHER_TYPE_CCMP
        wifi_profile.key = password

    iface.remove_all_network_profiles()
    profile = iface.add_network_profile(wifi_profile)

    iface.connect(profile)
    print(f"Connecting to '{ssid}'...")

    # establishing connection
    while iface.status() == pywifi.const.IFACE_CONNECTING:
        pass

    if iface.status() == pywifi.const.IFACE_CONNECTED:
        print(f"Connected to '{ssid}'")
        
            # wifi login page that you know this is way too common 
        if "192.168.1.1" or "192.168.0.1" in iface.gateway():
            print("yo kuna uradi")
            option= input.lower("wifi contains admin panel....  Do ou want to open it .....? (yes or no) :")
            if option == "yes":
                 webbrowser.open("http://192.168.1.1") 
            else:
                pass
        else:
                print("No login page detected for this network.")

        print(f"IP Address: {iface.iface.ifconfig()[0]['ip']}")
        print(f"DNS Servers: {', '.join(iface.dnsinfo())}")
    else:
        print('incorrect password or network error.')
if __name__ == "__main__":
    scan_wifi_networks()
