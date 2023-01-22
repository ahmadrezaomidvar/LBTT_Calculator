# LBTT_Calculator
Land and Buildings Transaction Tax (LBTT) calculator due on a property purchase in Scotland.

This project provides a Python class for calculating the Land and Buildings Transaction Tax (LBTT) due on a property purchase in Scotland. The class can be imported and used in other Python projects to provide LBTT calculation functionality.

The project is based on the following assumptions:

-	The buyer currently owns a property and lives in it as their main residence
-	The buyer does not conduct any business activity from their house
-	The buyer does not own any other properties
-	The buyer will still only own one house after purchasing the new one.


## Getting Started

These instructions will help you to get a copy of the project up and running on your local machine for development and testing purposes.

Prerequisites
Python 3.6 or later
Installing
Clone the repository to your local machine:

```bash
git clone git@github.com:ahmadrezaomidvar/LBTT_Calculator.git
```

## Usage

The LBTT class can be imported and instantiated to create an object that can perform LBTT calculations. The class uses an optional file tax_rate.json which is a dictionary with the tax rate values. If no file is available is passed, the default tax rate values are used.

```python
from lbtt_calculator import LBTT

lbtt_calculator = LBTT()
price = 150000
lbtt = lbtt_calculator.calculate(price)
print(f'LBTT for purchase price: £{round(price, 2)} is equal to £{lbtt}')
```

## Tax Rate Values

The tax rate values are stored in a JSON file called tax_rate.json. The file should contain a dictionary with the tax rate values. The keys of the dictionary are the threshold values and the values are the corresponding rates.

```json
{
    "145000": 0.0,
    "250000": 0.02,
    "325000": 0.05,
    "750000": 0.1,
    "inf": 0.12
}
```

If the tax_rate.json file is not found, the default tax rate values are used.

## Limitations

The class can only perform LBTT calculations for Scotland.
The class can only handle prices up to 10^11.
The class can only handle tax rate values specified in the JSON file or use default values.

## Running the tests

The project includes unit tests for the LBTT class. The tests can be run by executing the following command in the root directory of the project:

```bash
python -m unittest discover
```

## Authors

* **Reza Omidvar** - *Initial work* - [ahmadrezaomidvar](https://github.com/ahmadrezaomidvar)

## References
1. 	Land and Buildings Transaction Tax - Taxes - gov.scot [Internet]. [cited 2023 Jan 19];Available from: https://www.gov.scot/policies/taxes/land-and-buildings-transaction-tax/
2. 	New LBTT Rates Announced, Replacing Stamp Duty April 2015 - MOV8 Real Estate [Internet]. [cited 2023 Jan 19];Available from: https://www.mov8realestate.com/2015/01/changes-lbtt-rates-april/
3. 	Residential property | Revenue Scotland [Internet]. [cited 2023 Jan 19];Available from: https://revenue.scot/taxes/land-buildings-transaction-tax/residential-property#residential%20property%20rates%20and%20bands
4. 	Residential property | Revenue Scotland [Internet]. [cited 2023 Jan 19];Available from: https://revenue.scot/taxes/land-buildings-transaction-tax/residential-property
5. 	The Additional Dwelling Supplement (ADS) | Revenue Scotland [Internet]. [cited 2023 Jan 19];Available from: https://revenue.scot/taxes/land-buildings-transaction-tax/additional-dwelling-supplement-ads
6. 	ADS overview and aims | Revenue Scotland [Internet]. [cited 2023 Jan 19];Available from: https://revenue.scot/taxes/land-buildings-transaction-tax/lbtt-legislation-guidance/additional-dwelling-supplement-ads-technical/ads-overview-aims
 






