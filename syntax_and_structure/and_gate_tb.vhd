library ieee;
use ieee.std_logic_1164.all;

entity AND_gate_tb is
end entity AND_gate_tb;

architecture testbench of AND_gate_tb is
  component AND_gate is
    port (
      A, B : in std_logic;
      Y    : out std_logic
    );
  end component AND_gate;

  signal A_tb, B_tb, Y_tb : std_logic;

begin
  DUT: AND_gate
    port map (
      A => A_tb,
      B => B_tb,
      Y => Y_tb
    );

  stimulus_process: process
  begin
    A_tb <= '0';
    B_tb <= '0';
    wait for 10 ns;
    
    A_tb <= '0';
    B_tb <= '1';
    wait for 10 ns;
    
    A_tb <= '1';
    B_tb <= '0';
    wait for 10 ns;
    
    A_tb <= '1';
    B_tb <= '1';
    wait for 10 ns;
    
    wait; -- wait indefinitely
  end process stimulus_process;

end architecture testbench;
