class MyCalendar:

    def __init__(self):
        self.bookings = []  # List to store booked intervals

    def book(self, start: int, end: int) -> bool:
        # Loop through existing bookings to check for overlap
        for existingStart, existingEnd in self.bookings:
            # Check if new event overlaps with an existing one
            if start < existingEnd and end > existingStart:
                return False
        
        # No overlap, add the event to the list of bookings
        self.bookings.append((start, end))
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)

# Example 1:

# Input
# ["MyCalendar", "book", "book", "book"]
# [[], [10, 20], [15, 25], [20, 30]]
# Output
# [null, true, false, true]

# Explanation
# MyCalendar myCalendar = new MyCalendar();
# myCalendar.book(10, 20); // return True
# myCalendar.book(15, 25); // return False, It can not be booked because time 15 is already booked by another event.
# myCalendar.book(20, 30); // return True, The event can be booked, as the first event takes every time less than 20, but not including 20.
