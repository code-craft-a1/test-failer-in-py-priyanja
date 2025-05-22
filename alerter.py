alert_failure_count = 0

def network_alert_stub(celcius):
    print(f'ALERT: Temperature is {celcius} celcius')
    # Return 200 for ok
    # Return 500 for not-ok
    returnCode=500
    if celcius<=100 and celcius>=10:
        returnCode=200  
    return returnCode

def alert_in_celcius(farenheit):
    print(f'ALERT: Temperature is {farenheit} farenheit')
    global alert_failure_count
    if not isinstance(farenheit, (int, float)):
        alert_failure_count += 1
        return
    celcius = (farenheit - 32) * 5 / 9
    returnCode = network_alert_stub(celcius)
    if returnCode != 200:
        # non-ok response is not an error! Issues happen in life!
        # let us keep a count of failures to report
        # However, this code doesn't count failures!
        # Add a test below to catch this bug. Alter the stub above, if needed.
        alert_failure_count += 1
