#!/usr/bin/env python3
"""tests for pcr.py"""

import os
import re
import string
import random
from subprocess import getstatusoutput

prg = './pcr.py'


# --------------------------------------------------
def test_exists():
    """exists"""

    assert os.path.isfile(prg)


# --------------------------------------------------
def test_usage():
    """usage"""

    for flag in ['-h', '--help']:
        rv, out = getstatusoutput(f'{prg} {flag}')
        assert rv == 0
        assert out.lower().startswith('usage')


# --------------------------------------------------
def test_primer_seqs():
    """primer sequences"""

    good = 'CTTATTAGTTTACTATAAAGGAGTCGAAAGAGAAGTACCAAAGAT'
    rv, out = getstatusoutput(f'{prg} {good}')
    assert rv == 0
    assert re.search('Forward Primer in 5-3: "CTTATTAGTT"', out)
    assert re.search('Reverse Primer in 3-5: "ATGGTTTCTA"', out)

# --------------------------------------------------
def test_default():
    """Default sequence"""

    good = 'CTTATTAGTTTACTATAAAGGAGTCGAAAGAGAAGTACCAAAGAT'
    rv, out = getstatusoutput(f'{prg} {good}')
    assert rv == 0
    expected = """
Forward Primer in 5-3: "CTTATTAGTT"
Reverse Primer in 3-5: "ATGGTTTCTA"
Tm Forward: "24C"
Tm Reverse: "26C"
Polymerase: 100.0 uL
Forward Primer: 1.6 uL
Reverse Primer: 1.6 uL
BSA: 10.0 uL
Water: 36.8 uL
    """.strip()
    assert out.strip() == expected
