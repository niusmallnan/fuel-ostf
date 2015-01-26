#!/bin/bash

process_name=${PROCESS_NAME:="neunn-ostf"}
tmux_session_name=$process_name
echo "tmux session is [$tmux_session_name]"

cd /neunn-ostf
tmux new-session -s $tmux_session_name -n $tmux_session_name -d
tmux send-keys -t $tmux_session_name:0 "ostf-server --config-file etc/ostf/ostf.conf" C-m

/set_ssh.sh
/usr/sbin/sshd -D
