from db import get_conn
from models.package import Package


def get_all_packages() -> list[Package]:
    with get_conn() as db:
        res = db.cursor().execute("SELECT * FROM packages")
        db.commit()
        res = res.fetchall()
        packages: list[Package] = [Package(
                id=returned_package[0],
                height=returned_package[1],
                width=returned_package[2],
                depth=returned_package[3],
                is_shipped=returned_package[4])
            for returned_package in res]
        return packages

def get_package_by_id(id: int) -> Package:
    with get_conn() as db:
        res = db.cursor().execute("SELECT * FROM packages p WHERE p.id = (?)", (id,))
        db.commit()
        res = res.fetchone()
        package = None
        if res is not None:
            package = Package(
                id=res[0],
                height=res[1],
                width=res[2],
                depth=res[3],
                is_shipped=res[4]
            )
        return package
#
# def create_package(data):
#     with get_conn() as db:
#         res = db.cursor().execute(
#             "INSERT INTO packages (height, width, depth) VALUES ((?),(?),(?))",
#             (data["height"], data["width"], data["depth"])
#         )
#         db.commit()
#         return True
