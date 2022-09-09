from database import db

negdb = db.neg

async def negate_name(chat_id: int, name: str):
    negated = await get_negated_names
    if name in negated:
        return
    negated["names"] = name
    return await negdb.update_one({"chat_id": chat_id}, {"$set": {"names": negated}}, upsert=True)


async def get_negated_names(chat_id: int):
    negated_names = await negdb.find_one({"chat_id": chat_id})
    if not negated_names:
        return {}
    return negated_names["names"]
