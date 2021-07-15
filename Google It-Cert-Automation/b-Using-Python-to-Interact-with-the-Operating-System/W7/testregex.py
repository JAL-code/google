import re

teststring= "Jan 31 14:38:13 joseph-VirtualBox gnome-shell[1070]: Errors from xkbcomp are not fatal to the X server"
regex = r"(?P<DateTime>^\w*.\d*.\d*\:\d*\:\d*). \b(?P<Computer>[\w\-]*)\b \b(?P<Program>[\w-]*)\[(?P<Errorcode>[\d]*)\]: \b(?P<Description>[\w\W]*)$\b"
parse_log = re.search(regex, teststring)
datetime, computer, program, errorcode, description = parse_log.groups()
#print("G1: {}, G2: {}, G3: {}, G4: {}, G5: {}".format(datetime, computer, program, errorcode, description))
