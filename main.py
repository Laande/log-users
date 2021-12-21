import sys

from g_python.gextension import Extension
from g_python.hmessage import Direction
from g_python.hparsers import HEntity
from os import system

extension_info = {
    "title": "User logger",
    "description": "Log the users in room",
    "version": "1.0",
    "author": "Sigm4"
}
ext = Extension(extension_info, sys.argv)
ext.start()

system("clear")
print("{}LOGGING USERS{}".format('-' * 78, '-' * 78))
entities = []

def addUsers(message):
  entities.extend(HEntity.parse(message.packet))
  printEntities()

'''
def removeUser(message):
  playerIndex = int(message.packet.read_string())
  global entities
  entities = list(filter(lambda entity: entity.index == playerIndex, entities))
  printEntities()
'''

def clearUsers(_):
  entities.clear()
  printEntities()

def printEntities():
  print(list(map(lambda entity: entity.name, entities)))

ext.intercept(Direction.TO_CLIENT, addUsers, 'Users')
# ext.intercept(Direction.TO_CLIENT, removeUser, 'UserRemove')
ext.intercept(Direction.TO_CLIENT, clearUsers, 'RoomReady')

