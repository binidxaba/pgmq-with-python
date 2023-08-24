#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2023 rzavalet <rzavalet@noemail.com>
#
# Distributed under terms of the MIT license.

"""

"""

import random
import string
from tembo_pgmq_python import Message, PGMQueue


if __name__ == '__main__':
    host = "localhost"
    port = 5432
    username = "postgres"
    password = "postgres"
    database = "postgres"

    num_messages = 10000

    rnd = random.randint(0, 100)
    test_queue = "bench_queue_sample"

    queue = PGMQueue(host=host, 
                     port=port, 
                     username=username, 
                     password=password, 
                     database=database)

    try:
        #queue.drop_queue(test_queue)
        queue.create_queue(test_queue)

        for x in range(num_messages):

            payload = ''.join(random.choices(string.ascii_uppercase + string.digits, k = 10))
            msg = {"payload": payload}
            msg_id = queue.send(test_queue, msg)

            if (x+1) % 1000 == 0:
                print("Sent {} messages".format(x + 1))

    except Exception as e:
        print(f"{e}")
