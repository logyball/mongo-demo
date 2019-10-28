import pymongo as mongo
from os import system
from sys import argv
from pprint import pprint

MONGO_HOST = 'localhost'
SHARD_PORT = 30000
NON_SHARD_PORT = 27018
DOCUMENT_PROTOTYPE = {
    'port': -1,
    'name': 'service',
    'active': True
}
SHARD_1 = 'tic'
SHARD_2 = 'tac'
SHARD_3 = 'toe'
COLLECTION = 'services'
DB = 'demo_db'


def get_list_service_records():
    service_list = []
    for i in range(1000, 4000):
        new_doc = DOCUMENT_PROTOTYPE.copy()
        new_doc['port'] = i
        new_doc['name'] = new_doc['name'] + str(i)
        service_list.append(new_doc)
    return service_list


def get_client_init_db(sharded=False):
    client = mongo.MongoClient(MONGO_HOST, SHARD_PORT) if sharded else mongo.MongoClient(MONGO_HOST, NON_SHARD_PORT)
    db = client.demo_db
    col = db.services
    return client, db, col


def initialize_sharded_db():
    client, db, collection = get_client_init_db(sharded=True)
    collection_to_shard = DB + "." + COLLECTION
    admin_db = client.admin
    pprint(admin_db.command('enableSharding', DB))
    pprint(admin_db.command({
        'shardCollection': collection_to_shard,
        'key': {'port': 1}
    }))
    pprint(admin_db.command('addShardToZone', shard=SHARD_1, zone='low'))
    pprint(admin_db.command('addShardToZone', shard=SHARD_2, zone='mid'))
    pprint(admin_db.command('addShardToZone', shard=SHARD_3, zone='high'))
    pprint(admin_db.command(
        'updateZoneKeyRange',
        updateZoneKeyRange=COLLECTION,
        min=1000,
        max=1999,
        zone='low'
    ))
    pprint(admin_db.command(
        'updateZoneKeyRange',
        updateZoneKeyRange=COLLECTION,
        min=2000,
        max=2999,
        zone='mid'
    ))
    pprint(admin_db.command(
        'updateZoneKeyRange',
        updateZoneKeyRange=COLLECTION,
        min=3000,
        max=4000,
        zone='high'
    ))


def initialize_non_sharded_db():
    client, db, collection = get_client_init_db(sharded=False)
    service_records = get_list_service_records()
    collection.insert_many(service_records)


def main():
    if len(argv) < 2:
        print("supply an arg")
        exit(1)
    if argv[1] == 'shard':
        initialize_sharded_db()
    elif argv[1] == 'single':
        initialize_non_sharded_db()
    else:
        print("supply a valid arg")
        exit(1)


if __name__ == '__main__':
    main()