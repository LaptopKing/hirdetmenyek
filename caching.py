#!/usr/bin/env python3

import requests
import json
from pymongo import MongoClient

class downloadAnnouncements:

    def __init__(self):
    
        self.baseUrl = "https://hirdetmenyek.gov.hu"
        self.detailsUri = "/api/hirdetmenyek/reszletezo/"
        self.announcementUri = "/api/hirdetmenyek"
        self.linkToFileUri = "/api/csatolmany/"
        self.params = {
            "order":"desc",
            "targy":"",
            "kategoria":"",
            "forrasIntezmenyNeve":"",
            "ugyiratSzamIktatasiSzam":"",
            "telepules":"",
            "nev":"",
            "idoszak":"",
            "adottNap":"",
            "szo":"",
            "pageIndex":"0",
            "pageSize":"1",
            "sort":"kifuggesztesNapja"
        }
        self.totalAnnouncements = 0
        self.rowsUrl = self.baseUrl + self.announcementUri
        self.ids = []
        self.announcementDatas = []
        self.announcementFiles = []

    def makeRequest(self, url, params = None):

        if (params is None):

            response = requests.get(url, verify=False)
            self.checkResponseStatusCode(response)
            return response

        response = requests.get(url, verify=False, params=params)
        self.checkResponseStatusCode(response)
        return response

    def checkResponseStatusCode(self, response):

        if (response.status_code != 200):
            print(f"Status code is not 200, instead it is {response.status_code}!")
            exit()

    def getTotalAnnouncements(self):
        
        self.params["pageSize"] = 1
        
        response = self.makeRequest(self.rowsUrl, params=self.params)
        
        self.totalAnnouncements = str(response.json()["total"] - 1)

    def getAnnouncementIds(self):

        self.params["pageSize"] = self.totalAnnouncements

        response = self.makeRequest(self.rowsUrl, params=self.params)
        
        for row in response.json()["rows"]:
            self.ids.append(row["id"])

    def getAnnouncementDatas(self):

        for id in self.ids:

            url = self.baseUrl + self.detailsUri + str(id)
            response = self.makeRequest(url)
            
            announcementData = response.json()["hirdetmenyDTO"]
            announcementData["hirdetmenyId"] = str(id)
            announcementFile = response.json()["csatolmanyok"][0]
            announcementFile["hirdetmenyId"] = str(id)
            announcementFile["path"] = self.baseUrl + self.linkToFileUri + str(announcementFile["id"])

            self.announcementDatas.append(announcementData)
            self.announcementFiles.append(announcementFile)

            exit()



announcementDownloadClass = downloadAnnouncements()
announcementDownloadClass.getTotalAnnouncements()
announcementDownloadClass.getAnnouncementIds()
announcementDownloadClass.getAnnouncementDatas()


"""

response = requests.get("https://hirdetmenyek.gov.hu/api/hirdetmenyek?order=desc&targy=&kategoria=&forrasIntezmenyNeve=&ugyiratSzamIktatasiSzam=&telepules=&nev=&idoszak=&adottNap=&szo=&pageIndex=0&pageSize=14599&sort=kifuggesztesNapja", verify=False)

total = response.json()["rows"]

print(total)

"""
