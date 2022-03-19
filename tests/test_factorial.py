# Main framework to test 
from algorithms.Factorial.Factorial import factorial

def test_factorial():
    # Act 
    result = factorial(4)

    # Assert 
    assert result == 24