import sqlite3
from typing import Mapping, Tuple, Union


class Database:
    def __init__(self, path):
        self.conn = sqlite3.connect(path)

    def execute_query(self, query: str, parameters: Tuple):
        try:
            with self.conn as c:
                rows = c.execute(query, parameters).fetchall()
        except Exception as e:
            return {"result": str(e)}
        if len(rows):
            return {"result": "success", "rows": rows}
        return {"result": "success"}

    @staticmethod
    def make_q_tokens(num: int) -> str:
        return ','.join(('?',) * num)

    @staticmethod
    def make_q_eq_tokens(cols: Mapping[str, Union[int, float, str]]) -> str:
        return ','.join([f'{c}=?' for c in cols])

    def insert(self, parameters):
        sets = parameters["set"]
        column_tokens = ','.join(sets.keys())
        value_tokens = self.make_q_tokens(len(sets))
        q = "INSERT INTO simple({0}) VALUES ({1})".format(column_tokens, value_tokens)
        p = tuple(sets.values())
        return self.execute_query(q, p)

    def select(self, parameters):
        if "where" in parameters and len(parameters["where"]):
            where = parameters["where"]
            q_tokens = self.make_q_eq_tokens(where)
            q = "SELECT * FROM simple WHERE ({})".format(q_tokens)
            p = tuple(where.values())
            return self.execute_query(q, p)
        else:
            return self.execute_query("SELECT * FROM simple", tuple())

    def update(self, parameters):
        sets = parameters["set"]
        set_q_tokens = self.make_q_eq_tokens(sets)
        if "where" in parameters:
            where = parameters["where"]
            where_q_tokens = self.make_q_eq_tokens(where)
            q = "UPDATE simple SET {} WHERE ({})".format(set_q_tokens, where_q_tokens)
            p = tuple(sets.values()) + tuple(where.values())
        else:
            q = "UPDATE simple SET {}".format(set_q_tokens)
            p = tuple(sets.values())
        return self.execute_query(q, p)

    def delete(self, parameters):
        where = parameters["where"]
        where_q_tokens = self.make_q_eq_tokens(where)
        q = "DELETE FROM simple WHERE ({})".format(where_q_tokens)
        p = tuple(where.values())
        return self.execute_query(q, p)
