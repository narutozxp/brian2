'''
THIS FILE IS AUTOMATICALLY GENERATED BY A STATIC CODE GENERATION TOOL
DO NOT EDIT BY HAND

Instead edit the template:

    dev/tools/static_codegen/units_template.py
'''
from .fundamentalunits import (Unit, get_or_create_dimension,
                               standard_unit_register,
                               additional_unit_register)

{all}

Unit.automatically_register_units = False

#### FUNDAMENTAL UNITS
metre = Unit.create(get_or_create_dimension(m=1), "metre", "m")
meter = Unit.create(get_or_create_dimension(m=1), "meter", "m")
kilogram = Unit.create(get_or_create_dimension(kg=1), "kilogram", "kg")
gram = Unit.create_scaled_unit(kilogram, "m")
gram.set_name('gram')
gram.set_display_name('g')
gramme = Unit.create_scaled_unit(kilogram, "m")
gramme.set_name('gramme')
gramme.set_display_name('g')
second = Unit.create(get_or_create_dimension(s=1), "second", "s")
amp = Unit.create(get_or_create_dimension(A=1), "amp", "A")
kelvin = Unit.create(get_or_create_dimension(K=1), "kelvin", "K")
mole = Unit.create(get_or_create_dimension(mol=1), "mole", "mol")
candle = Unit.create(get_or_create_dimension(candle=1), "candle", "cd")
fundamental_units = [metre, meter, gram, second, amp, kelvin, mole, candle]

{derived}

{definitions}

{base_units}
{scaled_units}
{powered_units}
{additional_units}
{all_units}

Unit.automatically_register_units = True

map(standard_unit_register.add, base_units + scaled_units + powered_units)
map(additional_unit_register.add, additional_units)
