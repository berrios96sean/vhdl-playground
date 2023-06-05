-- Testbench for and_gate.vhd

library ieee;
use ieee.std_logic_1164.all;

entity tb is
end tb;

architecture testbench of tb is
  -- Add signals, components, and other testbench components here

  constant SIM_SPEED : time := 5 ns;

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
