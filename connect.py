def polacznie():
    import network
    ssid = '***'
    password = '***'
    
    n = network.WLAN(network.STA_IF)
    n.active(True)
    station.connect('ssid','password')
    while station.isconnectied() == False:
        print('brak polaczenia')