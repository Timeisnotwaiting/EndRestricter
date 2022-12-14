from database import db

negdb = db.neg

async def negate_name(chat_id: int, name: str):
    negated = await get_negated_names(chat_id)
    if name in negated and not len(negated) == 0:
        return
    if len(negated) == 0:
        negated = {"[]{}"}
    negated.add(name)
    return await negdb.update_one({"chat_id": chat_id}, {"$set": {"names": negated}}, upsert=True)

async def denegate_name(chat_id: int, name: str):
    negated = await get_negated_names(chat_id)
    if not name in negated:
        return
    if len(negated) == 1:
        return
    negated.remove(name)
    return await negdb.update_one({"chat_id": chat_id}, {"$set": {"names": negated}}, upsert=True)


async def get_negated_names(chat_id: int):
    negated_names = await negdb.find_one({"chat_id": chat_id})
    if not negated_names:
        return {}
    return negated_names["names"]

async def is_name_negated(chat_id: int, name: str):
    names = await get_negated_names(chat_id)
    if name in names:
        return True
    return False
