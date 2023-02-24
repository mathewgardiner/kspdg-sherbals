# Copyright (c) 2022, MASSACHUSETTS INSTITUTE OF TECHNOLOGY
# Subject to FAR 52.227-11 – Patent Rights – Ownership by the Contractor (May 2014).
# SPDX-License-Identifier: MIT

from kspdg.pe1.pe1_base import PursuitEvadeGroup1Env

class PursuitEnv_ePassive(PursuitEvadeGroup1Env):
    def __init__(self, loadfile: str, **kwargs):
        super().__init__(loadfile=loadfile, **kwargs)

    def evasive_maneuvers(self):
        '''Do not perform evasive maneuvers
        '''
        pass

class PE1_E1_I1_Env(PursuitEnv_ePassive):
    def __init__(self, **kwargs):
        super().__init__(loadfile=PursuitEvadeGroup1Env.LOADFILE_I1, **kwargs)

class PE1_E1_I2_Env(PursuitEnv_ePassive):
    def __init__(self, **kwargs):
        super().__init__(loadfile=PursuitEvadeGroup1Env.LOADFILE_I2, **kwargs)

class PE1_E1_I3_Env(PursuitEnv_ePassive):
    def __init__(self, **kwargs):
        super().__init__(loadfile=PursuitEvadeGroup1Env.LOADFILE_I3, **kwargs)

class PE1_E1_I4_Env(PursuitEnv_ePassive):
    def __init__(self, **kwargs):
        super().__init__(loadfile=PursuitEvadeGroup1Env.LOADFILE_I4, **kwargs)