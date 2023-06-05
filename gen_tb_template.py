import sys
import re


def generate_testbench(vhdl_file_path):
    try:
        with open(vhdl_file_path, 'r') as file:
            vhdl_code = file.read()
    except FileNotFoundError:
        print(f"Error: File '{vhdl_file_path}' not found.")
        return

    entity_name_match = re.search(r"entity\s+(\w+)", vhdl_code, re.IGNORECASE)
    architecture_name_match = re.search(r"architecture\s+(\w+)", vhdl_code, re.IGNORECASE)

    if not entity_name_match:
        print("Error: No entity block found in the VHDL file.")
        return

    if not architecture_name_match:
        print("Error: No architecture block found in the VHDL file.")
        return

    entity_name = entity_name_match.group(1)
    architecture_name = architecture_name_match.group(1)

    testbench_code = f"""\
-- Testbench for {entity_name}'s {architecture_name} architecture

library ieee;
use ieee.std_logic_1164.all;

entity {entity_name}_tb is
end {entity_name}_tb;

architecture testbench of {entity_name}_tb is
  -- Add signals, components, and other testbench components here
begin
  -- Add test stimuli and assertions here
end testbench;
"""

    tb_file_path = vhdl_file_path.replace('.vhd', '_tb.vhd')

    with open(tb_file_path, 'w') as file:
        file.write(testbench_code)

    print(f"Testbench generated successfully at '{tb_file_path}'.")


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python tb_generator.py <vhdl_file_path>")
    else:
        vhdl_file_path = sys.argv[1]
        generate_testbench(vhdl_file_path)
