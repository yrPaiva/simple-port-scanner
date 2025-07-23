# Criado para corrigir erro no pytest
import sys
import os

HERE = os.path.dirname(__file__)
SRC_PATH = os.path.join(HERE, 'src')
sys.path.insert(0, SRC_PATH)
