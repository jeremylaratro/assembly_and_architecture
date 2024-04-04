# Calculate the 32-bit hex address of a given MIPS instruction. 
# Need to know:
# - register numbers
# - opcode
# - function code


# Example given values:
# sltu $t3, $fp, $a1
# CHANGE values for problem
rs_value = 30  # $fp
rt_value = 5   # $a1
rd_value = 11  # $t3
shamt_value = 0
funct_value = 0x2B  # func code for `sltu`

# Constants for shifting:
# This is an r-type instruction so:
# opcode (6) | rs (5) | rt (5) | rd (5) | shamt (5) | funct (6)
# rs shift = 6 + 5 + 5 + 5 .. etc

shift_rs = 21
shift_rt = 16
shift_rd = 11
shift_shamt = 6


# Shift performed by doing (register value * (2^shift))
# Ex: rs = 30 and is 21 bits left, so val = (30 * (2**21))

rs_shifted = rs_value * (2 ** shift_rs)
rt_shifted = rt_value * (2 ** shift_rt)
rd_shifted = rd_value * (2 ** shift_rd)
shamt_shifted = shamt_value * (2 ** shift_shamt)  # This will remain 0
funct_shifted = funct_value  # funct does not need to be shifted, already in correct position


# Convert the shifted values to hexadecimal (func code is already in hex)

rs_hex = hex(rs_shifted)
rt_hex = hex(rt_shifted)
rd_hex = hex(rd_shifted)
shamt_hex = hex(shamt_shifted)  # Unused - will be '0x0' since shamt_value is 0
funct_hex = hex(funct_shifted)  # Convert to hex, even though it's already provided as hex

rs_hex, rt_hex, rd_hex, shamt_hex, funct_hex
