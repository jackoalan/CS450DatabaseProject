import itertools
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
    def make_q_eq_tokens(num: int) -> str:
        return ','.join(('?=?',) * num)

    @staticmethod
    def make_eq_parameters(params: Mapping[str, Union[int, float, str]]) -> Tuple[Union[int, float, str], ...]:
        return tuple(itertools.chain(*params.items()))

    def insert(self, parameters):
        sets = parameters["set"]
        q_tokens = self.make_q_tokens(len(sets))
        q = "INSERT INTO simple({0}) VALUES ({0})".format(q_tokens)
        p = tuple(sets.keys()) + tuple(sets.values())
        return self.execute_query(q, p)

    def select(self, parameters):
        if "where" in parameters and len(parameters["where"]):
            where = parameters["where"]
            q_tokens = self.make_q_eq_tokens(len(where))
            q = "SELECT * FROM simple WHERE ({})".format(q_tokens)
            p = self.make_eq_parameters(where)
            return self.execute_query(q, p)
        else:
            return self.execute_query("SELECT * FROM simple", tuple())

    def update(self, parameters):
        sets = parameters["set"]
        set_q_tokens = self.make_q_eq_tokens(len(sets))
        if "where" in parameters:
            where = parameters["where"]
            where_q_tokens = self.make_q_eq_tokens(len(where))
            q = "UPDATE simple SET {} WHERE ({})".format(set_q_tokens, where_q_tokens)
            p = self.make_eq_parameters(sets) + self.make_eq_parameters(where)
        else:
            q = "UPDATE simple SET {}".format(set_q_tokens)
            p = self.make_eq_parameters(sets)
        return self.execute_query(q, p)

    def delete(self, parameters):
        where = parameters["where"]
        where_q_tokens = self.make_q_eq_tokens(len(where))
        q = "DELETE FROM simple WHERE ({})".format(where_q_tokens)
        p = self.make_eq_parameters(where)
        return self.execute_query(q, p)
