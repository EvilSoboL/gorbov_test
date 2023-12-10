from controllers.database import DataBaseHandler


class Result:
    def __init__(self):
        self.date = None
        self.first_part_time = None
        self.second_part_time = None
        self.errors = None

        self.database = DataBaseHandler()

    def save_result(self, user_id, date, first_part_time, second_part_time, errors):
        self.date = date
        self.first_part_time = first_part_time
        self.second_part_time = second_part_time
        self.errors = errors

        self.database.insert_result(
            user_id,
            date,
            first_part_time,
            second_part_time,
            errors
        )


