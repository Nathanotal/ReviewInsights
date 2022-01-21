import json
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="./key.json"

# Use the application default credentials
cred = credentials.ApplicationDefault()
firebase_admin.initialize_app(cred, {
  'projectId': "review-visualization",
})

db = firestore.client()

def main():
    f = open("infoJSON.json")
    data = json.load(f)
    refCInfo = db.collection(u'companyInfo')
    refTNames = db.collection(u'TopicNames')
    
    for company in data:
        refCInfo.document(company).set(data[company])
    
    # f = open("TopicNames.json")
    # data = json.load(f)
    
    # refTNames.document(u"3xYZFVDo0fa8uBGGjwlo").set(data)


main()

