from g_python.gextension import Extension
from g_python.hmessage import Direction
from g_python.hparsers import HEntity
import datetime
import sys

extension_info = {
    "title": "User logger",
    "description": "Log the users in room",
    "version": "1.0",
    "author": "Sigm4"
}

ext = Extension(extension_info, sys.argv, silent=True)
ext.start()

print("\n----- LOGGING USERS -----")
entities = []


def add_users(message):
    entities.extend(HEntity.parse(message.packet))
    print_entities()


# def removeUser(message):
#   playerIndex = int(message.packet.read_string())
#   global entities
#   entities = list(filter(lambda entity: entity.index == playerIndex, entities))
#   printEntities()


def clear_users(_):
    entities.clear()
    date()
    print("List of users cleared")


def print_entities():
    date()
    print(list(map(lambda entity: entity.name, entities)))


def date():
    now = datetime.datetime.now().strftime('%d-%m-%Y - %H:%M')
    print(now, end="\n↪ ")


ext.intercept(Direction.TO_CLIENT, add_users, 'Users')
# ext.intercept(Direction.TO_CLIENT, removeUser, 'UserRemove')
ext.intercept(Direction.TO_CLIENT, clear_users, 'RoomReady')
