class NationalPark:
    def __init__(self, name):
        if not isinstance(name, str) or len(name) < 3:
            raise ValueError("NationalPark name must be a string of at least 3 characters.")
        self._name = name
        self._trips = []  # To store trips related to this park
        
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        raise AttributeError("Cannot change the name of the national park.")

    def trips(self):
        return self._trips
    
    def visitors(self):
        return list(set(trip.visitor for trip in self._trips))
    
    def total_visits(self):
        return len(self._trips)
    
    def best_visitor(self):
        if not self._trips:
            return None
        visitor_counts = {}
        for trip in self._trips:
            visitor_counts[trip.visitor] = visitor_counts.get(trip.visitor, 0) + 1
        return max(visitor_counts, key=visitor_counts.get)



class Trip:
    all = []  # Class-level attribute to keep track of all trip instances

    def __init__(self, visitor, national_park, start_date, end_date):
        self.visitor = visitor
        self.national_park = national_park
        self.start_date = start_date
        self.end_date = end_date
        Trip.all.append(self)  # Add this trip to the class-level list of all trips
        visitor.trips().append(self)  # Add this trip to the visitor's trips
        national_park.trips().append(self)  # Add this trip to the national park's trips

    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, value):
        if not isinstance(value, str) or len(value) < 7:
            raise ValueError("Start date must be a string of at least 7 characters.")
        self._start_date = value

    @property
    def end_date(self):
        return self._end_date

    @end_date.setter
    def end_date(self, value):
        if not isinstance(value, str) or len(value) < 7:
            raise ValueError("End date must be a string of at least 7 characters.")
        self._end_date = value


class Visitor:
    def __init__(self, name):
        if not isinstance(name, str) or not (1 <= len(name) <= 15):
            raise ValueError("Visitor name must be a string between 1 and 15 characters.")
        self._name = name
        self._trips = []  # To store trips related to this visitor

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not (1 <= len(value) <= 15):
            raise ValueError("Visitor name must be a string between 1 and 15 characters.")
        self._name = value

    def trips(self):
        return self._trips
    
    def national_parks(self):
        return list(set(trip.national_park for trip in self._trips))
    
    def total_visits_at_park(self, park):
        return sum(1 for trip in self._trips if trip.national_park == park)
