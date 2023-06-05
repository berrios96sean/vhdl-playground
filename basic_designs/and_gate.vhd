-- Simple AND gate implementation
-- Inputs: A, B
-- Output: Y

entity AND_gate is
  port (
    A, B : in std_logic;
    Y    : out std_logic
  );
end entity AND_gate;

architecture behavioral of AND_gate is
begin
  Y <= A and B;
end architecture behavioral;
