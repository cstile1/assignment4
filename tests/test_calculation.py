# tests/test_calculations.py

"""
Unit tests for the calculator_calculations module using pytest.

This test suite covers both positive and negative scenarios for the Calculation
classes and the CalculationFactory. It ensures that calculations execute correctly,
the factory creates appropriate instances, and error handling behaves as expected.

Tests are organized following the AAA (Arrange, Act, Assert) pattern and adhere
to PEP8 standards for code style and formatting.
"""

import pytest
from unittest.mock import patch
from app.operation import Operation
from app.calculation import (
    CalculationFactory,
    AddCalculation,
    SubtractCalculation,
    MultiplyCalculation,
    DivideCalculation,
    PowerCalculation,
    ModulusCalculation,
    Calculation
)

# -----------------------------------------------------------------------------------
# Test Concrete Calculation Classes
# -----------------------------------------------------------------------------------

@patch.object(Operation, 'addition')
def test_add_calculation_execute_positive(mock_addition):
    """
    Test the execute method of AddCalculation for a positive scenario.

    This test verifies that the AddCalculation class correctly calls the addition
    method of the Operation class with the provided operands and returns the expected result.
    """
    # Arrange
    a = 10.0  # First operand
    b = 5.0   # Second operand
    expected_result = 15.0  # Expected result of addition
    mock_addition.return_value = expected_result  # Mock the addition method's return value
    add_calc = AddCalculation(a, b)  # Instantiate AddCalculation with operands

    # Act
    result = add_calc.execute()  # Execute the addition calculation

    # Assert
    mock_addition.assert_called_once_with(a, b)  # Ensure addition was called with correct operands
    assert result == expected_result  # Verify the result matches the expected value


@patch.object(Operation, 'addition')
def test_add_calculation_execute_negative(mock_addition):
    """
    Test the execute method of AddCalculation for a negative scenario.

    This test ensures that if the Operation.addition method raises an exception,
    the AddCalculation.execute method propagates it correctly.
    """
    # Arrange
    a = 10.0
    b = 5.0
    mock_addition.side_effect = Exception("Addition error")  # Simulate an exception in addition
    add_calc = AddCalculation(a, b)

    # Act & Assert
    with pytest.raises(Exception) as exc_info:
        add_calc.execute()  # Attempt to execute addition, expecting an exception

    # Verify that the exception message is as expected
    assert str(exc_info.value) == "Addition error"


@patch.object(Operation, 'subtraction')
def test_subtract_calculation_execute_positive(mock_subtraction):
    """
    Test the execute method of SubtractCalculation for a positive scenario.

    This test verifies that the SubtractCalculation class correctly calls the subtraction
    method of the Operation class with the provided operands and returns the expected result.
    """
    # Arrange
    a = 10.0
    b = 5.0
    expected_result = 5.0
    mock_subtraction.return_value = expected_result
    subtract_calc = SubtractCalculation(a, b)

    # Act
    result = subtract_calc.execute()

    # Assert
    mock_subtraction.assert_called_once_with(a, b)
    assert result == expected_result


@patch.object(Operation, 'subtraction')
def test_subtract_calculation_execute_negative(mock_subtraction):
    """
    Test the execute method of SubtractCalculation for a negative scenario.

    This test ensures that if the Operation.subtraction method raises an exception,
    the SubtractCalculation.execute method propagates it correctly.
    """
    # Arrange
    a = 10.0
    b = 5.0
    mock_subtraction.side_effect = Exception("Subtraction error")
    subtract_calc = SubtractCalculation(a, b)

    # Act & Assert
    with pytest.raises(Exception) as exc_info:
        subtract_calc.execute()

    # Verify that the exception message is as expected
    assert str(exc_info.value) == "Subtraction error"


@patch.object(Operation, 'multiplication')
def test_multiply_calculation_execute_positive(mock_multiplication):
    """
    Test the execute method of MultiplyCalculation for a positive scenario.

    This test verifies that the MultiplyCalculation class correctly calls the multiplication
    method of the Operation class with the provided operands and returns the expected result.
    """
    # Arrange
    a = 10.0
    b = 5.0
    expected_result = 50.0
    mock_multiplication.return_value = expected_result
    multiply_calc = MultiplyCalculation(a, b)

    # Act
    result = multiply_calc.execute()

    # Assert
    mock_multiplication.assert_called_once_with(a, b)
    assert result == expected_result


@patch.object(Operation, 'multiplication')
def test_multiply_calculation_execute_negative(mock_multiplication):
    """
    Test the execute method of MultiplyCalculation for a negative scenario.

    This test ensures that if the Operation.multiplication method raises an exception,
    the MultiplyCalculation.execute method propagates it correctly.
    """
    # Arrange
    a = 10.0
    b = 5.0
    mock_multiplication.side_effect = Exception("Multiplication error")
    multiply_calc = MultiplyCalculation(a, b)

    # Act & Assert
    with pytest.raises(Exception) as exc_info:
        multiply_calc.execute()

    # Verify that the exception message is as expected
    assert str(exc_info.value) == "Multiplication error"


@patch.object(Operation, 'division')
def test_divide_calculation_execute_positive(mock_division):
    """
    Test the execute method of DivideCalculation for a positive scenario.

    This test verifies that the DivideCalculation class correctly calls the division
    method of the Operation class with the provided operands and returns the expected result.
    """
    # Arrange
    a = 10.0
    b = 5.0
    expected_result = 2.0
    mock_division.return_value = expected_result
    divide_calc = DivideCalculation(a, b)

    # Act
    result = divide_calc.execute()

    # Assert
    mock_division.assert_called_once_with(a, b)
    assert result == expected_result


@patch.object(Operation, 'division')
def test_divide_calculation_execute_negative(mock_division):
    """
    Test the execute method of DivideCalculation for a negative scenario.

    This test ensures that if the Operation.division method raises an exception,
    the DivideCalculation.execute method propagates it correctly.
    """
    # Arrange
    a = 10.0
    b = 5.0
    mock_division.side_effect = Exception("Division error")
    divide_calc = DivideCalculation(a, b)

    # Act & Assert
    with pytest.raises(Exception) as exc_info:
        divide_calc.execute()

    # Verify that the exception message is as expected
    assert str(exc_info.value) == "Division error"

@patch.object(Operation, 'power')
def test_power_calculation_execute_positive(mock_power):
    a, b = 2.0, 5.0
    mock_power.return_value = 32.0
    calc = PowerCalculation(a, b)
    result = calc.execute()
    mock_power.assert_called_once_with(a, b)
    assert result == 32.0

@patch.object(Operation, 'modulus')
def test_modulus_calculation_execute_positive(mock_modulus):
    a, b = 10.0, 3.0
    mock_modulus.return_value = 1.0
    calc = ModulusCalculation(a, b)
    result = calc.execute()
    mock_modulus.assert_called_once_with(a, b)
    assert result == 1.0

@patch.object(Operation, 'modulus')
def test_modulus_calculation_execute_zero_divisor(mock_modulus):
    a, b = 10.0, 0.0
    mock_modulus.side_effect = ValueError("Modulus by zero is not allowed.")
    calc = ModulusCalculation(a, b)
    with pytest.raises(ValueError) as exc:
        calc.execute()
    assert str(exc.value) == "Modulus by zero is not allowed."


def test_divide_calculation_execute_division_by_zero():
    """
    Test that DivideCalculation.execute raises ZeroDivisionError when dividing by zero.

    This test verifies that attempting to divide by zero using DivideCalculation
    correctly raises a ZeroDivisionError with an appropriate error message.
    """
    # Arrange
    a = 10.0
    b = 0.0
    divide_calc = DivideCalculation(a, b)

    # Act & Assert
    with pytest.raises(ZeroDivisionError) as exc_info:
        divide_calc.execute()

    # Verify the exception message is as expected
    assert str(exc_info.value) == "Cannot divide by zero."


# -----------------------------------------------------------------------------------
# Test CalculationFactory
# -----------------------------------------------------------------------------------

def test_factory_creates_add_calculation():
    """
    Test that CalculationFactory creates an AddCalculation instance.

    This test ensures that the factory correctly instantiates the AddCalculation
    class when the 'add' calculation type is requested.
    """
    # Arrange
    a = 10.0
    b = 5.0

    # Act
    calc = CalculationFactory.create_calculation('add', a, b)

    # Assert
    assert isinstance(calc, AddCalculation)  # Check if the instance is of AddCalculation
    assert calc.a == a                        # Verify the first operand
    assert calc.b == b                        # Verify the second operand


def test_factory_creates_subtract_calculation():
    """
    Test that CalculationFactory creates a SubtractCalculation instance.

    This test verifies that the factory correctly instantiates the SubtractCalculation
    class when the 'subtract' calculation type is requested.
    """
    # Arrange
    a = 10.0
    b = 5.0

    # Act
    calc = CalculationFactory.create_calculation('subtract', a, b)

    # Assert
    assert isinstance(calc, SubtractCalculation)
    assert calc.a == a
    assert calc.b == b


def test_factory_creates_multiply_calculation():
    """
    Test that CalculationFactory creates a MultiplyCalculation instance.

    This test ensures that the factory correctly instantiates the MultiplyCalculation
    class when the 'multiply' calculation type is requested.
    """
    # Arrange
    a = 10.0
    b = 5.0

    # Act
    calc = CalculationFactory.create_calculation('multiply', a, b)

    # Assert
    assert isinstance(calc, MultiplyCalculation)
    assert calc.a == a
    assert calc.b == b


def test_factory_creates_divide_calculation():
    """
    Test that CalculationFactory creates a DivideCalculation instance.

    This test verifies that the factory correctly instantiates the DivideCalculation
    class when the 'divide' calculation type is requested.
    """
    # Arrange
    a = 10.0
    b = 5.0

    # Act
    calc = CalculationFactory.create_calculation('divide', a, b)

    # Assert
    assert isinstance(calc, DivideCalculation)
    assert calc.a == a
    assert calc.b == b


def test_factory_create_unsupported_calculation():
    with pytest.raises(ValueError):
        CalculationFactory.create_calculation('sqrt', 9.0, 0.5)


def test_factory_register_calculation_duplicate():
    """
    Test that registering a calculation type that's already registered raises ValueError.

    This test verifies that attempting to register a calculation type that has already
    been registered with the factory results in a ValueError to prevent duplicate entries.
    """
    # Arrange & Act
    with pytest.raises(ValueError) as exc_info:
        @CalculationFactory.register_calculation('add')  # Attempt to register 'add' again
        class AnotherAddCalculation(Calculation):
            """
            AnotherAddCalculation attempts to register the 'add' calculation type again.
            """
            def execute(self) -> float:
                return Operation.addition(self.a, self.b)

    # Assert
    assert "Calculation type 'add' is already registered." in str(exc_info.value)


# -----------------------------------------------------------------------------------
# Test String Representations
# -----------------------------------------------------------------------------------

@patch.object(Operation, 'addition', return_value=15.0)
def test_calculation_str_representation_addition(mock_addition):
    """
    Test the __str__ method of AddCalculation.

    This test verifies that the string representation of an AddCalculation instance
    is formatted correctly, displaying the class name, operation, operands, and result.
    """
    # Arrange
    a = 10.0
    b = 5.0
    add_calc = AddCalculation(a, b)

    # Act
    calc_str = str(add_calc)

    # Assert
    # Expected string should reflect the operation name derived from the class name ('Add')
    expected_str = f"{add_calc.__class__.__name__}: {a} Add {b} = 15.0"
    assert calc_str == expected_str


@patch.object(Operation, 'subtraction', return_value=5.0)
def test_calculation_str_representation_subtraction(mock_subtraction):
    """
    Test the __str__ method of SubtractCalculation.

    This test verifies that the string representation of a SubtractCalculation instance
    is formatted correctly, displaying the class name, operation, operands, and result.
    """
    # Arrange
    a = 10.0
    b = 5.0
    subtract_calc = SubtractCalculation(a, b)

    # Act
    calc_str = str(subtract_calc)

    # Assert
    # Expected string should reflect the operation name derived from the class name ('Subtract')
    expected_str = f"{subtract_calc.__class__.__name__}: {a} Subtract {b} = 5.0"
    assert calc_str == expected_str


@patch.object(Operation, 'multiplication', return_value=50.0)
def test_calculation_str_representation_multiplication(mock_multiplication):
    """
    Test the __str__ method of MultiplyCalculation.

    This test verifies that the string representation of a MultiplyCalculation instance
    is formatted correctly, displaying the class name, operation, operands, and result.
    """
    # Arrange
    a = 10.0
    b = 5.0
    multiply_calc = MultiplyCalculation(a, b)

    # Act
    calc_str = str(multiply_calc)

    # Assert
    # Expected string should reflect the operation name derived from the class name ('Multiply')
    expected_str = f"{multiply_calc.__class__.__name__}: {a} Multiply {b} = 50.0"
    assert calc_str == expected_str


@patch.object(Operation, 'division', return_value=2.0)
def test_calculation_str_representation_division(mock_division):
    """
    Test the __str__ method of DivideCalculation.

    This test verifies that the string representation of a DivideCalculation instance
    is formatted correctly, displaying the class name, operation, operands, and result.
    """
    # Arrange
    a = 10.0
    b = 5.0
    divide_calc = DivideCalculation(a, b)

    # Act
    calc_str = str(divide_calc)

    # Assert
    # Expected string should reflect the operation name derived from the class name ('Divide')
    expected_str = f"{divide_calc.__class__.__name__}: {a} Divide {b} = 2.0"
    assert calc_str == expected_str


def test_calculation_repr_representation_subtraction():
    """
    Test the __repr__ method of SubtractCalculation.

    This test ensures that the repr representation of a SubtractCalculation instance
    accurately reflects the class name and the operands.
    """
    # Arrange
    a = 10.0
    b = 5.0
    subtract_calc = SubtractCalculation(a, b)

    # Act
    calc_repr = repr(subtract_calc)

    # Assert
    # The __repr__ should display the class name and the operands in a clear format
    expected_repr = f"{SubtractCalculation.__name__}(a={a}, b={b})"
    assert calc_repr == expected_repr


def test_calculation_repr_representation_division():
    """
    Test the __repr__ method of DivideCalculation.

    This test ensures that the repr representation of a DivideCalculation instance
    accurately reflects the class name and the operands.
    """
    # Arrange
    a = 10.0
    b = 5.0
    divide_calc = DivideCalculation(a, b)

    # Act
    calc_repr = repr(divide_calc)

    # Assert
    # The __repr__ should display the class name and the operands in a clear format
    expected_repr = f"{DivideCalculation.__name__}(a={a}, b={b})"
    assert calc_repr == expected_repr

def test_factory_creates_power_calculation():
    calc = CalculationFactory.create_calculation('power', 2.0, 5.0)
    assert isinstance(calc, PowerCalculation)
    assert calc.a == 2.0 and calc.b == 5.0

def test_factory_creates_modulus_calculation():
    calc = CalculationFactory.create_calculation('modulus', 10.0, 3.0)
    assert isinstance(calc, ModulusCalculation)
    assert calc.a == 10.0 and calc.b == 3.0


# -----------------------------------------------------------------------------------
# Parameterized Tests for Execute Method
# -----------------------------------------------------------------------------------

from unittest.mock import patch

@patch("app.calculation.Operation.addition")
@patch("app.calculation.Operation.subtraction")
@patch("app.calculation.Operation.multiplication")
@patch("app.calculation.Operation.division")
@patch("app.calculation.Operation.power")
@patch("app.calculation.Operation.modulus")
@pytest.mark.parametrize("calc_type, a, b, expected_result", [
    ('add', 10.0, 5.0, 15.0),
    ('subtract', 10.0, 5.0, 5.0),
    ('multiply', 10.0, 5.0, 50.0),
    ('divide', 10.0, 5.0, 2.0),
    ('power', 2.0, 5.0, 32.0),
    ('modulus', 10.0, 3.0, 1.0),
])
def test_calculation_execute_parameterized(
    mock_modulus, mock_power, mock_division, mock_multiplication, mock_subtraction, mock_addition,
    calc_type, a, b, expected_result
):
    if calc_type == 'add':
        mock_addition.return_value = expected_result
    elif calc_type == 'subtract':
        mock_subtraction.return_value = expected_result
    elif calc_type == 'multiply':
        mock_multiplication.return_value = expected_result
    elif calc_type == 'divide':
        mock_division.return_value = expected_result
    elif calc_type == 'power':
        mock_power.return_value = expected_result
    elif calc_type == 'modulus':
        mock_modulus.return_value = expected_result

    calc = CalculationFactory.create_calculation(calc_type, a, b)
    assert calc.execute() == expected_result


# -----------------------------------------------------------------------------------
# Parameterized Tests for String Representation
# -----------------------------------------------------------------------------------
@patch("app.calculation.Operation.addition", return_value=15.0)
@patch("app.calculation.Operation.subtraction", return_value=5.0)
@patch("app.calculation.Operation.multiplication", return_value=50.0)
@patch("app.calculation.Operation.division", return_value=2.0)
@patch("app.calculation.Operation.power", return_value=32.0)
@patch("app.calculation.Operation.modulus", return_value=1.0)
@pytest.mark.parametrize("calc_type, a, b, expected_str", [
    ('add', 10.0, 5.0, "AddCalculation: 10.0 Add 5.0 = 15.0"),
    ('subtract', 10.0, 5.0, "SubtractCalculation: 10.0 Subtract 5.0 = 5.0"),
    ('multiply', 10.0, 5.0, "MultiplyCalculation: 10.0 Multiply 5.0 = 50.0"),
    ('divide', 10.0, 5.0, "DivideCalculation: 10.0 Divide 5.0 = 2.0"),
    ('power', 2.0, 5.0, "PowerCalculation: 2.0 Power 5.0 = 32.0"),
    ('modulus', 10.0, 3.0, "ModulusCalculation: 10.0 Modulus 3.0 = 1.0"),
])
def test_calculation_str_parameterized(
    mock_modulus, mock_power, mock_division, mock_multiplication, mock_subtraction, mock_addition,
    calc_type, a, b, expected_str
):
    calc = CalculationFactory.create_calculation(calc_type, a, b)
    assert str(calc) == expected_str
