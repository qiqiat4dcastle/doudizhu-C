# from tensorpack.utils.stats import StatCounter
# from tensorpack.utils.utils import get_tqdm
from multiprocessing import *
import sys
import os
if os.name == 'nt':
    sys.path.insert(0, '../build/Release')
else:
    sys.path.insert(0, '../build.linux')
from datetime import datetime
from scripts.envs import make_env
from scripts.agents import make_agent


types = ['RHCP']


def eval_episode(env, agent):
    env.reset()
    env.prepare()
    done = False
    r = 0
    while not done:
        if env.get_role_ID() != agent.role_id:
            r, done = env.step_auto()
        else:
            r, done = env.step(agent.intention(env))
    if agent.role_id == 2:
        r = -r
    assert r != 0
    return int(r > 0)


role_id = 1
def eval_proc(file_name):
    print(file_name)
    f = open(os.path.join('./log') + file_name, 'w+')
    for te in types:
        for ta in types:
            agent = make_agent(ta, role_id)
            for i in range(1):
                env = make_env(te)
                # st = StatCounter()
                # with get_tqdm(total=100) as pbar:
                for j in range(100):
                    winning_rate = eval_episode(env, agent)
                    print(winning_rate)
                # f.write('%s with role id %d against %s, winning rate: %f\n' % (ta, role_id, te, st.average))
    # f.close()


if __name__ == '__main__':
    eval_proc("test.log")
    # procs = []
    # for i in range(cpu_count() // 2):
    #     procs.append(Process(target=eval_proc, args=('res%d.txt' % i,)))
    # for p in procs:
    #     p.start()
    # for p in procs:
    #     p.join()
