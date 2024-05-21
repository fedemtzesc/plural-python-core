'''
    Model for aircraft  flights
'''
from pprint import pp 


class   Flight:
    """Allocate a seat to a passenger."""
    
    def __init__(self, number, aircraft) -> None:
        if not number[:2].isalpha():
            raise ValueError(f"El codigo debe empezar con dos letras en '{number}'")
        
        if not number[:2].isupper():
            raise ValueError(f"Las primeras dos letras deben ser mayusculas en '{number}'")
            
        if not (number[2:].isdigit() and int(number[2:])<=9999):
            raise ValueError(f"El numero de ruta debe de ser un numero entre 0001 y 9999 en '{number}'")
        
        self._number = number
        self._aircraft = aircraft
        rows, seats = self._aircraft.seating_plan()
        self._seating = [None] + [{letter: None for letter in seats} for _ in rows]


    def number(self):
        return self._number
    
    def route(self):
        return self._number[2:]
    
    def airline(self):
        return self._number[:2]

    def aircraft_model(self):
        return self._aircraft.model()

    def allocate_seat(self, seat, passenger):
        """
            Allocate a seat to a passenger
            Args:
                seat: A seat designator such as '12C' or '21F'. 
                passenger: The passenger name. 
                
            Raises:
                CalueError: if the seat is unavalilable
        """    
        row, letter = self._parse_seat(seat)
        
        if self._seating[row][letter] is not None:
            raise ValueError(f"Seat {seat} already occupied/assinged")
        
        self._seating[row][letter] = passenger
        
    def _parse_seat(self, seat):
        rows, seat_letters = self._aircraft.seating_plan()
        
        letter = seat[-1]
        if letter not in seat_letters:
            raise ValueError(f"Invalid seat letter {letter}")
        
        row_text = seat[:-1]
        try:
            row = int(row_text)
        except ValueError:
            raise ValueError(f"Invalid seat row {row_text}")
        
        if row not in rows:
            raise ValueError(f"Invalid row number {row}")
        
        return row, letter
    
    def _relocate_passenger(self, from_seat, to_seat):
        """
            Relocate a passenger to a different seat
            
            Args:
                from_seat: The existing seat designator for the passenger
                to be moved
                
                to_seat: The new seat designator
        """
        from_row, from_letter = self._parse_seat(from_seat)
        if self._seating[from_row][from_letter] is None:
            raise ValueError(f"No passenger to relocate in seat {from_seat}")
        
        to_row, to_letter = self._parse_seat(to_seat)
        if not self._seating[to_row][to_letter] is None:
            raise ValueError(f"Seat {from_seat} already ocuppied!")
        
        self._seating[to_row][to_letter] = self._seating[from_row][from_letter]
        self._seating[from_row][from_letter] = None
        print(f"*** Passenger relocated successfully from seat {from_seat} to seat {to_seat}!")
        # Y mostramos la nueva configuracion de asientos
        
    def show_seats(self):
        pp(self._seating)    
    
        
class Aircraft:
    def __init__(self, registration, model, num_rows, num_seats_per_row) -> None:
        self._registration = registration
        self._model = model
        self._num_rows = num_rows
        self._num_seats_per_row = num_seats_per_row
        
    def registration(self):
       return self._registration
   
    def model(self):
        return self._model
    
    def seating_plan(self):
        return (range(1, self._num_rows + 1), 
                "ABCDEFGHJK"[:self._num_seats_per_row])
        
        
        
def make_flight():
    f = Flight("BA758", Aircraft("G-EUPT","Airbus A-319", num_rows=22, num_seats_per_row=6))
    f.allocate_seat("12A", "Federico")
    f.allocate_seat("15F", "Yolanda")
    f.allocate_seat("15E", "Valeria")
    f.allocate_seat("1C", "Sebastian")
    f.allocate_seat("1D", "Ximena")
    f.show_seats()
    f._relocate_passenger('12A', '22A')
    return f



    
if __name__ == '__main__':
    f = make_flight()
    f.show_seats()
        