from pyobserver1 import *

pub = Publisher(["lunch", 'dinner'])

bob = SubscriberOne('Bob')
alice = SubscriberTwo('Alice')
john = SubscriberOne('John')


pub.register("lunch", bob)
pub.register("dinner", alice, alice.receive)
pub.register("lunch", john)
pub.register("dinner", john)

pub.dispatch("lunch", "It's lunchtime")
pub.dispatch("dinner", "Time for Dinner")
