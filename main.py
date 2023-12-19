from http import HTTPStatus
from flask import Flask, request
from flask_restful import Resource, Api
from models import Smartphone


# from sqlalchemy import select


app = Flask(__name__)
api = Api(app)


class Recommendation(Resource):
    def post(self):
        criteria = request.get_json()
        valid_criteria = [
            "brand",
            "ram_gb",
            "processor",
            "storage_gb",
            "battery",
            "harga",
        ]
        smartphone = Smartphone()

        if not criteria:
            return "Criteria is empty", HTTPStatus.BAD_REQUEST.value

        if not all([v in valid_criteria for v in criteria]):
            return "Invalid criteria", HTTPStatus.NOT_FOUND.value

        recommendations = smartphone.get_recs(criteria)
        results = [
            {
                "smartphone_id": rec[0],
                "nama": smartphone.smartphone_data_dict[rec[0]],
                "skor": rec[1],
                "Rank": rank + 1,
            }
            for rank, rec in enumerate(recommendations.items()
        ]

        return {"Rekomendasi Smartphone Entry level": results}, HTTPStatus.OK.value


api.add_resource(Recommendation, "/recommendations")


# def create_table():
#     Base.metadata.create_all(engine)
#     print(f"{Fore.GREEN}[Success]: {Style.RESET_ALL}Database has created!")


# def run_saw():
#     saw = SimpleAdditiveWeighting()
#     print("result:", saw.calculate)


# def run_wp():
#     wp = WeightedProduct()
#     print("result:", wp.calculate)
#     pass


# if len(sys.argv) > 1:
#     arg = sys.argv[1]

#     if arg == "saw":
#         run_saw()
#     elif arg == "wp":
#         run_wp()
#     else:
#         print("command not found")


if __name__ == "__main__":
    app.run(port="5005", debug=True)
