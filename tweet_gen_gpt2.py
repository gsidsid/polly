import argparse
import logging
import sys
import unittest
from unittest.mock import patch

import run_generation


logging.basicConfig(level=logging.DEBUG)

logger = logging.getLogger()

testargs = ["run_generation.py", "--prompt=Hello", "--length=240", "--seed=42"]

model_type, model_name = ("--model_type=gpt2", "--model_name_or_path=gpt2")
with patch.object(sys, "argv", testargs + [model_type, model_name]):
    result = run_generation.main()
    print(result)