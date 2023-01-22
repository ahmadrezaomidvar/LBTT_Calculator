import json

class LBTT:
    """
    This class provides the functionality to calculate the Land and Buildings Transaction Tax (LBTT) calculator
    due on a property purchase in Scotland.
    """
    def __init__(self):
        """
        Inialise the LBTT calculator with the tax rate values
        
        Parameters:
            None
        Returns:
            None
        """
        self.tax_rate = self.get_tax_rate()

    def get_tax_rate(self):
        """
        Get the tax rate from the tax_rate.json file
        In case the file is not found, the default tax rate values are used
        
        Parameters:
            None
        Returns:
            dict: dictionary with the tax rate values
        """
        try:
            file_path = 'tax_rate.json'
            with open(file_path, 'r') as tax_rate_file:
                tax_rate = json.load(tax_rate_file)
                return {float(k): v for k, v in tax_rate.items()}
        except FileNotFoundError:
            print('tax_rate.json file not found, using default tax rate values')
            return {
                145000: 0.,
                250000: 0.02,
                325000: 0.05,
                750000: 0.1,
                float('inf'): 0.12
            }

    def calculate(self, price):
        """
        Calculate the LBTT due on a property purchase in Scotland

        Parameters:
            price: the purchase price of the property
        Raises:
            ValueError: if the price is negative
            ValueError: if the price is too large
        Returns:
            float: the LBTT due on the property purchase
        """
        if price < 0:
            raise ValueError('Invalid price. Price cannot be negative')
        elif price == 0:
            return 0.
        elif price > 10**11:
            raise ValueError('Invalid price. Price cannot be larger than 10^11')
        price = round(price, 2)

        lbtt = 0
        threshold = 0
        for limit, rate in self.tax_rate.items():
            if price > limit:
                lbtt += (limit - threshold) * rate
                threshold = limit
            else:
                lbtt += (price - threshold) * rate
                break

        return round(lbtt, 2)



if __name__ == '__main__':
    price = float(150000.34524353313131)
    lbtt = LBTT()
    print(f'LBTT for purchase price: £{round(price, 2)} is equal to £{lbtt.calculate(price)}')
