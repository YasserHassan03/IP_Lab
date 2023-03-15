import intel_jtag_uart
import sys

try:
    jtag=intel_jtag_uart.intel_jtag_uart()

except Exception as e:
    print(e)
    sys.exit(0)
print(jtag.read())
with open ('gimp.txt', 'w', newline='\r') as file:
    print("your gay")
    file.write('hello')      
    file.write((jtag.read()).decode())
file.close()

