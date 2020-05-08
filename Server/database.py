import sqlite3
from typing import Mapping, Tuple, Union


class Database:
    """
    Sqlite3 database adapter for basic CRUD operations on a single-table database.
    """
    def __init__(self, path):
        self.connection = sqlite3.connect(path)

    def execute_statement(self, statement: str, parameters: Tuple):
        """
        Run SQL statement using bound parameters against database.
        Exceptions are converted into JSON-format errors
        :param statement: Statement string; column values may be substituted with ? tokens
        :param parameters: Tuple of parameters to bind to ? tokens
        :return: Dict containing JSON-format result
        """
        try:
            with self.connection as transaction:
                rows = transaction.execute(statement, parameters).fetchall()
        except Exception as exc:
            return {"result": str(exc)}
        if len(rows):
            return {"result": "success", "rows": rows}
        return {"result": "success"}

    @staticmethod
    def make_statement_tokens(num: int) -> str:
        return ','.join(('?',) * num)

    @staticmethod
    def make_statement_eq_tokens(columns: Mapping[str, Union[int, float, str]]) -> str:
        return ','.join([f'"{column}"=?' for column in columns])

    def insert(self, parameters):
        """
        Insert dict key/values as database columns/row
        :param parameters: Dict containing a "set" dict of key/values
        :return: JSON-format result
        """
        sets = parameters["set"]
        column_tokens = ','.join(sets.keys())
        value_tokens = self.make_statement_tokens(len(sets))
        statement = "INSERT INTO simple({0}) VALUES ({1})".format(column_tokens, value_tokens)
        statement_params = tuple(sets.values())
        return self.execute_statement(statement, statement_params)

    def select(self, parameters):
        """
        Read dict key/values from database columns/row optionally selected by "where" key/values
        :param parameters: Dict containing an optional "where" dict of key/values
        :return: JSON-format result
        """
        if "where" in parameters and len(parameters["where"]):
            where = parameters["where"]
            statement_tokens = self.make_statement_eq_tokens(where)
            statement = "SELECT * FROM simple WHERE ({})".format(statement_tokens)
            statement_params = tuple(where.values())
            return self.execute_statement(statement, statement_params)
        else:
            return self.execute_statement("SELECT * FROM simple", tuple())

    def update(self, parameters):
        """
        Update dict key/values as database columns/row optionally selected by "where" key/values
        :param parameters: Dict containing a "set" dict of key/values and an optional "where" dict of key/values
        :return: JSON-format result
        """
        sets = parameters["set"]
        set_statement_tokens = self.make_statement_eq_tokens(sets)
        if "where" in parameters:
            where = parameters["where"]
            where_statement_tokens = self.make_statement_eq_tokens(where)
            statement = "UPDATE simple SET {} WHERE ({})".format(set_statement_tokens, where_statement_tokens)
            statement_params = tuple(sets.values()) + tuple(where.values())
        else:
            statement = "UPDATE simple SET {}".format(set_statement_tokens)
            statement_params = tuple(sets.values())
        return self.execute_statement(statement, statement_params)

    def delete(self, parameters):
        """
        Delete database row selected by "where" key/values
        :param parameters: Dict containing a "where" dict of key/values
        :return: JSON-format result
        """
        where = parameters["where"]
        where_statement_tokens = self.make_statement_eq_tokens(where)
        statement = "DELETE FROM simple WHERE ({})".format(where_statement_tokens)
        statement_params = tuple(where.values())
        return self.execute_statement(statement, statement_params)
