class Config(object):
    SEED = 1234
    RENDER_ENV = False
    REMOVE_HEIGHT_HACK = True
    DATA_DIR = 'data'
    ACTION_SIZE = 4 if REMOVE_HEIGHT_HACK else 3
    NUM_ROWS = 64
    NUM_COLS = 64
    IS_DISCRETE = False
    
    MAX_NUM_EPISODES = 5000
    MAX_NUM_STEPS = 15
    MAX_BUFFER_SIZE = 100000
