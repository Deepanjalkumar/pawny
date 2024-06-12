import requests,json,os
from elasticsearch import Elasticsearch
from dotenv import load_dotenv
load_dotenv()
es=Elasticsearch(["http://elasticsearch:9200"],basic_auth=('elastic', os.environ.get('ELASTIC_PASSWORD'))) # EDR Manager Address Host:Port

headers ={
    "X-OTX-API-KEY":"dec100cca0d7d43d911e6e08d93985a4b6c944543a63891133337ff20fe5c4bf",
    "Content-Type": "application/json"
}
data=requests.get(url="https://otx.alienvault.com/api/v1/search/pulses",headers=headers)


for i in range(0, len(data.json()["results"])):
    document={
        "id":data.json()["results"][i]["id"],
        "name":data.json()["results"][i]["name"],
        "description":"",
        "modified":data.json()["results"][i]["modified"],
        "created":data.json()["results"][i]["created"],
        "tags":data.json()["results"][i]["tags"],
        "references":data.json()["results"][i]["references"],
        "public":data.json()["results"][i]["public"],
        "adversary":data.json()["results"][i]["adversary"],
        "targeted_countries":data.json()["results"][i]["targeted_countries"],
        "malware_families":data.json()["results"][i]["malware_families"],
        "attack_ids":data.json()["results"][i]["attack_ids"],
        "industries":data.json()["results"][i]["industries"],
        "TLP":data.json()["results"][i]["TLP"],
        "cloned_from":data.json()["results"][i]["cloned_from"],
        "export_count":data.json()["results"][i]["export_count"],
        "upvotes_count":data.json()["results"][i]["upvotes_count"],
        "downvotes_count":data.json()["results"][i]["downvotes_count"],
        "votes_count":data.json()["results"][i]["votes_count"],
        "locked":data.json()["results"][i]["locked"],
        "pulse_source":data.json()["results"][i]["pulse_source"],
        "validator_count":data.json()["results"][i]["validator_count"],
        "comment_count":data.json()["results"][i]["comment_count"],
        "follower_count":data.json()["results"][i]["follower_count"],
        "vote":data.json()["results"][i]["vote"],
        "author":data.json()["results"][i]["author"],
        "indicator_type_counts":data.json()["results"][i]["indicator_type_counts"],
        "indicator_count":data.json()["results"][i]["indicator_count"],
        "is_author":data.json()["results"][i]["is_author"],
        "is_subscribing":data.json()["results"][i]["is_subscribing"],
        "subscriber_count":data.json()["results"][i]["subscriber_count"],
        "modified_text":data.json()["results"][i]["modified_text"],
        "is_modified":data.json()["results"][i]["is_modified"],
        "groups":data.json()["results"][i]["groups"],
        "in_group":data.json()["results"][i]["in_group"],
        "threat_hunter_scannable":data.json()["results"][i]["threat_hunter_scannable"],
        "threat_hunter_has_agents":data.json()["results"][i]["threat_hunter_has_agents"]   
    }
    
    resp= es.index(index="pulses", document=document)
    