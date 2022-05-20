#%%
'''
This is a Temperature module
it contains the Temperature class, which allows you to: 
 - Set a Temperature in either Degrees Celsius or Farenheit 
- Convert a Temperature between Degrees Celsius or Farenheit 
- Set a Temperatue to 0 
- Check if a Temperature is valid between -273 and 3000 
'''
from dataclasses import dataclass
from pydantic import BaseModel
from pydantic import validate_arguments

@dataclass
class Temperature(BaseModel): 
    ''' 
    This is the intialisation function featuring class decorator @dataclass
    Attribute : 
        heat_level(float): the heat_level represented in Degrees Celsius 
    '''
    heat_level : float


    def temp_f_convert(self):
        '''
        Function to convert a temperature from Degrees Celsius to Farenheit 
        Returns
            ----------
            float:
             The heat_level in Farenheit  
        '''
        temp_f = round((float(1.8 * self.heat_level) + 32))
        print("Temperature converted from Celsius to Farenheit")
        return temp_f


    @staticmethod
    @validate_arguments
    def temp_c_convert(temp_far:float):
        '''
        Function to convert a Temperature from Farenheit to Degrees Celsius 
        Argument:
            ...........
        temp_cels : Takes a temperature in Farenheit and outputs it as Celsius
        Returns:
            ..........
            str:  
                String representation of float variable  temp_cels + '°C' 
        '''    
        temp_cels = round(float((temp_far - 32) / 1.8),2)
        return str(temp_cels) 

    
    @staticmethod
    def is_temp_valid(check_temp:float):
        '''  
        Function to check if a temperature is valid 
        Returns
            .......
            Bool: True if conditions are met 
        '''
        if 3000 >= check_temp >= -273:
            return True
        else:
            return False 

          
    @classmethod
    @validate_arguments  
    def new_temp_f(cls, temp_fh:float): # farenheit 
        '''   
        Function to create a new instance of the Temperature Class 
        Args: 
            .......
            float
                temp_fh : The temperature in Farenheit 
        Returns: 
            .......
            A new instance of the Temperature Class in Celsius  
        '''
        temp_in_celsius = cls.temp_c_convert(temp_fh) # calls the staticmethod / function. Go to the class, go to the method, input the number into it.
        return cls(heat_level=temp_in_celsius)

    @classmethod
    def standard(cls): 
        ''' Function to set a temperature to zero using a new instance of the class 
            Attribute:
                .........
                int
                    temp_c = The temperature in Celsius
           '''
        standard_temp = 0 
        return cls(heat_level=standard_temp) 

Kettle = Temperature(heat_level=40.0) 
print(Kettle)
Bath = Kettle.temp_f_convert()
print(Bath)
print(Temperature.temp_c_convert(36.1))
print(Temperature.is_temp_valid(600))
print(Temperature.new_temp_f(40.1))