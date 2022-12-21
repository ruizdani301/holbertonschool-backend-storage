#!/usr/bin/env python3
"""Log stats"""
from pymongo import MongoClient

if __name__ == "__main__":
    client = MongoClient("mongodb://127.0.01:27017")
    nginx_collection = client.logs.nginx

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    path = "path"
    status = "/status"

    print(f"{nginx_collection.count_documents({})} logs")
    print("Methods:")

    for value in methods:
        count = nginx_collection.count_documents({"method": value})
        print(f"\tmethod {value}: {count}")
    print(f"{nginx_collection.count_documents({path: status})} status check")
    pipeline = [
        {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
        {"$limit": 10},
        {"$project": {"_id": 0, "ip": "$_id", "count": 1}},
    ]
    ip_collection = nginx_collection.aggregate(pipeline)
    print("IPs:")
    for ip in ip_collection:
        print("\t{}: {}".format(ip.get("ip"), ip.get("count")))
