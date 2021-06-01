import sched
import time
import botconfig as telegram
import database as db
import redditconfig as reddit

ping_interval = 180


#telegram.setup()
db.setup_db()
#db.add_turnips('Some title', 'my datetime', 'BCDEF')
#db.get_turnips()
#db.does_turnip_exist('Some title')

reddit.evaluatePosts()


# main loop
s = sched.scheduler(time.time, time.sleep)


def main_loop(sc):
    print("Polling reddit...")

    reddit.evaluatePosts()
    s.enter(ping_interval, 1, main_loop, (sc,))


s.enter(ping_interval, 1, main_loop, (s,))
s.run()
