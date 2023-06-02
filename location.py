import geocoder

def get_location():
    ip_loc = geocoder.ip('me')
    if ip_loc.ok:
        location = ip_loc.latlng
        print(location)
    else:
        print("Unable to fetch the location.")

get_location()
