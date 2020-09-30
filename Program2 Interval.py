'''
Program 2 Interval
'''
from goody import type_as_str
from math import sqrt
from goody import irange


class Interval:
    
    def __init__(self, min, max):
        self.min = min
        self.max = max
        
    @staticmethod
 

    def min_max(min_value, max_value = None):
        
        assert type(min_value) is int or type(min_value) is float,\
            'min value should be of type int or float'
        
        assert max_value is None or (type(max_value) is int or type(max_value) is float), \
            'interval.min_max: min_value(' + str(max_value) + ') not in/float type'
            
        if max_value is not None:
            assert min_value < max_value or min_value == max_value , \
                'interval.min_max: min value : {0} is greater than the max value : {1} '.format(min_value, max_value)
        
        if max_value == None:
            return Interval(min_value, min_value)
        
        else:
            return Interval(min_value, max_value)
 
    
    @staticmethod
    def mid_err(mid_value, error_interval = 0):
      
        assert type(mid_value) is int or type(mid_value) is float,\
            'mid value should be of type int or float'
        
        assert type(error_interval) is int or type(error_interval) is float and error_interval >= 0, \
            'interval.min_max: min_value(' + str(error_interval) + ') not in/float type'
            
        
        min_value, max_value = mid_value - error_interval, mid_value + error_interval
        min_value, max_value = round(min_value, 2), round(max_value, 2)
        
        return Interval(min_value, max_value)
            
 

    def __repr__(self):
        min = str(self.__dict__['min'])
        max = str(self.__dict__['max'])
     
        return ('Interval(' + min + ',' + max + ')')
    
   
   
    def __str__(self):
        error_interval = (self.__dict__['max'] - self.__dict__['min']) /2
        mid_value = self.__dict__['min'] + error_interval
        
        return '{}(+/-{})'.format(mid_value, abs(error_interval))
       
        
        
    def best(self):
        error_interval = (self.__dict__['max'] - self.__dict__['min']) /2
        mid_value = self.__dict__['min'] + error_interval
        
        return mid_value
    
    
    def error(self):
        return (self.__dict__['max'] - self.__dict__['min']) /2
    
    
    def relative_error(self):
        error_interval = (self.__dict__['max'] - self.__dict__['min']) /2
        mid_value = self.__dict__['min'] + error_interval
        
        return abs(error_interval/ mid_value) * 100

    
    def __bool__(self):
        min_value = self.__dict__['min']
        max_value = self.__dict__['max']
        
        if min_value == max_value:
            return False
        return True
    
    def __pos__(self):
        return self
    
    def __neg__(self):
        
        min_value = self.__dict__['min']
        max_value = self.__dict__['max']
        
        return Interval(-min_value, -max_value)
     
     
    def __add__(self, other):

        
        if isinstance(other, (int, float)):
            min_sums = self.__dict__['min'] + other
            max_sums = self.__dict__['max'] + other
            
            return Interval(min_sums, max_sums)
            
        elif isinstance(other, Interval):
          
            min_sums = self.__dict__['min'] + other.__dict__['min']
            max_sums = self.__dict__['max'] + other.__dict__['max']
          
            return Interval(min_sums, max_sums)
        
        else:
            return NotImplemented
     
    
    def __radd__(self, other):
        
        if other == 0:
            return self
        return self.__add__(other)
        
        
    def __sub__(self, other):
        #print('11111', self, type(self), other, type(other))
        
        
        if isinstance(other, (int, float)):
            min_minus = self.__dict__['min'] - other
            max_minus = self.__dict__['max'] - other
            
            return Interval(min_minus, max_minus)
        
        elif isinstance(other, Interval):
            
            min_minus = self.__dict__['min'] - other.__dict__['max']
            max_minus = self.__dict__['max'] - other.__dict__['min']
          
            return Interval(min_minus, max_minus)
        
        else:
            return NotImplemented
     
     
    def __rsub__(self, other):

        if isinstance(other, (int, float)):
            min_minus = other - self.__dict__['max']
            max_minus = other - self.__dict__['min']
            
            return Interval(min_minus, max_minus)
        return Interval.__sub__(self, other)
        
         
        
    def __mul__(self, other):
        
        if isinstance(other, (int, float)):
            min_value = (self.__dict__['min'] * other)
            max_value = (self.__dict__['max'] * other)
            
            return Interval(min_value, max_value)
        
        if type(other) == Interval:
            lista = []
            
            for item, value in other.__dict__.items():
               
                lista.append(self.__dict__['min'] * value)
                lista.append(self.__dict__['max'] * value)
                
            return Interval(min(lista), max(lista))
        
        else:
            return NotImplemented
        pass

    def __rmul__(self, other):
        if isinstance(other, (int, float)):
            lista = []
            lista.append(other * self.__dict__['min'])
            lista.append(other * self.__dict__['max'])
            return Interval(min(lista), max(lista))
        
        else:
            return Interval.__mul__(self, other)
        


    def __truediv__(self, other): 

        if isinstance(other, (int, float)):
            if other == 0:
                raise ZeroDivisionError
            else:
                lista = []
                lista.append((self.__dict__['min'] / other))
                lista.append((self.__dict__['max'] / other))
             
                return Interval(min(lista), max(lista))
         
        elif type(other) is Interval:
            
            if other.__dict__['min'] <= 0 <= other.__dict__['max']:
                raise ZeroDivisionError('Interval(' + str(other.__dict__['min']) + ',' + str(other.__dict__['max']) + ') contains a zero')
                 
            else:
                lista = []
                for value in other.__dict__.values():
                     
                    lista.append(self.__dict__['max'] / value)
                    lista.append(self.__dict__['min'] / value)
                 
                return Interval(min(lista), max(lista))
         
        else:
            return NotImplemented
        
        

    
    def __rtruediv__(self, other):
        if isinstance(other, (int, float)):
            if other == 0:
                raise ZeroDivisionError
            elif self.__dict__['min'] <= 0 <= self.__dict__['max']:
                raise ZeroDivisionError('Interval(' + str(self.__dict__['min']) + ',' + str(self.__dict__['max']) + ') contains a zero')

            else:
            
                lista = []
                lista.append(other / self.__dict__['min'])
                lista.append(other / self.__dict__['max'])
                return Interval(min(lista), max(lista))
         
        elif isinstance(other, Interval):
            
            if other.__dict__['min'] <= 0 <= other.__dict__['max']:
                raise ZeroDivisionError('Interval(' + str(other.__dict__['min']) + ',' + str(other.__dict__['max']) + ') contains a zero')

            else:
                return Interval.__div__(self, other)
        else:
            return NotImplemented
     
    
    def __pow__(self, other):
        if not isinstance(other, int):
            return NotImplemented
        else:
            min_value = self.__dict__['min']
            max_value = self.__dict__['max']
            
            if other == 0:
                return Interval(1.0, 1.0)
            elif other == 1:
                return Interval(min_value, max_value)
            elif other < 0:
                lista = []
                new_min = min_value ** other
                lista.append(new_min)
                new_max = max_value ** other
                lista.append(new_max)
                
                return Interval(min(lista), max(lista))
            else:
                new_min = min_value ** other
                new_max = max_value ** other
                return Interval(new_min, new_max)

            
    def __eq__(self, other):
        if isinstance(other, (int, float)):
            if other == self.__dict__['min'] and other ==  self.__dict__['max']:
                return True
            else:
                return False
        elif isinstance(other, Interval):
            
            if self.__dict__ == other.__dict__:
                return True
            else:
                return False
            
        else:
            return NotImplemented
                      
    
    def __neq__(self, other):
        if isinstance(other, (int, float)):
            if other != self.__dict__['min'] or other !=  self.__dict__['max']:
                return True
            else:
                return False
        elif isinstance(other, Interval):
            
            if self.__dict__ != other.__dict__:
                return True
            else:
                return False
            
        else:
            return NotImplemented
    

        

    @staticmethod
    def compare_mode(cm):
        return cm
    
    
    def __lt__(self, other):
        if Interval.compare_mode == "liberal":
            if type(other) == Interval:
                if self.best() < other.best():
                    return True
                return False
            if type(other) == int:
                if self.best() < other:
                    return True
                return False
        elif Interval.compare_mode == "conservative":
            if type(other) == Interval:
                if self.__dict__['min'] < other.__dict__['min'] and self.__dict__['max'] < other.__dict__['min']:
                    return True
                return False
            if type(other) == int:
                if self.__dict__['min'] < other and self.__dict__['max'] < other:
                    return True
                return False
        else:
            raise AssertionError
            

    
    def __le__(self, other):
        if Interval.compare_mode == "liberal":
            if type(other) == Interval:
                if self.best() <= other.best():
                    return True
                return False
            if type(other) == int:
                if self.best() <= other:
                    return True
                return False
        elif Interval.compare_mode == "conservative":
            if type(other) == Interval:
                if self.__dict__['min'] <= other.__dict__['min'] and self.__dict__['max'] <= other.__dict__['min']:
                    return True
                return False
            if type(other) == int:
                if self.__dict__['min'] <= other and self.__dict__['max'] <= other:
                    return True
                return False
        else:
            raise AssertionError
#         
# 
    def __gt__(self, other):
        if Interval.compare_mode == "liberal":
            if type(other) == Interval:
                if self.best() > other.best():
                    return True
                return False
            if type(other) == int:
                if self.best() > other:
                    return True
                return False
        elif Interval.compare_mode == "conservative":
            if type(other) == Interval:
                if self.__dict__['min'] > other.__dict__['max'] and self.__dict__['min'] > other.__dict__['max']:
                    return True
                return False
            if type(other) == int:
                if self.__dict__['min'] > other and self.__dict__['max'] > other:
                    return True
                return False
        else:
            raise AssertionError

          
    def __ge__(self, other):
        if Interval.compare_mode == "liberal":
            if type(other) == Interval:
                if self.best() >= other.best():
                    return True
                return False
            
            if type(other) == int:
                if self.best() >= other:
                    return True
                return False
        elif Interval.compare_mode == "conservative":
            if type(other) == Interval:
                if self.__dict__['min'] >= other.__dict__['max'] and self.__dict__['min'] >= other.__dict__['max']:
                    return True
                return False
            if type(other) == int:
                if self.__dict__['min'] >= other and self.__dict__['max'] >= other:
                    return True
                return False


        else:
            raise AssertionError  

    
    def __abs__(self):
        
        min_value = self.__dict__['min']
        max_value = self.__dict__['max']
        
        if self.__dict__['min'] <= 0 <= self.__dict__['max']:
            min_value = 0.0
            max_value = abs(max_value)
            
            return Interval(min_value, max_value)
        else:
            lista = []
            lista.append(abs(min_value))
            lista.append(abs(max_value))
    
            return Interval(min(lista), max(lista))


    def sqrt(self):
        min_value = self.__dict__['min']
        max_value = self.__dict__['max']
        
        if self.__dict__['min'] <= 0 <= self.__dict__['max']:
            raise ValueError
        else:
            lista = []
            lista.append(sqrt(min_value))
            lista.append(sqrt(max_value))
            
            return Interval(min(lista), max(lista))
    
    
     
    def __settattr__(self, name, value):
        if name not in self.__dict__:
            if name != 'min' or name != 'max':
                self.__dict__[name] = value
        else:
            raise AssertionError
        
        
        
        
            
        
        
    
    
    
    
    
    
if __name__ == '__main__':
    g = Interval.mid_err(9.8,.05)
    print(repr(g))
    g = Interval.min_max(9.75,9.85)
    print(repr(g))
    d = Interval.mid_err(100,1)
   
    t = (d/(2*g)).sqrt()
    print(t,repr(t),t.relative_error())    

    import driver    
    driver.default_file_name = 'bsc2.txt'
#     driver.default_show_exception=True
#     driver.default_show_exception_message=True
#     driver.default_show_traceback=True
    driver.driver()
