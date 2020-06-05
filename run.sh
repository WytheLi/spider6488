# test environment
#nohup /usr/local/bin/python3 ~/spider6488/run.py            > ~/spider6488/logs/log 2>&1 &
#nohup /usr/local/bin/python3 ~/spider6488/run_11x5.py       > ~/spider6488/logs/11x5.log 2>&1 &
#nohup /usr/local/bin/python3 ~/spider6488/run_k3.py         > ~/spider6488/logs/k3.log 2>&1 &
#nohup /usr/local/bin/python3 ~/spider6488/run_buy_plan.py   > ~/spider6488/logs/buy_plan.log 2>&1 &
#nohup /usr/local/bin/python3 ~/spider6488/run_kill_plan.py  > ~/spider6488/logs/kill_plan.log 2>&1 &


# production environment
nohup /usr/bin/python3 ~/spider6488/run.py            > /dev/null 2>&1 &
nohup /usr/bin/python3 ~/spider6488/run_11x5.py       > /dev/null 2>&1 &
nohup /usr/bin/python3 ~/spider6488/run_k3.py         > /dev/null 2>&1 &
nohup /usr/bin/python3 ~/spider6488/run_buy_plan.py   > /dev/null 2>&1 &
nohup /usr/bin/python3 ~/spider6488/run_kill_plan.py  > /dev/null 2>&1 &