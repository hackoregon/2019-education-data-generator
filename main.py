from generator.factory import Factory
from generator.strategy import Strategy
factory = Factory(5, "demo_dist", Strategy())
factory.pretty_print()