from bson.objectid import ObjectId
from project.infrastructure.constants.mongo_collections import Collections
from project.infrastructure.data_layer.data_layer_general import DataLayer


class ValidateAdress:

    @staticmethod
    async def this_address_has_exist(criteria: dict) -> bool:

        data_layer = DataLayer(Collections.person_address)
        result = await data_layer.get_by_filter(criteria)

        if len(result) > 0:
            return True

        return False

    @staticmethod
    async def this_address_is_active(_id: ObjectId) -> bool:

        data_layer = DataLayer(Collections.person_address)
        result = await data_layer.get_by_id(_id)

        if "status" in result and result["status"] == "active":
            return True
        return False
