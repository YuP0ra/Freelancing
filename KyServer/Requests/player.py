import time
import sqlite3


def onConnectionStarted(client):
    print("New Connection: ", client.address)


def onConnectionTimeout(client):
    pass


def onConnectionEnded(client):
    pass


def DEFAULT(client, request):
    print(request)
