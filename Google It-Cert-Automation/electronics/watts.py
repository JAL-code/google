voltage = 12  # DC voltage in volts
current = 0.050  # current in amperes
resistance = 0.12  # resistance in ohms

power = (current ** 2) * resistance  # power in watts

print("The power consumed by the wire is {:.7f} watts.".format(power))
