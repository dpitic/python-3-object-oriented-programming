import sqlite3
import datetime

"""
Demonstration of the template pattern.

The template pattern is useful for removing duplicate code. It is designed for
situations where there are several different tasks to accomplish that have some,
but not all, steps in common. The common steps are implemented in a base class,
and the distinct steps are overridden in subclasses to provide custom behaviour.

The template pattern is standard OOP application of inheritance to reduce
duplicate code.

This script implements a car sales reporting application. The sales records are
stored in an SQLite database table. The common tasks to be performed are
1. Select all sales of new vehicles and output them to the screen in a comma
delimited format.
2. Output a comma delimited list of all salespeople with their gross sales and
save it to a file that can be imported into a spreadsheet.
"""


class QueryTemplate:
    """
    Base class that implements the template used to perform the required steps.
    Each of the steps are implemented in their own separate method.
    """

    def connect(self):
        """
        Connect to the database.
        :return: None
        """
        self.conn = sqlite3.connect('sales.db')

    def construct_query(self):
        """
        Construct the required query. This should be overridden in subclasses
        to construct the specific query.
        :return: None
        """
        raise NotImplementedError()  # override this method

    def do_query(self):
        """
        Execute the database query.
        :return: None
        """
        results = self.conn.execute(self.query)
        self.results = results.fetchall()

    def format_results(self):
        """
        Format the query results into a comma delimited string.
        :return: None
        """
        output = []
        for row in self.results:
            row = [str(i) for i in row]
            output.append(', '.join(row))
        self.formatted_results = '\n'.join(output)

    def output_results(self):
        """
        Output the result data to the required destination. This should be
        overridden in subclasses to implement the required output.
        :return: None
        """
        raise NotImplementedError()  # override this method

    def process_format(self):
        """
        Primary method called by clients of this class used to manage and
        perform the required steps in the correct order.
        :return: None
        """
        self.connect()
        self.construct_query()
        self.do_query()
        self.format_results()
        self.output_results()


class NewVehiclesQuery(QueryTemplate):
    """
    Subclass used to select all sales of new vehicles and output them to the
    screen in comma delimited format.
    """

    def construct_query(self):
        """
        Select all sales of new vehicles.
        :return: None
        """
        self.query = "select * from Sales where new='true'"

    def output_results(self):
        """
        Output results to the screen in comma delimited format.
        :return: None
        """
        print(self.formatted_results)


class UserGrossQuery(QueryTemplate):
    """
    Subclass used to select all salespeople with the gross sales and save it to
    a file that can be imported into a spreadsheet.
    """

    def construct_query(self):
        """
        Select all salespeople with the gross sales.
        :return: None
        """
        self.query = ("select salesperson, sum(amt) " +
                      " from Sales group by salesperson")

    def output_results(self):
        """
        Save the results to a file that can be imported into a spreadsheet.
        :return: None
        """
        filename = 'gross_sales_{0}'.format(
            datetime.date.today().strftime('%Y%m%d')
        )
        with open(filename, 'w') as outfile:
            outfile.write(self.formatted_results)


# Main script execution function
def main():
    # Select all sales of new vehicles and output them to the screen in a
    # comma delimited format
    print('All sales of new vehicles:')
    template = NewVehiclesQuery()
    template.process_format()

    # Save a comma delimited list of all salespeople with their gross sales to
    # a file that can be imported into a spreadsheet
    template = UserGrossQuery()
    template.process_format()


# Import guard
if __name__ == '__main__':
    main()
