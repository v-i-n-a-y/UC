import pint

# Create a unit registry

def convert_units(value, units_from, units_to):
    try:

        ureg = pint.UnitRegistry()

        # Parse the input values with units using the unit registry
        value_with_units = value * ureg(units_from)

        # Convert to the target units
        converted_value = value_with_units.to(units_to).magnitude

        return converted_value
    except pint.UndefinedUnitError:
        return None  # Invalid units provided
    except pint.DimensionalityError:
        return None  # Incompatible units for conversion

# Example usage:

if __name__ == "__main__":

    value = 5
    units_from = "bar"
    units_to = "psi"

    converted_value = convert_units(value, units_from, units_to)
    if converted_value is not None:
        print(f"{value} {units_from} is equal to {converted_value} {units_to}")
    else:
        print("Invalid or incompatible units provided.")

