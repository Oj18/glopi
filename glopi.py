import sys
import os

import browser
import changelog

args = sys.argv

if len(args) == 2 and args[1] == "--version":
    print("Glopi Alpha 4")
    exit()

if len(args) == 2 and (args[1] == "--help" or args[1] == "--usage"):
    print("Look at the readme(.md) for help!")
    exit()

if len(args) > 2 and args[1] == "plain-changelog":
    id=args[2]

    path="/tmp/glopi"

    if not os.path.isdir("/tmp/glopi"):
        os.mkdir(path)

    #download cards
    browser.saveurl("https://app.gitkraken.com/api/glo/boards/" + id + "/cards?archived=undefined&fields=board_id,archived_date,board_id,due_date,name,column_id,created_by,created_date,members,labels,attachment_count,comment_count,total_task_count,completed_task_count,description,status,sync_provider_id,updated_date.js", path + "/cards.json")

    #download columns + further info
    browser.saveurl("https://app.gitkraken.com/api/glo/boards/" + id + "?fields=archived_date,invited_members,external_provider_members,members,id,name,columns,columns.name,labels,labels.sync_provider_id,sync_provider,sync_provider.type,sync_provider.options", path + "/columns.json")

    if len(args) == 4:
        file = args[3]
    else:
        file = ""
    
    #generate changelog
    changelog.make_plain(file)

    exit()

if len(args) > 2 and args[1] == "fancy-changelog":
    id=args[2]

    path="/tmp/glopi"

    if not os.path.isdir("/tmp/glopi"):
        os.mkdir(path)

    #download cards
    browser.saveurl("https://app.gitkraken.com/api/glo/boards/" + id + "/cards?archived=undefined&fields=board_id,archived_date,board_id,due_date,name,column_id,created_by,created_date,members,labels,attachment_count,comment_count,total_task_count,completed_task_count,description,status,sync_provider_id,updated_date.js", path + "/cards.json")

    #download columns + further info
    browser.saveurl("https://app.gitkraken.com/api/glo/boards/" + id + "?fields=archived_date,invited_members,external_provider_members,members,id,name,columns,columns.name,labels,labels.sync_provider_id,sync_provider,sync_provider.type,sync_provider.options", path + "/columns.json")

    if len(args) == 4:
        file = args[3]
    else:
        file = ""
    
    #generate changelog
    changelog.make_fancy(file)

    exit()

print("Unknown command. See readme.md for avaliable commands and info.")
exit()