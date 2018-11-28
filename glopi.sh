#!/bin/bash
#do $1, $2 etc for args

if [ $1 == "--version" ]
then
echo "Glopi Alpha 2"
exit
fi

if [ $1 == "--help" ] || [ $1 == "--usage" ]
then
echo "Look in the readme(.md) for help!"
exit
fi

if [ $1 == "changelog" ]
then
id="$2"

path="/tmp/glopi"

#check if tmp dir exists
mkdir $path

#download cards
python3 browser.py "https://app.gitkraken.com/api/glo/boards/$id/cards?archived=undefined&fields=board_id,archived_date,board_id,due_date,name,column_id,created_by,created_date,members,labels,attachment_count,comment_count,total_task_count,completed_task_count,description,status,sync_provider_id,updated_date.js" "$path/cards.json"

#download columns + further info
python3 browser.py "https://app.gitkraken.com/api/glo/boards/$id?fields=archived_date,invited_members,external_provider_members,members,id,name,columns,columns.name,labels,labels.sync_provider_id,sync_provider,sync_provider.type,sync_provider.options" "$path/columns.json"

#generate changelog
python3 changelog.py $3

exit
fi

echo "Unknown command"