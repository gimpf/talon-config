# from talon examples https://github.com/talonvoice/examples/blob/master/debug.py
from talon import noise, actions, ctrl
from talon.engine import engine

debugEngine = True
debugNoise = True

def listener(topic, m):
    if topic == 'cmd' and m['cmd']['cmd'] == 'g.load' and m['success'] == True:
        print('engine event: [grammar reloaded]')
    else:
        print(f'engine event: {topic}', m)

if debugEngine:
    engine.register('', listener)

# def on_pop(active):
#     print(f"pop active:{active}")
#
# def on_hiss(active):
#     print(f"hiss active:{active}")
#
# noise.register('pop', on_pop)
# noise.register('hiss', on_hiss)

def on_noise(noise, active):
    print(f"noise {noise} active:{active}")

if debugNoise:
    noise.register('', on_noise)
