set id 1
for uid in (seq 1 8)
  for tid in (seq 0 9)
    set id (math $id + 1)
    echo \
"- model: notifications.NotificationSetting
  pk: $id
  fields:
    is_enabled: true
    medium: email
    type: $tid
    user: $uid
"
  end
end
