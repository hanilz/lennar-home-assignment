from db import get_conn
from models.truck import Truck


def get_all_trucks() -> list[Truck]:
    with get_conn() as db:
        res = db.cursor().execute("SELECT * FROM trucks")
        db.commit()
        res = res.fetchall()
        trucks: list[Truck] = [
            Truck(
                id=returned_truck[0],
                height=returned_truck[1],
                width=returned_truck[2],
                depth=returned_truck[3],
                is_shipped=returned_truck[4])
            for returned_truck in res]
        return trucks

def get_truck_by_id(id: int) -> Truck:
    with get_conn() as db:
        res = db.cursor().execute("SELECT * FROM trucks t WHERE t.id = (?)", (id,))
        db.commit()
        res = res.fetchone()
        truck = None
        if res is not None:
            truck = Truck(
                id=res[0],
                height=res[1],
                width=res[2],
                depth=res[3],
                is_shipped=res[4]
            )
        return truck
#
# def create_truck(data):
#     with get_conn() as db:
#         res = db.cursor().execute(
#             "INSERT INTO trucks (height, width, depth) VALUES ((?),(?),(?))",
#             (data["height"],data["width"], data["depth"])
#         )
#         db.commit()
#         return True
#
