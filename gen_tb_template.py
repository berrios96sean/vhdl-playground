import sys
import re


def extract_simulation_speed(simulation_speed):
    # Extract the numeric value and unit from the simulation speed argument
    match = re.match(r"(\d+)(\D+)", simulation_speed)
    if match:
        value = match.group(1)
        unit = match.group(2)
        return value, unit
    else:
        print("Error: Invalid simulation speed argument.")
        return None, None


def generate_testbench(vhdl_file_path, simulation_speed):
    value, unit = extract_simulation_speed(simulation_speed)
    if value is None or unit is None:
        return

    # Read VHDL code from the file
    try:
        with open(vhdl_file_path, 'r') as file:
            vhdl_code = file.read()
    except FileNotFoundError:
        print(f"Error: File '{vhdl_file_path}' not found.")
        return

    # Analyze the VHDL code to extract relevant information for the testbench generation
    # Add code here to analyze the VHDL code and extract signals, components, stimuli, etc.

    # Generate the testbench code based on the analysis and command line parameters
    testbench_code = f"""\
-- Testbench for {vhdl_file_path}

library ieee;
use ieee.std_logic_1164.all;

entity tb is
end tb;

architecture testbench of tb is
  -- Add signals, components, and other testbench components here

  constant SIM_SPEED : time := {value} {unit};

begin
  -- Add test stimuli and assertions here

  -- Add code here to stimulate the DUT and perform assertions based on the simulation speed
  stimulus_process: process
  begin
    -- Add code here to generate test stimuli
    -- e.g., signal_name <= '1';
    wait for SIM_SPEED / 2;

    -- Add code here to perform assertions
    -- e.g., assert signal_name = '0' report "Signal mismatch" severity error;
    wait for SIM_SPEED / 2;

    -- Repeat the stimuli and assertions as necessary
  end process stimulus_process;

end testbench;
"""

    tb_file_path = vhdl_file_path.replace('.vhd', '_tb.vhd')

    with open(tb_file_path, 'w') as file:
        file.write(testbench_code)

    print(f"Testbench generated successfully at '{tb_file_path}'.")


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Usage: python tb_generator.py <vhdl_file_path> <simulation_speed>")
    else:
        vhdl_file_path = sys.argv[1]
        simulation_speed = sys.argv[2]
        generate_testbench(vhdl_file_path, simulation_speed)
