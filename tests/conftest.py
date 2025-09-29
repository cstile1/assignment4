# tests/conftest.py

import pytest
import importlib

# Import the calculator module that defines and registers all classes
import app.calculation as calcmod

@pytest.fixture(autouse=True)
def ensure_factory_has_all_calculations():
    """
    Reload app.calculation before each test so the @register_calculation
    decorators run and all operations (including power/modulus) are registered.
    Then, defensively ensure the registry includes all expected types.
    """
    importlib.reload(calcmod)

    # Make sure _calculations includes every operation we support
    calcmod.CalculationFactory._calculations.update({
        'add':      calcmod.AddCalculation,
        'subtract': calcmod.SubtractCalculation,
        'multiply': calcmod.MultiplyCalculation,
        'divide':   calcmod.DivideCalculation,
        'power':    calcmod.PowerCalculation,
        'modulus':  calcmod.ModulusCalculation,
    })
