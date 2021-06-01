import sched
import time
import botconfig as telegram
import database as db
import redditconfig as reddit

ping_interval = 180

if __name__=='__main__':
    #telegram.setup()
    db.setup_db()

    print("---- Polling Reddit ----")
    reddit.evaluatePosts()

    # main loop
    s = sched.scheduler(time.time, time.sleep)

    def main_loop(sc):
        print("\n---- Polling Reddit ----")
        reddit.evaluatePosts()
        s.enter(ping_interval, 1, main_loop, (sc,))

    try:
        s.enter(ping_interval, 1, main_loop, (s,))
        s.run()
    except KeyboardInterrupt:
        print("---- Stopping the bot ----")