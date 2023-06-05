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


def extract_entity_info(vhdl_code):
    entity_match = re.search(r"entity\s+(\w+)", vhdl_code, re.IGNORECASE)
    if entity_match:
        entity_name = entity_match.group(1)
        port_match = re.search(r"port\s*\((.*?)\)\s*;", vhdl_code, re.IGNORECASE | re.DOTALL)
        if port_match:
            port_map = port_match.group(1)
            return entity_name, port_map.strip()
        else:
            print("Error: No port declaration found in the VHDL file.")
            return None, None
    else:
        print("Error: No entity block found in the VHDL file.")
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

    entity_name, port_map = extract_entity_info(vhdl_code)
    if entity_name is None or port_map is None:
        return

    tb_entity = f"entity tb is\nend tb;"

    # Analyze the VHDL code to extract relevant information for the testbench generation
    # Add code here to analyze the VHDL code and extract signals, components, stimuli, etc.

    # Generate the testbench code based on the analysis and command line parameters
    testbench_code = f"""\
-- Testbench for {vhdl_file_path}

library ieee;
use ieee.std_logic_1164.all;

{tb_entity}

architecture testbench of tb is
  -- Add signals, components, and other testbench components here
  -- Add signals here
  signal clk : std_logic;
  signal reset : std_logic;
  signal data_in : std_logic_vector(7 downto 0);
  signal data_out : std_logic_vector(7 downto 0);

  -- Add components here
  component {entity_name}
    port (
      -- Add entity ports here based on the extracted port map
      {port_map}
    );
  end component;

  signal dut_clk : std_logic;

begin
  -- Add testbench code here

  -- Instantiate the entity
  dut_inst : {entity_name}
    port map (
      -- Map the entity ports to signals or constants here if needed
    );

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
