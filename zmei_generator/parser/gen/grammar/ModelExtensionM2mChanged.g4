
parser grammar ModelExtensionM2mChanged;

options { tokenVocab=ZmeiLangSimpleLexer; }

import Base;

an_m2m_changed:
    AN_M2M_CHANGED
    python_code
    ;
